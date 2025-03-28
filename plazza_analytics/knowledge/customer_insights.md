# Customer Analysis Methodology

## Repeat Customer Analysis

This document outlines the complete methodology for analyzing repeat customers in the Plazza database ecosystem, with a focus on identifying top customers, their purchasing patterns, and behavioral insights.

### Database Connection and Environment Setup

First, establish a connection to the CockroachDB database:

```python
import os
import json
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to database
db_url = os.getenv('DATABASE_URL_USER_TRANSACTIONS')
if not db_url:
    print('DATABASE_URL_USER_TRANSACTIONS not set')
    exit(1)

conn = psycopg2.connect(db_url)
cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
```

### 1. Identify Repeat Customers

To find repeat customers (those with more than one order):

```sql
WITH order_counts AS (
    SELECT contact_uuid, COUNT(*) as order_count
    FROM airtable_orders
    WHERE is_processed = TRUE AND contact_uuid IS NOT NULL
    GROUP BY contact_uuid
    HAVING COUNT(*) > 1
)
SELECT COUNT(*) as repeat_customers_count, 
       MAX(order_count) as max_orders,
       SUM(order_count) as total_repeat_orders
FROM order_counts
```

### 2. Find Top Repeat Customers

To identify the customers with the most orders:

```sql
WITH customer_orders AS (
    SELECT 
        ao.contact_uuid, 
        COUNT(*) as order_count,
        ac.first_name,
        ac.last_name,
        ac.phone
    FROM airtable_orders ao
    JOIN airtable_contacts ac ON ao.contact_uuid = ac.contact_uuid
    WHERE ao.is_processed = TRUE AND ao.contact_uuid IS NOT NULL
    GROUP BY ao.contact_uuid, ac.first_name, ac.last_name, ac.phone
    ORDER BY order_count DESC
    LIMIT 5
)
SELECT * FROM customer_orders
```

### 3. Analyze Customer Order Distribution

To understand how repeat orders are distributed among customers:

```sql
WITH order_counts AS (
    SELECT contact_uuid, COUNT(*) as order_count
    FROM airtable_orders
    WHERE is_processed = TRUE AND contact_uuid IS NOT NULL
    GROUP BY contact_uuid
)
SELECT 
    order_count, 
    COUNT(*) as customer_count
FROM order_counts
WHERE order_count > 1
GROUP BY order_count
ORDER BY order_count DESC
```

### 4. Get Detailed Customer Profiles with Financial Metrics

To analyze top customers with their spending patterns:

```sql
WITH customer_orders AS (
    SELECT 
        ao.contact_uuid, 
        COUNT(*) as order_count,
        ac.first_name,
        ac.last_name,
        ac.phone,
        MAX(ao.created_at) as last_order_date,
        SUM(ao.bill_total_amount) as total_spent
    FROM airtable_orders ao
    JOIN airtable_contacts ac ON ao.contact_uuid = ac.contact_uuid
    WHERE ao.is_processed = TRUE AND ao.contact_uuid IS NOT NULL
    GROUP BY ao.contact_uuid, ac.first_name, ac.last_name, ac.phone
    HAVING COUNT(*) > 1
    ORDER BY order_count DESC, total_spent DESC
    LIMIT 20
)
SELECT * FROM customer_orders
```

### 5. Calculate Repeat Customer Metrics

To gather overall statistics about repeat customers:

```sql
WITH order_stats AS (
    SELECT 
        ao.contact_uuid,
        COUNT(*) as order_count,
        SUM(ao.bill_total_amount) as total_spent
    FROM airtable_orders ao
    WHERE ao.is_processed = TRUE AND ao.contact_uuid IS NOT NULL
    GROUP BY ao.contact_uuid
    HAVING COUNT(*) > 1
)
SELECT 
    COUNT(*) as total_repeat_customers,
    AVG(order_count) as avg_orders_per_customer,
    MAX(order_count) as max_orders,
    AVG(total_spent) as avg_spent_per_customer,
    MAX(total_spent) as max_spent,
    SUM(total_spent) as total_revenue_from_repeat
FROM order_stats
```

### 6. Calculate Order Percentage from Repeat Customers

To determine what percentage of total orders come from repeat customers:

```sql
SELECT
    (SELECT COUNT(*) FROM airtable_orders WHERE is_processed = TRUE) as total_orders,
    (SELECT COUNT(*) FROM airtable_orders WHERE is_processed = TRUE AND contact_uuid IN (
        SELECT contact_uuid 
        FROM airtable_orders 
        WHERE is_processed = TRUE 
        GROUP BY contact_uuid 
        HAVING COUNT(*) > 1
    )) as repeat_customer_orders
```

Then calculate the percentage:
```python
repeat_percentage = (order_counts['repeat_customer_orders'] / order_counts['total_orders'] * 100)
```

### 7. Analyze Individual Customer Purchase Patterns

To analyze what specific products a customer orders and identify repeat purchases:

```sql
SELECT 
    ao.order_id,
    ao.created_at,
    ao.status,
    ao.bill_total_amount,
    ao.raw_data
FROM airtable_orders ao
WHERE 
    ao.contact_uuid = %s
    AND ao.is_processed = TRUE
ORDER BY ao.created_at
```

Then parse the raw_data to extract product information:

