import os
import psycopg2
import psycopg2.extras
import json
import shutil
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from crewai.tools import BaseTool
from pydantic import Field
from crewai.knowledge.knowledge import Knowledge
from crewai_visualization import visualize_analysis_results, VisualizationTool

# Load environment variables
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please set it in your .env file or environment.")
os.environ["OPENAI_API_KEY"] = openai_key

# Path to the analysis results file
ANALYSIS_RESULTS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sales_ai_run_result.md")

class PreviousAnalysisTool(BaseTool):
    name: str = "PreviousAnalysisTool"
    description: str = """Access the historical analysis results.
    
    This tool retrieves the previous analysis results that were stored from past runs.
    Use this tool to:
    1. Check what insights were discovered in previous analyses
    2. Compare new findings against historical data
    3. Build upon previous recommendations rather than starting from scratch
    
    The previous analysis contains information about:
    - Database structure summary
    - Inventory-Sales Gap Analysis
    - Data Consistency Analysis
    - Actionable Recommendations
    
    USAGE:
    Simply call the tool with no parameters to retrieve the entire previous analysis.
    
    NOTE: For specific queries about previous analysis, the built-in knowledge system 
    will automatically retrieve relevant information. Use this tool only when you need
    to see the full previous analysis.
    """
    
    def _run(self) -> str:
        try:
            if os.path.exists(ANALYSIS_RESULTS_PATH):
                with open(ANALYSIS_RESULTS_PATH, 'r') as file:
                    content = file.read()
                    
                    # Extract the final answer section which contains the actual analysis
                    if "## Final Answer:" in content:
                        final_answer = content.split("## Final Answer:")[1].strip()
                        
                        # Format the content for better readability
                        formatted_content = self._format_analysis_content(final_answer)
                        return f"## Previous Analysis Results\n\n{formatted_content}"
                    
                    # If no final answer section, return the whole content
                    formatted_content = self._format_analysis_content(content)
                    return f"## Previous Analysis Results\n\n{formatted_content}"
            else:
                return "No previous analysis results found."
        except Exception as e:
            return f"Error retrieving previous analysis: {str(e)}"
    
    def _format_analysis_content(self, content: str) -> str:
        """Format the analysis content for better readability."""
        # Split content into sections
        sections = []
        current_section = ""
        current_title = "Overview"
        
        for line in content.split("\n"):
            # Check if this is a section header
            if line.startswith("## "):
                # Save the previous section if it's not empty
                if current_section.strip():
                    sections.append({
                        "title": current_title,
                        "content": current_section.strip()
                    })
                
                # Start a new section
                current_title = line.replace("## ", "").strip()
                current_section = ""
            else:
                current_section += line + "\n"
        
        # Add the last section
        if current_section.strip():
            sections.append({
                "title": current_title,
                "content": current_section.strip()
            })
        
        # Format sections into a readable format
        if not sections:
            return content  # Return original if parsing failed
        
        formatted_text = ""
        for section in sections:
            formatted_text += f"### {section['title']}\n\n{section['content']}\n\n"
        
        return formatted_text

