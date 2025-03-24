"""
Dashboard view for the Streamlit frontend.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from datetime import datetime, timedelta
import os
import re
import json
from utils import (
    get_files_by_pattern, 
    check_kb_freshness, 
    get_router_performance_stats,
    extract_metadata_from_log,
    parent_dir
)

# ---- Config ----
RESULTS_DIR = parent_dir / "Run_Results"
VISUALS_DIR = parent_dir / "visuals"
KB_FILE = parent_dir / "knowledge" / "sales_analysis_results.md"
ROUTER_LOGS_DIR = parent_dir / "Run_Results" / "router_logs"

def get_router_log_data():
    """Get router logs and convert to DataFrame for analysis."""
    if not ROUTER_LOGS_DIR.exists():
        return pd.DataFrame()
    
    logs = get_files_by_pattern(ROUTER_LOGS_DIR, "conversation_*.md")
    data = []
    
    for log in logs:
        metadata = extract_metadata_from_log(log)
        if "error" not in metadata:
            data.append(metadata)
    
    if not data:
        return pd.DataFrame()
    
    df = pd.DataFrame(data)
    
    # Clean up and parse timestamps
    if "timestamp" in df.columns:
        df["date"] = df["timestamp"].dt.date
        df["hour"] = df["timestamp"].dt.hour
    
    return df

def get_visualization_stats():
    """Get statistics about visualizations."""
    if not VISUALS_DIR.exists():
        return {"png_count": 0, "html_count": 0, "total": 0, "last_generated": None}
    
    png_files = list(VISUALS_DIR.glob("*.png"))
    html_files = list(VISUALS_DIR.glob("*.html"))
    
    stats = {
        "png_count": len(png_files),
        "html_count": len(html_files),
        "total": len(png_files) + len(html_files),
        "last_generated": None
    }
    
    all_files = png_files + html_files
    if all_files:
        latest_file = max(all_files, key=os.path.getmtime)
        stats["last_generated"] = datetime.fromtimestamp(latest_file.stat().st_mtime)
    
    return stats

def get_chat_history_stats():
    """Get statistics about chat history."""
    if not RESULTS_DIR.exists():
        return {"total": 0, "last_chat": None}
    
    md_files = get_files_by_pattern(RESULTS_DIR, "chat_result_*.md")
    
    stats = {
        "total": len(md_files),
        "last_chat": None
    }
    
    if md_files:
        latest_file = md_files[0]  # Already sorted by mtime
        stats["last_chat"] = datetime.fromtimestamp(latest_file.stat().st_mtime)
    
    return stats

# ---- Main Dashboard ----
def display_dashboard():
    st.title("📊 Plazza AI System Dashboard")
    
    # System Overview Cards
    st.subheader("System Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        kb_status, kb_time = check_kb_freshness()
        st.metric("Knowledge Base Status", kb_status)
        if kb_time:
            st.caption(f"Last Updated: {kb_time}")
    
    with col2:
        viz_stats = get_visualization_stats()
        st.metric("Total Visualizations", viz_stats["total"])
        if viz_stats["last_generated"]:
            st.caption(f"Last Generated: {viz_stats['last_generated'].strftime('%Y-%m-%d %H:%M')}")
    
    with col3:
        chat_stats = get_chat_history_stats()
        st.metric("Total Chat Queries", chat_stats["total"])
        if chat_stats["last_chat"]:
            st.caption(f"Last Chat: {chat_stats['last_chat'].strftime('%Y-%m-%d %H:%M')}")
    
    # Router Performance
    st.subheader("Advanced Router Performance")
    
    router_stats = get_router_performance_stats()
    
    if not router_stats or router_stats.get("total_queries", 0) == 0:
        st.info("No router data available yet.")
        return
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Routed Queries", router_stats["total_queries"])
    
    with col2:
        error_rate = router_stats["routing_errors"] / router_stats["total_queries"] * 100 if router_stats["total_queries"] > 0 else 0
        st.metric("Routing Error Rate", f"{error_rate:.1f}%")
    
    with col3:
        avg_length = router_stats["average_character_length"]
        st.metric("Avg Response Length", f"{avg_length:.0f} chars")
    
    # Agent Usage Chart
    if router_stats.get("agents_used"):
        # Create DataFrame from the agent usage dictionary
        agent_df = pd.DataFrame({
            "Agent": list(router_stats["agents_used"].keys()),
            "Count": list(router_stats["agents_used"].values())
        })
        
        # Create a pie chart
        fig = px.pie(
            agent_df, 
            values="Count", 
            names="Agent", 
            title="Query Distribution by Agent",
            color_discrete_sequence=px.colors.qualitative.Plotly
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    
    # Router Logs Over Time
    router_df = get_router_log_data()
    
    if not router_df.empty and "date" in router_df.columns:
        # Group by date and count
        date_counts = router_df.groupby("date").size().reset_index(name="count")
        
        fig = px.bar(
            date_counts, 
            x="date", 
            y="count", 
            title="Router Queries by Date",
            labels={"date": "Date", "count": "Number of Queries"}
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Hour of day distribution if we have enough data
        if len(router_df) > 5 and "hour" in router_df.columns:
            hour_counts = router_df.groupby("hour").size().reset_index(name="count")
            
            fig = px.bar(
                hour_counts, 
                x="hour", 
                y="count", 
                title="Query Distribution by Hour",
                labels={"hour": "Hour of Day", "count": "Number of Queries"}
            )
            st.plotly_chart(fig, use_container_width=True)

    # Advanced System Analytics
    if viz_stats["total"] > 0 and chat_stats["total"] > 0:
        st.subheader("System Analytics")
        
        # Calculate ratio of visualizations to queries
        viz_per_query = viz_stats["total"] / chat_stats["total"] if chat_stats["total"] > 0 else 0
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Visualizations per Query", f"{viz_per_query:.2f}")
        
        with col2:
            # Calculate HTML vs PNG ratio
            html_ratio = viz_stats["html_count"] / viz_stats["total"] * 100 if viz_stats["total"] > 0 else 0
            st.metric("Interactive Viz Ratio", f"{html_ratio:.1f}%")

if __name__ == "__main__":
    st.set_page_config(
        page_title="Plazza AI Dashboard",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    display_dashboard()