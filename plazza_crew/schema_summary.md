# Database Schema Summary

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

## Database: plazza_erp (Use DATABASE_URL_ERP)

### Table: inventory_transactions
- `transaction_id` TEXT - Primary identifier for transactions
- `vendor_name` TEXT - Name of the vendor
- `invoice_number` TEXT - Invoice reference number
- `invoice_date` TIMESTAMP - Date of the invoice
- `product_id` TEXT - Product identifier
- `batch_number` TEXT - Batch identifier
- `expiry_date` DATE - Expiration date of product
- `conversion_factor` DECIMAL - Conversion factor
- `quantity` DECIMAL - Quantity of product
- `free_quantity` DECIMAL - Free quantity included
- `mrp` DECIMAL - Maximum Retail Price
- `purchase_rate` DECIMAL - Purchase rate
- `ptr` DECIMAL - Price to Retailer
- `scheme_discount` DECIMAL - Scheme discount
- `cash_discount_percent` DECIMAL - Cash discount percentage
- `special_discount_percent` DECIMAL - Special discount percentage
- `hsn_code` TEXT - HSN code for tax
- `cess_amount` DECIMAL - Cess amount
- `freight_charges` DECIMAL - Freight charges
- `other_charges` DECIMAL - Other charges
- `purchase_order_number` TEXT - PO number
- `customer_order_number` TEXT - Customer order number
- `lr_number` TEXT - LR number
- `shipping_code` INTEGER - Shipping code
- `credit_days` TEXT - Credit days
- `rack_location` TEXT - Rack location
- `total_amount` DECIMAL - Total amount
- `created_at` TIMESTAMP - Record creation time
- `updated_at` TIMESTAMP - Record update time
- `gst_rate` DECIMAL - GST rate
- `plazza_selling_price_incl_gst` DECIMAL - Selling price with GST
- `product_name` TEXT - Name of the product
- `effective_customer_discount` DECIMAL - Effective customer discount
- `package` TEXT - Package information
- `distributor` TEXT - Distributor name
- `item_code` TEXT - Item code
- `transaction_type` TEXT - Type of transaction (PURCHASE, SALE, etc.)
- `reference_transaction_id` TEXT - Reference transaction ID
- `remaining_quantity` TEXT - Remaining quantity
- `consumption_status` TEXT - Consumption status
- `is_expired` BOOLEAN - Whether the product is expired
- `is_damaged` BOOLEAN - Whether the product is damaged
- `po_id` TEXT - Purchase order ID
- `expiry_status` TEXT - Expiry status

## Database: defaultdb (Use DATABASE_URL)

### Table: all_products
- `product_id` TEXT - Primary identifier for products
- `name` TEXT - Product name
- `manufacturers` TEXT - Manufacturer names
- `salt_composition` TEXT - Chemical composition
- `medicine_type` TEXT - Type of medicine
- `package` TEXT - Package information
- `product_form` TEXT - Form of the product (Tab, Capsule, etc.)
- `mrp` DECIMAL - Maximum Retail Price
- `plazza_selling_price_incl_gst` DECIMAL - Selling price with GST
- `normalized_name` TEXT - Normalized product name for searching
- `name_search_words` TEXT[] - Search words extracted from name

## Database: user_transactions (Use DATABASE_URL_USER_TRANSACTIONS)

### Table: orders
- `order_id` TEXT - Primary identifier for orders
- `contact_id` TEXT - Customer contact ID
- `status` TEXT - Order status (cart, pending, paid, cancelled)
- `bill_total_amount` DECIMAL - Total bill amount
- `created_at` TIMESTAMP - Order creation time
- `updated_at` TIMESTAMP - Order update time

### Table: order_items
- `order_id` TEXT - Reference to orders
- `product_id` TEXT - Product identifier
- `medicine_name` TEXT - Name of medicine
- `quantity` INTEGER - Quantity ordered
- `mrp` DECIMAL - Maximum Retail Price
- `selling_price` DECIMAL - Actual selling price
- `discount_percentage` DECIMAL - Discount percentage

### Table: contacts
- `id` TEXT - Primary identifier for contacts
- `first_name` TEXT - First name
- `last_name` TEXT - Last name
- `email` TEXT - Email address
- `gender` TEXT - Gender
- `date_of_birth` TEXT - Date of birth