class CockroachDBTool(BaseTool):
    name: str = "CockroachDBTool"
    description: str = """Execute SQL queries against one of the CockroachDB databases in the Plazza ecosystem.
    
    AVAILABLE DATABASES (you must specify which one to use with the 'database' parameter):

    1. user_transactions - Customer and order management
       - contacts: customer information (id, first_name, last_name, email, gender, customer_type, zoho_contact_id)
       - contact_addresses: addresses linked to contacts (id, contact_id, address_id, house_number, locality, state, pincode, latitude, longitude)
       - contact_phones: phone numbers (id, contact_id, phone_number, is_primary)
       - orders: order information (id, order_id, contact_id, status, bill_total_amount, delivery_type, tookan_job_id, whatsapp_notification_status)
       - order_items: individual items (id, order_id, product_id, medicine_name, mrp, selling_price, quantity, item_total)
       - payments: payment details (id, payment_id, customer_id, order_amount, payment_status, payment_method, qr_code_id, qr_code_url, zoho_payment_id)
       - products: product catalog (id, product_id, medicine_name, medicine_type, mrp, quantity_available)
       - stores: store information (id, name, address, city, state, pincode, gst_number)
       - tookan_jobs: delivery tracking (id, order_id, job_id, agent_id, job_status, tracking_url)
       - whatsapp_messages: message history (id, message_id, order_id, status)
       - whatsapp_notifications: notification tracking (id, message_id, order_id, phone_number, template_id, status)
       - zoho_config: Zoho integration settings (id, organization_id, tax_settings, account_settings)
       - zoho_tokens: Zoho authentication tokens (id, token, expires_at, is_valid)

    2. defaultdb - Core product catalog
       - all_products: complete product catalog (product_id, name, manufacturers, salt_composition, medicine_type)
       - inventory_products: inventory tracking (product_id, vendor_id, batch_number, expiry_date, stock_qty)
       - plazza_price_table: pricing information (product_id, mrp, selling_price, discount_percentage)
       - validated_matches: validated product matches between systems (product_id, vendor_product_id, confidence)
       - matching_logs: product matching tracking (match_id, product_id, confidence_score, matching_method)

    3. plazza_erp - ERP system for business operations
       - inventory_transactions: inventory movement (transaction_id, product_id, quantity, transaction_type)
       - promotional_coupons: promo codes (coupon_code, discount_type, discount_value, valid_from, valid_to)
       - one_time_coupons: single-use codes (coupon_code, used, used_by, used_at)
       - conversations: customer chat history (conversation_id, customer_id, conversation_text)

    4. user_events - User activity tracking
       - session_events: user session data (session_id, user_id, event_type, timestamp)
       - user_searches: search history (search_id, user_id, search_term, results_count)
       - page_views: page view tracking (page_id, user_id, page_name, time_spent)
       - conversion_events: purchase funnel events (event_id, user_id, event_type, product_id)

    REQUIRED PARAMETERS:
    - query: The SQL query to execute against the selected database
    - database: The database to query (must be one of: "user_transactions", "defaultdb", "plazza_erp", "user_events")
    
    USAGE EXAMPLES:
    - To query user transaction data:
      CockroachDBTool(query="SELECT * FROM orders LIMIT 5", database="user_transactions")
    
    - To query product catalog:
      CockroachDBTool(query="SELECT * FROM all_products LIMIT 5", database="defaultdb")
    
    - To query coupon data:
      CockroachDBTool(query="SELECT * FROM promotional_coupons LIMIT 5", database="plazza_erp")
    
    IMPORTANT: 
    - Always explore the database schema first by running a query to understand table structures before attempting analysis.
    - When analyzing sales or product data, always include medicine_name along with product_id in your query
    - When reporting product metrics, use the medicine_name rather than just the product_id to make the analysis more understandable
    - Include both product_id and medicine_name in your results (e.g., "Product: SOMPRAZ L CAP (165005), Quantity: 30")
    - Filter out test products by excluding product_ids that contain 'TEST' or 'test' when doing production analysis
    """
    
    def _run(self, query: str, database: str) -> str:
        # Map database names to environment variables
        db_connection_vars = {
            "user_transactions": "DATABASE_URL_USER_TRANSACTIONS",
            "defaultdb": "DATABASE_URL",
            "plazza_erp": "DATABASE_URL_ERP",
            "user_events": "DATABASE_URL_USER"
        }
        
        # Validate database parameter
        if database not in db_connection_vars:
            return f"Error: '{database}' is not a valid database. Choose from: {', '.join(db_connection_vars.keys())}"
        
        # Get the appropriate connection string
        connection_var = db_connection_vars[database]
        connection_string = os.getenv(connection_var)
        
        if not connection_string:
            return f"Error: Environment variable {connection_var} is not set"
        
        # Always apply test data filtering to any product-related query
        # This ensures consistent filtering regardless of query structure
        test_product_filter = (
            "product_id NOT LIKE '%TEST%' AND "
            "product_id NOT LIKE '%test%' AND "
            "product_id NOT LIKE 'p%' AND "
            "medicine_name NOT LIKE 'Test%' AND "
            "product_id NOT IN ('MED001', 'TEST-MED-001', 'TEST001', 'TEST002') AND "
            "order_id NOT LIKE '%TEST%' AND "
            "order_id NOT LIKE 'POD-WEBHOOK%' AND "
            "bill_total_amount > 10"
        )
        
        # Check if this is a top products query for special handling
        is_top_products_query = False
        if ('SUM(quantity)' in query or 'sum(' in query.lower()) and 'GROUP BY' in query and 'ORDER BY' in query:
            is_top_products_query = True
            
            # Modify query to include medicine_name
            if 'medicine_name' not in query:
                # Replace GROUP BY product_id with GROUP BY product_id, medicine_name
                query = query.replace(
                    'GROUP BY product_id', 
                    'GROUP BY product_id, medicine_name'
                )
                
                # Replace SELECT product_id with SELECT product_id, medicine_name
                if 'SELECT product_id' in query:
                    query = query.replace(
                        'SELECT product_id', 
                        'SELECT product_id, medicine_name'
                    )
                
                # Apply test data filtering
                if 'WHERE' in query:
                    # Add test filters to existing WHERE clause
                    query = query.replace(
                        'WHERE', 
                        f"WHERE {test_product_filter} AND "
                    )
                else:
                    # Add new WHERE clause with test filters
                    before_group = query.split('GROUP BY')[0]
                    after_group = 'GROUP BY' + query.split('GROUP BY')[1]
                    query = f"{before_group} WHERE {test_product_filter} {after_group}"
            
        try:
            conn = psycopg2.connect(connection_string)
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                
                if not rows:
                    return f"No results found for query in {database} database"
                
                result_str = f"Results from {database} database:\n"
                
                # Special handling for top products query
                if is_top_products_query and 'medicine_name' in query:
                    filtered_rows = []
                    for row in rows:
                        row_dict = dict(row)
                        # Extra test data filter at display level
                        product_id = row_dict.get('product_id', '')
                        if product_id and (
                            'TEST' in product_id or 
                            'test' in product_id or 
                            product_id in ['MED001', 'TEST-MED-001', 'TEST001', 'TEST002', 'p1', 'p2'] or
                            product_id.startswith('p')):
                            continue
                        filtered_rows.append(row_dict)
                    
                    # Display filtered rows
                    for row_dict in filtered_rows[:20]:
                        if 'product_id' in row_dict and 'medicine_name' in row_dict:
                            result_str += f"{{'product_id': '{row_dict['product_id']}', 'medicine_name': '{row_dict['medicine_name']}', 'total_quantity': {row_dict.get('total_quantity', row_dict.get('sum', 0))}}}\n"
                        else:
                            result_str += f"{row_dict}\n"
                else:
                    result_str += "\n".join([str(dict(row)) for row in rows[:20]])
                    
                if len(rows) > 20:
                    result_str += f"\n...and {len(rows) - 20} more rows"
                return result_str
                
        except Exception as e:
            return f"Error executing query on {database} database: {str(e)}"
        finally:
            if conn:
                conn.close()

