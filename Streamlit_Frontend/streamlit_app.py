import streamlit as st
from datetime import datetime
import os
import json
from pathlib import Path
import sys
import time

# Setup module path for Core_Scripts access
parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

# Ensure Core_Scripts is in the path
core_scripts_dir = parent_dir / "Core_Scripts"
if core_scripts_dir.exists() and str(core_scripts_dir) not in sys.path:
    sys.path.append(str(core_scripts_dir))

# Print Python import paths for debugging
print("Python import paths:")
for p in sys.path:
    print(f"- {p}")

# Check for module availability
try:
    from Core_Scripts.crewai_visualization import CrewAIVisualization
    print("✅ Successfully imported CrewAIVisualization")
    VISUALIZATION_AVAILABLE = True
except ImportError as e:
    print(f"❌ Error importing CrewAIVisualization: {e}")
    VISUALIZATION_AVAILABLE = False

# Constants
RESULTS_DIR = parent_dir / "Run_Results"
VISUALS_DIR = parent_dir / "visuals"
KB_FILE = parent_dir / "knowledge" / "sales_analysis_results.md"

# ---- Helper Functions ----

def get_latest_result_file(extension=".json"):
    """Find the most recent result file with the given extension."""
    files = sorted(RESULTS_DIR.glob(f"chat_result_*{extension}"), key=os.path.getmtime, reverse=True)
    return files[0] if files else None

def load_json_data(filepath):
    """Load JSON data from a file."""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return {}

def check_kb_freshness():
    """Check freshness of the knowledge base and return status and timestamp."""
    if not KB_FILE.exists():
        return "❌ Missing", "N/A"
    
    timestamp = None
    try:
        with open(KB_FILE, "r") as f:
            for line in f:
                if "## Full Analysis on" in line:
                    ts_str = line.replace("## Full Analysis on", "").strip()
                    try:
                        timestamp = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
                        break  # Use the first (most recent) timestamp found
                    except:
                        continue
    except Exception as e:
        print(f"Error reading KB file: {e}")
    
    # Fallback to file modification time if no timestamp found
    if not timestamp:
        try:
            timestamp = datetime.fromtimestamp(KB_FILE.stat().st_mtime)
        except:
            return "🟠 Unknown", "N/A"
    
    # Determine freshness (less than 7 days is considered fresh)
    delta_days = (datetime.now() - timestamp).days
    
    if delta_days <= 1:
        freshness = "🟢 Very fresh (today)"
    elif delta_days <= 7:
        freshness = "🟢 Fresh"
    elif delta_days <= 14:
        freshness = "🟠 Stale"
    else:
        freshness = "🔴 Very stale"
    
    return freshness, timestamp.strftime("%Y-%m-%d %H:%M:%S")

def display_visualizations():
    """Display the most recent visualizations from visuals directory."""
    global VISUALIZATION_AVAILABLE
    
    if not VISUALS_DIR.exists():
        st.info("No visualizations directory found.")
        return
    
    try:
        image_files = sorted(VISUALS_DIR.glob("*.png"), key=os.path.getmtime, reverse=True)
        html_files = sorted(VISUALS_DIR.glob("*.html"), key=os.path.getmtime, reverse=True)
    except Exception as e:
        st.error(f"Error accessing visualization files: {e}")
        return

    if not image_files and not html_files:
        if not VISUALIZATION_AVAILABLE:
            st.info("No visualizations found. CrewAI Visualization module is not available.")
        else:
            st.info("No visualizations found.")
        return

    # Display up to 3 most recent images
    for img in image_files[:3]:
        try:
            st.image(str(img), caption=img.name)
        except Exception as e:
            st.error(f"Error displaying image {img.name}: {e}")

    # Display up to 3 most recent HTML visualizations
    for html in html_files[:3]:
        st.markdown(f"### {html.name}")
        try:
            with open(html, "r", encoding="utf-8") as f:
                st.components.v1.html(f.read(), height=500, scrolling=True)
        except Exception as e:
            st.error(f"Error displaying HTML {html.name}: {e}")

