# PlazzaCrew Project - Documentation

This document outlines the PlazzaCrew project's architecture, database connections, and key modifications made to the codebase.

## Project Overview

PlazzaCrew is a CrewAI-based project that uses AI agents to perform database queries across multiple PostgreSQL/CockroachDB databases. It provides a natural language interface for querying sales data, inventory transactions, and other business information.

### Key Components:

1. **CrewAI Agents**:
   - User Query Handler: Interprets natural language queries
   - PostgreSQL Query Agent: Converts queries to SQL and executes them

2. **Custom Tools**:
   - PostgreSQLTool: Executes SQL queries against the appropriate database

3. **Databases**:
   - `user_transactions`: Contains customer and order data (orders, contacts, etc.)
   - `plazza_erp`: Contains inventory and operational data (inventory_transactions)
   - `defaultdb`: Contains product catalog data (all_products)

## Database Connections

The system uses environment variables to connect to different CockroachDB databases:

```
DATABASE_URL_USER_TRANSACTIONS = "postgresql://user:password@host:port/user_transactions"
DATABASE_URL_ERP = "postgresql://user:password@host:port/plazza_erp"
DATABASE_URL = "postgresql://user:password@host:port/defaultdb"
```

Each database contains specific tables:
- **user_transactions**: orders, contacts, order_items
- **plazza_erp**: inventory_transactions
- **defaultdb**: all_products

## Key Architecture Decisions

### 1. Smart Database Selection

The PostgreSQLTool automatically detects which database to use based on the table mentioned in the SQL query:

```python
TABLE_TO_DB_MAP: ClassVar[Dict[str, str]] = {
    "orders": "DATABASE_URL_USER_TRANSACTIONS",
    "contacts": "DATABASE_URL_USER_TRANSACTIONS",
    "order_items": "DATABASE_URL_USER_TRANSACTIONS",
    "inventory_transactions": "DATABASE_URL_ERP",
    "all_products": "DATABASE_URL"
}
```

This removes the need for the agent to explicitly specify which database to use in queries.

### 2. Explicit Schema Documentation

The schema_summary.md file provides comprehensive documentation of the database structure with explicit table-to-database mapping:

```
## Database Mapping Guide

### Connection String to Database Mapping
- `DATABASE_URL_ERP` → connects to `plazza_erp` database
- `DATABASE_URL_USER_TRANSACTIONS` → connects to `user_transactions` database
- `DATABASE_URL` → connects to `defaultdb` database

### Table to Database Mapping
| Table Name | Database | Connection String |
|------------|----------|-------------------|
| inventory_transactions | plazza_erp | DATABASE_URL_ERP |
| all_products | defaultdb | DATABASE_URL |
| orders | user_transactions | DATABASE_URL_USER_TRANSACTIONS |
| order_items | user_transactions | DATABASE_URL_USER_TRANSACTIONS |
| contacts | user_transactions | DATABASE_URL_USER_TRANSACTIONS |
```

This documentation helps both the AI and human developers understand which tables exist in which databases.

### 3. Regex-Based Table Detection

The PostgreSQLTool uses regex to detect table names in SQL queries:

```python
table_pattern = r'(?:from|join|update|into)\s+([a-z0-9_]+)'
matches = re.findall(table_pattern, sql_lower)
```

This allows for more reliable detection of the tables being queried and the appropriate database to use.

## Recent Modifications

### 1. Enhanced PostgreSQLTool (custom_postgres_tool.py)

- Added a more robust database selection mechanism using regex
- Created a comprehensive TABLE_TO_DB_MAP with all tables
- Added ClassVar type annotations for Pydantic compatibility
- Improved error handling and result formatting
- Added better debugging output

### 2. Schema Documentation Updates (schema_summary.md)

- Added explicit Database Mapping Guide at the top
- Created a Table to Database Mapping section
- Updated section headers to include connection string information
- Enhanced table descriptions with more detail

### 3. Import Path Fixes (main.py, crew.py)

- Fixed Python module import paths using sys.path
- Added proper error handling for missing environment variables
- Enhanced database connection detection and reporting

## Known Issues and Workarounds

### 1. Raw Vendor Transactions Table

In the error logs, the system attempted to query a `raw_vendor_transactions` table that exists in the `plazza_erp` database but might not be documented in the schema. This occurred during schema discovery when the SQL agent was exploring tables via `information_schema.tables`.

### 2. Pydantic ClassVar Requirements

Due to Pydantic v2 requirements in CrewAI, all class variables in tool classes must use proper type annotations with ClassVar:

```python
from typing import ClassVar, Dict, Any

class PostgreSQLTool(BaseTool):
    TABLE_TO_DB_MAP: ClassVar[Dict[str, str]] = {...}
```

This prevents the "non-annotated attribute" error.

### 3. Import Path Management

To properly handle imports in the Python package, add the project root to sys.path:

```python
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))
```

## Usage Guide

### Interactive Mode

To run the system in interactive mode:

```bash
cd /Users/aniruddhasen/Projects/crewai/plazza_crew
PYTHONPATH=. python src/plazza_crew/main.py
```

This will start a simple chat interface where you can:
- Enter natural language queries at the prompt
- Type 'exit' to end the session

### Example Queries

The system accepts natural language queries like:

```
Find the total amount of sales in April 2025
List the top 5 orders by bill amount
How many contacts do we have in the database?
Show inventory transactions from vendor 'Vardhaman'
What products do we have in the all_products table?
```

### Environment Setup

Ensure your .env file has the following variables:

```
DATABASE_URL=postgresql://user:password@host:port/defaultdb
DATABASE_URL_ERP=postgresql://user:password@host:port/plazza_erp
DATABASE_URL_USER_TRANSACTIONS=postgresql://user:password@host:port/user_transactions
OPENAI_API_KEY=your-openai-api-key
```

## Troubleshooting

### Database Connection Issues

If you see errors like "Unknown database 'orders'", check:
1. Your environment variables are set correctly
2. The PostgreSQLTool is using the correct database mapping
3. The schema_summary.md file has the correct table-to-database mapping

### Import Errors

If you see "No module named 'plazza_crew'", use one of these solutions:

1. Set PYTHONPATH: `PYTHONPATH=. python src/plazza_crew/main.py` 
2. Add the project to sys.path programmatically (as implemented)

### CrewAI Compatibility

This project uses CrewAI with Pydantic v2 compatibility. Any class attributes in tool classes must have proper type annotations with ClassVar.