# Modified Knowledge integration - fixed path handling
def create_knowledge_source():
    """Create a knowledge source from the analysis results file."""
    knowledge_file = 'sales_analysis_results.md'  # Relative path - will be prefixed with 'knowledge/'
    knowledge_path = os.path.join('knowledge', knowledge_file)
    
    # Check if the file exists
    if os.path.exists(knowledge_path):
        # First copy the latest content to knowledge directory
        if os.path.exists(ANALYSIS_RESULTS_PATH):
            shutil.copy2(ANALYSIS_RESULTS_PATH, knowledge_path)
        
        print(f"Creating knowledge source from {knowledge_file}")
        from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
        
        # Use relative path that will work with CrewAI's knowledge directory structure
        markdown_source = TextFileKnowledgeSource(
            file_paths=[knowledge_file],  # Just the filename, CrewAI will prepend "knowledge/"
            chunk_size=800,
            chunk_overlap=200,
            metadata={"source": "sales_analysis", "date": os.path.getmtime(knowledge_path)}
        )
        
        # Create the knowledge object
        return Knowledge(
            collection_name="sales_analysis",
            sources=[markdown_source]
        )
    else:
        print(f"Warning: Knowledge file {knowledge_path} not found")
        return None

# Create knowledge source
try:
    sales_knowledge = create_knowledge_source()
except Exception as e:
    print(f"Warning: Could not create knowledge source: {str(e)}")
    sales_knowledge = None

