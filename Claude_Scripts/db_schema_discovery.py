"""
Database Schema Discovery Tool

This script explores the CockroachDB cluster to discover and document new databases and tables.
"""

import os
import psycopg2
import psycopg2.extras
import json
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Connection strings for each database
db_connection_vars = {
    "user_transactions": "DATABASE_URL_USER_TRANSACTIONS",
    "defaultdb": "DATABASE_URL",
    "plazza_erp": "DATABASE_URL_ERP",
    "user_events": "DATABASE_URL_USER"
}

def get_database_connection(db_name):
    """Get a database connection for the specified database"""
    conn_var = db_connection_vars.get(db_name)
    if not conn_var:
        raise ValueError(f"Unknown database: {db_name}")
    
    conn_string = os.getenv(conn_var)
    if not conn_string:
        raise ValueError(f"Environment variable {conn_var} is not set")
    
    return psycopg2.connect(conn_string)

def list_all_databases():
    """List all databases in the cluster"""
    # Use the defaultdb connection to list all databases
    conn = get_database_connection("defaultdb")
    databases = []
    
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("SHOW DATABASES;")
            for row in cursor.fetchall():
                databases.append(row[0])
    finally:
        conn.close()
    
    return databases

def list_tables_in_database(db_name):
    """List all tables in a specific database"""
    conn = get_database_connection(db_name)
    tables = []
    
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)
            for row in cursor.fetchall():
                tables.append(row[0])
    finally:
        conn.close()
    
    return tables

def get_table_schema(db_name, table_name):
    """Get the schema for a specific table"""
    conn = get_database_connection(db_name)
    columns = []
    
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("""
                SELECT column_name, data_type, is_nullable
                FROM information_schema.columns
                WHERE table_schema = 'public' AND table_name = %s
                ORDER BY ordinal_position;
            """, (table_name,))
            
            for row in cursor.fetchall():
                columns.append({
                    "name": row['column_name'],
                    "type": row['data_type'],
                    "nullable": row['is_nullable'] == 'YES'
                })
    finally:
        conn.close()
    
    return columns

def get_table_sample(db_name, table_name, limit=5):
    """Get a sample of data from a specific table"""
    conn = get_database_connection(db_name)
    sample = []
    
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            # Use safe identifier quoting
            cursor.execute(f"SELECT * FROM \"{table_name}\" LIMIT %s", (limit,))
            for row in cursor.fetchall():
                sample.append(dict(row))
    except Exception as e:
        return [{"error": str(e)}]
    finally:
        conn.close()
    
    return sample

def discover_new_databases():
    """Discover new databases not in our known list"""
    all_databases = list_all_databases()
    
    # Filter to known databases with connection strings
    known_databases = [db for db in all_databases if db in db_connection_vars]
    
    # Also note any new databases discovered
    new_databases = [db for db in all_databases if db not in db_connection_vars and not db.startswith('system')]
    
    return {
        "known_databases": known_databases,
        "new_databases": new_databases
    }

def explore_database(db_name):
    """Explore a specific database and return its structure"""
    try:
        tables = list_tables_in_database(db_name)
        db_structure = {
            "tables": {}
        }
        
        for table_name in tables:
            columns = get_table_schema(db_name, table_name)
            sample = get_table_sample(db_name, table_name, limit=2)
            
            db_structure["tables"][table_name] = {
                "columns": columns,
                "sample": sample
            }
        
        return db_structure
    except Exception as e:
        print(f"Error exploring database {db_name}: {str(e)}")
        return {"error": str(e)}

def explore_all_databases():
    """Explore all known and new databases"""
    database_info = discover_new_databases()
    
    # Create output structure
    result = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "known_databases": {},
        "new_databases": {}
    }
    
    # Explore known databases
    for db_name in database_info["known_databases"]:
        print(f"Exploring known database: {db_name}")
        result["known_databases"][db_name] = explore_database(db_name)
    
    # Attempt to explore new databases if possible
    for db_name in database_info["new_databases"]:
        print(f"Discovered new database: {db_name}")
        # You would need a connection string for each new database
        # This is just a placeholder - in reality you would need to prompt for credentials
        result["new_databases"][db_name] = {"message": "Connection details not available"}
    
    return result

def generate_markdown_report(data):
    """Generate a markdown report of the database exploration"""
    md = f"# CockroachDB Schema Discovery Report\n\n"
    md += f"Report generated at: {data['generated_at']}\n\n"
    
    md += "## Database Overview\n\n"
    
    # Known databases summary
    md += "### Known Databases\n\n"
    for db_name, db_info in data['known_databases'].items():
        if 'error' in db_info:
            md += f"- {db_name}: Error connecting - {db_info['error']}\n"
        else:
            table_count = len(db_info['tables']) if 'tables' in db_info else 0
            md += f"- {db_name}: {table_count} tables\n"
    
    md += "\n"
    
    # New databases discovered
    if data['new_databases']:
        md += "### Newly Discovered Databases\n\n"
        for db_name in data['new_databases']:
            md += f"- {db_name}\n"
        md += "\n"
    else:
        md += "### No New Databases Discovered\n\n"
    
    # Detailed tables information for each known database
    md += "## Detailed Database Information\n\n"
    
    for db_name, db_info in data['known_databases'].items():
        md += f"### {db_name}\n\n"
        
        if 'error' in db_info:
            md += f"Error connecting to database: {db_info['error']}\n\n"
            continue
        
        if 'tables' not in db_info:
            md += "No tables found or error exploring database.\n\n"
            continue
        
        md += f"Contains {len(db_info['tables'])} tables.\n\n"
        
        # List tables
        md += "#### Tables\n\n"
        for table_name, table_info in sorted(db_info['tables'].items()):
            md += f"##### {table_name}\n\n"
            
            if 'columns' in table_info:
                # Table structure
                md += "| Column | Type | Nullable |\n"
                md += "|--------|------|----------|\n"
                
                for column in table_info['columns']:
                    nullable = "Yes" if column['nullable'] else "No"
                    md += f"| {column['name']} | {column['type']} | {nullable} |\n"
                
                md += "\n"
                
                # Sample data if available
                if 'sample' in table_info and table_info['sample']:
                    md += "Sample data:\n\n"
                    md += "```json\n"
                    md += json.dumps(table_info['sample'], indent=2, default=str)
                    md += "\n```\n\n"
            else:
                md += "Could not retrieve column information.\n\n"
    
    return md

def main():
    """Main function"""
    print("Starting CockroachDB schema discovery...")
    
    # Explore all databases
    exploration_data = explore_all_databases()
    
    # Save the raw JSON data
    output_dir = "Ref_documents"
    os.makedirs(output_dir, exist_ok=True)
    
    json_path = os.path.join(output_dir, "cockroachdb_exploration.json")
    with open(json_path, 'w') as f:
        json.dump(exploration_data, f, indent=2, default=str)
    print(f"Raw exploration data saved to {json_path}")
    
    # Generate markdown report
    md_report = generate_markdown_report(exploration_data)
    md_path = os.path.join(output_dir, "CockroachDB_Discovery_Report.md")
    with open(md_path, 'w') as f:
        f.write(md_report)
    print(f"Markdown report saved to {md_path}")
    
    # Print summary
    print("\nSummary:")
    print(f"- Known databases: {', '.join(exploration_data['known_databases'].keys())}")
    
    if exploration_data['new_databases']:
        print(f"- New databases discovered: {', '.join(exploration_data['new_databases'].keys())}")
    else:
        print("- No new databases discovered.")

if __name__ == "__main__":
    main()