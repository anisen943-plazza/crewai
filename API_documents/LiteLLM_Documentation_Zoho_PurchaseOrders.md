# Zoho Books Purchase Orders API Documentation

This comprehensive documentation covers the Zoho Books Purchase Orders API, providing detailed information about creating, reading, updating, and managing purchase orders through the API.

**Base URL**: `https://www.zohoapis.com/books/v3`

**Authentication**: OAuth 2.0 with appropriate scopes

## Table of Contents

1. [Overview](#overview)
2. [Authentication](#authentication)
3. [Purchase Order Endpoints](#purchase-order-endpoints)
   - [Create a Purchase Order](#create-a-purchase-order)
   - [List Purchase Orders](#list-purchase-orders)
   - [Get a Purchase Order](#get-a-purchase-order)
   - [Update a Purchase Order](#update-a-purchase-order)
   - [Delete a Purchase Order](#delete-a-purchase-order)
4. [Purchase Order Status Management](#purchase-order-status-management)
   - [Mark as Open](#mark-a-purchase-order-as-open)
   - [Mark as Billed](#mark-a-purchase-order-as-billed)
   - [Mark as Cancelled](#cancel-a-purchase-order)
5. [Inventory and Item Management](#inventory-and-item-management)
   - [List Items with Inventory](#list-items-with-inventory)
   - [Item Stock Fields](#item-stock-fields)
6. [Common Use Cases](#common-use-cases)
   - [Automated Reordering](#automated-reordering)
   - [Purchase Order Tracking](#purchase-order-tracking)

## Overview

Purchase orders in Zoho Books allow you to place and manage orders to your vendors/suppliers. The API provides comprehensive functionality to programmatically create and manage these purchase orders.

Key features of the Purchase Order API:
- Create, read, update, and delete purchase orders
- Manage purchase order status (draft, open, billed, cancelled)
- Associate purchase orders with vendors and items
- Track delivery dates, payment terms, and more
- Support for multiple currencies and tax treatments

## Authentication

All API requests require authentication using OAuth 2.0. You'll need:

1. A valid OAuth access token
2. Your organization ID

The required OAuth scope for purchase orders depends on the operation:
- Create: `ZohoBooks.purchaseorders.CREATE`
- Read: `ZohoBooks.purchaseorders.READ`
- Update: `ZohoBooks.purchaseorders.UPDATE`
- Delete: `ZohoBooks.purchaseorders.DELETE`

Example authorization header:
```
Authorization: Zoho-oauthtoken 1000.xx.xx
```

## Purchase Order Endpoints

### Create a Purchase Order

Creates a new purchase order in Zoho Books.

**Endpoint**: `POST /purchaseorders`

**OAuth Scope**: `ZohoBooks.purchaseorders.CREATE`

#### Request Parameters

##### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| vendor_id | string | ID of the vendor for the purchase order |
| line_items | array | Array of line items in the purchase order |

##### Optional Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| purchaseorder_number | string | Unique number for the purchase order |
| reference_number | string | Reference number for the purchase order |
| date | string | Date of the purchase order (format: yyyy-mm-dd) |
| delivery_date | string | Expected delivery date (format: yyyy-mm-dd) |
| currency_id | string | ID of the currency |
| exchange_rate | decimal | Exchange rate for the currency |
| discount | decimal | Discount applied to the purchase order |
| is_inclusive_tax | boolean | Whether tax is inclusive in the item rate |
| notes | string | Additional notes for the purchase order |
| terms | string | Terms and conditions |
| billing_address | object | Billing address details |
| shipping_address | object | Shipping address details |
| contact_persons | array | List of contact person IDs |
| custom_fields | array | List of custom fields |
| attachments | array | List of attachments |

#### Line Item Parameters

Each line item in the `line_items` array should contain:

| Parameter | Type | Description |
|-----------|------|-------------|
| item_id | string | ID of the item being ordered |
| quantity | decimal | Quantity of the item |
| rate | decimal | Rate/price per unit |
| description | string | Description of the line item (optional) |
| unit | string | Unit of measurement (optional) |
| tax_id | string | ID of the tax applied (optional) |
| tax_name | string | Name of the tax (optional) |
| tax_percentage | decimal | Percentage of tax (optional) |

#### Example Request

```json
{
  "vendor_id": "460000000026049",
  "purchaseorder_number": "PO-00001",
  "date": "2023-04-12",
  "delivery_date": "2023-04-20",
  "reference_number": "REF-001",
  "is_inclusive_tax": false,
  "notes": "Please deliver items as soon as possible",
  "terms": "Net 30",
  "line_items": [
    {
      "item_id": "460000000027009",
      "quantity": 10,
      "rate": 112.50,
      "description": "Generic Antibiotics - 500mg"
    },
    {
      "item_id": "460000000027010",
      "quantity": 20,
      "rate": 75.00,
      "description": "Pain Relievers - 200mg"
    }
  ],
  "billing_address": {
    "address": "4590 Roosevelt Way NE",
    "city": "Seattle",
    "state": "Washington",
    "zip": "98105",
    "country": "U.S.A",
    "phone": "9090909090"
  },
  "shipping_address": {
    "address": "4590 Roosevelt Way NE",
    "city": "Seattle",
    "state": "Washington",
    "zip": "98105",
    "country": "U.S.A",
    "phone": "9090909090"
  }
}
```

#### Response

A successful request returns the created purchase order details with HTTP status code 201.

```json
{
  "code": 0,
  "message": "The purchase order has been created",
  "purchaseorder": {
    "purchaseorder_id": "460000000074263",
    "vendor_id": "460000000026049",
    "vendor_name": "MedSupply Inc.",
    "status": "draft",
    "purchaseorder_number": "PO-00001",
    "reference_number": "REF-001",
    "date": "2023-04-12",
    "delivery_date": "2023-04-20",
    "currency_id": "460000000000097",
    "currency_code": "USD",
    "currency_symbol": "$",
    "exchange_rate": 1.00,
    "is_inclusive_tax": false,
    "discount": 0.00,
    "discount_type": "item_level",
    "is_discount_before_tax": true,
    "contact_persons": [],
    "line_items": [
      {
        "line_item_id": "460000000074264",
        "item_id": "460000000027009",
        "name": "Generic Antibiotics - 500mg",
        "description": "Generic Antibiotics - 500mg",
        "quantity": 10.00,
        "rate": 112.50,
        "unit": "",
        "tax_id": "",
        "tax_name": "",
        "tax_percentage": 0.00,
        "item_total": 1125.00
      },
      {
        "line_item_id": "460000000074265",
        "item_id": "460000000027010",
        "name": "Pain Relievers - 200mg",
        "description": "Pain Relievers - 200mg",
        "quantity": 20.00,
        "rate": 75.00,
        "unit": "",
        "tax_id": "",
        "tax_name": "",
        "tax_percentage": 0.00,
        "item_total": 1500.00
      }
    ],
    "sub_total": 2625.00,
    "tax_total": 0.00,
    "total": 2625.00,
    "billing_address": {
      "address": "4590 Roosevelt Way NE",
      "city": "Seattle",
      "state": "Washington",
      "zip": "98105",
      "country": "U.S.A",
      "phone": "9090909090"
    },
    "shipping_address": {
      "address": "4590 Roosevelt Way NE",
      "city": "Seattle",
      "state": "Washington",
      "zip": "98105",
      "country": "U.S.A",
      "phone": "9090909090"
    },
    "notes": "Please deliver items as soon as possible",
    "terms": "Net 30",
    "created_time": "2023-04-12T10:15:00-0700",
    "last_modified_time": "2023-04-12T10:15:00-0700"
  }
}
```

### List Purchase Orders

Retrieves a list of purchase orders based on filter criteria.

**Endpoint**: `GET /purchaseorders`

**OAuth Scope**: `ZohoBooks.purchaseorders.READ`

#### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| filter_by | string | Filter by status (All, Draft, Open, Billed, Cancelled) |
| purchaseorder_number | string | Filter by purchase order number |
| reference_number | string | Filter by reference number |
| date | string | Filter by purchase order date |
| vendor_id | string | Filter by vendor ID |
| vendor_name | string | Filter by vendor name |
| item_id | string | Filter by item ID in line items |
| status | string | Filter by status (draft, open, billed, cancelled) |
| total | decimal | Filter by total amount |
| page | integer | Page number for pagination |
| per_page | integer | Number of records per page (max: 200) |
| sort_column | string | Column to sort by (vendor_name, purchaseorder_number, date, delivery_date, total) |
| sort_order | string | asc or desc |
| search_text | string | Search text across purchaseorder_number, reference_number, vendor_name |

#### Example Request

```
GET /purchaseorders?filter_by=Open&per_page=10&sort_column=date&sort_order=desc
```

#### Response

```json
{
  "code": 0,
  "message": "success",
  "purchaseorders": [
    {
      "purchaseorder_id": "460000000074263",
      "vendor_id": "460000000026049",
      "vendor_name": "MedSupply Inc.",
      "status": "open",
      "purchaseorder_number": "PO-00001",
      "reference_number": "REF-001",
      "date": "2023-04-12",
      "delivery_date": "2023-04-20",
      "currency_id": "460000000000097",
      "currency_code": "USD",
      "total": 2625.00,
      "created_time": "2023-04-12T10:15:00-0700",
      "last_modified_time": "2023-04-12T11:30:00-0700"
    },
    // Additional purchase orders...
  ],
  "page_context": {
    "page": 1,
    "per_page": 10,
    "has_more_page": false,
    "report_name": "Purchase Orders",
    "applied_filter": "Status.Open",
    "sort_column": "date",
    "sort_order": "D"
  }
}
```

### Get a Purchase Order

Retrieves details of a specific purchase order.

**Endpoint**: `GET /purchaseorders/{purchaseorder_id}`

**OAuth Scope**: `ZohoBooks.purchaseorders.READ`

#### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| purchaseorder_id | string | ID of the purchase order to retrieve |

#### Example Request

```
GET /purchaseorders/460000000074263
```

#### Response

```json
{
  "code": 0,
  "message": "success",
  "purchaseorder": {
    "purchaseorder_id": "460000000074263",
    "vendor_id": "460000000026049",
    "vendor_name": "MedSupply Inc.",
    "status": "open",
    "purchaseorder_number": "PO-00001",
    "reference_number": "REF-001",
    "date": "2023-04-12",
    "delivery_date": "2023-04-20",
    "currency_id": "460000000000097",
    "currency_code": "USD",
    "currency_symbol": "$",
    "exchange_rate": 1.00,
    "is_inclusive_tax": false,
    "discount": 0.00,
    "discount_type": "item_level",
    "is_discount_before_tax": true,
    "contact_persons": [],
    "line_items": [
      {
        "line_item_id": "460000000074264",
        "item_id": "460000000027009",
        "name": "Generic Antibiotics - 500mg",
        "description": "Generic Antibiotics - 500mg",
        "quantity": 10.00,
        "rate": 112.50,
        "unit": "",
        "tax_id": "",
        "tax_name": "",
        "tax_percentage": 0.00,
        "item_total": 1125.00
      },
      {
        "line_item_id": "460000000074265",
        "item_id": "460000000027010",
        "name": "Pain Relievers - 200mg",
        "description": "Pain Relievers - 200mg",
        "quantity": 20.00,
        "rate": 75.00,
        "unit": "",
        "tax_id": "",
        "tax_name": "",
        "tax_percentage": 0.00,
        "item_total": 1500.00
      }
    ],
    "sub_total": 2625.00,
    "tax_total": 0.00,
    "total": 2625.00,
    "billing_address": {
      "address": "4590 Roosevelt Way NE",
      "city": "Seattle",
      "state": "Washington",
      "zip": "98105",
      "country": "U.S.A",
      "phone": "9090909090"
    },
    "shipping_address": {
      "address": "4590 Roosevelt Way NE",
      "city": "Seattle",
      "state": "Washington",
      "zip": "98105",
      "country": "U.S.A",
      "phone": "9090909090"
    },
    "notes": "Please deliver items as soon as possible",
    "terms": "Net 30",
    "created_time": "2023-04-12T10:15:00-0700",
    "last_modified_time": "2023-04-12T11:30:00-0700"
  }
}
```

### Update a Purchase Order

Updates an existing purchase order.

**Endpoint**: `PUT /purchaseorders/{purchaseorder_id}`

**OAuth Scope**: `ZohoBooks.purchaseorders.UPDATE`

#### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| purchaseorder_id | string | ID of the purchase order to update |

#### Request Parameters

The request parameters are similar to the [Create a Purchase Order](#create-a-purchase-order) endpoint. When updating line items, include `line_item_id` for existing line items.

#### Example Request

```json
{
  "delivery_date": "2023-04-22",
  "notes": "Please deliver items as soon as possible - Updated note",
  "line_items": [
    {
      "line_item_id": "460000000074264",
      "quantity": 15,
      "rate": 112.50
    },
    {
      "line_item_id": "460000000074265",
      "quantity": 20,
      "rate": 75.00
    },
    {
      "item_id": "460000000027011",
      "quantity": 5,
      "rate": 95.00,
      "description": "Allergy Medication - 10mg"
    }
  ]
}
```

#### Response

A successful request returns the updated purchase order details with HTTP status code 200.

```json
{
  "code": 0,
  "message": "The purchase order has been updated",
  "purchaseorder": {
    // Updated purchase order details...
  }
}
```

### Delete a Purchase Order

Deletes a specific purchase order.

**Endpoint**: `DELETE /purchaseorders/{purchaseorder_id}`

**OAuth Scope**: `ZohoBooks.purchaseorders.DELETE`

#### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| purchaseorder_id | string | ID of the purchase order to delete |

#### Example Request

```
DELETE /purchaseorders/460000000074263
```

#### Response

```json
{
  "code": 0,
  "message": "The purchase order has been deleted"
}
```

## Purchase Order Status Management

### Mark a Purchase Order as Open

Changes the status of a purchase order to "open".

**Endpoint**: `POST /purchaseorders/{purchaseorder_id}/status/open`

**OAuth Scope**: `ZohoBooks.purchaseorders.UPDATE`

#### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| purchaseorder_id | string | ID of the purchase order |

#### Example Request

```
POST /purchaseorders/460000000074263/status/open
```

#### Response

```json
{
  "code": 0,
  "message": "The purchase order status has been changed to open"
}
```

### Mark a Purchase Order as Billed

Changes the status of a purchase order to "billed".

**Endpoint**: `POST /purchaseorders/{purchaseorder_id}/status/billed`

**OAuth Scope**: `ZohoBooks.purchaseorders.UPDATE`

#### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| purchaseorder_id | string | ID of the purchase order |

#### Example Request

```
POST /purchaseorders/460000000074263/status/billed
```

#### Response

```json
{
  "code": 0,
  "message": "The purchase order status has been changed to billed"
}
```

### Cancel a Purchase Order

Changes the status of a purchase order to "cancelled".

**Endpoint**: `POST /purchaseorders/{purchaseorder_id}/status/cancelled`

**OAuth Scope**: `ZohoBooks.purchaseorders.UPDATE`

#### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| purchaseorder_id | string | ID of the purchase order |

#### Example Request

```
POST /purchaseorders/460000000074263/status/cancelled
```

#### Response

```json
{
  "code": 0,
  "message": "The purchase order has been cancelled"
}
```

## Inventory and Item Management

### List Items with Inventory

To implement automated reordering, you'll need to track item inventory levels. Use the Items API to list items with their current stock information.

**Endpoint**: `GET /items`

**OAuth Scope**: `ZohoBooks.items.READ`

#### Example Request

```
GET /items
```

#### Response

The response includes inventory-related fields for each item:

```json
{
  "code": 0,
  "message": "success",
  "items": [
    {
      "item_id": "460000000027009",
      "name": "Generic Antibiotics - 500mg",
      "item_type": "inventory",
      "status": "active",
      "description": "Generic Antibiotics - 500mg tablets",
      "rate": 112.50,
      "reorder_level": 5,
      "locations": [
        {
          "location_id": "460000000000001",
          "location_name": "Main Warehouse",
          "location_stock_on_hand": 20,
          "location_available_stock": 12,
          "location_actual_available_stock": 12
        }
      ],
      "purchase_account_id": "460000000000106",
      "inventory_account_id": "460000000000107",
      "created_time": "2023-01-10T08:00:00-0700",
      "last_modified_time": "2023-04-12T14:30:00-0700"
    },
    // Additional items...
  ],
  "page_context": {
    "page": 1,
    "per_page": 200,
    "has_more_page": false,
    "report_name": "Items",
    "applied_filter": "",
    "sort_column": "name",
    "sort_order": "A"
  }
}
```

### Item Stock Fields

Key inventory-related fields in the item response:

| Field | Description |
|-------|-------------|
| reorder_level | The minimum stock level before reordering |
| locations | Array of location objects with stock information |
| location_stock_on_hand | Total physical stock at the location |
| location_available_stock | Stock available for sale/use |
| location_actual_available_stock | Actual available stock after accounting for commitments |

## Common Use Cases

### Automated Reordering

To implement automated reordering with a standard reorder point of 2:

1. **Monitor Inventory Levels**:
   - Fetch all items using the `GET /items` endpoint
   - Filter items where `location_available_stock < 2`

2. **Group Items by Vendor**:
   - For efficiency, group items that need reordering by vendor

3. **Create Purchase Orders**:
   - For each vendor, create a purchase order using the `POST /purchaseorders` endpoint
   - Include all items below reorder point in the line_items array
   - Set quantity to a standard reorder amount or based on usage patterns

4. **Track Purchase Order Status**:
   - Monitor the status of created purchase orders
   - Update local inventory tracking system with pending orders

### Purchase Order Tracking

To track the status of purchase orders:

1. **List Active Purchase Orders**:
   - Use `GET /purchaseorders?filter_by=Open` to get all open purchase orders

2. **Check Status of Specific Order**:
   - Use `GET /purchaseorders/{purchaseorder_id}` to get detailed information

3. **Update Status Based on Delivery**:
   - Use the status change endpoints to mark orders as received/billed
   - Update inventory records when items are received

## Error Handling

Common error codes and their meanings:

| Code | Description |
|------|-------------|
| 0 | Success |
| 1000 | Invalid request - check error message for details |
| 1001 | Required parameters missing |
| 1011 | Vendor not found |
| 1012 | Item not found |
| 1013 | Purchase order not found |
| 2001 | Authentication error - invalid token |
| 2002 | Authorization error - insufficient permissions |

Always check the `message` field in the response for detailed error information.

---

## API Notes and Best Practices

1. **Rate Limiting**: 
   - Zoho Books API has rate limits that vary by plan
   - Implement exponential backoff for retries

2. **Webhook Integration**:
   - Use webhooks to receive real-time notifications about purchase order status changes
   - Configure webhooks in the Zoho Books developer console

3. **Bulk Operations**:
   - For creating multiple purchase orders, consider batch processing
   - Monitor API usage to stay within limits

4. **Error Handling**:
   - Always handle errors gracefully
   - Implement logging for API calls and responses
   - Store failed operations for retry

5. **Testing**:
   - Use Zoho's sandbox environment for testing before production
   - Test all error scenarios and edge cases