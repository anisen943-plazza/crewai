import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from crewai.tools import BaseTool
from pydantic import Field

# Load environment variables
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please set it in your .env file or environment.")
os.environ["OPENAI_API_KEY"] = openai_key

class CockroachDBTool(BaseTool):
    name: str = "CockroachDBTool"
    description: str = """Execute SQL queries against one of the CockroachDB databases in the Plazza ecosystem.
    
    AVAILABLE DATABASES (you must specify which one to use with the 'database' parameter):

    1. user_transactions - Customer and order management
       - contacts: customer information (id, first_name, last_name, email, etc.)
       - contact_addresses: addresses linked to contacts (address_id, house_number, locality, state, pincode)
       - contact_phones: phone numbers linked to contacts (phone_number, is_primary)
       - orders: order information (order_id, contact_id, status, bill_total_amount, created_at)
       - order_items: individual items in orders (product_id, medicine_name, quantity, mrp, selling_price)
       - payIments: payment details (payment_id, customer_id, order_amount, payment_status, payment_method)
       - products: product catalog (product_id, medicine_name, medicine_type, mrp, quantity_available)
       - stores: store information (name, address, city, state, pincode, gst_number)
       - tookan_jobs: delivery tracking (job_id, agent_id, job_status, tracking_url)
       - whatsapp_messages: message history (message_id, order_id, status)
       - zoho_config: Zoho integration settings (organization_id, tax_settings)

    2. defaultdb - Core product catalog
       - all_products: complete product catalog (product_id, name, manufacturers, salt_composition, medicine_type)
       - inventory_products: inventory tracking (product_id, vendor_id, batch_number, expiry_date, stock_qty)
       - plazza_price_table: pricing information (product_id, mrp, selling_price, discount_percentage)
       - validated_matches: validated product matches between systems (product_id, vendor_product_id, confidence)

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
    
    IMPORTANT: Always explore the database schema first by running a query to understand table structures before attempting analysis.
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
        
        try:
            conn = psycopg2.connect(connection_string)
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                
                if not rows:
                    return f"No results found for query in {database} database"
                
                result_str = f"Results from {database} database:\n"
                result_str += "\n".join([str(dict(row)) for row in rows[:20]])
                if len(rows) > 20:
                    result_str += f"\n...and {len(rows) - 20} more rows"
                return result_str
                
        except Exception as e:
            return f"Error executing query on {database} database: {str(e)}"
        finally:
            if conn:
                conn.close()

# Create the NL2SQL Agent
data_analyst = Agent(
    role="Enterprise Data Analyst",
    goal="Analyze business data across multiple databases to identify trends and provide actionable insights",
    backstory="""You are an expert SQL data analyst with years of experience in retail and 
    pharmaceutical analytics. You understand multi-database ecosystems intuitively and can translate
    natural language questions into precise SQL queries for CockroachDB.
    
    You're skilled at identifying which database contains the necessary data and can construct 
    complex queries for cross-database analysis. You're thorough in your approach, 
    always exploring database schemas first before diving into analytical queries.
    
    Your expertise includes retail sales analysis, inventory management, customer behavior tracking,
    and promotional campaign effectiveness.""",
    tools=[CockroachDBTool()],
    llm=LLM(model="gpt-4o", temperature=0.2, max_tokens=4000),  # Using more focused parameters
    verbose=True
)

# Create the analysis task
analysis_task = Task(
    description="""
    Conduct a focused cross-database analysis of the Plazza ecosystem, targeting specific business insights. 
    This is a streamlined analysis focusing on the two most important business questions.
    
    ## Initial Exploration
    
    First explore the key database schemas:
       1. Examine the user_transactions database (identify tables and their key columns)
       2. Examine the defaultdb database (identify tables and their key columns)
       3. Get sample data from critical tables to understand structure
    
    ## Targeted Business Questions (Focus on these two only)
    
    1. **Inventory-Sales Gap Analysis**
       - Identify the top 5 products with high inventory levels (defaultdb) and low sales (user_transactions)
       - Provide a summary table with product name, inventory quantity, sales volume, and estimated capital value
    
    2. **Data Consistency Analysis**
       - Check for products that exist in inventory but not in the product catalog
       - Provide a count of inconsistencies and 2-3 examples
    
    ## Methodology
    
    For each analysis:
    1. Clearly identify which tables in which databases you need to query
    2. Execute focused queries using the CockroachDBTool with the appropriate database parameter
    3. Keep queries simple and limit results to small samples (LIMIT 5-10)
    4. Provide 2-3 actionable recommendations based on your findings
    
    Keep your analysis concise and focus on quality insights rather than quantity.
    """,
    expected_output="""
    A focused cross-database business intelligence report including:
    
    1. Brief summary of database structures (tables and relationships)
    2. Analysis of inventory-sales gap with top 5 products identified
    3. Data consistency findings with examples of inconsistencies
    4. Specific, actionable recommendations (2-3) for business operations
    """,
    agent=data_analyst
)

# Create and run the crew
crew = Crew(
    agents=[data_analyst],
    tasks=[analysis_task],
    verbose=True
)

result = crew.kickoff()
print(result)