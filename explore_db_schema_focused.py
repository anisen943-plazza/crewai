import os
import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
import logging
from dotenv import load_dotenv
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("db-explorer")

# Load environment variables
load_dotenv()

class DatabaseConnection:
    def __init__(self, db_url=None):
        self.db_url = db_url or os.getenv("DATABASE_URL")
        if not self.db_url:
            raise ValueError("DATABASE_URL environment variable is not set")
        
        logger.info(f"Connecting to database...")
    
    @contextmanager
    def get_connection(self):
        conn = None
        try:
            conn = psycopg2.connect(self.db_url)
            conn.autocommit = False
            logger.info("Database connection established")
            yield conn
        except Exception as e:
            logger.error(f"Database connection error: {str(e)}")
            raise
        finally:
            if conn:
                conn.close()
                logger.info("Database connection closed")
    
    @contextmanager
    def get_cursor(self, cursor_factory=RealDictCursor):
        with self.get_connection() as conn:
            cursor = conn.cursor(cursor_factory=cursor_factory)
            try:
                yield cursor
                conn.commit()
            except Exception:
                conn.rollback()
                logger.error("Database query error")
                raise
            finally:
                cursor.close()

    def get_database_info(self):
        """Get basic database information."""
        with self.get_cursor() as cursor:
            cursor.execute("SELECT current_database(), current_user;")
            return cursor.fetchone()
    
    def get_tables(self, schema='public'):
        """Get all tables in a specific schema."""
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = %s AND table_type = 'BASE TABLE'
                ORDER BY table_name;
            """, (schema,))
            return [row['table_name'] for row in cursor.fetchall()]
    
    def get_table_columns(self, table_name, schema='public'):
        """Get detailed information about table columns."""
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT 
                    column_name, 
                    data_type, 
                    character_maximum_length,
                    column_default, 
                    is_nullable
                FROM information_schema.columns
                WHERE table_schema = %s AND table_name = %s
                ORDER BY ordinal_position;
            """, (schema, table_name))
            return cursor.fetchall()
    
    def get_primary_key(self, table_name, schema='public'):
        """Get primary key columns for a table."""
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT c.column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.constraint_column_usage AS ccu USING (constraint_schema, constraint_name)
                JOIN information_schema.columns AS c 
                    ON c.table_schema = tc.constraint_schema
                    AND c.table_name = tc.table_name
                    AND c.column_name = ccu.column_name
                WHERE tc.constraint_type = 'PRIMARY KEY'
                    AND tc.table_schema = %s
                    AND tc.table_name = %s;
            """, (schema, table_name))
            return [row['column_name'] for row in cursor.fetchall()]
    
    def get_foreign_keys(self, table_name, schema='public'):
        """Get foreign key relationships for a table."""
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT
                    tc.constraint_name,
                    kcu.column_name,
                    ccu.table_schema AS foreign_table_schema,
                    ccu.table_name AS foreign_table_name,
                    ccu.column_name AS foreign_column_name
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                    ON tc.constraint_name = kcu.constraint_name
                    AND tc.table_schema = kcu.table_schema
                JOIN information_schema.constraint_column_usage AS ccu
                    ON ccu.constraint_name = tc.constraint_name
                    AND ccu.table_schema = tc.constraint_schema
                WHERE tc.constraint_type = 'FOREIGN KEY'
                    AND tc.table_schema = %s
                    AND tc.table_name = %s;
            """, (schema, table_name))
            return cursor.fetchall()
    
    def get_sample_data(self, table_name, schema='public', limit=5):
        """Get sample data from the table."""
        try:
            with self.get_cursor() as cursor:
                cursor.execute(f"""
                    SELECT * FROM "{schema}"."{table_name}" LIMIT {limit};
                """)
                return cursor.fetchall()
        except Exception as e:
            logger.warning(f"Could not get sample data for {schema}.{table_name}: {str(e)}")
            return []
    
    def generate_schema_documentation(self, output_dir):
        """Generate comprehensive documentation of the database schema."""
        db_info = self.get_database_info()
        schema = 'public'  # Focus only on public schema for CockroachDB
        
        # Create database structure
        db_structure = {
            "database_name": db_info['current_database'],
            "user": db_info['current_user'],
            "tables": {}
        }
        
        tables = self.get_tables(schema)
        for table in tables:
            # Get table details
            columns = self.get_table_columns(table, schema)
            primary_keys = self.get_primary_key(table, schema)
            foreign_keys = self.get_foreign_keys(table, schema)
            sample_data = self.get_sample_data(table, schema)
            
            table_data = {
                "name": table,
                "columns": columns,
                "primary_keys": primary_keys,
                "foreign_keys": foreign_keys,
                "sample_data": sample_data if sample_data else None
            }
            
            db_structure["tables"][table] = table_data
        
        # Save raw JSON data
        json_path = os.path.join(output_dir, "database_schema.json")
        with open(json_path, "w") as f:
            json.dump(db_structure, f, indent=2, default=str)
        
        # Generate markdown documentation
        self._generate_markdown_docs(db_structure, output_dir)
        
        return db_structure
    
    def _generate_markdown_docs(self, db_structure, output_dir):
        """Generate markdown documentation from the database structure."""
        # Main README
        readme_content = f"""# CockroachDB Schema Documentation - {db_structure['database_name']}

## Database Information
- **Database Name:** {db_structure['database_name']}
- **User:** {db_structure['user']}
- **Tables:** {len(db_structure['tables'])}

## Connection Information

### Connection String Format
```
postgresql://username:password@hostname:port/database?sslmode=verify-full
```

### Connection Parameters
- **Hostname:** plazza-catalogue-3852.jxf.gcp-us-central1.cockroachlabs.cloud
- **Port:** 26257
- **Database:** {db_structure['database_name']}
- **SSL Mode:** verify-full

## Connection Code Examples

### Python (with psycopg2)
```python
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    conn = None
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL_USER_TRANSACTIONS"))
        yield conn
    finally:
        if conn:
            conn.close()

@contextmanager
def get_db_cursor(cursor_factory=RealDictCursor):
    with get_db_connection() as conn:
        cursor = conn.cursor(cursor_factory=cursor_factory)
        try:
            yield cursor
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            cursor.close()

# Example query
with get_db_cursor() as cursor:
    cursor.execute("SELECT * FROM table_name LIMIT 10")
    results = cursor.fetchall()
```

### Python (with Connection Pool)
```python
import os
from psycopg2.pool import ThreadedConnectionPool
from contextlib import contextmanager
import logging
from psycopg2.extras import RealDictCursor

logger = logging.getLogger(__name__)

class DatabasePool:
    _instance = None
    pool = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabasePool, cls).__new__(cls)
        return cls._instance

    def init_pool(self, minconn=2, maxconn=10):
        if self.pool is None:
            try:
                db_url = os.getenv("DATABASE_URL_USER_TRANSACTIONS")
                if not db_url:
                    raise ValueError("DATABASE_URL_USER_TRANSACTIONS is not set")
                
                self.pool = ThreadedConnectionPool(
                    minconn,
                    maxconn,
                    db_url
                )
                # Test connection
                with self.get_connection() as conn:
                    with conn.cursor() as cursor:
                        cursor.execute("SELECT 1")
                        cursor.fetchone()
                
                logger.info("Database pool initialized successfully")
            except Exception:
                logger.error("Failed to initialize database pool")
                raise

    def close_pool(self):
        if self.pool is not None:
            self.pool.closeall()
            logger.info("Database pool closed")
            self.pool = None

    @contextmanager
    def get_connection(self):
        conn = None
        try:
            # Check if pool exists and initialize if needed
            if self.pool is None:
                self.init_pool()
                
            conn = self.pool.getconn()
            
            # Check if connection is closed and reconnect if needed
            if conn.closed:
                logger.warning("Connection was closed, getting a new one")
                self.pool.putconn(conn)
                
                # Reinitialize the pool to force new connections
                self.close_pool()
                self.init_pool()
                conn = self.pool.getconn()
                
            yield conn
        except Exception:
            logger.error("Database connection error")
            raise
        finally:
            if conn and not conn.closed:
                self.pool.putconn(conn)
            elif conn:
                logger.warning("Not returning closed connection to pool")

    @contextmanager
    def get_cursor(self, cursor_factory=RealDictCursor):
        with self.get_connection() as conn:
            cursor = conn.cursor(cursor_factory=cursor_factory)
            try:
                yield cursor
                conn.commit()
            except Exception:
                conn.rollback()
                raise
            finally:
                cursor.close()

# Global instance
db_pool = DatabasePool()
db_pool.init_pool()

# Example usage
with db_pool.get_cursor() as cursor:
    cursor.execute("SELECT * FROM table_name LIMIT 10")
    results = cursor.fetchall()
```

## Tables
"""
        
        # Add links to each table
        for table_name in sorted(db_structure['tables'].keys()):
            readme_content += f"- [{table_name}](#{table_name.lower()})\n"
        
        readme_content += "\n"
        
        # Add detailed table documentation
        for table_name, table in sorted(db_structure['tables'].items()):
            readme_content += f"## {table_name}\n\n"
            
            # Columns
            readme_content += "### Columns\n\n"
            readme_content += "| Column | Type | Length | Default | Nullable |\n"
            readme_content += "|--------|------|--------|---------|----------|\n"
            
            for col in table['columns']:
                col_type = col['data_type']
                if col['character_maximum_length']:
                    col_type += f"({col['character_maximum_length']})"
                
                readme_content += f"| {col['column_name']} | {col_type} | {col['character_maximum_length'] or '-'} | {col['column_default'] or '-'} | {col['is_nullable']} |\n"
            
            # Primary Keys
            if table['primary_keys']:
                readme_content += "\n### Primary Key\n\n"
                readme_content += f"- {', '.join(table['primary_keys'])}\n"
            
            # Foreign Keys
            if table['foreign_keys']:
                readme_content += "\n### Foreign Keys\n\n"
                readme_content += "| Column | References |\n"
                readme_content += "|--------|------------|\n"
                
                for fk in table['foreign_keys']:
                    readme_content += f"| {fk['column_name']} | {fk['foreign_table_schema']}.{fk['foreign_table_name']}.{fk['foreign_column_name']} |\n"
            
            # Sample Data (if available)
            if table['sample_data'] and len(table['sample_data']) > 0:
                readme_content += "\n### Sample Data\n\n"
                
                # Get column names
                columns = table['sample_data'][0].keys()
                readme_content += "| " + " | ".join(columns) + " |\n"
                readme_content += "|" + "|".join(["---" for _ in columns]) + "|\n"
                
                for row in table['sample_data']:
                    # Format each value to handle special characters and long content
                    values = []
                    for col in columns:
                        val = str(row[col]).replace("|", "\\|")
                        if len(val) > 50:
                            val = val[:47] + "..."
                        values.append(val)
                    
                    readme_content += "| " + " | ".join(values) + " |\n"
            
            readme_content += "\n"
        
        # Create README
        with open(os.path.join(output_dir, "README.md"), "w") as f:
            f.write(readme_content)

def main():
    # Create the output directory
    output_dir = "/Users/aniruddhasen/Projects/crewai/API_documents/user_transactions"
    os.makedirs(output_dir, exist_ok=True)
    
    # Focus only on the user_transactions database
    db_url = os.getenv("DATABASE_URL_USER_TRANSACTIONS", "postgresql://aniruddha:qls3UibsCfTOXA9P7CbgnQ@plazza-catalogue-3852.jxf.gcp-us-central1.cockroachlabs.cloud:26257/user_transactions?sslmode=verify-full")
    
    try:
        logger.info(f"Generating documentation for user_transactions database...")
        db = DatabaseConnection(db_url)
        db.generate_schema_documentation(output_dir)
        
        logger.info(f"Documentation generated successfully in {output_dir}")
    except Exception as e:
        logger.error(f"Failed to generate documentation: {str(e)}")
        raise

if __name__ == "__main__":
    main()