class RetentionAnalysisTool(BaseTool):
    name: str = "RetentionAnalysisTool"
    description: str = """Perform comprehensive customer retention analysis across the Plazza ecosystem.
    
    This specialized tool analyzes customer retention patterns by:
    1. Filtering out test data and outliers
    2. Calculating key retention metrics (repeat rates, time between purchases)
    3. Identifying product categories that drive repeat purchases
    4. Analyzing the correlation between discounts and customer retention
    
    The tool performs multiple coordinated SQL queries and statistical analyses to provide a
    complete picture of customer retention dynamics.
    
    USAGE:
    Simply call this tool with no parameters to execute a full retention analysis.
    
    RESULTS INCLUDE:
    - Repeat vs one-time customer percentages (with test data filtered)
    - Average time between first and second purchases
    - Product categories that drive highest retention
    - Discount impact analysis on repeat purchase behavior
    - Customer lifecycle value estimates
    - Retention rate by cohort (when data available)
    """
    
    def _run(self) -> str:
        """Execute comprehensive retention analysis across databases"""
        try:
            # Initialize analysis results
            results = []
            
            # Check if we have database access
            connection_string = os.getenv("DATABASE_URL_USER_TRANSACTIONS")
            if not connection_string:
                return "Error: Environment variable DATABASE_URL_USER_TRANSACTIONS is not set"
            
            # Connect to the database
            conn = psycopg2.connect(connection_string)
            
            # QUERY 1: Calculate clean repeat vs. one-time customer percentages
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                # Filter out test orders and customers
                cursor.execute("""
                SELECT 
                    COUNT(DISTINCT contact_id) as total_customers,
                    COUNT(DISTINCT CASE WHEN customer_order_count > 1 THEN contact_id END) as repeat_customers,
                    ROUND(COUNT(DISTINCT CASE WHEN customer_order_count > 1 THEN contact_id END)::numeric / 
                          NULLIF(COUNT(DISTINCT contact_id), 0)::numeric * 100, 1) as repeat_percentage
                FROM (
                    SELECT 
                        o.contact_id, 
                        COUNT(o.order_id) as customer_order_count
                    FROM orders o
                    JOIN order_items oi ON o.order_id = oi.order_id
                    WHERE 
                        o.contact_id IS NOT NULL
                        AND o.status = 'paid'
                        AND o.order_id NOT LIKE '%TEST%'
                        AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                        AND oi.product_id NOT LIKE '%TEST%'
                        AND oi.product_id NOT LIKE '%test%'
                        AND oi.product_id NOT LIKE 'p%'
                        AND oi.medicine_name NOT LIKE 'Test%'
                        AND oi.product_id NOT IN ('MED001', 'TEST-MED-001', 'TEST001', 'TEST002', 'p1', 'p2')
                        AND o.bill_total_amount > 10  -- Filter out very small test transactions
                    GROUP BY o.contact_id
                ) as customer_counts
                """)
                
                retention_data = cursor.fetchone()
                if retention_data:
                    results.append(f"## Customer Retention Analysis (Clean Data)\n")
                    results.append(f"Total unique customers: {retention_data['total_customers']}")
                    results.append(f"Repeat customers: {retention_data['repeat_customers']}")
                    results.append(f"One-time customers: {retention_data['total_customers'] - retention_data['repeat_customers']}")
                    results.append(f"Repeat customer percentage: {retention_data['repeat_percentage']}%")
                    results.append(f"One-time customer percentage: {100 - retention_data['repeat_percentage']}%\n")
            
            # QUERY 2: Calculate time between purchases
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("""
                WITH filtered_orders AS (
                    SELECT 
                        o.contact_id, 
                        o.order_id,
                        o.created_at,
                        ROW_NUMBER() OVER (PARTITION BY o.contact_id ORDER BY o.created_at) as purchase_number
                    FROM orders o
                    JOIN order_items oi ON o.order_id = oi.order_id
                    WHERE 
                        o.contact_id IS NOT NULL
                        AND o.status = 'paid'
                        AND o.order_id NOT LIKE '%TEST%'
                        AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                        AND oi.product_id NOT LIKE '%TEST%'
                        AND oi.product_id NOT LIKE '%test%'
                        AND oi.product_id NOT LIKE 'p%'
                        AND oi.medicine_name NOT LIKE 'Test%'
                        AND oi.product_id NOT IN ('MED001', 'TEST-MED-001', 'TEST001', 'TEST002', 'p1', 'p2')
                        AND o.bill_total_amount > 10
                )
                SELECT
                    AVG(EXTRACT(DAY FROM (second_purchase.created_at - first_purchase.created_at))) as avg_days_between_purchases,
                    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY EXTRACT(DAY FROM (second_purchase.created_at - first_purchase.created_at))) as median_days_between_purchases
                FROM 
                    filtered_orders first_purchase
                JOIN 
                    filtered_orders second_purchase 
                    ON first_purchase.contact_id = second_purchase.contact_id
                    AND first_purchase.purchase_number = 1
                    AND second_purchase.purchase_number = 2
                """)
                
                time_data = cursor.fetchone()
                if time_data and time_data['avg_days_between_purchases'] is not None:
                    results.append(f"## Time Between Purchases\n")
                    results.append(f"Average days between first and second purchase: {time_data['avg_days_between_purchases']:.1f} days")
                    results.append(f"Median days between first and second purchase: {time_data['median_days_between_purchases']:.1f} days\n")
            
            # QUERY 3: Products that drive repeat purchases
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("""
                WITH repeat_customers AS (
                    SELECT DISTINCT contact_id
                    FROM (
                        SELECT 
                            o.contact_id, 
                            COUNT(o.order_id) as order_count
                        FROM orders o
                        JOIN order_items oi ON o.order_id = oi.order_id
                        WHERE 
                            o.contact_id IS NOT NULL
                            AND o.status = 'paid'
                            AND o.order_id NOT LIKE '%TEST%'
                            AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                            AND oi.product_id NOT LIKE '%TEST%'
                            AND oi.product_id NOT LIKE '%test%'
                            AND oi.product_id NOT LIKE 'p%'
                            AND oi.medicine_name NOT LIKE 'Test%'
                            AND oi.product_id NOT IN ('MED001', 'TEST-MED-001', 'TEST001', 'TEST002', 'p1', 'p2')
                            AND o.bill_total_amount > 10
                        GROUP BY o.contact_id
                        HAVING COUNT(o.order_id) > 1
                    ) as multi_purchasers
                ),
                first_purchase_products AS (
                    SELECT 
                        o.contact_id,
                        oi.product_id,
                        oi.medicine_name,
                        ROW_NUMBER() OVER (PARTITION BY o.contact_id ORDER BY o.created_at) as purchase_order
                    FROM orders o
                    JOIN order_items oi ON o.order_id = oi.order_id
                    WHERE 
                        o.contact_id IN (SELECT contact_id FROM repeat_customers)
                        AND o.status = 'paid'
                        AND o.order_id NOT LIKE '%TEST%'
                        AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                        AND oi.product_id NOT LIKE '%TEST%'
                        AND oi.product_id NOT LIKE '%test%'
                        AND oi.product_id NOT LIKE 'p%'
                        AND oi.medicine_name NOT LIKE 'Test%'
                        AND oi.product_id NOT IN ('MED001', 'TEST-MED-001', 'TEST001', 'TEST002', 'p1', 'p2')
                        AND o.bill_total_amount > 10
                )
                SELECT 
                    product_id,
                    medicine_name,
                    COUNT(*) as first_purchase_count,
                    ROUND((COUNT(*)::numeric / NULLIF((SELECT COUNT(*) FROM repeat_customers), 0)::numeric) * 100, 1) as percentage_of_repeat_customers
                FROM first_purchase_products
                WHERE purchase_order = 1
                GROUP BY product_id, medicine_name
                ORDER BY first_purchase_count DESC
                LIMIT 5
                """)
                
                driving_products = cursor.fetchall()
                if driving_products:
                    results.append(f"## Products Driving Repeat Purchases\n")
                    results.append(f"Products most commonly purchased in first orders by customers who later made repeat purchases:")
                    for i, product in enumerate(driving_products, 1):
                        results.append(f"{i}. Product: {product['medicine_name']} ({product['product_id']}), " +
                                     f"First-time purchases: {product['first_purchase_count']}, " +
                                     f"Present in {product['percentage_of_repeat_customers']}% of repeat customers' first orders")
                    results.append("")
            
            # QUERY 4: Discount impact on retention
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("""
                WITH order_discounts AS (
                    SELECT 
                        o.contact_id,
                        o.order_id,
                        o.bill_total_amount,
                        o.item_total,
                        CASE 
                            WHEN o.item_total > 0 THEN (1 - (o.bill_total_amount / o.item_total)) * 100 
                            ELSE 0 
                        END as discount_percentage,
                        ROW_NUMBER() OVER (PARTITION BY o.contact_id ORDER BY o.created_at) as purchase_number
                    FROM orders o
                    JOIN order_items oi ON o.order_id = oi.order_id
                    WHERE 
                        o.contact_id IS NOT NULL
                        AND o.status = 'paid'
                        AND o.order_id NOT LIKE '%TEST%'
                        AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                        AND oi.product_id NOT LIKE '%TEST%'
                        AND oi.product_id NOT LIKE '%test%'
                        AND oi.product_id NOT LIKE 'p%'
                        AND oi.medicine_name NOT LIKE 'Test%'
                        AND oi.product_id NOT IN ('MED001', 'TEST-MED-001', 'TEST001', 'TEST002', 'p1', 'p2')
                        AND o.bill_total_amount > 10
                        AND o.item_total > 0
                )
                SELECT
                    CASE 
                        WHEN discount_percentage = 0 THEN 'No discount'
                        WHEN discount_percentage > 0 AND discount_percentage <= 10 THEN '0-10% discount'
                        WHEN discount_percentage > 10 AND discount_percentage <= 20 THEN '10-20% discount'
                        WHEN discount_percentage > 20 THEN '20%+ discount'
                    END as discount_bracket,
                    COUNT(DISTINCT contact_id) as total_customers,
                    COUNT(DISTINCT CASE WHEN contact_id IN (
                        SELECT contact_id FROM order_discounts WHERE purchase_number > 1
                    ) THEN contact_id END) as returning_customers,
                    ROUND(COUNT(DISTINCT CASE WHEN contact_id IN (
                        SELECT contact_id FROM order_discounts WHERE purchase_number > 1
                    ) THEN contact_id END)::numeric / 
                    NULLIF(COUNT(DISTINCT contact_id), 0)::numeric * 100, 1) as retention_rate
                FROM order_discounts
                WHERE purchase_number = 1
                GROUP BY discount_bracket
                ORDER BY MIN(discount_percentage)
                """)
                
                discount_impact = cursor.fetchall()
                if discount_impact:
                    results.append(f"## Discount Impact on Retention\n")
                    results.append(f"Retention rates based on first purchase discount:")
                    for bracket in discount_impact:
                        results.append(f"- {bracket['discount_bracket']}: {bracket['retention_rate']}% retention rate " +
                                     f"({bracket['returning_customers']} returning out of {bracket['total_customers']} customers)")
                    results.append("")
            
            # Combine all results
            return "\n".join(results)
            
        except Exception as e:
            return f"Error performing retention analysis: {str(e)}"
        finally:
            if 'conn' in locals() and conn:
                conn.close()

