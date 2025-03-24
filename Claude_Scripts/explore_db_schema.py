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
            except Exception as e:
                conn.rollback()
                logger.error(f"Database query error: {str(e)}")
                raise
            finally:
                cursor.close()

    def get_database_info(self):
        """Get basic database information."""
        with self.get_cursor() as cursor:
            cursor.execute("SELECT current_database(), current_user;")
            return cursor.fetchone()
    
    def get_schemas(self):
        """Get all schemas in the database."""
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT schema_name 
                FROM information_schema.schemata 
                WHERE schema_name NOT IN ('pg_catalog', 'information_schema', 'crdb_internal', 'pg_extension')
                ORDER BY schema_name;
            """)
            return [row['schema_name'] for row in cursor.fetchall()]
    
    def get_tables(self, schema='public'):
        """Get all tables in a specific schema."""
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = %s
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
    
    def get_indexes(self, table_name, schema='public'):
        """Get indexes for a table (CockroachDB specific)."""
        with self.get_cursor() as cursor:
            # For CockroachDB, we need to use crdb_internal schema
            try:
                cursor.execute("""
                    SELECT 
                        i.name AS index_name,
                        i.unique AS is_unique,
                        array_to_string(i.column_names, ', ') AS column_names,
                        i.storing_column_names AS storing_columns,
                        i.index_type
                    FROM crdb_internal.indexes i
                    JOIN crdb_internal.tables t ON i.table_id = t.table_id
                    WHERE t.schema_name = %s AND t.name = %s;
                """, (schema, table_name))
                return cursor.fetchall()
            except Exception as e:
                logger.warning(f"Could not get indexes for {schema}.{table_name}: {str(e)}")
                return []
    
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
        schemas = self.get_schemas()
        
        # Create database structure
        db_structure = {
            "database_name": db_info['current_database'],
            "user": db_info['current_user'],
            "schemas": {}
        }
        
        for schema in schemas:
            tables = self.get_tables(schema)
            schema_data = {
                "name": schema,
                "tables": {}
            }
            
            for table in tables:
                # Get table details
                columns = self.get_table_columns(table, schema)
                primary_keys = self.get_primary_key(table, schema)
                foreign_keys = self.get_foreign_keys(table, schema)
                indexes = self.get_indexes(table, schema)
                sample_data = self.get_sample_data(table, schema)
                
                table_data = {
                    "name": table,
                    "columns": columns,
                    "primary_keys": primary_keys,
                    "foreign_keys": foreign_keys,
                    "indexes": indexes,
                    "sample_data": sample_data if sample_data else None
                }
                
                schema_data["tables"][table] = table_data
            
            db_structure["schemas"][schema] = schema_data
        
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
- **User:** {db_structure['database_name']}
- **Schemas:** {', '.join(db_structure['schemas'].keys())}

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
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
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
                self.pool = ThreadedConnectionPool(
                    minconn,
                    maxconn,
                    os.getenv("DATABASE_URL")
                )
                logger.info("Database pool initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize database pool: {str(e)}")
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
            conn = self.pool.getconn()
            yield conn
        except Exception as e:
            logger.error(f"Database connection error: {str(e)}")
            raise
        finally:
            if conn:
                self.pool.putconn(conn)

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

## Schemas
"""
        
        # Add links to each schema
        for schema_name, schema in db_structure['schemas'].items():
            readme_content += f"- [{schema_name.capitalize()} Schema](./schemas/{schema_name}.md)\n"
        
        # Create schemas directory
        schemas_dir = os.path.join(output_dir, "schemas")
        os.makedirs(schemas_dir, exist_ok=True)
        
        # Create main README
        with open(os.path.join(output_dir, "README.md"), "w") as f:
            f.write(readme_content)
        
        # Create individual schema documentation
        for schema_name, schema in db_structure['schemas'].items():
            schema_content = f"# {schema_name.capitalize()} Schema\n\n"
            schema_content += "## Tables\n\n"
            
            # Add table of contents
            for table_name in schema['tables'].keys():
                schema_content += f"- [{table_name}](#{table_name.lower()})\n"
            
            schema_content += "\n"
            
            # Process each table
            for table_name, table in schema['tables'].items():
                schema_content += f"## {table_name}\n\n"
                
                # Columns
                schema_content += "### Columns\n\n"
                schema_content += "| Column | Type | Length | Default | Nullable |\n"
                schema_content += "|--------|------|--------|---------|----------|\n"
                
                for col in table['columns']:
                    col_type = col['data_type']
                    if col['character_maximum_length']:
                        col_type += f"({col['character_maximum_length']})"
                    
                    schema_content += f"| {col['column_name']} | {col_type} | {col['character_maximum_length'] or '-'} | {col['column_default'] or '-'} | {col['is_nullable']} |\n"
                
                # Primary Keys
                if table['primary_keys']:
                    schema_content += "\n### Primary Key\n\n"
                    schema_content += f"- {', '.join(table['primary_keys'])}\n"
                
                # Foreign Keys
                if table['foreign_keys']:
                    schema_content += "\n### Foreign Keys\n\n"
                    schema_content += "| Column | References |\n"
                    schema_content += "|--------|------------|\n"
                    
                    for fk in table['foreign_keys']:
                        schema_content += f"| {fk['column_name']} | {fk['foreign_table_schema']}.{fk['foreign_table_name']}.{fk['foreign_column_name']} |\n"
                
                # Indexes
                if table['indexes']:
                    schema_content += "\n### Indexes\n\n"
                    schema_content += "| Name | Columns | Type | Unique |\n"
                    schema_content += "|------|---------|------|--------|\n"
                    
                    for idx in table['indexes']:
                        schema_content += f"| {idx['index_name']} | {idx['column_names']} | {idx['index_type']} | {idx['is_unique']} |\n"
                
                # Sample Data
                if table['sample_data']:
                    schema_content += "\n### Sample Data\n\n"
                    
                    # Get column names
                    if table['sample_data']:
                        columns = table['sample_data'][0].keys()
                        schema_content += "| " + " | ".join(columns) + " |\n"
                        schema_content += "|" + "|".join(["---" for _ in columns]) + "|\n"
                        
                        for row in table['sample_data']:
                            schema_content += "| " + " | ".join([str(row[col]) for col in columns]) + " |\n"
                
                schema_content += "\n"
            
            # Write schema documentation
            with open(os.path.join(schemas_dir, f"{schema_name}.md"), "w") as f:
                f.write(schema_content)

