import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from crewai.tools import BaseTool
from pydantic import Field

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

class CockroachDBTool(BaseTool):
    name: str = "CockroachDBTool"
    description: str = """Execute SQL queries against a CockroachDB database containing:
    - contacts: customer information (id, first_name, last_name, email, etc.)
    - contact_addresses: addresses linked to contacts
    - contact_phones: phone numbers linked to contacts
    - orders: order information (order_id, contact_id, status, amounts)
    - order_items: individual items in orders (product_id, medicine_name, quantity, prices)
    - payments: payment details (payment_id, customer_id, payment_status, etc.)
    - products: product catalog (product_id, medicine_name, prices, quantities)
    
    Use this tool to query the database and analyze sales data.
    """
    
    def _run(self, sql_query: str) -> str:
        try:
            conn = psycopg2.connect(os.getenv("DATABASE_URL_USER_TRANSACTIONS"))
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute(sql_query)
                rows = cursor.fetchall()
                
                if not rows:
                    return "No results found"
                
                result_str = "\n".join([str(dict(row)) for row in rows[:20]])
                if len(rows) > 20:
                    result_str += f"\n...and {len(rows) - 20} more rows"
                return result_str
                
        except Exception as e:
            return f"Error executing query: {str(e)}"
        finally:
            if conn:
                conn.close()

# Create the NL2SQL Agent
data_analyst = Agent(
    role="Sales Data Analyst",
    goal="Analyze sales data to identify trends and provide actionable insights",
    backstory="""You are an expert SQL data analyst with years of experience in retail and 
    pharmaceutical analytics. You understand database schemas intuitively and can translate
    natural language questions into precise SQL queries for CockroachDB.""",
    tools=[CockroachDBTool()],
    llm=LLM(model="gpt-4o"),  # CrewAI will use OPENAI_API_KEY from your .env file
    verbose=True
)

# Create the analysis task
analysis_task = Task(
    description="""
    Analyze the sales data to identify key business insights:
    
    1. First examine the database schema to understand available tables and relationships
    2. Then answer these questions by translating them to SQL and executing:
       - What are the top 5 selling products by quantity?
       - What is the average order value?
       - Which payment methods are most frequently used?
       - How many unique customers have placed orders?
       - What are the total sales by month?
        - What is the average time between order and payment?
        - List the orders successfully paid within last 72 hours.
    
    For each question:
    1. Write the SQL query
    2. Execute it using the CockroachDBTool
    3. Analyze the results and provide business insights
    """,
    expected_output="""A comprehensive sales analysis with SQL queries and insights for each question,
    highlighting key trends and actionable recommendations.""",
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