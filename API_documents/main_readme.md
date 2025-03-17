# CockroachDB API Documentation - plazza-catalogue-3852

This documentation provides a comprehensive overview of the CockroachDB cluster used by the Plazza ecosystem.

## Cluster Information
- **Hostname:** plazza-catalogue-3852.jxf.gcp-us-central1.cockroachlabs.cloud
- **Port:** 26257
- **SSL Mode:** verify-full

## Databases
- [user_transactions](./user_transactions/README.md) - Customer and order management

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
   - Set appropriate min and max pool sizes based on your workload (recommended: min=2, max=10)
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

## Related Documentation

For more information on database-related services in the Plazza ecosystem, refer to these projects:

- **Plazza_POS** - Point-of-sale system with cart, payments integration
- **plazza_db_ops** - Database operations for product matching and inventory management
- **sync-to-ES** - Data synchronization between CockroachDB and Elasticsearch
- **medicine-search** - API for medicine search using Elasticsearch