def main():
    # Create the output directory
    output_dir = "/Users/aniruddhasen/Projects/crewai/API_documents"
    os.makedirs(output_dir, exist_ok=True)
    
    # Database URLs for different databases in the cluster
    db_urls = {
        "defaultdb": os.getenv("DATABASE_URL", "postgresql://aniruddha:qls3UibsCfTOXA9P7CbgnQ@plazza-catalogue-3852.jxf.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"),
        "user_transactions": os.getenv("DATABASE_URL_USER_TRANSACTIONS", "postgresql://aniruddha:qls3UibsCfTOXA9P7CbgnQ@plazza-catalogue-3852.jxf.gcp-us-central1.cockroachlabs.cloud:26257/user_transactions?sslmode=verify-full"),
        "plazza_erp": os.getenv("DATABASE_URL_ERP", "postgresql://aniruddha:qls3UibsCfTOXA9P7CbgnQ@plazza-catalogue-3852.jxf.gcp-us-central1.cockroachlabs.cloud:26257/plazza_erp?sslmode=verify-full")
    }
    
    # Create a combined README
    combined_readme = '''# CockroachDB API Documentation - plazza-catalogue-3852

## Cluster Information
- **Hostname:** plazza-catalogue-3852.jxf.gcp-us-central1.cockroachlabs.cloud
- **Port:** 26257
- **SSL Mode:** verify-full

## Databases
- [defaultdb](./defaultdb/README.md) - Core product catalog database
- [user_transactions](./user_transactions/README.md) - Customer and order management
- [plazza_erp](./plazza_erp/README.md) - ERP system for business operations

## Connection Information

### Connection String Format
```
postgresql://username:password@hostname:port/database?sslmode=verify-full
```

### Connection Code Examples

#### Python (with Connection Pool)
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
        # Initialize the connection pool
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
                
                logger.info("✅ Database pool initialized successfully")
            except Exception as e:
                logger.error(f"❌ Failed to initialize database pool: {str(e)}")
                raise

    def close_pool(self):
        # Close all pool connections
        if self.pool is not None:
            self.pool.closeall()
            logger.info("🔌 Database pool closed")
            self.pool = None

    @contextmanager
    def get_connection(self):
        # Get a database connection from the pool
        conn = None
        try:
            # Check if pool exists and initialize if needed
            if self.pool is None:
                self.init_pool()
                
            conn = self.pool.getconn()
            
            # Check if connection is closed and reconnect if needed
            if conn.closed:
                logger.warning("⚠️ Connection was closed, getting a new one")
                self.pool.putconn(conn)
                
                # Reinitialize the pool to force new connections
                self.close_pool()
                self.init_pool()
                conn = self.pool.getconn()
                
            logger.info("🔗 Acquired database connection from pool")
            yield conn
        except Exception as e:
            logger.error(f"❌ Database connection error: {str(e)}")
            raise
        finally:
            if conn and not conn.closed:
                self.pool.putconn(conn)
                logger.info("🔙 Released database connection back to pool")
            elif conn:
                logger.warning("⚠️ Not returning closed connection to pool")

    @contextmanager
    def get_cursor(self, cursor_factory=RealDictCursor):
        # Get a database cursor with automatic cleanup
        with self.get_connection() as conn:
            cursor = conn.cursor(cursor_factory=cursor_factory)
            try:
                yield cursor
                conn.commit()
            except Exception as e:
                conn.rollback()
                logger.error(f"❌ Database query error: {str(e)}")
                raise
            finally:
                if not cursor.closed:
                    cursor.close()

# Global instance
db_pool = DatabasePool()

# Example usage
with db_pool.get_cursor() as cursor:
    cursor.execute("SELECT * FROM table_name LIMIT 10")
    results = cursor.fetchall()
```

## Database Usage Guidelines

1. **Connection Pooling**
   - Always use connection pooling for production applications
   - Set appropriate min and max pool sizes based on your workload
   - Close pools properly when shutting down the application

2. **Query Best Practices**
   - Use parameterized queries to prevent SQL injection
   - Keep transactions short to minimize locking
   - Use LIMIT clauses to avoid retrieving large result sets
   - Create appropriate indexes for query patterns

3. **Error Handling**
   - Implement comprehensive try/catch blocks for database operations
   - Handle connection errors with proper retries
   - Log database errors with sufficient context for debugging

4. **Security**
   - Never commit database credentials to version control
   - Use environment variables for storing connection information
   - Implement proper access controls at the database level
'''

    # Write combined README
    with open(os.path.join(output_dir, "README.md"), "w") as f:
        f.write(combined_readme)
    
    # Process each database
    for db_name, db_url in db_urls.items():
        try:
            if not db_url:
                logger.warning(f"No connection URL provided for {db_name}, skipping...")
                continue
            
            # Create database directory
            db_dir = os.path.join(output_dir, db_name)
            os.makedirs(db_dir, exist_ok=True)
            
            logger.info(f"Generating documentation for {db_name} database...")
            db = DatabaseConnection(db_url)
            db.generate_schema_documentation(db_dir)
            
            logger.info(f"Documentation for {db_name} generated successfully")
        except Exception as e:
            logger.error(f"Failed to generate documentation for {db_name}: {str(e)}")
            logger.error(f"Continuing with next database...")
    
    logger.info(f"All documentation generated successfully in {output_dir}")

if __name__ == "__main__":
    main()