# Create the NL2SQL Agent
data_analyst = Agent(
    role="Enterprise Data Analyst",
    goal="Analyze business data across multiple databases to identify sales trends and customer behavior patterns",
    backstory="""You are an expert SQL data analyst with years of experience in retail and 
    pharmaceutical analytics. You understand multi-database ecosystems intuitively and can translate
    natural language questions into precise SQL queries for CockroachDB.
    
    You're skilled at identifying which database contains the necessary data and can construct 
    queries to extract meaningful insights. Your approach is data-driven but also builds upon 
    historical knowledge from past analyses.
    
    Your expertise includes retail sales pattern analysis, customer segmentation, repeat purchase behavior,
    and promotional campaign effectiveness.
    
    IMPORTANT: You have THREE complementary ways to access data and insights:
    
    1. Your KNOWLEDGE BASE contains previous analysis results that automatically provide relevant context
       during your reasoning. This is your primary source of historical insights and should be referenced
       throughout your analysis.
       
    2. The PreviousAnalysisTool gives you direct access to the full previous analysis if needed.
    
    3. The RetentionAnalysisTool provides specialized in-depth retention metrics with test data already
       filtered out. This is your primary tool for customer retention analysis, offering metrics like
       time-between-purchases and discount impact on retention.
       
    4. The VisualizationTool allows you to create visual representations of your analysis results,
       including bar charts, pie charts, and interactive dashboards. This helps make your insights
       more accessible and actionable.
    
    Always leverage all these data sources to provide comprehensive insights that build upon previous
    work. Focus on identifying actionable patterns and making specific, data-driven recommendations.
    
    Make sure your analysis is formatted in a way that works well with the VisualizationTool to create
    compelling data visualizations.""",
    tools=[CockroachDBTool(), PreviousAnalysisTool(), RetentionAnalysisTool(), VisualizationTool()],
    llm=LLM(model="gpt-4o", temperature=0.2, max_tokens=4000),  # Using more focused parameters
    knowledge=sales_knowledge,
    verbose=True
)