def get_router_logs():
    """Get list of router conversation logs, sorted by most recent first."""
    router_logs_dir = parent_dir / "Run_Results" / "router_logs"
    if not router_logs_dir.exists():
        return []
    
    log_files = sorted(router_logs_dir.glob("conversation_*.md"), key=os.path.getmtime, reverse=True)
    return log_files

# ---- App Setup ----
st.set_page_config(
    page_title="Plazza AI Chat",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("💬 Plazza AI — Intelligent Chat & Analytics")

# ---- Chat Mode Selection ----
chat_mode = st.radio("Select Chat Mode:", ["🧠 AI Orchestrator", "⚡ Fast Chat (Standard)"])
st.markdown("---")

# ---- User Input ----
# Using a form to enable Enter key submission
with st.form(key="chat_form"):
    query = st.text_input("Ask a question:")
    submit_button = st.form_submit_button("Submit")

if submit_button and query:
        with st.spinner("Processing your request..."):
            try:
                if chat_mode == "🧠 AI Orchestrator":
                    try:
                        from Core_Scripts.advanced_router import run_advanced_router
                    except ImportError as e:
                        st.error(f"Error importing Advanced Router: {e}")
                        st.info("Check that Core_Scripts directory is properly configured.")
                        st.stop()
                    
                    result = run_advanced_router(query)
                else:
                    try:
                        from Core_Scripts.plazza_chat import PlazzaChat
                    except ImportError as e:
                        st.error(f"Error importing PlazzaChat: {e}")
                        st.info("Check that Core_Scripts directory is properly configured.")
                        st.stop()
                    
                    chat_handler = PlazzaChat()
                    result = chat_handler.run_chat(query)
                
                # Store results in session state
                st.session_state["last_input"] = query
                st.session_state["last_result"] = result
                st.success("Query processed successfully!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                import traceback
                st.code(traceback.format_exc())
                st.stop()

# ---- Sidebar Status ----
with st.sidebar:
    st.header("📚 System Status")
    
    # Knowledge Base Status
    st.subheader("Knowledge Base")
    status, ts = check_kb_freshness()
    st.markdown(f"**Status**: {status}")
    st.markdown(f"**Last Updated**: {ts}")
    
    st.markdown("---")
    
    # Latest Metadata
    st.subheader("📂 Latest Metadata")
    latest_json = get_latest_result_file(".json")
    if latest_json:
        data = load_json_data(latest_json)
        st.markdown(f"- **Agent**: {data.get('agent', 'N/A')}")
        st.markdown(f"- **Tools Used**: {', '.join(data.get('tools_used', []))}")
        st.markdown(f"- **Analysis Type**: {data.get('analysis_type', 'N/A')}")
        st.markdown(f"- **Focus Area**: {data.get('focus_area', 'N/A')}")
        st.markdown(f"- **Timestamp**: {data.get('timestamp', 'N/A')}")
    else:
        st.info("No metadata available.")
    
    st.markdown("---")
    
    # Router Logs
    st.subheader("📝 Recent Router Logs")
    logs = get_router_logs()
    if logs:
        for i, log in enumerate(logs[:5]):  # Show 5 most recent logs
            with st.expander(f"Log {log.stem}"):
                try:
                    with open(log, "r") as f:
                        st.markdown(f.read())
                except Exception as e:
                    st.error(f"Error reading log file: {e}")
    else:
        st.info("No router logs available.")

# ---- Main Content Area ----

# Show result if we just processed a query
if "last_result" in st.session_state:
    st.markdown("### 🧠 Chat Result")
    st.markdown(st.session_state["last_result"])
# Otherwise show last chat result from file
else:
    st.markdown("### 🧠 Last Chat Result")
    latest_md = get_latest_result_file(".md")
    if latest_md:
        try:
            with open(latest_md, "r") as f:
                st.markdown(f.read(), unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error reading last chat result: {e}")
    else:
        st.info("No chat result found yet.")

# ---- Visualizations ----
st.markdown("---")
st.subheader("📊 Visualizations")
display_visualizations()

# ---- Footer ----
st.markdown("---")
st.markdown("### 🛠️ Plazza AI System")
st.markdown("Powered by CrewAI with advanced agent orchestration")
st.markdown(f"Knowledge Base last updated: {ts if ts else 'Unknown'}")