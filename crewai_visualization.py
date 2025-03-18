"""
CrewAI Visualization Module

This module provides visualization capabilities for CrewAI analysis results,
particularly for business analytics and sales data.

To use this module as part of your CrewAI workflow:

1. Import the visualize_analysis_results function
2. Call the function after your crew.kickoff() to generate visualizations
3. Access the enhanced markdown with embedded visualizations

Example:
```python
from crewai_visualization import visualize_analysis_results

# Run your CrewAI analysis
result = crew.kickoff()
save_analysis_results(result)

# Generate visualizations
viz_results = visualize_analysis_results(ANALYSIS_RESULTS_PATH)
print(f"Visualizations generated in {viz_results}")
```
"""

import os
import re
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
from datetime import datetime
from crewai.tools import BaseTool

# Set up styling
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

class CrewAIVisualization:
    """Class for creating visualizations from CrewAI analysis results"""
    
    def __init__(self, output_dir="visuals"):
        """
        Initialize the visualization module
        
        Args:
            output_dir (str): Directory to save visualizations to
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Set up color palette
        self.colors = sns.color_palette("viridis", 10)
        self.accent_colors = sns.color_palette("Set2", 8)
        
    def extract_product_names(self, product_ids, database_url=None):
        """
        Replace product IDs with product names by querying the database
        
        Args:
            product_ids (list): List of product IDs
            database_url (str): Database connection string
            
        Returns:
            dict: Mapping of product IDs to product names
        """
        import psycopg2
        import psycopg2.extras
        from dotenv import load_dotenv
        
        load_dotenv()
        
        # Use provided database_url or get from environment
        if not database_url:
            database_url = os.getenv("DATABASE_URL_USER_TRANSACTIONS")
            
        if not database_url:
            print("Warning: No database connection available. Using product IDs instead of names.")
            return {pid: pid for pid in product_ids}
            
        try:
            conn = psycopg2.connect(database_url)
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                placeholders = ','.join(['%s'] * len(product_ids))
                query = f"SELECT product_id, medicine_name FROM order_items WHERE product_id IN ({placeholders}) GROUP BY product_id, medicine_name"
                cursor.execute(query, product_ids)
                results = cursor.fetchall()
                
                # Create mapping dictionary
                product_names = {row['product_id']: row['medicine_name'] for row in results}
                
                # Fill in any missing values with the original ID
                for pid in product_ids:
                    if pid not in product_names:
                        product_names[pid] = pid
                        
                return product_names
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return {pid: pid for pid in product_ids}
        finally:
            if conn:
                conn.close()
    
    def parse_markdown_content(self, content):
        """
        Parse markdown content into structured data for visualization
        
        Args:
            content (str): Markdown content from analysis
            
        Returns:
            dict: Structured data extracted from markdown
        """
        data = {
            "top_products": [],
            "sales_metrics": {},
            "repeat_customers": {},
            "recommendations": []
        }
        
        # Extract top products section
        top_products_match = re.search(r"Top 5 Selling Products by Quantity[^\n]*:(.*?)(?=-|\n\n)", content, re.DOTALL)
        if top_products_match:
            products_text = top_products_match.group(1)
            product_matches = re.findall(r"Product ID: ([^,]+), Quantity: (\d+)", products_text)
            
            if product_matches:
                product_ids = [match[0] for match in product_matches]
                quantities = [int(match[1]) for match in product_matches]
                
                # Replace product IDs with names
                product_names = self.extract_product_names(product_ids)
                
                for i, (pid, qty) in enumerate(zip(product_ids, quantities)):
                    name = product_names.get(pid, pid)
                    data["top_products"].append({
                        "product_id": pid,
                        "product_name": name,
                        "quantity": qty
                    })
        
        # Extract metrics
        avg_order_match = re.search(r"Average Order Value[^\n]*: \$([0-9.]+)", content)
        if avg_order_match:
            data["sales_metrics"]["avg_order_value"] = float(avg_order_match.group(1))
            
        avg_items_match = re.search(r"Average Items per Order[^\n]*: ([0-9.]+)", content)
        if avg_items_match:
            data["sales_metrics"]["avg_items_per_order"] = float(avg_items_match.group(1))
            
        # Extract repeat customer percentages
        repeat_match = re.search(r"Repeat Customers: ([0-9.]+)%", content)
        if repeat_match:
            data["repeat_customers"]["repeat_percentage"] = float(repeat_match.group(1))
            
        onetime_match = re.search(r"One-Time Customers: ([0-9.]+)%", content)
        if onetime_match:
            data["repeat_customers"]["onetime_percentage"] = float(onetime_match.group(1))
        
        # Extract recommendations
        recommendations_match = re.search(r"#### 4\. Actionable Recommendations(.*?)####", content, re.DOTALL)
        if recommendations_match:
            rec_text = recommendations_match.group(1)
            rec_items = re.findall(r"\d+\.\s+\*\*([^:]+)\*\*:(.*?)(?=\d+\.\s+\*\*|$)", rec_text, re.DOTALL)
            
            for title, content in rec_items:
                data["recommendations"].append({
                    "title": title.strip(),
                    "content": content.strip()
                })
                
        return data
    
    def create_sales_bar_chart(self, data, filename=None):
        """
        Create a bar chart of top selling products
        
        Args:
            data (dict): Parsed data from markdown
            filename (str): Output filename (optional)
            
        Returns:
            str: Path to saved visualization file
        """
        if not data["top_products"]:
            return None
            
        # Extract data
        df = pd.DataFrame(data["top_products"])
        
        # Create the plot
        plt.figure(figsize=(12, 8))
        ax = sns.barplot(x="product_name", y="quantity", data=df, palette="viridis")
        
        # Customize the plot
        plt.title("Top Selling Products by Quantity", fontsize=18)
        plt.xlabel("Product Name", fontsize=14)
        plt.ylabel("Quantity Sold", fontsize=14)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        
        # Add values on top of bars
        for i, v in enumerate(df["quantity"]):
            ax.text(i, v + 0.5, str(v), ha='center', fontsize=12)
            
        # Save the plot
        if not filename:
            filename = f"{self.output_dir}/top_products_{self.timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches="tight")
        plt.close()
        
        return filename
    
    def create_customer_pie_chart(self, data, filename=None):
        """
        Create a pie chart of repeat vs one-time customers
        
        Args:
            data (dict): Parsed data from markdown
            filename (str): Output filename (optional)
            
        Returns:
            str: Path to saved visualization file
        """
        if not data["repeat_customers"]:
            return None
            
        # Extract data
        repeat = data["repeat_customers"].get("repeat_percentage", 0)
        onetime = data["repeat_customers"].get("onetime_percentage", 0)
        
        # If onetime is 0 but repeat is not 100, adjust to make total 100%
        if onetime == 0 and repeat != 100:
            onetime = 100 - repeat
            
        labels = ['Repeat Customers', 'One-Time Customers']
        values = [repeat, onetime]
        
        # Create the pie chart using Plotly for better interactivity
        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=.4,
            textinfo='label+percent',
            marker=dict(colors=['#2ECC71', '#3498DB'])
        )])
        
        fig.update_layout(
            title="Customer Retention Analysis",
            font=dict(size=14),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            annotations=[dict(text="Customer<br>Types", x=0.5, y=0.5, font_size=14, showarrow=False)]
        )
        
        # Save the plot
        if not filename:
            filename = f"{self.output_dir}/customer_retention_{self.timestamp}.html"
        fig.write_html(filename)
        
        # Also create a static image for embedding
        img_filename = f"{self.output_dir}/customer_retention_{self.timestamp}.png"
        fig.write_image(img_filename)
        
        return filename
    
    def create_metrics_dashboard(self, data, filename=None):
        """
        Create a dashboard with key business metrics
        
        Args:
            data (dict): Parsed data from markdown
            filename (str): Output filename (optional)
            
        Returns:
            str: Path to saved visualization file
        """
        # Create a subplot figure with 2 rows and 2 columns
        fig = make_subplots(
            rows=2, cols=2,
            specs=[
                [{"type": "indicator"}, {"type": "indicator"}],
                [{"type": "bar", "colspan": 2}, None]
            ],
            subplot_titles=("Average Order Value", "Average Items per Order", "Top Selling Products")
        )
        
        # Add average order value indicator
        fig.add_trace(go.Indicator(
            mode="number+delta",
            value=data["sales_metrics"].get("avg_order_value", 0),
            number={"prefix": "$", "font": {"size": 40}},
            delta={"reference": 150, "relative": True, "position": "bottom"},
            title={"text": "Avg Order Value"}
        ), row=1, col=1)
        
        # Add average items per order indicator
        fig.add_trace(go.Indicator(
            mode="number+delta",
            value=data["sales_metrics"].get("avg_items_per_order", 0),
            number={"font": {"size": 40}},
            delta={"reference": 1.5, "relative": True, "position": "bottom"},
            title={"text": "Avg Items per Order"}
        ), row=1, col=2)
        
        # Add top products bar chart
        if data["top_products"]:
            df = pd.DataFrame(data["top_products"])
            fig.add_trace(go.Bar(
                x=df["product_name"],
                y=df["quantity"],
                marker=dict(color=px.colors.qualitative.Vivid),
                text=df["quantity"],
                textposition="auto"
            ), row=2, col=1)
        
        # Update layout
        fig.update_layout(
            title_text="Business Performance Dashboard",
            height=800,
            width=1200,
            showlegend=False,
            template="plotly_white"
        )
        
        # Save the plot
        if not filename:
            filename = f"{self.output_dir}/metrics_dashboard_{self.timestamp}.html"
        fig.write_html(filename)
        
        # Also create static image
        img_filename = f"{self.output_dir}/metrics_dashboard_{self.timestamp}.png"
        fig.write_image(img_filename)
        
        return filename
    
    def generate_all_visualizations(self, markdown_content, output_dir=None):
        """
        Generate all visualizations from markdown content
        
        Args:
            markdown_content (str): Markdown content from analysis
            output_dir (str): Directory to save visualizations to (optional)
            
        Returns:
            dict: Paths to all generated visualization files
        """
        if output_dir:
            self.output_dir = output_dir
            os.makedirs(output_dir, exist_ok=True)
            
        # Parse the markdown content
        data = self.parse_markdown_content(markdown_content)
        
        # Generate visualizations
        results = {}
        
        # Create bar chart
        bar_chart = self.create_sales_bar_chart(data)
        if bar_chart:
            results["top_products_chart"] = bar_chart
            
        # Create pie chart
        pie_chart = self.create_customer_pie_chart(data)
        if pie_chart:
            results["customer_retention_chart"] = pie_chart
            
        # Create dashboard
        dashboard = self.create_metrics_dashboard(data)
        if dashboard:
            results["metrics_dashboard"] = dashboard
            
        return results
    
    def embed_visualizations_in_markdown(self, markdown_content, visualization_paths):
        """
        Embed visualizations into markdown content
        
        Args:
            markdown_content (str): Original markdown content
            visualization_paths (dict): Paths to visualization files
            
        Returns:
            str: Enhanced markdown with embedded visualizations
        """
        # Create visualization section
        visualization_md = "\n\n## Visualizations\n\n"
        
        # Add dashboard if available
        if "metrics_dashboard" in visualization_paths:
            dashboard_png = visualization_paths["metrics_dashboard"].replace(".html", ".png")
            visualization_md += f"### Business Metrics Dashboard\n\n"
            visualization_md += f"![Business Metrics Dashboard]({dashboard_png})\n\n"
            visualization_md += f"[Interactive Dashboard]({visualization_paths['metrics_dashboard']})\n\n"
        
        # Add top products chart if available
        if "top_products_chart" in visualization_paths:
            visualization_md += f"### Top Selling Products\n\n"
            visualization_md += f"![Top Products]({visualization_paths['top_products_chart']})\n\n"
        
        # Add customer retention chart if available
        if "customer_retention_chart" in visualization_paths:
            retention_png = visualization_paths["customer_retention_chart"].replace(".html", ".png")
            visualization_md += f"### Customer Retention Analysis\n\n"
            visualization_md += f"![Customer Retention]({retention_png})\n\n"
            visualization_md += f"[Interactive Chart]({visualization_paths['customer_retention_chart']})\n\n"
        
        # Insert visualizations before recommendations section
        if "#### 4. Actionable Recommendations" in markdown_content:
            enhanced_md = markdown_content.replace(
                "#### 4. Actionable Recommendations", 
                f"{visualization_md}\n#### 4. Actionable Recommendations"
            )
        else:
            # If no recommendations section, add visualizations at the end
            enhanced_md = markdown_content + visualization_md
            
        return enhanced_md


def visualize_analysis_results(input_file, output_dir="visuals"):
    """
    Generate visualizations from analysis results file
    
    Args:
        input_file (str): Path to analysis results markdown file
        output_dir (str): Directory to save visualizations to
        
    Returns:
        dict: Paths to generated visualization files
    """
    # Read the markdown content
    with open(input_file, 'r') as f:
        markdown_content = f.read()
        
    # Create visualizer
    visualizer = CrewAIVisualization(output_dir=output_dir)
    
    # Generate visualizations
    viz_paths = visualizer.generate_all_visualizations(markdown_content)
    
    # Enhance markdown with visualizations
    enhanced_md = visualizer.embed_visualizations_in_markdown(markdown_content, viz_paths)
    
    # Save enhanced markdown
    enhanced_path = os.path.join(output_dir, os.path.basename(input_file))
    with open(enhanced_path, 'w') as f:
        f.write(enhanced_md)
        
    # Return paths to all generated files
    viz_paths["enhanced_markdown"] = enhanced_path
    return viz_paths


# Direct integration with CrewAI
class VisualizationTool(BaseTool):
    """
    Integration of visualization capabilities as a CrewAI tool
    
    This allows the visualization module to be used directly within the CrewAI workflow
    as a tool that agents can call to generate visualizations from analysis results.
    """
    
    name: str = "VisualizationTool"
    description: str = """Generate visualizations from analysis results.
    
    This tool creates visual representations of business analysis data, including:
    - Bar charts for product sales
    - Pie charts for customer retention
    - Interactive dashboards for business metrics
    
    Simply call this tool to process the latest analysis results and generate
    visualizations that make the insights more accessible and actionable.
    
    No parameters are needed. The tool automatically processes the most recent analysis.
    """
    
    def _run(self) -> str:
        """Run the visualization tool on the latest analysis results"""
        try:
            # Find the latest analysis results file
            import os
            from datetime import datetime
            
            # Look in standard locations
            potential_paths = [
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "sales_ai_run_result.md"),
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "knowledge", "sales_analysis_results.md"),
            ]
            
            # Find the most recent file
            valid_paths = [(p, os.path.getmtime(p)) for p in potential_paths if os.path.exists(p)]
            if not valid_paths:
                return "No analysis results found to visualize."
                
            # Sort by modification time (most recent first)
            valid_paths.sort(key=lambda x: x[1], reverse=True)
            latest_file = valid_paths[0][0]
            
            # Generate visualizations
            visuals_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "visuals")
            viz_results = visualize_analysis_results(latest_file, output_dir=visuals_dir)
            
            # Format the results for the agent
            result_summary = [
                f"# Visualizations Created Successfully",
                f"",
                f"Analysis from {os.path.basename(latest_file)} visualized with:",
                f"",
            ]
            
            for viz_type, viz_path in viz_results.items():
                if viz_type == "enhanced_markdown":
                    continue
                result_summary.append(f"- **{viz_type.replace('_', ' ').title()}**: `{os.path.basename(viz_path)}`")
            
            result_summary.append(f"")
            result_summary.append(f"All visualizations are saved in: `{visuals_dir}`")
            result_summary.append(f"")
            result_summary.append(f"Enhanced markdown with embedded visualizations: `{os.path.basename(viz_results.get('enhanced_markdown', ''))}`")
            
            return "\n".join(result_summary)
            
        except Exception as e:
            return f"Error generating visualizations: {str(e)}"

if __name__ == "__main__":
    import argparse
    import sys
    
    # If running from CrewAI import path, make sure we have BaseTool available
    try:
        from crewai.tools import BaseTool
    except ImportError:
        try:
            # Check if we're in the CrewAI project
            import os
            sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            from crewai.tools import BaseTool
        except ImportError:
            # Define a dummy BaseTool for standalone usage
            class BaseTool:
                name: str = "BaseTool"
                description: str = "Base tool class"
                
                def _run(self, *args, **kwargs):
                    pass
    
    parser = argparse.ArgumentParser(description="Generate visualizations from CrewAI analysis results")
    parser.add_argument("input_file", help="Path to analysis results markdown file")
    parser.add_argument("--output-dir", default="visuals", help="Directory to save visualizations to")
    
    args = parser.parse_args()
    
    # Generate visualizations
    results = visualize_analysis_results(args.input_file, args.output_dir)
    
    # Print results
    print(f"Visualizations generated in {args.output_dir}:")
    for key, path in results.items():
        print(f"  - {key}: {path}")