# Create the analysis task
analysis_task = Task(
    description="""
    Conduct a comprehensive analysis of the Plazza ecosystem focusing on sales patterns, customer retention, and product performance.
    
    ## Historical Context - IMPORTANT: USE YOUR KNOWLEDGE BASE
    
    Your first task is to access prior knowledge. Two approaches are available:
    1. Your knowledge base has been preloaded with previous analysis results - use this for context
    2. Explicitly call the PreviousAnalysisTool if you need more comprehensive history
    
    IMPORTANT: Begin by reviewing any prior findings about sales patterns or customer behavior.
    Try to specifically reference insights from your knowledge base in your analysis.
    
    ## Data Cleaning Guidelines
    
    IMPORTANT: Filter out test data to ensure accurate business analysis:
    1. Exclude products with IDs containing 'TEST', 'test', 'p1', or similar test identifiers
    2. Exclude orders that appear to be test transactions (e.g., unusually low values like $1.00)
    3. For statistical calculations, exclude extreme outliers that could skew analysis
    4. Always report product names along with IDs for better readability (e.g., "SOMPRAZ L CAP (165005)")
    
    ## Initial Exploration
    
    First, explore the key database tables you'll need for this analysis:
       1. Examine the user_transactions database, focusing on orders and order_items
       2. Examine the customer-related tables (contacts, contact_phones)
       3. Get a small sample of data to understand structure
    
    ## Targeted Business Questions
    
    1. **Sales Pattern Analysis**
       - Analyze the recent sales patterns from order_items 
       - Identify the top 5 selling products by quantity AND revenue
       - Calculate average order value and items per order
       - Identify any seasonal or weekly trends in sales
       - Compare with any previous findings - have patterns changed?
    
    2. **Customer Retention Analysis**
       - Identify customers who have made multiple orders
       - Calculate the percentage of repeat vs. one-time customers
       - Determine the average time between first and second orders
       - Analyze what products are commonly purchased by repeat customers vs. one-time customers
       - Note any customer retention insights from previous analyses
    
    3. **Product Performance Analysis**
       - Identify products with high inventory but low sales (overstock risk)
       - Calculate profit margins on top-selling products
       - Identify product categories that drive repeat purchases
       - Analyze if discount levels correlate with repeat purchases
    
    ## Visualization-Ready Output
    
    IMPORTANT: Format your analysis so it can be easily visualized:
    - For product rankings, include both product name and ID
    - Present numerical data in consistent formats suitable for charts
    - Group related metrics together for dashboard presentation
    - Use clear section headers that align with visualization categories
    
    ## Methodology
    
    For each analysis:
    1. Use the appropriate tables (orders, order_items, contacts)
    2. Execute SQL queries using the CockroachDBTool with proper filtering of test data
    3. Use the RetentionAnalysisTool for in-depth customer retention metrics (already filtered from test data)
    4. Look for data in both your knowledge base and current queries
    5. Provide 3-4 actionable business recommendations
    6. Explicitly note when your recommendations build upon previous findings
    
    ## Visualization Requirement - MANDATORY
    
    IMPORTANT: You MUST use the VisualizationTool to create visual representations of your findings.
    This is a critical business requirement and should be done immediately after completing your
    text analysis. Simply add the line "Generating visualizations..." and call the VisualizationTool
    with no parameters. The tool will automatically generate:
    
    - Bar charts for product sales analysis
    - Pie charts for customer retention metrics
    - Interactive dashboards for business metrics
    
    This step is absolutely mandatory as stakeholders require visualizations to better understand the
    insights. You cannot complete this task successfully without using the VisualizationTool.
    
    Keep your analysis concise and practical, highlighting insights directly relevant to business operations.
    Remember to leverage your knowledge base for historical context throughout your analysis.
    """,
    expected_output="""
    A comprehensive business intelligence report including:
    
    1. Brief overview of the sales and customer database structure
    2. Key sales pattern insights with product names (not just IDs) and performance metrics
    3. Detailed customer retention analysis with time-between-purchase metrics
    4. Product performance analysis highlighting inventory efficiency
    5. Clear, visualization-ready data points throughout all sections
    6. Specific, actionable recommendations for business operations
    7. Summary connecting your new findings with historical context from your knowledge base
    """,
    agent=data_analyst
)

