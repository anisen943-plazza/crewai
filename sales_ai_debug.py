import os
import psycopg2
import psycopg2.extras
import time
import traceback
import signal
import json
import shutil
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from crewai.tools import BaseTool
from pydantic import Field
from crewai.knowledge.knowledge import Knowledge

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
        # For debug mode, let's use a simpler formatting approach
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

def save_analysis_results(content, filepath=ANALYSIS_RESULTS_PATH):
    """
    Save the analysis results to a file for future reference.
    Also saves a copy to the knowledge directory for RAG.
    Debug version is simplified but maintains compatibility with main version.
    
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
        
        # Format the content with clear section headers
        if not content.startswith("# "):
            content = f"# Sales Analysis Results (Debug Mode) - {timestamp}\n\n{content}"
        
        # For debug mode, we'll just replace the file to keep things simple
        if os.path.exists(filepath):
            print("DEBUG: Replacing previous analysis results with new debug results")
        
        # Save to main filepath
        with open(filepath, 'w') as file:
            file.write(content)
        print(f"DEBUG: Analysis results saved to {filepath}")
        
        # Also save to knowledge directory
        knowledge_file = os.path.join('knowledge', 'sales_analysis_results.md')
        os.makedirs('knowledge', exist_ok=True)
        with open(knowledge_file, 'w') as file:
            file.write(content)
        print(f"DEBUG: Analysis results also saved to {knowledge_file} for RAG integration")
        
    except Exception as e:
        print(f"DEBUG: Error saving analysis results: {str(e)}")

# Set a timeout for the entire process
TIMEOUT_SECONDS = 300  # 5 minutes

def handle_timeout(signum, frame):
    print("TIMEOUT: Process took too long, exiting")
    raise TimeoutError("Process timed out")

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
    
    IMPORTANT: Always explore the database schema first by running a query to understand table structures before attempting analysis.
    """
    
    def _run(self, query: str, database: str) -> str:
        print(f"DEBUG: Running query on {database}: {query[:100]}...")
        start_time = time.time()
        
        try:
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
            
            conn = None
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
                    
                    print(f"DEBUG: Query completed in {time.time() - start_time:.2f} seconds. Result rows: {len(rows)}")
                    return result_str
                    
            except Exception as e:
                error_msg = f"Error executing query on {database} database: {str(e)}"
                print(f"DEBUG: {error_msg}")
                print(f"DEBUG: {traceback.format_exc()}")
                return error_msg
            finally:
                if conn:
                    conn.close()
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            print(f"DEBUG: {error_msg}")
            print(f"DEBUG: {traceback.format_exc()}")
            return error_msg

def run_with_timeout():
    try:
        # Set the timeout handler
        signal.signal(signal.SIGALRM, handle_timeout)
        signal.alarm(TIMEOUT_SECONDS)
        
        print("DEBUG: Creating knowledge source from previous analysis...")
        
        # Create a Knowledge object for previous analysis results
        def create_knowledge_source():
            """Create a knowledge source from the analysis results file."""
            knowledge_file = 'sales_analysis_results.md'  # Relative path - will be prefixed with 'knowledge/'
            knowledge_path = os.path.join('knowledge', knowledge_file)
            
            # Check if the file exists
            if os.path.exists(knowledge_path):
                # First copy the latest content to knowledge directory
                if os.path.exists(ANALYSIS_RESULTS_PATH):
                    shutil.copy2(ANALYSIS_RESULTS_PATH, knowledge_path)
                
                print(f"DEBUG: Creating knowledge source from {knowledge_file}")
                from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
                
                # Use relative path that will work with CrewAI's knowledge directory structure
                markdown_source = TextFileKnowledgeSource(
                    file_paths=[knowledge_file],  # Just the filename, CrewAI will prepend "knowledge/"
                    chunk_size=500,              # Smaller chunks for debug mode
                    chunk_overlap=100,           # Less overlap for debug mode
                    metadata={"source": "sales_analysis_debug", "date": os.path.getmtime(knowledge_path)}
                )
                
                # Create the knowledge object
                return Knowledge(
                    collection_name="sales_analysis_debug",
                    sources=[markdown_source]
                )
            else:
                print(f"DEBUG: Warning: Knowledge file {knowledge_path} not found")
                return None
                
        # Create knowledge source
        try:
            sales_knowledge = create_knowledge_source()
            if sales_knowledge:
                print("DEBUG: Knowledge source created successfully with optimized parameters")
            else:
                # Create an empty knowledge collection if no file exists yet
                sales_knowledge = Knowledge(collection_name="sales_analysis_debug")
                print("DEBUG: No previous analysis file found. Created empty knowledge collection.")
        except Exception as e:
            print(f"DEBUG: Could not create knowledge source: {str(e)}")
            sales_knowledge = None
            
        print("DEBUG: Creating data analyst agent...")
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
            and promotional campaign effectiveness.
            
            IMPORTANT: Before beginning any new analysis, always check previous analysis results using the
            PreviousAnalysisTool to avoid redundant work and to build upon previous findings. Use this 
            historical context to guide your current analysis and identify important trends over time.""",
            tools=[CockroachDBTool(), PreviousAnalysisTool()],
            llm=LLM(model="gpt-4o", temperature=0.1, max_tokens=2000),  # Reduced temperature and token limit
            knowledge=[sales_knowledge] if sales_knowledge else None,
            verbose=True
        )
        
        print("DEBUG: Creating analysis task...")
        # Create a simplified analysis task for testing
        analysis_task = Task(
            description="""
            Conduct a focused test analysis of the database ecosystem:
            
            ## Historical Context
            
            Begin by retrieving previous analysis results using the PreviousAnalysisTool to understand what has already been done.
            
            ## New Analysis
            
            1. Examine the structure of the user_transactions database (what tables exist)
            2. Examine the structure of the defaultdb (what tables exist)
            3. Get sample data from one table in each database
            
            ## Comparison
            
            Compare your findings with the previous analysis to identify any changes in the database structure or data.
            
            Return a simple report on what you found, including table structures and example data.
            """,
            expected_output="""
            A simple report with:
            1. Brief reference to previous analysis findings
            2. List of tables in user_transactions
            3. List of tables in defaultdb
            4. Sample data from one table in each database
            5. Notes on any changes observed compared to previous analysis
            """,
            agent=data_analyst
        )
        
        print("DEBUG: Creating and running crew...")
        # Create and run the crew
        crew = Crew(
            agents=[data_analyst],
            tasks=[analysis_task],
            verbose=True
        )
        
        print("DEBUG: Starting crew execution...")
        result = crew.kickoff()
        
        # Cancel the alarm
        signal.alarm(0)
        
        print("\n\nFINAL RESULT:")
        print(result)
        
        # Save the results for future reference
        save_analysis_results(result)
        
    except TimeoutError:
        print("Execution timed out!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print(traceback.format_exc())

if __name__ == "__main__":
    run_with_timeout()