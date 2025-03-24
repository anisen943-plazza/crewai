import streamlit as st
from datetime import datetime
import os
import json
from pathlib import Path
import sys
import base64

# Add parent directory to path to allow importing Core_Scripts modules
parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

# ---- Config ----
RESULTS_DIR = parent_dir / "Run_Results"
VISUALS_DIR = parent_dir / "visuals"
KB_FILE = parent_dir / "knowledge" / "sales_analysis_results.md"

# ---- Utils ----

def get_latest_result_file(extension=".json"):
    """Find the most recent result file with the given extension."""
    files = sorted(RESULTS_DIR.glob(f"chat_result_*{extension}"), key=os.path.getmtime, reverse=True)
    return files[0] if files else None

def load_json_data(filepath):
    """Load JSON data from a file."""
    with open(filepath, "r") as f:
        return json.load(f)

def load_markdown(filepath):
    """Load markdown content from a file."""
    with open(filepath, "r") as f:
        return f.read()

def display_visualizations():
    """Display the most recent visualizations from visuals directory."""
    image_files = sorted(VISUALS_DIR.glob("*.png"), key=os.path.getmtime, reverse=True)
    html_files = sorted(VISUALS_DIR.glob("*.html"), key=os.path.getmtime, reverse=True)

    if not image_files and not html_files:
        st.info("No visualizations found.")
        return

    st.subheader("📊 Visualizations")

    # Display up to 3 most recent images
    for img in image_files[:3]:
        st.image(str(img), caption=img.name)

    # Display up to 3 most recent HTML visualizations
    for html in html_files[:3]:
        st.markdown(f"### {html.name}")
        with open(html, "r", encoding="utf-8") as f:
            st.components.v1.html(f.read(), height=500, scrolling=True)

def check_kb_freshness():
    """Check freshness of the knowledge base and return status and timestamp."""
    if not KB_FILE.exists():
        return "❌ Not found", None
    
    timestamp = None
    with open(KB_FILE, "r") as f:
        for line in f:
            if "## Full Analysis on" in line:
                ts_str = line.replace("## Full Analysis on", "").strip()
                try:
                    timestamp = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
                    break  # Use the first (most recent) timestamp found
                except:
                    continue
    
    # Fallback to file modification time if no timestamp found in content
    if not timestamp:
        timestamp = datetime.fromtimestamp(KB_FILE.stat().st_mtime)
    
    # Determine freshness (less than 7 days is considered fresh)
    delta_days = (datetime.now() - timestamp).days
    freshness = "🟢 Fresh" if delta_days < 7 else "🟠 Stale"
    
    return freshness, timestamp.strftime("%Y-%m-%d %H:%M:%S")

def get_router_logs():
    """Get list of router conversation logs, sorted by most recent first."""
    router_logs_dir = parent_dir / "Run_Results" / "router_logs"
    if not router_logs_dir.exists():
        return []
    
    log_files = sorted(router_logs_dir.glob("conversation_*.md"), key=os.path.getmtime, reverse=True)
    return log_files

# ---- UI ----

st.set_page_config(
    page_title="Plazza AI Chat",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("💬 Plazza AI — Intelligent Chat & Analytics")

# ---- Chat Tabs ----
tab1, tab2 = st.tabs(["Standard Chat", "Advanced Router"])

with tab1:
    st.subheader("Standard Chat Interface")
    standard_input = st.text_input("Ask a question:", key="standard_input")
    
    if standard_input and st.button("Submit to Standard Chat"):
        with st.spinner("Processing with Standard Chat..."):
            try:
                # Import here to avoid loading issues
                from Core_Scripts.plazza_chat import PlazzaChat
                pc = PlazzaChat()
                result = pc.run_chat(standard_input)
                
                st.markdown(result)
                st.session_state["last_input"] = standard_input
                st.success("Query processed successfully!")
            except Exception as e:
                st.error(f"Error: {str(e)}")

with tab2:
    st.subheader("Advanced Router (AI Orchestrator)")
    router_input = st.text_input("Ask a question:", key="router_input")
    
    if router_input and st.button("Submit to Advanced Router"):
        with st.spinner("Processing with AI Orchestrator..."):
            try:
                # Import here to avoid loading issues
                from Core_Scripts.advanced_router import run_advanced_router
                result = run_advanced_router(router_input)
                
                st.markdown(result)
                st.session_state["last_router_input"] = router_input
                st.success("Query processed successfully!")
            except Exception as e:
                st.error(f"Error: {str(e)}")

# ---- Sidebar ----
with st.sidebar:
    st.header("📚 System Status")
    
    # Knowledge Base Status
    st.subheader("Knowledge Base")
    status, ts = check_kb_freshness()
    st.markdown(f"**Status**: {status}")
    if ts:
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
                content = load_markdown(log)
                st.markdown(content)
    else:
        st.info("No router logs available.")

# ---- Output Area ----
st.markdown("---")
st.subheader("🧠 Last Chat Result")

latest_md = get_latest_result_file(".md")
if latest_md:
    st.markdown(load_markdown(latest_md), unsafe_allow_html=True)
else:
    st.info("No chat result found yet.")

# ---- Visualizations ----
display_visualizations()

# ---- Footer ----
st.markdown("---")
st.markdown("### 🛠️ Plazza AI System")
st.markdown("Powered by CrewAI with advanced agent orchestration")
st.markdown(f"Knowledge Base last updated: {ts if ts else 'Unknown'}")