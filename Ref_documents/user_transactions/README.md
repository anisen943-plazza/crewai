# CockroachDB Schema Documentation - user_transactions

## Database Information
- **Database Name:** user_transactions
- **User:** aniruddha
- **Tables:** 13

## Connection Information

### Connection String Format
```
postgresql://username:password@hostname:port/database?sslmode=verify-full
```

### Connection Parameters
- **Hostname:** plazza-catalogue-3852.jxf.gcp-us-central1.cockroachlabs.cloud
- **Port:** 26257
- **Database:** user_transactions
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
- [contact_addresses](#contact_addresses)
- [contact_phones](#contact_phones)
- [contacts](#contacts)
- [order_items](#order_items)
- [orders](#orders)
- [payments](#payments)
- [products](#products)
- [stores](#stores)
- [tookan_jobs](#tookan_jobs)
- [whatsapp_messages](#whatsapp_messages)
- [whatsapp_notifications](#whatsapp_notifications)
- [zoho_config](#zoho_config)
- [zoho_tokens](#zoho_tokens)

## contact_addresses

### Columns

| Column | Type | Length | Default | Nullable |
|--------|------|--------|---------|----------|
| id | uuid | - | gen_random_uuid() | NO |
| contact_id | uuid | - | - | YES |
| address_id | character varying | - | - | YES |
| house_number | character varying | - | - | YES |
| floor | character varying | - | - | YES |
| landmark | character varying | - | - | YES |
| building_name | character varying | - | - | YES |
| locality | character varying | - | - | YES |
| state | character varying | - | - | YES |
| pincode | character varying | - | - | YES |
| latitude | numeric | - | - | YES |
| longitude | numeric | - | - | YES |
| is_primary | boolean | - | false | YES |
| created_at | timestamp with time zone | - | current_timestamp() | YES |
| state_code | character varying(2) | 2 | - | YES |
| country | character varying | - | 'India' | YES |

### Primary Key

- id

### Foreign Keys

| Column | References |
|--------|------------|
| contact_id | public.contacts.id |

### Sample Data

| id | contact_id | address_id | house_number | floor | landmark | building_name | locality | state | pincode | latitude | longitude | is_primary | created_at | state_code | country |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 54d0aa51-da05-44a7-9d7e-935753cd4dcd | d150b315-89b3-47f7-9bca-c3b89e168d8e | None | 102 | 1st Floor | Near Kempegowda Metro Station | Elegant Enclave | Malleshwaram | Karnataka | 560003 | 12.99750000 | 77.57730000 | True | 2025-03-12 10:56:07.213400+00:00 | KA | India |

## contact_phones

### Columns

| Column | Type | Length | Default | Nullable |
|--------|------|--------|---------|----------|
| id | uuid | - | gen_random_uuid() | NO |
| contact_id | uuid | - | - | YES |
| phone_number | character varying | - | - | NO |
| is_primary | boolean | - | false | YES |
| created_at | timestamp with time zone | - | current_timestamp() | YES |

### Primary Key

- id

### Foreign Keys

| Column | References |
|--------|------------|
| contact_id | public.contacts.id |

### Sample Data

| id | contact_id | phone_number | is_primary | created_at |
|---|---|---|---|---|
| 192ba446-5936-479b-be0a-b8d0c67e6dff | d150b315-89b3-47f7-9bca-c3b89e168d8e | 8850959517 | True | 2025-03-01 13:52:27.689759+00:00 |
| 81c08956-1d41-40fe-94e8-8163147685a3 | fda8b2c6-dce1-4a06-a0ab-d81edcf95327 | 9999999999 | True | 2025-03-11 11:28:11.427076+00:00 |
| 9b9bd4bf-67c6-4da4-b648-8c665bad765c | 63be6990-4c7f-4754-a7cb-b1bcd092b385 | 9876543210 | True | 2025-02-28 01:05:00.931186+00:00 |
| fbd9a030-c774-4c63-b875-2a842306bb4f | c56e9b12-3e7e-45f7-92b8-e29433e8d82a | 8090390832 | True | 2025-03-11 11:27:35.581020+00:00 |

## contacts

### Columns

| Column | Type | Length | Default | Nullable |
|--------|------|--------|---------|----------|
| id | uuid | - | gen_random_uuid() | NO |
| contact_id | character varying | - | - | YES |
| first_name | character varying | - | - | NO |
| last_name | character varying | - | - | YES |
| email | character varying | - | - | YES |
| gender | character varying | - | - | YES |
| imei | character varying | - | - | YES |
| last_login | timestamp with time zone | - | - | YES |
| app_version | character varying | - | - | YES |
| os_version | character varying | - | - | YES |
| created_at | timestamp with time zone | - | current_timestamp() | YES |
| updated_at | timestamp with time zone | - | current_timestamp() | YES |
| customer_type | character varying(20) | 20 | 'WALK_IN' | YES |
| zoho_contact_id | character varying | - | - | YES |
| store_id | uuid | - | - | YES |
| gst_treatment | character varying | - | 'consumer' | YES |
| contact_type | character varying | - | 'customer' | YES |
| customer_sub_type | character varying | - | 'individual' | YES |

### Primary Key

- id

### Sample Data

| id | contact_id | first_name | last_name | email | gender | imei | last_login | app_version | os_version | created_at | updated_at | customer_type | zoho_contact_id | store_id | gst_treatment | contact_type | customer_sub_type |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 63be6990-4c7f-4754-a7cb-b1bcd092b385 | 63be6990-4c7f-4754-a7cb-b1bcd092b385 | Test Customer | None | None | NOT_SPECIFIED | None | None | None | None | 2025-02-28 01:05:00.931186+00:00 | 2025-02-28 01:05:00.931186+00:00 | WALK_IN | 2325214000000108002 | None | consumer | customer | individual |
| c56e9b12-3e7e-45f7-92b8-e29433e8d82a | c56e9b12-3e7e-45f7-92b8-e29433e8d82a | Abhi Tiwari | None | None | Male | None | None | None | None | 2025-03-11 11:27:35.581020+00:00 | 2025-03-11 11:27:35.581020+00:00 | WALK_IN | None | None | consumer | customer | individual |
| d150b315-89b3-47f7-9bca-c3b89e168d8e | d150b315-89b3-47f7-9bca-c3b89e168d8e | Test Customer | None | None | NOT_SPECIFIED | None | None | None | None | 2025-03-01 13:52:27.689759+00:00 | 2025-03-01 13:52:27.689759+00:00 | WALK_IN | 2325214000000118089 | None | consumer | customer | individual |
| fda8b2c6-dce1-4a06-a0ab-d81edcf95327 | fda8b2c6-dce1-4a06-a0ab-d81edcf95327 | Test User | None | None | Male | None | None | None | None | 2025-03-11 11:28:11.427076+00:00 | 2025-03-11 11:28:11.427076+00:00 | WALK_IN | 2325214000000159002 | None | consumer | customer | individual |

## order_items

### Columns

| Column | Type | Length | Default | Nullable |
|--------|------|--------|---------|----------|
| id | uuid | - | gen_random_uuid() | NO |
| order_id | character varying | - | - | NO |
| product_id | character varying | - | - | NO |
| medicine_name | character varying | - | - | NO |
| distributor_name | character varying | - | - | YES |
| mrp | numeric | - | - | NO |
| selling_price | numeric | - | - | NO |
| quantity | bigint | - | - | NO |
| item_total | numeric | - | - | NO |
| created_at | timestamp with time zone | - | current_timestamp() | YES |
| updated_at | timestamp with time zone | - | current_timestamp() | YES |
| item_discount | numeric | - | 0.00 | YES |
| tax_name | character varying | - | - | YES |
| tax_id | character varying | - | - | YES |
| pre_tax_rate | numeric | - | - | YES |

### Primary Key

- id

### Foreign Keys

| Column | References |
|--------|------------|
| order_id | public.orders.order_id |

### Sample Data

| id | order_id | product_id | medicine_name | distributor_name | mrp | selling_price | quantity | item_total | created_at | updated_at | item_discount | tax_name | tax_id | pre_tax_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 18687892-2312-4a6d-8393-cd6003db8151 | CART-16445809 | 165005 | SOMPRAZ L CAP | Mahavir | 320.00 | 267.52 | 1 | 267.52 | 2025-02-28 12:58:35.628899+00:00 | 2025-02-28 12:58:35.628899+00:00 | 0.00 | None | None | None |
| 2644b31f-3a78-440b-a89e-afbff6899515 | CART-60abaf4f | 158091 | DOLO 650 MG TAB | Mahavir | 33.76 | 28.22 | 1 | 28.22 | 2025-03-05 04:19:11.195562+00:00 | 2025-03-05 04:19:11.195562+00:00 | 0.00 | None | None | None |
| 27eebd4a-f6cb-43a1-bd33-71eeefa1cab6 | CART-42a76b87 | 199853 | MYMI D TAB | vardhaman | 170.00 | 143.62 | 2 | 287.24 | 2025-03-11 11:27:34.181327+00:00 | 2025-03-11 11:27:34.181327+00:00 | 0.00 | None | None | None |
| 31f6df42-7511-4c77-a308-bd4adbbafe96 | TEST_POD_123456 | PROD123 | Paracetamol | ABC Pharma | 1.50 | 1.00 | 1 | 1.00 | 2025-03-13 11:27:57.036780+00:00 | 2025-03-13 11:27:57.036780+00:00 | 0.00 | None | None | None |
| 352aa2eb-eb83-4718-b9dd-37766856ccc7 | CART-fd7d59c7 | 165005 | SOMPRAZ L CAP | Mahavir | 320.00 | 267.52 | 1 | 267.52 | 2025-02-28 04:47:53.958368+00:00 | 2025-02-28 04:47:53.958368+00:00 | 0.00 | None | None | None |

## orders

### Columns

| Column | Type | Length | Default | Nullable |
|--------|------|--------|---------|----------|
| id | uuid | - | gen_random_uuid() | NO |
| order_id | character varying | - | - | YES |
| contact_id | uuid | - | - | YES |
| status | character varying | - | - | NO |
| bill_total_amount | numeric | - | - | YES |
| item_total | numeric | - | - | YES |
| delivery_charges | numeric | - | - | YES |
| platform_fee | numeric | - | - | YES |
| packaging_charges | numeric | - | - | YES |
| convenience_fee | numeric | - | - | YES |
| created_at | timestamp with time zone | - | current_timestamp() | YES |
| updated_at | timestamp with time zone | - | current_timestamp() | YES |
| cart_discount | numeric | - | 0.00 | YES |
| cart_notes | jsonb | - | - | YES |
| zoho_invoice_id | character varying | - | - | YES |
| zoho_invoice_number | character varying | - | - | YES |
| zoho_invoice_status | character varying | - | - | YES |
| place_of_supply | character varying(2) | 2 | - | YES |
| store_id | uuid | - | - | YES |
| delivery_type | character varying(20) | 20 | - | YES |
| tookan_job_id | character varying(64) | 64 | - | YES |
| whatsapp_notification_status | character varying(20) | 20 | - | YES |

### Primary Key

- id

### Foreign Keys

| Column | References |
|--------|------------|
| contact_id | public.contacts.id |

### Sample Data

| id | order_id | contact_id | status | bill_total_amount | item_total | delivery_charges | platform_fee | packaging_charges | convenience_fee | created_at | updated_at | cart_discount | cart_notes | zoho_invoice_id | zoho_invoice_number | zoho_invoice_status | place_of_supply | store_id | delivery_type | tookan_job_id | whatsapp_notification_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0491494f-7c2e-433f-aeba-7eeeab7a9279 | CART-de52864f | d150b315-89b3-47f7-9bca-c3b89e168d8e | paid | 267.52 | 267.52 | None | None | None | None | 2025-03-03 09:04:46.071054+00:00 | 2025-03-03 09:05:37.731349+00:00 | 0.00 | None | 2325214000000118106 | INV-000014 | draft | KA | None | None | None | None |
| 0499b73c-3148-4361-a8ba-f414b0cfecde | CART-11688daa | d150b315-89b3-47f7-9bca-c3b89e168d8e | paid | 267.52 | 267.52 | None | None | None | None | 2025-03-03 00:31:38.966459+00:00 | 2025-03-03 00:32:34.955198+00:00 | 0.00 | None | 2325214000000133002 | INV-000013 | draft | KA | None | None | None | None |
| 06737103-7483-4c5f-9164-17e45cdf0b44 | CART-7e5964ac | d150b315-89b3-47f7-9bca-c3b89e168d8e | paid | 267.52 | 267.52 | None | None | None | None | 2025-03-03 11:26:07.637341+00:00 | 2025-03-03 11:27:27.677677+00:00 | 0.00 | None | 2325214000000110036 | INV-000016 | draft | KA | None | None | None | None |
| 076478fd-e5f0-4d5e-8c7b-afcf02bb2f47 | CART-c5fc9c96 | d150b315-89b3-47f7-9bca-c3b89e168d8e | paid | 267.52 | 267.52 | None | None | None | None | 2025-03-04 09:17:15.603562+00:00 | 2025-03-04 09:18:18.850282+00:00 | 0.00 | None | 2325214000000124226 | INV-000019 | draft | KA | None | None | None | None |
| 0b2af2ae-1cf5-4472-bf8d-013b61eff980 | CART-ac51d678 | d150b315-89b3-47f7-9bca-c3b89e168d8e | paid | 267.52 | 267.52 | None | None | None | None | 2025-03-03 09:22:50.890212+00:00 | 2025-03-03 09:23:35.661697+00:00 | 0.00 | None | 2325214000000132015 | INV-000015 | draft | KA | None | None | None | None |

## payments

### Columns

| Column | Type | Length | Default | Nullable |
|--------|------|--------|---------|----------|
| id | uuid | - | gen_random_uuid() | NO |
| payment_id | character varying | - | - | YES |
| customer_id | uuid | - | - | YES |
| order_amount | numeric | - | - | NO |
| payment_status | character varying | - | - | NO |
| payment_method | character varying | - | - | YES |
| transaction_id | character varying | - | - | YES |
| payment_date | timestamp with time zone | - | - | YES |
| razorpay_payment_link | character varying | - | - | YES |
| upi_id | character varying | - | - | YES |
| bank_name | character varying | - | - | YES |
| card_token_id | character varying | - | - | YES |
| payment_gateway | character varying | - | - | YES |
| discount_amount | numeric | - | - | YES |
| discount_code | character varying | - | - | YES |
| payment_fees | numeric | - | - | YES |
| created_at | timestamp with time zone | - | current_timestamp() | YES |
| updated_at | timestamp with time zone | - | current_timestamp() | YES |
| qr_code_id | character varying | - | - | YES |
| qr_code_url | character varying | - | - | YES |
| qr_usage | character varying | - | - | YES |
| qr_status | character varying | - | - | YES |
| qr_fixed_amount | boolean | - | - | YES |
| qr_payment_amount | numeric | - | - | YES |
| qr_close_by | timestamp with time zone | - | - | YES |
| qr_closed_at | timestamp with time zone | - | - | YES |
| qr_close_reason | character varying | - | - | YES |
| qr_notes | jsonb | - | - | YES |
| order_id | character varying | - | - | YES |
| payment_instrument | character varying(20) | 20 | 'POS_UPI_QR' | YES |
| zoho_payment_id | character varying | - | - | YES |
| zoho_account_id | character varying | - | - | YES |
| zoho_account_name | character varying | - | - | YES |
| zoho_account_type | character varying | - | 'Payment Clearing' | YES |
| store_id | uuid | - | - | YES |

### Primary Key

- id

### Foreign Keys

| Column | References |
|--------|------------|
| customer_id | public.contacts.id |
| order_id | public.orders.order_id |

### Sample Data

| id | payment_id | customer_id | order_amount | payment_status | payment_method | transaction_id | payment_date | razorpay_payment_link | upi_id | bank_name | card_token_id | payment_gateway | discount_amount | discount_code | payment_fees | created_at | updated_at | qr_code_id | qr_code_url | qr_usage | qr_status | qr_fixed_amount | qr_payment_amount | qr_close_by | qr_closed_at | qr_close_reason | qr_notes | order_id | payment_instrument | zoho_payment_id | zoho_account_id | zoho_account_name | zoho_account_type | store_id |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 006fe177-042d-46d8-a07e-eb9b767e6dbe | pay_Q18g0Ni5lznN1t | None | 267.52 | captured | upi | None | 2025-02-28 12:59:39.141018+00:00 | None | 8850959517-2@ibl | None | None | None | None | None | 6.47 | 2025-02-28 12:58:44.558583+00:00 | 2025-02-28 12:59:39.141018+00:00 | qr_Q18fXnlejUCzr1 | https://rzp.io/rzp/cIbzeob | single_use | closed | True | 267.52 | 2025-03-01 18:28:42+00:00 | 2025-02-28 12:59:39.141018+00:00 | None | {'order_id': 'CART-16445809'} | CART-16445809 | POS_UPI_QR | 2325214000000127021 | 2325214000000111001 | Customer Order Payments | Payment Clearing | None |
| 0133c004-3559-4716-8341-5537bc0a8a16 | None | None | 267.52 | pending | None | None | None | None | None | None | None | None | None | None | None | 2025-02-28 01:22:10.687021+00:00 | 2025-02-28 01:22:10.687021+00:00 | qr_Q0wnk4jjZ54NUQ | https://rzp.io/rzp/LjsQaE1 | single_use | active | True | 267.52 | 2025-03-01 06:52:08+00:00 | None | None | {'order_id': 'CART-99ef475e'} | CART-99ef475e | POS_UPI_QR | None | None | None | Payment Clearing | None |
| 068f184e-3905-4dc9-b6fe-ee0110861191 | None | None | 267.52 | unknown | None | None | 2025-02-28 01:19:50.359712+00:00 | None | None | None | None | None | None | None | 0.00 | 2025-02-28 01:19:47.420875+00:00 | 2025-02-28 01:19:50.359712+00:00 | qr_Q0wlDrdtuO5l2K | https://rzp.io/rzp/THsrUJgi | single_use | closed | True | 267.52 | 2025-03-01 06:49:45+00:00 | 2025-02-28 01:19:50.359712+00:00 | None | {'order_id': 'CART-fcc59d6b'} | CART-fcc59d6b | POS_UPI_QR | None | None | None | Payment Clearing | None |
| 1cf1d027-755d-4ec5-99c8-4d62f63ac57b | pay_Q2Ii8uSreqJWGX | None | 267.52 | captured | upi | None | 2025-03-03 11:27:27.677677+00:00 | None | 8850959517-2@ybl | None | None | None | None | None | 6.47 | 2025-03-03 11:26:34.577034+00:00 | 2025-03-03 11:27:27.677677+00:00 | qr_Q2IhTig4ywC3Oi | https://rzp.io/rzp/fTkH7eV | single_use | closed | True | 267.52 | 2025-03-04 16:56:23+00:00 | 2025-03-03 11:27:27.677677+00:00 | None | {'order_id': 'CART-7e5964ac'} | CART-7e5964ac | POS_UPI_QR | 2325214000000125096 | 2325214000000111001 | Customer Order Payments | Payment Clearing | None |
| 1e69be57-24e1-44cf-98e4-d9e4912fd3dc | None | None | 143.62 | pending | None | None | None | None | None | None | None | None | None | None | None | 2025-03-11 11:28:40.605145+00:00 | 2025-03-11 11:28:40.605145+00:00 | qr_Q5T0iPPGveLIwc | https://rzp.io/rzp/GTkrTBA | single_use | active | True | 143.62 | 2025-03-12 16:58:37+00:00 | None | None | {'order_id': 'CART-af8d7653'} | CART-af8d7653 | POS_UPI_QR | None | None | None | Payment Clearing | None |

## products

### Columns

| Column | Type | Length | Default | Nullable |
|--------|------|--------|---------|----------|
| id | uuid | - | gen_random_uuid() | NO |
| product_id | character varying | - | - | YES |
| medicine_name | character varying | - | - | NO |
| medicine_type | character varying | - | - | YES |
| mrp | numeric | - | - | NO |
| distributor_name | character varying | - | - | YES |
| plazza_selling_price_incl_gst | numeric | - | - | NO |
| effective_customer_discount | numeric | - | - | YES |
| quantity_ordered | bigint | - | - | YES |
| item_total | numeric | - | - | YES |
| quantity_available | bigint | - | - | YES |
| created_at | timestamp with time zone | - | current_timestamp() | YES |
| updated_at | timestamp with time zone | - | current_timestamp() | YES |
| order_id | character varying | - | - | YES |

### Primary Key

- id

### Foreign Keys

| Column | References |
|--------|------------|
| order_id | public.orders.order_id |

## stores

### Columns

| Column | Type | Length | Default | Nullable |
|--------|------|--------|---------|----------|
| id | uuid | - | gen_random_uuid() | NO |
| name | character varying | - | - | NO |
| address | character varying | - | - | YES |
| city | character varying | - | - | YES |
| state | character varying | - | - | YES |
| state_code | character varying(2) | 2 | - | YES |
| pincode | character varying | - | - | YES |
| phone | character varying | - | - | YES |
| email | character varying | - | - | YES |
| gst_number | character varying | - | - | YES |
| created_at | timestamp with time zone | - | current_timestamp() | YES |
| updated_at | timestamp with time zone | - | current_timestamp() | YES |

### Primary Key

- id

## tookan_jobs

### Columns

| Column | Type | Length | Default | Nullable |
|--------|------|--------|---------|----------|
| id | uuid | - | gen_random_uuid() | NO |
| order_id | character varying | - | - | NO |
| job_id | character varying(64) | 64 | - | NO |
| agent_id | character varying(64) | 64 | - | YES |
| agent_name | character varying(128) | 128 | - | YES |
| job_status | character varying(20) | 20 | 'pending' | YES |
| tracking_url | text | - | - | YES |
| created_at | timestamp with time zone | - | current_timestamp() | YES |
| updated_at | timestamp with time zone | - | current_timestamp() | YES |

### Primary Key

- id

### Foreign Keys

| Column | References |
|--------|------------|
| order_id | public.orders.order_id |

### Sample Data

| id | order_id | job_id | agent_id | agent_name | job_status | tracking_url | created_at | updated_at |
|---|---|---|---|---|---|---|---|---|
| 71ea9d2f-6a86-4d4f-864e-a5058b92da15 | TEST_POD_123456 | 555137576 | None | None | pending | https://jungl.ml/e94VdGaad | 2025-03-13 11:27:57.036780+00:00 | 2025-03-13 11:27:57.036780+00:00 |

## whatsapp_messages

### Columns

| Column | Type | Length | Default | Nullable |
|--------|------|--------|---------|----------|
| id | uuid | - | gen_random_uuid() | NO |
| message_id | character varying | - | - | NO |
| order_id | character varying | - | - | YES |
| invoice_id | character varying | - | - | YES |
| invoice_number | character varying | - | - | YES |
| destination | character varying | - | - | YES |
| status | character varying | - | - | NO |
| raw_payload | jsonb | - | - | YES |
| created_at | timestamp with time zone | - | current_timestamp() | YES |
| updated_at | timestamp with time zone | - | current_timestamp() | YES |

### Primary Key

- id

## whatsapp_notifications

### Columns

| Column | Type | Length | Default | Nullable |
|--------|------|--------|---------|----------|
| id | uuid | - | gen_random_uuid() | NO |
| message_id | character varying(64) | 64 | - | YES |
| order_id | character varying | - | - | NO |
| phone_number | character varying(16) | 16 | - | NO |
| template_id | character varying(64) | 64 | - | NO |
| status | character varying(20) | 20 | 'pending' | YES |
| created_at | timestamp with time zone | - | current_timestamp() | YES |
| updated_at | timestamp with time zone | - | current_timestamp() | YES |

### Primary Key

- id

### Foreign Keys

| Column | References |
|--------|------------|
| order_id | public.orders.order_id |

## zoho_config

### Columns

| Column | Type | Length | Default | Nullable |
|--------|------|--------|---------|----------|
| id | uuid | - | gen_random_uuid() | NO |
| store_id | uuid | - | - | YES |
| organization_id | character varying | - | - | NO |
| tax_settings | jsonb | - | - | YES |
| account_settings | jsonb | - | - | YES |
| created_at | timestamp with time zone | - | current_timestamp() | YES |
| updated_at | timestamp with time zone | - | current_timestamp() | YES |

### Primary Key

- id

### Sample Data

| id | store_id | organization_id | tax_settings | account_settings | created_at | updated_at |
|---|---|---|---|---|---|---|
| bf8d1305-8205-4653-bc7c-f2bd254f0f99 | None | 60037206983 | {'0': {'percentage': 0, 'tax_id': '232521400000... | None | 2025-02-28 03:59:28.460432+00:00 | 2025-02-28 03:59:28.460432+00:00 |

## zoho_tokens

### Columns

| Column | Type | Length | Default | Nullable |
|--------|------|--------|---------|----------|
| id | uuid | - | gen_random_uuid() | NO |
| token | character varying | - | - | NO |
| expires_at | timestamp with time zone | - | - | NO |
| is_valid | boolean | - | true | YES |
| created_at | timestamp with time zone | - | current_timestamp() | YES |

### Primary Key

- id

