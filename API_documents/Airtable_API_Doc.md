# Explanation of the entire Airtable schema and the column names in each Table

Below is an explanation of how the data is structured and what each (or groups of) column represents, along with notes on how the Airtable API “sees” these fields. In our dataset the information is split across several related tables, and each field is configured in Airtable as one of the supported field types (text, number, date, attachment, linked record, etc). The API documentation tells you that when you retrieve records (via “List records” or “Get record”) you’ll get a JSON “fields” object whose keys are either the field names (or IDs, if you request that) and whose values follow the formatting rules for that field’s type.   
**How the API Document Informs Usage**

	•	**Authentication & Scopes:**

To read (or write) these records, your API token must have the appropriate scopes (for example, data.records:read to view data and data.records:write to update).

The endpoints (List records, Get record) return a JSON object where every record’s fields are keyed by their field name (or field ID if requested).

	•	**Field Types & Formatting:**

Each field in the CSV corresponds to an Airtable field type. For example, timestamps are “dateTime” fields (returned as ISO‑8601 strings or formatted strings when using cellFormat=string), attachments (like prescription images or medicine images) are “multipleAttachments” fields (returned as an array of attachment objects), and linked records (like those referencing the Medicines or Address tables) are returned either as arrays of record IDs or as expanded objects if you use lookups.

	•	**Record Relationships:**

Several columns (for example, “Medicines Table,” “Payments Table,” “AddressID”) are pointers or linked record fields. In the API you will see these as arrays of IDs, and you can use the “get base schema” endpoint to see how the relationships are defined.

**In Summary**

	•	**Orders Table:**

Contains every detail needed to process and track an order—from customer and delivery details to payment breakdowns and timestamps for every stage of the order lifecycle. It integrates with other tables (Medicines, Payments, Address) and external systems (Tookan, Zoho).

	•	**Contacts Table:**

Captures customer personal details, addresses, device/app metadata, and marketing information.

	•	**Medicines Table:**

Describes the products (medicines) offered, including usage, pricing, inventory, and regulatory compliance details.

	•	**Payments Table:**

Logs payment transactions, linking orders to external payment and invoicing systems with all the necessary financial details.

	•	**Address Table:**

Provides structured address and geolocation data that supports order delivery and customer location verification.

Using the Airtable API, you can query any of these tables with endpoints like “List records” and “Get record.” Each field’s data type (as described in the API documentation) determines how you read, update, and display the information in your integration. This structure ensures that each column both contains the necessary data about the order process and is accessible in a predictable, typed manner through Airtable’s API

