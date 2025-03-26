# src/plazza_analytics/tools/config.py

# Maps logical DB names to environment variable names
DB_CONNECTION_VARS = {
    "user_transactions": "DATABASE_URL_USER_TRANSACTIONS",
    "defaultdb": "DATABASE_URL",
    "plazza_erp": "DATABASE_URL_ERP",
    "user_events": "DATABASE_URL_USER"
}

# In-memory schema cache for reuse during a single run
DB_SCHEMA_CACHE = {}