# Create and run the crew
crew = Crew(
    agents=[data_analyst],
    tasks=[analysis_task],
    verbose=True
)

def save_analysis_results(content, filepath=ANALYSIS_RESULTS_PATH):
    """
    Save the analysis results to a file for future reference.
    Also saves a copy to the knowledge directory for RAG.
    
    Args:
        content (str): The analysis results to save
        filepath (str): The path to save the results to
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Add timestamp and metadata to help with retrieval
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Convert CrewOutput to string if needed
        if hasattr(content, 'raw'):
            content = content.raw
        
        # Format the content with clear section headers
        if isinstance(content, str) and not content.startswith("# "):
            content = f"# Sales Analysis Results - {timestamp}\n\n{content}"
        
        # Check if we need to preserve previous analysis history
        if os.path.exists(filepath):
            # Read existing content to determine what to keep
            with open(filepath, 'r') as file:
                existing_content = file.read()
                
            # Only append previous content if it doesn't already contain similar analysis
            # This avoids duplicating content in the RAG system
            if len(existing_content) > 0 and existing_content != content:
                # Check timestamps to decide what to keep
                if "# Sales Analysis Results - " in existing_content:
                    # Extract date from previous analysis
                    import re
                    match = re.search(r"# Sales Analysis Results - (\d{4}-\d{2}-\d{2})", existing_content)
                    if match:
                        prev_date = match.group(1)
                        # If previous analysis is more than 30 days old, replace it
                        try:
                            prev_datetime = datetime.strptime(prev_date, "%Y-%m-%d")
                            now = datetime.now()
                            if (now - prev_datetime).days > 30:
                                # Keep only the new content
                                print("Previous analysis is over 30 days old. Replacing with new analysis.")
                            else:
                                # Preserve history by adding new content at the beginning
                                content = f"{content}\n\n## Previous Analysis\n\n{existing_content.split('# ')[1]}"
                                print("Preserving previous analysis history in the file.")
                        except Exception as e:
                            print(f"Could not parse previous date: {e}")
        
        # Save to main filepath
        with open(filepath, 'w') as file:
            file.write(str(content))
        print(f"Analysis results saved to {filepath}")
        
        # Also save to knowledge directory
        knowledge_file = os.path.join('knowledge', 'sales_analysis_results.md')
        os.makedirs('knowledge', exist_ok=True)
        with open(knowledge_file, 'w') as file:
            file.write(str(content))
        print(f"Analysis results also saved to {knowledge_file} for RAG integration")
        
    except Exception as e:
        print(f"Error saving analysis results: {str(e)}")

# Run the crew and get the results
result = crew.kickoff()

# Save the results for future use
save_analysis_results(result)

# Note: We're not auto-generating visualizations here anymore
# Instead, we've integrated the VisualizationTool directly into the agent's toolkit,
# allowing the agent to decide when and how to create visualizations as part of its analysis

# Generate visualizations from the results
print("Generating visualizations...")
try:
    from crewai_visualization import visualize_analysis_results
    viz_paths = visualize_analysis_results(ANALYSIS_RESULTS_PATH)
    print(f"Visualizations generated and saved to {viz_paths.get('enhanced_markdown', 'visuals directory')}")
except Exception as e:
    print(f"Error generating visualizations: {str(e)}")

# Display the results
print(result)