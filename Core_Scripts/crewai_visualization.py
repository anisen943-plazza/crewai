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

# Or use directly with analysis content:
viz_results = visualize_analysis_results(content=result)

# Generate with JSON output for dashboard integration
viz_results = visualize_analysis_results(content=result, enable_json_output=True)
print(f"JSON data available at: {viz_results['json_path']}")
```

The module also provides visualization tools for CrewAI:
- VisualizationTool: General-purpose visualization tool for agents
- TopProductsChartTool: Specialized tool for product sales charts
- CustomerRetentionChartTool: Specialized tool for retention analysis
- MetricsDashboardTool: Specialized tool for business metrics dashboards

All tools can be used with either file paths or inline content.

ENHANCEMENT (March 24, 2025):
- Added JSON export capability for dashboard integration
- Implemented enable_json_output parameter with JSON path in results
- Designed for maximum reuse with external visualization systems

The JSON output follows the same structure as the parsed markdown sections
and can be used to feed external visualization systems.
"""

import os
import re
import json
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import zipfile

# Import BaseTool for CrewAI integration
try:
    from crewai.tools import BaseTool
except ImportError:
    # Define a dummy BaseTool for standalone usage
    class BaseTool:
        name: str = "BaseTool"
        description: str = "Base tool class"
        
        def _run(self, *args, **kwargs):
            pass
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
from datetime import datetime
from crewai.tools import BaseTool
import numpy as np
import matplotlib.colors as mcolors
from textwrap import dedent

# Set up styling with Plazza colors
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# Plazza brand colors
PLAZZA_PRIMARY = "#FF0084"  # Bright pink
PLAZZA_BACKGROUND = "#fafafa"  # Light gray 
PLAZZA_CARD_BG = "white"
PLAZZA_CARD_SHADOW = "rgba(0,0,0,0.1)"

# Create a custom color palette based on Plazza primary color
plazza_palette = sns.color_palette([
    PLAZZA_PRIMARY,  # Primary 
    "#3498DB",       # Blue
    "#2ECC71",       # Green
    "#9B59B6",       # Purple
    "#F1C40F",       # Yellow
    "#E74C3C"        # Red
])

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
        
        # Set up Plazza color palette
        self.colors = plazza_palette
        self.accent_colors = sns.color_palette("Set2", 8)
        
        # Plazza brand colors as instance variables
        self.primary_color = PLAZZA_PRIMARY
        self.background_color = PLAZZA_BACKGROUND
        self.card_bg_color = PLAZZA_CARD_BG
        self.card_shadow = PLAZZA_CARD_SHADOW
        
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
            "time_series_data": {},
            "geographic_data": {},
            "comparative_data": {},
            "recommendations": []
        }
        
        # Extract top products section with enhanced pattern matching
        top_products_patterns = [
            r"Top 5 Selling Products by Quantity[^\n]*:(.*?)(?=-|\n\n)", 
            r"Top (?:\d+) Products by (?:Sales|Quantity|Revenue)[^\n]*:(.*?)(?=\n\n|\n##)",
            r"Best Selling Products[^\n]*:(.*?)(?=\n\n|\n##)"
        ]
        
        for pattern in top_products_patterns:
            top_products_match = re.search(pattern, content, re.DOTALL)
            if top_products_match:
                products_text = top_products_match.group(1)
                # Try multiple patterns for product extraction
                product_patterns = [
                    r"Product(?:\s+ID)?:\s+([^,]+),\s+Quantity:\s+(\d+)",
                    r"([A-Z0-9-]+)\s*-\s*([^:]+):\s*(\d+)",
                    r"([^:]+)\s*:\s*(\d+)\s+units",
                ]
                
                for p_pattern in product_patterns:
                    product_matches = re.findall(p_pattern, products_text)
                    if product_matches:
                        if len(product_matches[0]) == 2:  # Pattern 1 format
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
                        elif len(product_matches[0]) == 3:  # Pattern 2 format
                            for pid, name, qty in product_matches:
                                data["top_products"].append({
                                    "product_id": pid.strip(),
                                    "product_name": name.strip(),
                                    "quantity": int(qty)
                                })
                        break
                
                if data["top_products"]:
                    break
        
        # Extract metrics with more flexible patterns
        metrics_patterns = {
            "avg_order_value": [
                r"Average Order Value[^\n]*: \$([0-9.]+)",
                r"Average Order Value[^\n]*: ₹([0-9.]+)",
                r"Avg\. Order Value:\s*\$?([0-9.]+)"
            ],
            "avg_items_per_order": [
                r"Average Items per Order[^\n]*: ([0-9.]+)", 
                r"Avg\. Items/Order:\s*([0-9.]+)"
            ],
            "total_sales": [
                r"Total Sales[^\n]*: \$([0-9,.]+)",
                r"Total Sales[^\n]*: ₹([0-9,.]+)",
                r"Total Revenue:\s*\$?([0-9,.]+)",
            ],
            "conversion_rate": [
                r"Conversion Rate[^\n]*: ([0-9.]+)%"
            ]
        }
        
        for metric, patterns in metrics_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, content)
                if match:
                    # Clean value by removing commas
                    value_str = match.group(1).replace(',', '')
                    data["sales_metrics"][metric] = float(value_str)
                    break
        
        # Extract repeat customer percentages
        retention_patterns = {
            "repeat_percentage": [
                r"Repeat Customers: ([0-9.]+)%",
                r"Repeat (?:Customers|Buyers|Purchasers):\s*([0-9.]+)%"
            ],
            "onetime_percentage": [
                r"One-Time Customers: ([0-9.]+)%",
                r"(?:One|First)-Time (?:Customers|Buyers|Purchasers):\s*([0-9.]+)%"
            ],
            "churn_rate": [
                r"Churn Rate: ([0-9.]+)%"
            ]
        }
        
        for metric, patterns in retention_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, content)
                if match:
                    data["repeat_customers"][metric] = float(match.group(1))
                    break
        
        # Extract time series data (monthly sales, trends)
        time_series_match = re.search(r"(?:Monthly|Quarterly) (?:Sales|Revenue) Trend[^\n]*:(.*?)(?=\n\n|\n##)", content, re.DOTALL)
        if time_series_match:
            ts_text = time_series_match.group(1)
            # Look for month-value pairs
            ts_matches = re.findall(r"(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[^\d]*(\d+)", ts_text)
            
            # Also try to match YYYY-MM format
            if not ts_matches:
                ts_matches = re.findall(r"(20\d{2}-\d{2})[^\d]*(\d+)", ts_text)
            
            if ts_matches:
                data["time_series_data"]["periods"] = [m[0] for m in ts_matches]
                data["time_series_data"]["values"] = [int(m[1]) for m in ts_matches]
        
        # Try to extract geographic data
        geo_match = re.search(r"(?:Regional|Geographic|Location)[^\n]*Distribution[^\n]*:(.*?)(?=\n\n|\n##)", content, re.DOTALL)
        if geo_match:
            geo_text = geo_match.group(1)
            geo_matches = re.findall(r"([^:,]+):\s*(\d+)%?", geo_text)
            
            if geo_matches:
                data["geographic_data"]["regions"] = [m[0].strip() for m in geo_matches]
                data["geographic_data"]["values"] = [int(m[1]) for m in geo_matches]
        
        # Extract comparative data (this period vs last)
        comp_match = re.search(r"Period[^\n]*Comparison[^\n]*:(.*?)(?=\n\n|\n##)", content, re.DOTALL)
        if comp_match:
            comp_text = comp_match.group(1)
            metric_matches = re.findall(r"([^:]+):\s*([+-]?\d+)%", comp_text)
            
            if metric_matches:
                data["comparative_data"]["metrics"] = [m[0].strip() for m in metric_matches]
                data["comparative_data"]["changes"] = [int(m[1]) for m in metric_matches]
        
        # Extract recommendations with improved pattern
        rec_patterns = [
            r"#### [0-9]\. Actionable Recommendations(.*?)(?=####|\Z)",
            r"## Recommendations(.*?)(?=##|\Z)",
            r"### [0-9]\. Actionable Recommendations(.*?)(?=###|\Z)",
            r"Recommendations:(.*?)(?=##|\Z)"
        ]
        
        for pattern in rec_patterns:
            recommendations_match = re.search(pattern, content, re.DOTALL)
            if recommendations_match:
                rec_text = recommendations_match.group(1)
                
                # Try different patterns for recommendation formats
                format_patterns = [
                    r"\d+\.\s+\*\*([^:]+)\*\*:(.*?)(?=\d+\.\s+\*\*|$)",  # Numbered with bold title
                    r"\*\s+\*\*([^:]+)\*\*:(.*?)(?=\*\s+\*\*|$)",         # Bullet with bold title
                    r"\d+\.\s+([^:]+):(.*?)(?=\d+\.\s+|$)",               # Numbered without bold
                    r"\*\s+([^:]+):(.*?)(?=\*\s+|$)"                      # Bullet without bold
                ]
                
                for fp in format_patterns:
                    rec_items = re.findall(fp, rec_text, re.DOTALL)
                    if rec_items:
                        for title, content in rec_items:
                            data["recommendations"].append({
                                "title": title.strip(),
                                "content": content.strip()
                            })
                        break
                
                if data["recommendations"]:
                    break
        
        # Ensure we have at least empty structures for visualization functions
        if not data["top_products"] and "total_sales" in data["sales_metrics"]:
            # Try to extract from tables if present
            table_match = re.search(r"\|[^|]+\|[^|]+\|.*?\n\|[-:]+\|[-:]+\|.*?\n((?:\|[^|]+\|[^|]+\|.*?\n)+)", content)
            if table_match:
                table_content = table_match.group(1)
                rows = table_content.strip().split("\n")
                
                # Try to determine if this is a product table
                if len(rows) > 0:
                    first_row = rows[0]
                    if "product" in first_row.lower() or "item" in first_row.lower():
                        for row in rows:
                            cells = [cell.strip() for cell in row.split("|")[1:-1]]
                            if len(cells) >= 2:
                                try:
                                    name = cells[0]
                                    quantity = int(cells[1].replace(',', ''))
                                    data["top_products"].append({
                                        "product_id": f"P{len(data['top_products'])+1}",
                                        "product_name": name,
                                        "quantity": quantity
                                    })
                                except (ValueError, IndexError):
                                    pass
                
        return data
    
    def create_sales_bar_chart(self, data, filename=None):
        """
        Create a bar chart of top selling products with Plazza styling
        
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
        
        # Create a Plotly figure instead of matplotlib for better interactivity
        import matplotlib.colors as mcolors
            
        # Create a color gradient based on Plazza primary color
        base_color = mcolors.to_rgb(self.primary_color)
        n_colors = len(df) if len(df) > 0 else 1
        colors = []
            
        for i in range(n_colors):
            # Create gradient effect
            factor = 0.7 + (0.3 * (i / max(1, n_colors - 1)))
            color = tuple(min(1.0, c * factor) for c in base_color)
            colors.append(mcolors.to_hex(color))
        
        # Create the Plotly figure
        fig = go.Figure()
        
        # Add bar chart
        fig.add_trace(go.Bar(
            x=df["product_name"],
            y=df["quantity"],
            marker=dict(color=colors),
            text=df["quantity"],
            textposition="auto",
            textfont=dict(family="system-ui, sans-serif", size=12),
            hovertemplate="<b>%{x}</b><br>Quantity: %{y}<extra></extra>"
        ))
        
        # Apply Plazza styling to the layout
        fig.update_layout(
            title={
                'text': "Top Selling Products by Quantity",
                'font': {'size': 22, 'color': self.primary_color, 'family': "system-ui, sans-serif"},
                'y': 0.95
            },
            font=dict(family="system-ui, sans-serif", size=14),
            paper_bgcolor=self.background_color,
            plot_bgcolor=self.background_color,
            margin=dict(t=80, b=100, l=40, r=40),
            height=600,
            width=900
        )
        
        # Update axes
        fig.update_xaxes(
            title_text="Product Name",
            title_font=dict(family="system-ui, sans-serif", size=14, color="#666"),
            tickfont=dict(family="system-ui, sans-serif", size=12),
            tickangle=-45
        )
        
        fig.update_yaxes(
            title_text="Quantity Sold",
            title_font=dict(family="system-ui, sans-serif", size=14, color="#666"),
            tickfont=dict(family="system-ui, sans-serif", size=12),
            gridcolor='rgba(0,0,0,0.05)'
        )
        
        # Add a styled card-like border
        fig.update_layout(
            shapes=[
                dict(
                    type="rect",
                    xref="paper",
                    yref="paper",
                    x0=0,
                    y0=0,
                    x1=1,
                    y1=1,
                    line=dict(
                        color="rgba(0,0,0,0.1)",
                        width=1,
                    ),
                    fillcolor="rgba(0,0,0,0)",
                    layer="below"
                )
            ]
        )
        
        # Save the plot as both HTML and PNG
        if not filename:
            filename_base = f"{self.output_dir}/top_products_{self.timestamp}"
            html_filename = f"{filename_base}.html"
            png_filename = f"{filename_base}.png"
        else:
            html_filename = filename
            png_filename = filename.replace('.html', '.png') if filename.endswith('.html') else f"{filename}.png"
        
        # Create custom HTML with Plazza styling
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Plazza Top Products</title>
    <style>
        :root {{ --plazza: {self.primary_color}; }}
        body {{ 
            font-family: system-ui, sans-serif;
            margin: 0;
            padding: 20px;
            background: {self.background_color};
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .card {{
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        h1, h2 {{ color: var(--plazza); }}
        .chart {{ height: 600px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <h2>Top Selling Products</h2>
            <div id="chart" class="chart"></div>
        </div>
    </div>
</body>
</html>"""
        
        # Combine with Plotly's HTML
        plotly_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        final_html = html_content.replace('<div id="chart" class="chart"></div>', plotly_html)
        
        with open(html_filename, 'w') as f:
            f.write(final_html)
        
        # Save the PNG for embedding
        fig.write_image(png_filename)
        
        return html_filename
    
    def create_customer_pie_chart(self, data, filename=None):
        """
        Create a pie chart of repeat vs one-time customers with Plazza styling
        
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
        
        # Create the pie chart using Plotly with Plazza styling
        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=.4,
            textinfo='label+percent',
            marker=dict(colors=[self.primary_color, '#3498DB']),
            textfont=dict(size=14, family="system-ui, sans-serif"),
            pull=[0.05, 0],  # Slightly pull out the first slice
            insidetextorientation='radial'
        )])
        
        # Apply Plazza styling to the layout
        fig.update_layout(
            title={
                'text': "Customer Retention Analysis",
                'font': {'size': 22, 'color': self.primary_color, 'family': "system-ui, sans-serif"},
                'y': 0.95
            },
            font=dict(family="system-ui, sans-serif", size=14),
            legend=dict(
                orientation="h", 
                yanchor="bottom", 
                y=1.02, 
                xanchor="right", 
                x=1,
                font=dict(family="system-ui, sans-serif")
            ),
            annotations=[
                dict(
                    text="Customer<br>Types", 
                    x=0.5, 
                    y=0.5, 
                    font_size=16, 
                    font_family="system-ui, sans-serif",
                    font_color=self.primary_color,
                    showarrow=False
                )
            ],
            paper_bgcolor=self.background_color,
            plot_bgcolor=self.background_color,
            margin=dict(t=80, b=40, l=40, r=40),
        )
        
        # Add a styled card-like border
        fig.update_layout(
            shapes=[
                dict(
                    type="rect",
                    xref="paper",
                    yref="paper",
                    x0=0,
                    y0=0,
                    x1=1,
                    y1=1,
                    line=dict(
                        color="rgba(0,0,0,0.1)",
                        width=1,
                    ),
                    fillcolor="rgba(0,0,0,0)",
                    layer="below"
                )
            ]
        )
        
        # Save the plot
        if not filename:
            filename = f"{self.output_dir}/customer_retention_{self.timestamp}.html"
        
        # Write the HTML with custom CSS for Plazza styling
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Plazza Customer Retention</title>
    <style>
        :root {{ --plazza: {self.primary_color}; }}
        body {{ 
            font-family: system-ui, sans-serif;
            margin: 0;
            padding: 20px;
            background: {self.background_color};
        }}
        .card {{
            background: {self.card_bg_color};
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 1px 3px {self.card_shadow};
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1, h2 {{ color: var(--plazza); }}
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <h2>Customer Retention Analysis</h2>
            <div id="chart" style="height: 500px;"></div>
        </div>
    </div>
</body>
</html>"""
        
        # Combine with Plotly's HTML
        plotly_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        final_html = html_content.replace('<div id="chart" style="height: 500px;"></div>', plotly_html)
        
        with open(filename, 'w') as f:
            f.write(final_html)
        
        # Also create a static image for embedding
        img_filename = f"{self.output_dir}/customer_retention_{self.timestamp}.png"
        fig.write_image(img_filename)
        
        return filename
    
    def create_metrics_dashboard(self, data, filename=None):
        """
        Create a dashboard with key business metrics using Plazza styling
        
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
        
        # Add average order value indicator with Plazza styling
        fig.add_trace(go.Indicator(
            mode="number+delta",
            value=data["sales_metrics"].get("avg_order_value", 0),
            number={
                "prefix": "₹", 
                "font": {"size": 40, "color": self.primary_color, "family": "system-ui, sans-serif"}
            },
            delta={
                "reference": 150, 
                "relative": True, 
                "position": "bottom",
                "font": {"size": 14, "family": "system-ui, sans-serif"}
            },
            title={
                "text": "Avg Order Value",
                "font": {"size": 16, "family": "system-ui, sans-serif", "color": "#666"}
            }
        ), row=1, col=1)
        
        # Add average items per order indicator with Plazza styling
        fig.add_trace(go.Indicator(
            mode="number+delta",
            value=data["sales_metrics"].get("avg_items_per_order", 0),
            number={
                "font": {"size": 40, "color": self.primary_color, "family": "system-ui, sans-serif"}
            },
            delta={
                "reference": 1.5, 
                "relative": True, 
                "position": "bottom",
                "font": {"size": 14, "family": "system-ui, sans-serif"}
            },
            title={
                "text": "Avg Items per Order",
                "font": {"size": 16, "family": "system-ui, sans-serif", "color": "#666"}
            }
        ), row=1, col=2)
        
        # Add top products bar chart with Plazza styling
        if data["top_products"]:
            df = pd.DataFrame(data["top_products"])
            
            # Create color gradient based on Plazza primary color
            import matplotlib.colors as mcolors
            import numpy as np
            
            # Create a color gradient based on Plazza primary color
            base_color = mcolors.to_rgb(self.primary_color)
            n_colors = len(df) if len(df) > 0 else 1
            colors = []
            
            for i in range(n_colors):
                # Create gradient effect
                factor = 0.7 + (0.3 * (i / max(1, n_colors - 1)))
                color = tuple(min(1.0, c * factor) for c in base_color)
                colors.append(mcolors.to_hex(color))
            
            fig.add_trace(go.Bar(
                x=df["product_name"],
                y=df["quantity"],
                marker=dict(color=colors),
                text=df["quantity"],
                textposition="auto",
                textfont=dict(family="system-ui, sans-serif", size=12),
                hovertemplate="<b>%{x}</b><br>Quantity: %{y}<extra></extra>"
            ), row=2, col=1)
            
            # Update xaxis for better readability
            fig.update_xaxes(
                tickangle=-45,
                tickfont=dict(family="system-ui, sans-serif", size=10),
                title_text="",
                row=2, col=1
            )
            
            # Update yaxis
            fig.update_yaxes(
                title_text="Quantity Sold",
                title_font=dict(family="system-ui, sans-serif", size=12, color="#666"),
                tickfont=dict(family="system-ui, sans-serif", size=10),
                row=2, col=1
            )
        
        # Update layout with Plazza styling
        fig.update_layout(
            title={
                'text': "Plazza Performance Insights",
                'font': {'size': 24, 'color': self.primary_color, 'family': "system-ui, sans-serif"},
                'y': 0.98
            },
            height=800,
            width=1200,
            showlegend=False,
            paper_bgcolor=self.background_color,
            plot_bgcolor=self.background_color,
            margin=dict(t=100, b=40, l=40, r=40),
            font=dict(family="system-ui, sans-serif"),
        )
        
        # Update subplot titles to match Plazza styling
        for i in fig['layout']['annotations']:
            i['font'] = dict(family="system-ui, sans-serif", size=16, color=self.primary_color)
            i['y'] = i['y'] - 0.03  # Adjust the vertical position of titles
        
        # Save the plot
        if not filename:
            filename = f"{self.output_dir}/metrics_dashboard_{self.timestamp}.html"
        
        # Create custom HTML with Plazza styling
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Plazza Insights</title>
    <style>
        :root {{ --plazza: {self.primary_color}; }}
        body {{ 
            font-family: system-ui, sans-serif;
            margin: 0;
            padding: 20px;
            background: {self.background_color};
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .card {{
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 24px;
        }}
        .kpi {{
            text-align: center;
            padding: 16px;
        }}
        .kpi-value {{
            font-size: 32px;
            font-weight: bold;
            color: var(--plazza);
        }}
        .kpi-label {{
            font-size: 14px;
            color: #666;
        }}
        h1, h2 {{ color: var(--plazza); }}
        .chart {{ height: 600px; }}
        .tooltip {{
            position: absolute;
            padding: 8px;
            background: rgba(0,0,0,0.8);
            color: white;
            border-radius: 4px;
            font-size: 12px;
            pointer-events: none;
        }}
        .insight-card {{
            background: #f8f9fa;
            padding: 16px;
            border-radius: 8px;
            margin-bottom: 16px;
        }}
        .insight-title {{
            font-weight: bold;
            color: var(--plazza);
            margin-bottom: 8px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Plazza Performance Insights</h1>
        
        <div class="card">
            <div id="dashboard" class="chart"></div>
        </div>

        <div class="card">
            <h2>Key Findings</h2>
            <div class="grid">
                <div class="insight-card">
                    <div class="insight-title">Sales Performance</div>
                    <p>Average order value of ₹{data["sales_metrics"].get("avg_order_value", 0):.2f} with 
                    {data["sales_metrics"].get("avg_items_per_order", 0):.1f} items per order on average.</p>
                </div>
                <div class="insight-card">
                    <div class="insight-title">Customer Loyalty</div>
                    <p>{data["repeat_customers"].get("repeat_percentage", 0)}% of customers are repeat buyers, 
                    showing strong service satisfaction and product quality.</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""
        
        # Combine with Plotly's HTML
        plotly_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        final_html = html_content.replace('<div id="dashboard" class="chart"></div>', plotly_html)
        
        with open(filename, 'w') as f:
            f.write(final_html)
        
        # Also create static image
        img_filename = f"{self.output_dir}/metrics_dashboard_{self.timestamp}.png"
        fig.write_image(img_filename)
        
        return filename
    
    def create_time_series_chart(self, data, filename=None):
        """
        Create a time series chart for trend analysis with Plazza styling
        
        Args:
            data (dict): Parsed data from markdown
            filename (str): Output filename (optional)
            
        Returns:
            str: Path to saved visualization file
        """
        if not data.get("time_series_data") or not data["time_series_data"].get("periods"):
            return None
            
        # Extract data
        periods = data["time_series_data"]["periods"]
        values = data["time_series_data"]["values"]
        
        # Create a DataFrame for the time series data
        df = pd.DataFrame({
            "Period": periods,
            "Value": values
        })
        
        # Create the Plotly figure
        fig = go.Figure()
        
        # Add line chart with markers
        fig.add_trace(go.Scatter(
            x=df["Period"],
            y=df["Value"],
            mode='lines+markers',
            name='Trend',
            line=dict(color=self.primary_color, width=3),
            marker=dict(
                size=10,
                color=self.primary_color,
                line=dict(width=2, color='white')
            ),
            hovertemplate="<b>%{x}</b><br>Value: %{y}<extra></extra>"
        ))
        
        # Apply Plazza styling to the layout
        fig.update_layout(
            title={
                'text': "Sales Trend Analysis",
                'font': {'size': 22, 'color': self.primary_color, 'family': "system-ui, sans-serif"},
                'y': 0.95
            },
            font=dict(family="system-ui, sans-serif", size=14),
            paper_bgcolor=self.background_color,
            plot_bgcolor=self.background_color,
            margin=dict(t=80, b=80, l=40, r=40),
            height=500,
            width=900
        )
        
        # Update axes
        fig.update_xaxes(
            title_text="Time Period",
            title_font=dict(family="system-ui, sans-serif", size=14, color="#666"),
            tickfont=dict(family="system-ui, sans-serif", size=12),
            gridcolor='rgba(0,0,0,0.05)'
        )
        
        fig.update_yaxes(
            title_text="Sales Value",
            title_font=dict(family="system-ui, sans-serif", size=14, color="#666"),
            tickfont=dict(family="system-ui, sans-serif", size=12),
            gridcolor='rgba(0,0,0,0.05)'
        )
        
        # Add a styled card-like border
        fig.update_layout(
            shapes=[
                dict(
                    type="rect",
                    xref="paper",
                    yref="paper",
                    x0=0,
                    y0=0,
                    x1=1,
                    y1=1,
                    line=dict(
                        color="rgba(0,0,0,0.1)",
                        width=1,
                    ),
                    fillcolor="rgba(0,0,0,0)",
                    layer="below"
                )
            ]
        )
        
        # Save the plot as both HTML and PNG
        if not filename:
            filename_base = f"{self.output_dir}/sales_trend_{self.timestamp}"
            html_filename = f"{filename_base}.html"
            png_filename = f"{filename_base}.png"
        else:
            html_filename = filename
            png_filename = filename.replace('.html', '.png') if filename.endswith('.html') else f"{filename}.png"
        
        # Create custom HTML with Plazza styling
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Plazza Sales Trend</title>
    <style>
        :root {{ --plazza: {self.primary_color}; }}
        body {{ 
            font-family: system-ui, sans-serif;
            margin: 0;
            padding: 20px;
            background: {self.background_color};
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .card {{
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        h1, h2 {{ color: var(--plazza); }}
        .chart {{ height: 500px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <h2>Sales Trend Analysis</h2>
            <div id="chart" class="chart"></div>
        </div>
    </div>
</body>
</html>"""
        
        # Combine with Plotly's HTML
        plotly_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        final_html = html_content.replace('<div id="chart" class="chart"></div>', plotly_html)
        
        with open(html_filename, 'w') as f:
            f.write(final_html)
        
        # Save the PNG for embedding
        fig.write_image(png_filename)
        
        return html_filename
        
    def create_geographic_chart(self, data, filename=None):
        """
        Create a geographic distribution chart with Plazza styling
        
        Args:
            data (dict): Parsed data from markdown
            filename (str): Output filename (optional)
            
        Returns:
            str: Path to saved visualization file
        """
        if not data.get("geographic_data") or not data["geographic_data"].get("regions"):
            return None
            
        # Extract data
        regions = data["geographic_data"]["regions"]
        values = data["geographic_data"]["values"]
        
        # Create a DataFrame
        df = pd.DataFrame({
            "Region": regions,
            "Value": values
        })
        
        # Sort by value descending
        df = df.sort_values(by="Value", ascending=False)
        
        # Create a color scale based on Plazza primary color
        import matplotlib.colors as mcolors
        base_color = mcolors.to_rgb(self.primary_color)
        n_colors = len(df) if len(df) > 0 else 1
        colors = []
        
        for i in range(n_colors):
            factor = 0.5 + (0.5 * (i / max(1, n_colors - 1)))
            color = tuple(min(1.0, c * factor) for c in base_color)
            colors.append(mcolors.to_hex(color))
        
        # Create the Plotly figure
        fig = go.Figure()
        
        # Add bar chart
        fig.add_trace(go.Bar(
            x=df["Region"],
            y=df["Value"],
            marker=dict(color=colors),
            text=df["Value"],
            textposition="auto",
            hovertemplate="<b>%{x}</b><br>Value: %{y}<extra></extra>"
        ))
        
        # Apply Plazza styling
        fig.update_layout(
            title={
                'text': "Geographic Distribution",
                'font': {'size': 22, 'color': self.primary_color, 'family': "system-ui, sans-serif"},
                'y': 0.95
            },
            font=dict(family="system-ui, sans-serif", size=14),
            paper_bgcolor=self.background_color,
            plot_bgcolor=self.background_color,
            margin=dict(t=80, b=80, l=40, r=40),
            height=500,
            width=900
        )
        
        # Update axes
        fig.update_xaxes(
            title_text="Region",
            title_font=dict(family="system-ui, sans-serif", size=14, color="#666"),
            tickfont=dict(family="system-ui, sans-serif", size=12)
        )
        
        fig.update_yaxes(
            title_text="Value",
            title_font=dict(family="system-ui, sans-serif", size=14, color="#666"),
            tickfont=dict(family="system-ui, sans-serif", size=12),
            gridcolor='rgba(0,0,0,0.05)'
        )
        
        # Save the plot
        if not filename:
            filename_base = f"{self.output_dir}/geographic_distribution_{self.timestamp}"
            html_filename = f"{filename_base}.html"
            png_filename = f"{filename_base}.png"
        else:
            html_filename = filename
            png_filename = filename.replace('.html', '.png') if filename.endswith('.html') else f"{filename}.png"
        
        # Create custom HTML with Plazza styling
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Plazza Geographic Distribution</title>
    <style>
        :root {{ --plazza: {self.primary_color}; }}
        body {{ 
            font-family: system-ui, sans-serif;
            margin: 0;
            padding: 20px;
            background: {self.background_color};
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .card {{
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        h1, h2 {{ color: var(--plazza); }}
        .chart {{ height: 500px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <h2>Geographic Distribution</h2>
            <div id="chart" class="chart"></div>
        </div>
    </div>
</body>
</html>"""
        
        # Combine with Plotly's HTML
        plotly_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        final_html = html_content.replace('<div id="chart" class="chart"></div>', plotly_html)
        
        with open(html_filename, 'w') as f:
            f.write(final_html)
        
        # Save the PNG for embedding
        fig.write_image(png_filename)
        
        return html_filename
        
    def create_comparative_chart(self, data, filename=None):
        """
        Create a comparative chart for period-over-period metrics
        
        Args:
            data (dict): Parsed data from markdown
            filename (str): Output filename (optional)
            
        Returns:
            str: Path to saved visualization file
        """
        if not data.get("comparative_data") or not data["comparative_data"].get("metrics"):
            return None
            
        # Extract data
        metrics = data["comparative_data"]["metrics"]
        changes = data["comparative_data"]["changes"]
        
        # Create DataFrame
        df = pd.DataFrame({
            "Metric": metrics,
            "Change": changes
        })
        
        # Sort by absolute change value
        df = df.sort_values(by="Change", key=abs, ascending=False)
        
        # Create the Plotly figure
        fig = go.Figure()
        
        # Add bar chart with conditional coloring (positive/negative)
        fig.add_trace(go.Bar(
            x=df["Metric"],
            y=df["Change"],
            marker=dict(
                color=[self.primary_color if x >= 0 else "#E74C3C" for x in df["Change"]]
            ),
            text=[f"{x:+}%" for x in df["Change"]],
            textposition="outside",
            hovertemplate="<b>%{x}</b><br>Change: %{text}<extra></extra>"
        ))
        
        # Apply Plazza styling
        fig.update_layout(
            title={
                'text': "Period-over-Period Comparison",
                'font': {'size': 22, 'color': self.primary_color, 'family': "system-ui, sans-serif"},
                'y': 0.95
            },
            font=dict(family="system-ui, sans-serif", size=14),
            paper_bgcolor=self.background_color,
            plot_bgcolor=self.background_color,
            margin=dict(t=80, b=80, l=40, r=40),
            height=500,
            width=900
        )
        
        # Add a zero line
        fig.update_layout(
            shapes=[
                dict(
                    type="line",
                    xref="paper",
                    yref="y",
                    x0=0,
                    y0=0,
                    x1=1,
                    y1=0,
                    line=dict(
                        color="rgba(0,0,0,0.3)",
                        width=1,
                        dash="dash"
                    )
                )
            ]
        )
        
        # Update axes
        fig.update_xaxes(
            title_text="Metric",
            title_font=dict(family="system-ui, sans-serif", size=14, color="#666"),
            tickfont=dict(family="system-ui, sans-serif", size=12)
        )
        
        fig.update_yaxes(
            title_text="Change (%)",
            title_font=dict(family="system-ui, sans-serif", size=14, color="#666"),
            tickfont=dict(family="system-ui, sans-serif", size=12),
            gridcolor='rgba(0,0,0,0.05)',
            zeroline=True,
            zerolinecolor="rgba(0,0,0,0.3)",
            zerolinewidth=1
        )
        
        # Save the plot
        if not filename:
            filename_base = f"{self.output_dir}/comparative_analysis_{self.timestamp}"
            html_filename = f"{filename_base}.html"
            png_filename = f"{filename_base}.png"
        else:
            html_filename = filename
            png_filename = filename.replace('.html', '.png') if filename.endswith('.html') else f"{filename}.png"
        
        # Create custom HTML with Plazza styling
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Plazza Comparative Analysis</title>
    <style>
        :root {{ --plazza: {self.primary_color}; }}
        body {{ 
            font-family: system-ui, sans-serif;
            margin: 0;
            padding: 20px;
            background: {self.background_color};
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .card {{
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        h1, h2 {{ color: var(--plazza); }}
        .chart {{ height: 500px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <h2>Period-over-Period Comparison</h2>
            <div id="chart" class="chart"></div>
        </div>
    </div>
</body>
</html>"""
        
        # Combine with Plotly's HTML
        plotly_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        final_html = html_content.replace('<div id="chart" class="chart"></div>', plotly_html)
        
        with open(html_filename, 'w') as f:
            f.write(final_html)
        
        # Save the PNG for embedding
        fig.write_image(png_filename)
        
        return html_filename
    
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
        
        # Create bar chart for top products
        bar_chart = self.create_sales_bar_chart(data)
        if bar_chart:
            results["top_products_chart"] = bar_chart
            
        # Create pie chart for customer retention
        pie_chart = self.create_customer_pie_chart(data)
        if pie_chart:
            results["customer_retention_chart"] = pie_chart
            
        # Create dashboard for metrics
        dashboard = self.create_metrics_dashboard(data)
        if dashboard:
            results["metrics_dashboard"] = dashboard
        
        # Create time series chart if data available
        time_series = self.create_time_series_chart(data)
        if time_series:
            results["time_series_chart"] = time_series
            
        # Create geographic chart if data available
        geo_chart = self.create_geographic_chart(data)
        if geo_chart:
            results["geographic_chart"] = geo_chart
            
        # Create comparative chart if data available
        comp_chart = self.create_comparative_chart(data)
        if comp_chart:
            results["comparative_chart"] = comp_chart
            
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
            products_png = visualization_paths["top_products_chart"].replace(".html", ".png")
            visualization_md += f"### Top Selling Products\n\n"
            visualization_md += f"![Top Products]({products_png})\n\n"
            visualization_md += f"[Interactive Chart]({visualization_paths['top_products_chart']})\n\n"
        
        # Add customer retention chart if available
        if "customer_retention_chart" in visualization_paths:
            retention_png = visualization_paths["customer_retention_chart"].replace(".html", ".png")
            visualization_md += f"### Customer Retention Analysis\n\n"
            visualization_md += f"![Customer Retention]({retention_png})\n\n"
            visualization_md += f"[Interactive Chart]({visualization_paths['customer_retention_chart']})\n\n"
        
        # Add time series chart if available
        if "time_series_chart" in visualization_paths:
            time_series_png = visualization_paths["time_series_chart"].replace(".html", ".png")
            visualization_md += f"### Sales Trend Analysis\n\n"
            visualization_md += f"![Sales Trend]({time_series_png})\n\n"
            visualization_md += f"[Interactive Trend Chart]({visualization_paths['time_series_chart']})\n\n"
        
        # Add geographic chart if available
        if "geographic_chart" in visualization_paths:
            geo_png = visualization_paths["geographic_chart"].replace(".html", ".png")
            visualization_md += f"### Geographic Distribution\n\n"
            visualization_md += f"![Geographic Distribution]({geo_png})\n\n"
            visualization_md += f"[Interactive Map]({visualization_paths['geographic_chart']})\n\n"
        
        # Add comparative chart if available
        if "comparative_chart" in visualization_paths:
            comp_png = visualization_paths["comparative_chart"].replace(".html", ".png")
            visualization_md += f"### Period-over-Period Comparison\n\n"
            visualization_md += f"![Comparative Analysis]({comp_png})\n\n"
            visualization_md += f"[Interactive Comparison]({visualization_paths['comparative_chart']})\n\n"
        
        # Create a section for visual insights if we have at least three visualizations
        if len(visualization_paths) >= 3:
            visualization_md += f"### Key Visual Insights\n\n"
            visualization_md += f"- **Data at a Glance**: The visualizations above provide a comprehensive view of your business metrics in an easy-to-understand format.\n"
            visualization_md += f"- **Interactive Exploration**: Click on any 'Interactive' links to explore the data dynamically with filtering and hover details.\n"
            visualization_md += f"- **Presentation Ready**: These visualizations are designed with Plazza branding for direct use in presentations and reports.\n\n"
        
        # Insert visualizations before recommendations section
        recommendation_patterns = [
            "#### 4. Actionable Recommendations", 
            "## Recommendations",
            "### Recommendations",
            "# Recommendations",
            "Recommendations:"
        ]
        
        # Try to find a recommendation section to insert before
        inserted = False
        for pattern in recommendation_patterns:
            if pattern in markdown_content:
                enhanced_md = markdown_content.replace(
                    pattern, 
                    f"{visualization_md}\n{pattern}"
                )
                inserted = True
                break
                
        if not inserted:
            # If no recommendations section, add visualizations at the end
            enhanced_md = markdown_content + visualization_md
            
        return enhanced_md


def visualize_analysis_results(input_file=None, content=None, output_dir=None):
    """
    Generate visualizations from analysis results
    
    Args:
        input_file (str, optional): Path to analysis results markdown file
        content (str, optional): Direct markdown content to visualize
        output_dir (str, optional): Directory to save visualizations to
        
    Returns:
        dict: Paths to generated visualization files
    
    Note:
        You must provide either input_file or content. If both are provided,
        content takes precedence.
    """
    # Load environment variables for configuration
    from dotenv import load_dotenv
    import os
    load_dotenv()
    
    # Get output directory from environment or use default
    if output_dir is None:
        output_dir = os.getenv("VISUALIZATION_OUTPUT_DIR", "visuals")
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
        
    # Get markdown content from either content or file
    if content is not None:
        markdown_content = content
        # Create a default filename for enhanced markdown
        filename = f"analysis_visualization_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    elif input_file is not None:
        # Read the markdown content from file
        with open(input_file, 'r') as f:
            markdown_content = f.read()
        filename = os.path.basename(input_file)
    else:
        # Try to use default input file from environment variable
        default_input_file = os.getenv("DEFAULT_ANALYSIS_FILE")
        
        if default_input_file and os.path.exists(default_input_file):
            with open(default_input_file, 'r') as f:
                markdown_content = f.read()
            filename = os.path.basename(default_input_file)
        else:
            # Look for files in common locations
            parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            potential_paths = [
                os.path.join(parent_dir, "Run_Results", "sales_ai_run_result.md"),
                os.path.join(parent_dir, "knowledge", "sales_analysis_results.md"),
            ]
            
            for path in potential_paths:
                if os.path.exists(path):
                    with open(path, 'r') as f:
                        markdown_content = f.read()
                    filename = os.path.basename(path)
                    break
            else:
                raise ValueError("No input file specified or found. Please provide either input_file or content.")
        
    # Create visualizer
    visualizer = CrewAIVisualization(output_dir=output_dir)
    
    # Generate visualizations
    viz_paths = visualizer.generate_all_visualizations(markdown_content)
    
    # Enhance markdown with visualizations
    enhanced_md = visualizer.embed_visualizations_in_markdown(markdown_content, viz_paths)
    
    # Save enhanced markdown
    enhanced_path = os.path.join(output_dir, filename)
    with open(enhanced_path, 'w') as f:
        f.write(enhanced_md)
    
    # Export parsed data as JSON for reuse
    import json
    data = visualizer.parse_markdown_content(markdown_content)
    with open(os.path.join(output_dir, f"parsed_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"), "w") as f:
        json.dump(data, f, indent=2)
        
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
    - Time series charts for trend analysis
    - Geographic charts for regional data
    - Comparative charts for period-over-period analysis
    
    Usage:
    1. With no parameters: Tool automatically processes the most recent analysis file
       or uses the DEFAULT_ANALYSIS_FILE from environment variables.
    2. With input_data: Pass markdown content directly to generate visualizations.
    
    Parameters:
    - input_data (optional): Direct markdown content to visualize. If not provided, 
                            the tool will use the configured default analysis file.
    
    For more specific visualization needs, you can use specialized visualization tools:
    - TopProductsChartTool - For product sales visualizations only
    - CustomerRetentionChartTool - For customer retention analysis only
    - MetricsDashboardTool - For business metrics dashboards only
    """
    
    def _run(self, input_data: str = None) -> str:
        """
        Run the visualization tool on analysis results
        
        Args:
            input_data: Optional markdown content to visualize directly
        """
        try:
            # Get visualization output directory from environment or use default
            from dotenv import load_dotenv
            load_dotenv()
            
            parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            visuals_dir = os.getenv("VISUALIZATION_OUTPUT_DIR", os.path.join(parent_dir, "visuals"))
            os.makedirs(visuals_dir, exist_ok=True)
            
            # Create a visualization log entry
            log_file = os.path.join(visuals_dir, "visualization_log.md")
            log_entry = f"## Visualization Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            
            # If input_data is provided, use it directly
            if input_data:
                log_entry += "- Source: Direct markdown content\n"
                viz_results = visualize_analysis_results(content=input_data, output_dir=visuals_dir)
                source_description = "direct content"
            else:
                # Otherwise, find the latest analysis results file
                # Look in standard locations
                potential_paths = [
                    os.path.join(parent_dir, "Run_Results", "sales_ai_run_result.md"),
                    os.path.join(parent_dir, "knowledge", "sales_analysis_results.md"),
                ]
                
                # Find the most recent file
                valid_paths = [(p, os.path.getmtime(p)) for p in potential_paths if os.path.exists(p)]
                if not valid_paths:
                    return "No analysis results found to visualize."
                    
                # Sort by modification time (most recent first)
                valid_paths.sort(key=lambda x: x[1], reverse=True)
                latest_file = valid_paths[0][0]
                log_entry += f"- Source: {os.path.basename(latest_file)}\n"
                
                # Generate visualizations
                viz_results = visualize_analysis_results(input_file=latest_file, output_dir=visuals_dir)
                source_description = os.path.basename(latest_file)
            
            # Format the results for the agent
            result_summary = [
                f"# Visualizations Created Successfully",
                f"",
                f"Analysis from {source_description} visualized with:",
                f"",
            ]
            
            # Log the generated files
            log_entry += "- Generated files:\n"
            
            for viz_type, viz_path in viz_results.items():
                if viz_type == "enhanced_markdown":
                    continue
                result_summary.append(f"- **{viz_type.replace('_', ' ').title()}**: `{os.path.basename(viz_path)}`")
                log_entry += f"  - {viz_type}: {os.path.basename(viz_path)}\n"
            
            result_summary.append(f"")
            result_summary.append(f"All visualizations are saved in: `{visuals_dir}`")
            result_summary.append(f"")
            result_summary.append(f"Enhanced markdown with embedded visualizations: `{os.path.basename(viz_results.get('enhanced_markdown', ''))}`")
            
            # Optional: Create a ZIP bundle
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            zip_filename = os.path.join(visuals_dir, f"visualization_bundle_{timestamp}.zip")
            
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for viz_type, viz_path in viz_results.items():
                    if os.path.exists(viz_path):
                        zipf.write(viz_path, arcname=os.path.basename(viz_path))
            
            result_summary.append(f"")
            result_summary.append(f"ZIP bundle of all visualizations: `{os.path.basename(zip_filename)}`")
            
            # Save log entry
            log_entry += f"- ZIP bundle: {os.path.basename(zip_filename)}\n\n"
            with open(log_file, 'a') as f:
                f.write(log_entry)
            
            return "\n".join(result_summary)
            
        except Exception as e:
            return f"Error generating visualizations: {str(e)}"

# Specialized visualization tools for specific chart types
class TopProductsChartTool(BaseTool):
    name: str = "TopProductsChartTool"
    description: str = """Create a top selling products chart from analysis content.
    
    This tool extracts product sales data from the markdown analysis and generates 
    a bar chart showing the top-selling products. It can be used to quickly create
    product sales visualizations without generating all other chart types.
    
    Parameters:
    - input_data: Markdown content containing the analysis to visualize
    """
    
    def _run(self, input_data: str) -> str:
        try:
            # Get visualization output directory
            from dotenv import load_dotenv
            load_dotenv()
            
            parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            visuals_dir = os.getenv("VISUALIZATION_OUTPUT_DIR", os.path.join(parent_dir, "visuals"))
            os.makedirs(visuals_dir, exist_ok=True)
            
            # Create visualizer and parse content
            visualizer = CrewAIVisualization(output_dir=visuals_dir)
            data = visualizer.parse_markdown_content(input_data)
            
            # Generate product sales chart
            chart_path = visualizer.create_sales_bar_chart(data)
            
            if not chart_path:
                return "No product sales data found in the provided content."
                
            return f"Product sales chart created successfully: {os.path.basename(chart_path)}"
            
        except Exception as e:
            return f"Error creating product sales chart: {str(e)}"


class CustomerRetentionChartTool(BaseTool):
    name: str = "CustomerRetentionChartTool"
    description: str = """Create a customer retention pie chart from analysis content.
    
    This tool extracts customer retention data from the markdown analysis and generates
    a pie chart showing the distribution of repeat vs one-time customers. It can be used
    to quickly create retention visualizations without generating all other chart types.
    
    Parameters:
    - input_data: Markdown content containing the analysis to visualize
    """
    
    def _run(self, input_data: str) -> str:
        try:
            # Get visualization output directory
            from dotenv import load_dotenv
            load_dotenv()
            
            parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            visuals_dir = os.getenv("VISUALIZATION_OUTPUT_DIR", os.path.join(parent_dir, "visuals"))
            os.makedirs(visuals_dir, exist_ok=True)
            
            # Create visualizer and parse content
            visualizer = CrewAIVisualization(output_dir=visuals_dir)
            data = visualizer.parse_markdown_content(input_data)
            
            # Generate customer retention chart
            chart_path = visualizer.create_customer_pie_chart(data)
            
            if not chart_path:
                return "No customer retention data found in the provided content."
                
            return f"Customer retention chart created successfully: {os.path.basename(chart_path)}"
            
        except Exception as e:
            return f"Error creating customer retention chart: {str(e)}"


class MetricsDashboardTool(BaseTool):
    name: str = "MetricsDashboardTool"
    description: str = """Create a comprehensive business metrics dashboard from analysis content.
    
    This tool extracts key metrics from the markdown analysis and generates an interactive
    dashboard with multiple visualizations. It provides a holistic view of business performance
    across sales, customer, and product dimensions.
    
    Parameters:
    - input_data: Markdown content containing the analysis to visualize
    """
    
    def _run(self, input_data: str) -> str:
        try:
            # Get visualization output directory
            from dotenv import load_dotenv
            load_dotenv()
            
            parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            visuals_dir = os.getenv("VISUALIZATION_OUTPUT_DIR", os.path.join(parent_dir, "visuals"))
            os.makedirs(visuals_dir, exist_ok=True)
            
            # Create visualizer and parse content
            visualizer = CrewAIVisualization(output_dir=visuals_dir)
            data = visualizer.parse_markdown_content(input_data)
            
            # Generate metrics dashboard
            dashboard_path = visualizer.create_metrics_dashboard(data)
            
            if not dashboard_path:
                return "Not enough data found to create a comprehensive dashboard."
                
            return f"Business metrics dashboard created successfully: {os.path.basename(dashboard_path)}"
            
        except Exception as e:
            return f"Error creating metrics dashboard: {str(e)}"


# Zip export utility
def export_visualizations_as_zip(output_dir, zip_name=None):
    """
    Export all visualizations in the output directory as a ZIP file
    
    Args:
        output_dir: Directory containing visualizations
        zip_name: Optional name for the ZIP file (default: visuals_bundle_{timestamp}.zip)
        
    Returns:
        str: Path to the created ZIP file
    """
    if zip_name is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        zip_name = f"visuals_bundle_{timestamp}.zip"
        
    zip_path = os.path.join(output_dir, zip_name)
    
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(output_dir):
            for file in files:
                # Skip the zip file itself
                if file == zip_name:
                    continue
                    
                file_path = os.path.join(root, file)
                zipf.write(file_path, arcname=os.path.basename(file_path))
                
    return zip_path


if __name__ == "__main__":
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(description="Generate visualizations from CrewAI analysis results")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="Path to analysis results markdown file")
    group.add_argument("--content", help="Direct markdown content to visualize (use - for stdin)")
    
    parser.add_argument("--output-dir", help="Directory to save visualizations to")
    parser.add_argument("--zip", action="store_true", help="Create a ZIP bundle of all visualizations")
    parser.add_argument("--chart-type", choices=["all", "sales", "retention", "dashboard", "time-series", "geographic", "comparative"], 
                        default="all", help="Specific chart type to generate")
    
    args = parser.parse_args()
    
    # Get content from stdin if requested
    if args.content == "-":
        print("Enter or paste markdown content (press Ctrl+D when finished):")
        content = sys.stdin.read()
    else:
        content = args.content
    
    # Generate visualizations
    if args.file:
        results = visualize_analysis_results(input_file=args.file, output_dir=args.output_dir)
    else:
        results = visualize_analysis_results(content=content, output_dir=args.output_dir)
    
    # Create ZIP bundle if requested
    if args.zip and results:
        output_dir = args.output_dir or "visuals"
        zip_path = export_visualizations_as_zip(output_dir)
        print(f"\nZIP bundle created: {zip_path}")
    
    # Print results
    output_dir = args.output_dir or "visuals"
    print(f"\nVisualizations generated in {output_dir}:")
    for key, path in results.items():
        print(f"  - {key}: {path}")
        
    # Log event
    log_file = os.path.join(output_dir, "visualization_log.md")
    log_entry = f"## CLI Visualization Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    log_entry += f"- Source: {'File: ' + args.file if args.file else 'Direct content'}\n"
    log_entry += "- Generated files:\n"
    
    for viz_type, viz_path in results.items():
        log_entry += f"  - {viz_type}: {os.path.basename(viz_path)}\n"
        
    with open(log_file, 'a') as f:
        f.write(log_entry + "\n")