```python
all_products = {}

for order in orders:
    # Extract products from raw_data
    try:
        if order['raw_data']:
            raw_data = json.loads(order['raw_data']) if isinstance(order['raw_data'], str) else order['raw_data']
            
            # Extract product names and quantities from Airtable structure
            medicine_names = raw_data.get('Medicine Name (from Medicines Table)', [])
            medicine_quantities = raw_data.get('Medicine Quantity', [])
            medicine_prices = raw_data.get('Medicine Price', [])
            
            # Process each product in the order
            if medicine_names and isinstance(medicine_names, list):
                for j in range(len(medicine_names)):
                    product_name = medicine_names[j]
                    # Normalize the product name for consistent comparison
                    normalized_name = product_name.lower().strip()
                    quantity = medicine_quantities[j] if j < len(medicine_quantities) else 1
                    
                    # Track product purchases
                    if normalized_name in all_products:
                        all_products[normalized_name]['count'] += 1
                        all_products[normalized_name]['quantities'].append(quantity)
                        all_products[normalized_name]['original_names'].add(product_name)
                    else:
                        all_products[normalized_name] = {
                            'count': 1,
                            'quantities': [quantity],
                            'original_names': {product_name}
                        }
    except Exception as e:
        print(f'Error parsing raw_data: {str(e)}')
```

### 8. Identify Repeat Purchase Patterns

Calculate what percentage of products are ordered multiple times:

```python
repeat_products = {p: data for p, data in all_products.items() if data['count'] > 1}
repeat_percentage = (len(repeat_products) / len(all_products)) * 100

if repeat_percentage > 50:
    purchase_behavior = "This customer tends to order the same products repeatedly"
else:
    purchase_behavior = "This customer tends to order a variety of different products"
```

### 9. Handle Name Variations in Product Analysis

The analysis should normalize product names to handle case variations and slight naming differences:

```python
normalized_name = product_name.lower().strip()
```

This captures cases like "Augmentin dds 457/5ml" and "augmentin dds 457/5ml" as the same product.

### 10. Key Metrics to Report

The complete analysis should include:

1. Total number of repeat customers
2. Percentage of total orders from repeat customers
3. Average orders per repeat customer
4. Top customers by order count (name, phone, order count)
5. Spending patterns of top customers
6. Product repurchase behavior (% of products ordered multiple times)
7. Distribution of repeat customers by order count

## Example Query Results

As of March 2025, the analysis revealed:
- 116 repeat customers (with 2+ orders)
- These repeat customers account for 72.7% of all processed orders
- Repeat customers place an average of 3.2 orders each
- Top customer: Riddhi Kedia (Phone: 9830530506) with 11 orders
- Riddhi Kedia tends to order a variety of different products (only 11.1% of products were repeat purchases)
- Highest spending repeat customer: Tribhuvan Suthar (7014444277) with ₹9,415.65 total

## Note on Database-Specific Implementation

This methodology relies on the specific structure of the airtable_orders and airtable_contacts tables in the Plazza database. These tables store raw Airtable data with a specific schema:
- contact_uuid is a deterministic UUID based on the customer's phone number
- raw_data contains the complete JSON record from Airtable
- Product information is stored within arrays in the raw_data field

If the database schema changes, the queries and extraction logic would need to be updated accordingly.

---

## Generated on 2025-03-27 13:51:26

## Retention Analysis Report

### Data Volume Report:
- Regular orders table: 28 paid orders
- Airtable orders table: 0 paid orders
- Total orders across all sources: 28
- Regular orders represent: 100.0% of total
- Airtable orders represent: 0.0% of total

### Sales Summary:
- Regular orders total: ₹6,564.10
- Airtable orders total: ₹0.00
- Combined total sales: ₹6,564.10

### Retention Summary:
- Total customers: 2
- Repeat customers: 2
- One-time customers: 0
- Repeat rate: 100.0%

### Time Between Purchases:
- Average days between 1st and 2nd order: 0.5 days

### Discount Impact:
- Could not analyze discount impact: relation 'airtable_order_items' does not exist

### Recent Cohort Performance:
- Could not analyze cohort performance due to issues with the database.

---

## Generated on 2025-03-27 13:58:02

## Repeat Customers Analysis

- Total customers: 2
- Repeat customers: 2
- One-time customers: 0
- Repeat rate: 100.0%
- Average days between 1st and 2nd order: 0.5 days
- Regular orders total: ₹6,564.10

*Analysis generated on 2025-03-27 13:57:52 using RetentionAnalysisTool with schema discovery.*

---

## Generated on 2025-03-28 06:28:10

## Data Volume Report
- Regular orders table: 28 paid orders
- Airtable orders table: 0 paid orders
- Total orders across all sources: 28
- Regular orders represent: 100.0% of total
- Airtable orders represent: 0.0% of total

## Sales Summary
- Regular orders total: ₹6,564.10
- Airtable orders total: ₹0.00
- Combined total sales: ₹6,564.10

## Retention Summary
- Total customers: 2
- Repeat customers: 2
- One-time customers: 0
- Repeat rate: 100.0%

## Time Between Purchases
- Average days between 1st and 2nd order: 0.5 days

## Discount Impact
⚠️ Could not analyze discount impact: relation 'airtable_order_items' does not exist

## Recent Cohort Performance
⚠️ Could not analyze cohort performance: current transaction is aborted, commands ignored until end of transaction block

*Analysis generated on 2025-03-28 06:27:58 using RetentionAnalysisTool with schema discovery.*