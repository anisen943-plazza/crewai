

# Invoices

Invoice is a document sent to your client that indicates the products/services sold by you with the payment information that the client has to make.

End Points


Create an invoice


[POST  \\
\\
\\
/invoices](https://www.zoho.com/books/api/v3/invoices/#create-an-invoice)

Update an invoice using a custom field's unique value


[PUT   \\
\\
\\
/invoices](https://www.zoho.com/books/api/v3/invoices/#update-an-invoice-using-a-custom-fields-unique-value)

List invoices


[GET   \\
\\
\\
/invoices](https://www.zoho.com/books/api/v3/invoices/#list-invoices)

Update an invoice


[PUT   \\
\\
\\
/invoices/{invoice\_id}](https://www.zoho.com/books/api/v3/invoices/#update-an-invoice)

Get an invoice


[GET   \\
\\
\\
/invoices/{invoice\_id}](https://www.zoho.com/books/api/v3/invoices/#get-an-invoice)

Delete an invoice


[DELETE\\
\\
\\
/invoices/{invoice\_id}](https://www.zoho.com/books/api/v3/invoices/#delete-an-invoice)

Mark an invoice as sent


[POST  \\
\\
\\
/invoices/{invoice\_id}/status/sent](https://www.zoho.com/books/api/v3/invoices/#mark-an-invoice-as-sent)

Void an invoice


[POST  \\
\\
\\
/invoices/{invoice\_id}/status/void](https://www.zoho.com/books/api/v3/invoices/#void-an-invoice)

Mark as draft


[POST  \\
\\
\\
/invoices/{invoice\_id}/status/draft](https://www.zoho.com/books/api/v3/invoices/#mark-as-draft)

Email invoices


[POST  \\
\\
\\
/invoices/email](https://www.zoho.com/books/api/v3/invoices/#email-invoices)

Create an instant invoice


[POST  \\
\\
\\
/invoices/fromsalesorder](https://www.zoho.com/books/api/v3/invoices/#create-an-instant-invoice)

Submit an invoice for approval


[POST  \\
\\
\\
/invoices/{invoice\_id}/submit](https://www.zoho.com/books/api/v3/invoices/#submit-an-invoice-for-approval)

Approve an invoice.


[POST  \\
\\
\\
/invoices/{invoice\_id}/approve](https://www.zoho.com/books/api/v3/invoices/#approve-an-invoice)

Email an invoice


[POST  \\
\\
\\
/invoices/{invoice\_id}/email](https://www.zoho.com/books/api/v3/invoices/#email-an-invoice)

Get invoice email content


[GET   \\
\\
\\
/invoices/{invoice\_id}/email](https://www.zoho.com/books/api/v3/invoices/#get-invoice-email-content)

Remind Customer


[POST  \\
\\
\\
/invoices/{invoice\_id}/paymentreminder](https://www.zoho.com/books/api/v3/invoices/#remind-customer)

Get payment reminder mail content


[GET   \\
\\
\\
/invoices/{invoice\_id}/paymentreminder](https://www.zoho.com/books/api/v3/invoices/#get-payment-reminder-mail-content)

Bulk invoice reminder


[POST  \\
\\
\\
/invoices/paymentreminder](https://www.zoho.com/books/api/v3/invoices/#bulk-invoice-reminder)

Bulk export Invoices


[GET   \\
\\
\\
/invoices/pdf](https://www.zoho.com/books/api/v3/invoices/#bulk-export-invoices)

Bulk print invoices


[GET   \\
\\
\\
/invoices/print](https://www.zoho.com/books/api/v3/invoices/#bulk-print-invoices)

Disable payment reminder


[POST  \\
\\
\\
/invoices/{invoice\_id}/paymentreminder/disable](https://www.zoho.com/books/api/v3/invoices/#disable-payment-reminder)

Enable payment reminder


[POST  \\
\\
\\
/invoices/{invoice\_id}/paymentreminder/enable](https://www.zoho.com/books/api/v3/invoices/#enable-payment-reminder)

Write off invoice


[POST  \\
\\
\\
/invoices/{invoice\_id}/writeoff](https://www.zoho.com/books/api/v3/invoices/#write-off-invoice)

Cancel write off


[POST  \\
\\
\\
/invoices/{invoice\_id}/writeoff/cancel](https://www.zoho.com/books/api/v3/invoices/#cancel-write-off)

Update billing address


[PUT   \\
\\
\\
/invoices/{invoice\_id}/address/billing](https://www.zoho.com/books/api/v3/invoices/#update-billing-address)

Update shipping address


[PUT   \\
\\
\\
/invoices/{invoice\_id}/address/shipping](https://www.zoho.com/books/api/v3/invoices/#update-shipping-address)

List invoice templates


[GET   \\
\\
\\
/invoices/templates](https://www.zoho.com/books/api/v3/invoices/#list-invoice-templates)

Update invoice template


[PUT   \\
\\
\\
/invoices/{invoice\_id}/templates/{template\_id}](https://www.zoho.com/books/api/v3/invoices/#update-invoice-template)

List invoice payments


[GET   \\
\\
\\
/invoices/{invoice\_id}/payments](https://www.zoho.com/books/api/v3/invoices/#list-invoice-payments)

List credits applied


[GET   \\
\\
\\
/invoices/{invoice\_id}/creditsapplied](https://www.zoho.com/books/api/v3/invoices/#list-credits-applied)

Apply credits


[POST  \\
\\
\\
/invoices/{invoice\_id}/credits](https://www.zoho.com/books/api/v3/invoices/#apply-credits)

Delete a payment


[DELETE\\
\\
\\
/invoices/{invoice\_id}/payments/{invoice\_payment\_id}](https://www.zoho.com/books/api/v3/invoices/#delete-a-payment)

Delete applied credit


[DELETE\\
\\
\\
/invoices/{invoice\_id}/creditsapplied/{creditnotes\_invoice\_id}](https://www.zoho.com/books/api/v3/invoices/#delete-applied-credit)

Add attachment to an invoice


[POST  \\
\\
\\
/invoices/{invoice\_id}/attachment](https://www.zoho.com/books/api/v3/invoices/#add-attachment-to-an-invoice)

Update attachment preference


[PUT   \\
\\
\\
/invoices/{invoice\_id}/attachment](https://www.zoho.com/books/api/v3/invoices/#update-attachment-preference)

Get an invoice attachment


[GET   \\
\\
\\
/invoices/{invoice\_id}/attachment](https://www.zoho.com/books/api/v3/invoices/#get-an-invoice-attachment)

Delete an attachment


[DELETE\\
\\
\\
/invoices/{invoice\_id}/attachment](https://www.zoho.com/books/api/v3/invoices/#delete-an-attachment)

Delete the expense receipt


[DELETE\\
\\
\\
/invoices/expenses/{expense\_id}/receipt](https://www.zoho.com/books/api/v3/invoices/#delete-the-expense-receipt)

Update custom field in existing invoices


[PUT   \\
\\
\\
/invoice/{invoice\_id}/customfields](https://www.zoho.com/books/api/v3/invoices/#update-custom-field-in-existing-invoices)

Add comment


[POST  \\
\\
\\
/invoices/{invoice\_id}/comments](https://www.zoho.com/books/api/v3/invoices/#add-comment)

List invoice comments & history


[GET   \\
\\
\\
/invoices/{invoice\_id}/comments](https://www.zoho.com/books/api/v3/invoices/#list-invoice-comments-and-history)

Update comment


[PUT   \\
\\
\\
/invoices/{invoice\_id}/comments/{comment\_id}](https://www.zoho.com/books/api/v3/invoices/#update-comment)

Delete a comment


[DELETE\\
\\
\\
/invoices/{invoice\_id}/comments/{comment\_id}](https://www.zoho.com/books/api/v3/invoices/#delete-a-comment)

Generate payment link


[GET   \\
\\
\\
/share/paymentlink](https://www.zoho.com/books/api/v3/invoices/#generate-payment-link)

### Attribute

invoice\_id

string

ID of the invoice

ach\_payment\_initiated

boolean

invoice\_number

string

Search invoices by invoice number.Variants: `invoice_number_startswith` and `invoice_number_contains`. Max-length \[100\]

is\_pre\_gst

boolean

🇮🇳

India


only

Applicable for transactions that fall before july 1, 2017

place\_of\_supply

string

🇮🇳

India


,GCConly

Place where the goods/services are supplied to. (If not given, `place of contact` given for the contact will be taken)

Supported codes for UAE emirates are :

Abu Dhabi - `AB`,

Ajman - `AJ`,

Dubai - `DU`,

Fujairah - `FU`,

Ras al-Khaimah - `RA`,

Sharjah - `SH`,

Umm al-Quwain - `UM`

Supported codes for the GCC countries are :

United Arab Emirates - `AE`,

Saudi Arabia - `SA`,

Bahrain - `BH`,

Kuwait - `KW`,

Oman - `OM`,

Qatar - `QA`.

gst\_no

string

🇮🇳

India


only

15 digit GST identification number of the customer.

gst\_treatment

string

🇮🇳

India


only

Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are ` business_gst ` , ` business_none ` , ` overseas ` , ` consumer `.

cfdi\_usage

string

🇲🇽

Mexico


only

Choose CFDI Usage. Allowed values:

`acquisition_of_merchandise`, `return_discount_bonus`, `general_expense`, `buildings`, `furniture_office_equipment`, `transport_equipment`, `computer_equipmentdye_molds_tools`, `telephone_communication`, `satellite_communication`, `other_machinery_equipment`, `hospital_expense`, `medical_expense_disability`, `funeral_expense`, `donation`, `interest_mortage_loans`, `contribution_sar`, `medical_expense_insurance_pormium`, `school_transportation_expense`, `deposit_saving_account`, `payment_educational_service`, `no_tax_effect`, `payment`, `payroll`.

cfdi\_reference\_type

string

🇲🇽

Mexico


only

Choose CFDI Reference Type. Allowed values:

`return_of_merchandise`, `substitution_previous_cfdi`, `transfer_of_goods`, `invoice_generated_from_order`, `cfdi_for_advance`.

reference\_invoice\_id

string

🇲🇽

Mexico


only

Associate the reference invoice.

vat\_treatment

string

🇬🇧

United Kingdom


only

(Optional) VAT treatment for the invoices. VAT treatment denotes the location of the customer, if the customer resides in UK then the VAT treatment is `uk`. If the customer is in an EU country & VAT registered, you are resides in Northen Ireland and selling Goods then his VAT treatment is `eu_vat_registered`, if he resides outside of the UK then his VAT treatment is `overseas` (For Pre Brexit, this can be split as `eu_vat_registered`, `eu_vat_not_registered` and `non_eu`).

tax\_treatment

string

GCC,🇲🇽

Mexico


,🇰🇪

Kenya


,🇿🇦

South Africa


only

VAT treatment for the invoice .Choose whether the contact falls under: `vat_registered`, `vat_not_registered`, `gcc_vat_not_registered`, `gcc_vat_registered`, `non_gcc`.

`dz_vat_registered` and `dz_vat_not_registered` supported only for **UAE**.

`home_country_mexico`, `border_region_mexico`, `non_mexico` supported only for **MX**.

**For Kenya Edition:** `vat_registered` , `vat_not_registered` , `non_kenya`(A business that is located outside Kenya).

**For SouthAfrica Edition:** `vat_registered`, `vat_not_registered`, `overseas`(A business that is located outside SouthAfrica).

is\_reverse\_charge\_applied

boolean

🇿🇦

South Africa


only

(Required if customer tax treatment is `vat_registered`)

Used to specify whether the transaction is applicable for Domestic Reverse Charge (DRC) or not.

vat\_reg\_no

string

Enter VAT registration number.

date

string

Search invoices by invoice date. Default date format is yyyy-mm-dd. ` Variants: date_start, date_end, date_before and date_after`.

status

string

Search invoices by invoice status.Allowed Values: `sent`, `draft`, `overdue`, `paid`, `void`, `unpaid`, `partially_paid` and `viewed`

payment\_terms

integer

Payment terms in days e.g. 15, 30, 60. Invoice due date will be calculated based on this. Max-length \[100\]

payment\_terms\_label

string

Used to override the default payment terms label. Default value for 15 days is "Net 15 Days". Max-length \[100\]

due\_date

string

Search invoices by due date. Default date format is yyyy-mm-dd. ` Variants: due_date_start, due_date_end, due_date_before and due_date_after `

payment\_expected\_date

string

The expected date of payment

last\_payment\_date

string

The last payment date of the invoice

reference\_number

string

The reference number of the invoice

customer\_id

string

ID of the customer the invoice has to be created.

customer\_name

string

The name of the customer. Max-length \[100\]

contact\_persons

array

Array of contact person(s) for whom invoice has to be sent.

currency\_id

string

The currency id of the currency

currency\_code

string

The currency code in which the invoice is created.

exchange\_rate

float

Exchange rate of the currency.

discount

float

Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length \[100\]

is\_discount\_before\_tax

boolean

Used to specify how the discount has to applied. Either before or after the calculation of tax.

discount\_type

string

How the discount is specified. Allowed values: `entity_level` and `item_level`.

is\_inclusive\_tax

boolean

Used to specify whether the line item rates are inclusive or exclusivr of tax.

recurring\_invoice\_id

string

ID of the recurring invoice from which the invoice is created.

is\_viewed\_by\_client

boolean

has\_attachment

boolean

client\_viewed\_time

string

line\_items

array

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

line\_item\_id

string

The line item id

item\_id

string

Search invoices by item id.

project\_id

string

ID of the Project.

sat\_item\_key\_code

string

🇲🇽

Mexico


only

Add SAT Item Key Code for your goods/services. Download the [CFDI Catalogs.](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls)

unitkey\_code

string

🇲🇽

Mexico


only

Add SAT Unit Key Code for your goods/services. Download the [CFDI Catalogs.](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls)

project\_name

string

Name of the project.

time\_entry\_ids

array

IDs of the time entries associated with the project.

warehouses

array

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

warehouse\_id

string

Enter warehouse ID

warehouse\_name

string

Enter warehouse name.

warehouse\_stock\_on\_hand

string

Available stock in your warehouse.

item\_type

string

Enter goods/services

product\_type

string

Enter `goods` or `services` .

**For SouthAfrica Edition:** `service`, `goods`, `capital_service` and `capital_goods`

expense\_id

string

Add billable expense id which needs to be convert to invoice

expense\_receipt\_name

string

name

string

The name of the line item. Max-length \[100\]

description

string

The description of the line items. Max-length \[2000\]

item\_order

integer

The order of the line item\_order

bcy\_rate

float

base currency rate

rate

double

Rate of the line item.

quantity

float

The quantity of line item

unit

string

Unit of the line item e.g. kgs, Nos. Max-length \[100\]

discount\_amount

float

The discount amount on the line item

discount

float

Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length \[100\]

tags

array

Filter all your reports based on the tag

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

is\_tag\_mandatory

boolean

Boolean to check if the tag is mandatory

tag\_id

string

ID of the reporting tag

tag\_name

string

Name of the reporting tag

tag\_option\_id

string

ID of the reporting tag's option

tag\_option\_name

string

Name of the reporting tag's option

tax\_id

string

ID of the tax.

tds\_tax\_id

string

🇲🇽

Mexico


only

ID of the TDS tax.

tax\_name

string

The name of the tax

tax\_type

string

The type of the tax

tax\_percentage

float

The percentage of tax levied

tax\_treatment\_code

string

GCConly

Specify reason for using out of scope.

Supported values for UAE are `uae_same_tax_group`, `uae_reimbursed_expense` and `uae_others`.

Supported values for Bahrain are `bahrain_same_tax_group`, `bahrain_transfer_of_concern`, `bahrain_disbursement`, `bahrain_head_to_branch_transaction`, `bahrain_warranty_repair_services` and `bahrain_others`.

Supported values for Saudi Arabia are `ksa_pvt_health`, `ksa_pvt_edu`, `ksa_reimbursed_expense` and `ksa_house_sales`.

item\_total

float

The total amount of the line items

header\_name

string

Name of the item header

header\_id

string

ID of the item header

shipping\_charge

string

Shipping charges applied to the invoice. Max-length \[100\]

adjustment

double

Adjustments made to the invoice.

adjustment\_description

string

Customize the adjustment description. E.g. Rounding off.

sub\_total

float

The sub total of the all items

tax\_total

double

The total amount of the tax levied

total

string

The total amount to be paid

taxes

array

List of the taxes levied

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

tax\_name

string

The name of the tax

tax\_amount

float

The amount of the tax levied

payment\_reminder\_enabled

boolean

Boolean to check if reminders have been enabled

payment\_made

float

The amount paid

credits\_applied

float

The credits applied

tax\_amount\_withheld

float

The tax amount which has been withheld

balance

string

The unpaid amount

write\_off\_amount

float

The write off amount

allow\_partial\_payments

boolean

Boolean to check if partial payments are allowed for the contact

price\_precision

integer

The precision value on the price

payment\_options

object

Payment options for the invoice, online payment gateways and bank accounts. Will be displayed in the pdf.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

payment\_gateways

array

Online payment gateways through which payment can be made.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

configured

boolean

Boolean check to see if a payment gateway has been configured

additional\_field1

string

Paypal payment method. Allowed Values: `standard` and `adaptive`

gateway\_name

string

Name of the payment gateway associated with the invoice. E.g. paypal, stripe.Allowed Values: `paypal`, `authorize_net`, `payflow_pro`, `stripe`, `2checkout` and `braintree`

is\_emailed

boolean

Boolean check to see if the mail has been sent

reminders\_sent

integer

The no of reminders sent

last\_reminder\_sent\_date

string

The date the last email was sent

billing\_address

object

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

address

string

Billing address for the invoice

street2

string

city

string

City of the customer’s billing address.

state

string

State of the customer’s billing address.

zip

string

Zip code of the customer’s billing address.

country

string

Country of the customer’s billing address.

fax

string

Customer's fax number.

shipping\_address

object

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

address

string

Shipping address for the invoice

street2

string

city

string

City of the customer’s Shipping address.

state

string

State of the customer’s Shipping address.

zip

string

Zip code of the customer’s Shipping address.

country

string

Country of the customer’s Shipping address.

fax

string

Customer's fax number.

notes

string

The notes added below expressing gratitude or for conveying some information.

terms

string

The terms added below expressing gratitude or for conveying some information.

custom\_fields

array

Custom fields for an invoice.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

customfield\_id

long

value

string

Value of the Custom Field

template\_id

string

ID of the pdf template associated with the invoice.

template\_name

string

created\_time

string

The time of creation of the invoices

last\_modified\_time

string

attachment\_name

string

can\_send\_in\_mail

boolean

salesperson\_id

string

salesperson\_name

string

Name of the salesperson. Max-length \[200\]

invoice\_url

string

Example

`{
    "invoice_id": 982000000567114,
    "ach_payment_initiated": false,
    "invoice_number": "INV-00003",
    "is_pre_gst": true,
    "place_of_supply": "TN",
    "gst_no": "22AAAAA0000A1Z5",
    "gst_treatment": "business_gst",
    "cfdi_usage": "acquisition_of_merchandise",
    "cfdi_reference_type": "return_of_merchandise",
    "reference_invoice_id": "132738000000126013",
    "vat_treatment": "string",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "vat_reg_no": "string",
    "date": "2013-11-17",
    "status": "draft",
    "payment_terms": 15,
    "payment_terms_label": "Net 15",
    "due_date": "2013-12-03",
    "payment_expected_date": " ",
    "last_payment_date": " ",
    "reference_number": " ",
    "customer_id": 982000000567001,
    "customer_name": "Bowman & Co",
    "contact_persons": [\
        "982000000870911",\
        "982000000870915"\
    ],
    "currency_id": 982000000000190,
    "currency_code": "USD",
    "exchange_rate": 1,
    "discount": 0,
    "is_discount_before_tax": true,
    "discount_type": "item_level",
    "is_inclusive_tax": false,
    "recurring_invoice_id": " ",
    "is_viewed_by_client": false,
    "has_attachment": false,
    "client_viewed_time": "",
    "line_items": [\
        {\
            "line_item_id": 982000000567021,\
            "item_id": 982000000030049,\
            "project_id": 90300000087378,\
            "sat_item_key_code": 71121206,\
            "unitkey_code": "E48",\
            "project_name": "Sample Project",\
            "time_entry_ids": [],\
            "warehouses": [\
                {\
                    "warehouse_id": "",\
                    "warehouse_name": "",\
                    "warehouse_stock_on_hand": ""\
                }\
            ],\
            "item_type": "goods",\
            "product_type": "goods",\
            "expense_id": " ",\
            "expense_receipt_name": "string",\
            "name": "Hard Drive",\
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",\
            "item_order": 1,\
            "bcy_rate": 120,\
            "rate": 120,\
            "quantity": 1,\
            "unit": " ",\
            "discount_amount": 0,\
            "discount": 0,\
            "tags": [\
                {\
                    "is_tag_mandatory": false,\
                    "tag_id": 982000000009070,\
                    "tag_name": "Location",\
                    "tag_option_id": 982000000002670,\
                    "tag_option_name": "USA"\
                }\
            ],\
            "tax_id": 982000000557028,\
            "tds_tax_id": "982000000557012",\
            "tax_name": "VAT",\
            "tax_type": "tax",\
            "tax_percentage": 12.5,\
            "tax_treatment_code": "uae_others",\
            "item_total": 120,\
            "header_name": "Electronic devices",\
            "header_id": 982000000000670\
        }\
    ],
    "shipping_charge": 0,
    "adjustment": 0,
    "adjustment_description": " ",
    "sub_total": 10000,
    "tax_total": 22.6,
    "total": 10000,
    "taxes": [\
        {\
            "tax_name": "VAT",\
            "tax_amount": 19.13\
        }\
    ],
    "payment_reminder_enabled": true,
    "payment_made": 26.91,
    "credits_applied": 22.43,
    "tax_amount_withheld": 0,
    "balance": 40.6,
    "write_off_amount": 0,
    "allow_partial_payments": true,
    "price_precision": 2,
    "payment_options": {
        "payment_gateways": [\
            {\
                "configured": true,\
                "additional_field1": "standard",\
                "gateway_name": "paypal"\
            }\
        ]
    },
    "is_emailed": false,
    "reminders_sent": 1,
    "last_reminder_sent_date": " ",
    "billing_address": {
        "address": "4900 Hopyard Rd, Suite 310",
        "street2": "McMillan Avenue",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600"
    },
    "shipping_address": {
        "address": "4900 Hopyard Rd, Suit 310",
        "street2": "McMillan Avenue",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 945881,
        "country": "USA",
        "fax": "+1-925-924-9600"
    },
    "notes": "Looking forward for your business.",
    "terms": "Terms & Conditions apply",
    "custom_fields": [\
        {\
            "customfield_id": "46000000012845",\
            "value": "Normal"\
        }\
    ],
    "template_id": 982000000000143,
    "template_name": "Service - Classic",
    "created_time": "2013-11-18T02:17:40-0800",
    "last_modified_time": "2013-11-18T02:02:51-0800",
    "attachment_name": " ",
    "can_send_in_mail": true,
    "salesperson_id": " ",
    "salesperson_name": " ",
    "invoice_url": "https://books.zoho.com/SecurePayment?CInvoiceID=23d84d0cf64f9a72ea0c66fded25a08c8bafd0ab508aff05323a9f80e2cd03fdc5dd568d3d6407bbda969d3e870d740b6fce549a9438c4ea"
}`

## Create an invoice

Create an invoice for your customer.


`OAuth Scope : ZohoBooks.invoices.CREATE`

### Arguments

customer\_id

string

(Required)


ID of the customer the invoice has to be created.

currency\_id

string

The currency id of the currency

contact\_persons

array

Array of contact person(s) for whom invoice has to be sent.

invoice\_number

string

Search invoices by invoice number.Variants: `invoice_number_startswith` and `invoice_number_contains`. Max-length \[100\]

place\_of\_supply

string

🇮🇳

India


,GCConly

Place where the goods/services are supplied to. (If not given, `place of contact` given for the contact will be taken)

Supported codes for UAE emirates are :

Abu Dhabi - `AB`,

Ajman - `AJ`,

Dubai - `DU`,

Fujairah - `FU`,

Ras al-Khaimah - `RA`,

Sharjah - `SH`,

Umm al-Quwain - `UM`

Supported codes for the GCC countries are :

United Arab Emirates - `AE`,

Saudi Arabia - `SA`,

Bahrain - `BH`,

Kuwait - `KW`,

Oman - `OM`,

Qatar - `QA`.

vat\_treatment

string

🇬🇧

United Kingdom


only

(Optional) VAT treatment for the invoices. VAT treatment denotes the location of the customer, if the customer resides in UK then the VAT treatment is `uk`. If the customer is in an EU country & VAT registered, you are resides in Northen Ireland and selling Goods then his VAT treatment is `eu_vat_registered`, if he resides outside of the UK then his VAT treatment is `overseas` (For Pre Brexit, this can be split as `eu_vat_registered`, `eu_vat_not_registered` and `non_eu`).

tax\_treatment

string

GCC,🇲🇽

Mexico


,🇰🇪

Kenya


,🇿🇦

South Africa


only

VAT treatment for the invoice .Choose whether the contact falls under: `vat_registered`, `vat_not_registered`, `gcc_vat_not_registered`, `gcc_vat_registered`, `non_gcc`.

`dz_vat_registered` and `dz_vat_not_registered` supported only for **UAE**.

`home_country_mexico`, `border_region_mexico`, `non_mexico` supported only for **MX**.

**For Kenya Edition:** `vat_registered` , `vat_not_registered` , `non_kenya`(A business that is located outside Kenya).

**For SouthAfrica Edition:** `vat_registered`, `vat_not_registered`, `overseas`(A business that is located outside SouthAfrica).

is\_reverse\_charge\_applied

boolean

🇿🇦

South Africa


only

(Required if customer tax treatment is `vat_registered`)

Used to specify whether the transaction is applicable for Domestic Reverse Charge (DRC) or not.

gst\_treatment

string

🇮🇳

India


only

Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are ` business_gst ` , ` business_none ` , ` overseas ` , ` consumer `.

gst\_no

string

🇮🇳

India


only

15 digit GST identification number of the customer.

cfdi\_usage

string

🇲🇽

Mexico


only

Choose CFDI Usage. Allowed values:

`acquisition_of_merchandise`, `return_discount_bonus`, `general_expense`, `buildings`, `furniture_office_equipment`, `transport_equipment`, `computer_equipmentdye_molds_tools`, `telephone_communication`, `satellite_communication`, `other_machinery_equipment`, `hospital_expense`, `medical_expense_disability`, `funeral_expense`, `donation`, `interest_mortage_loans`, `contribution_sar`, `medical_expense_insurance_pormium`, `school_transportation_expense`, `deposit_saving_account`, `payment_educational_service`, `no_tax_effect`, `payment`, `payroll`.

reference\_number

string

The reference number of the invoice

template\_id

string

ID of the pdf template associated with the invoice.

date

string

Search invoices by invoice date. Default date format is yyyy-mm-dd. ` Variants: date_start, date_end, date_before and date_after`.

payment\_terms

integer

Payment terms in days e.g. 15, 30, 60. Invoice due date will be calculated based on this. Max-length \[100\]

payment\_terms\_label

string

Used to override the default payment terms label. Default value for 15 days is "Net 15 Days". Max-length \[100\]

due\_date

string

Search invoices by due date. Default date format is yyyy-mm-dd. ` Variants: due_date_start, due_date_end, due_date_before and due_date_after `

discount

float

Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length \[100\]

is\_discount\_before\_tax

boolean

Used to specify how the discount has to applied. Either before or after the calculation of tax.

discount\_type

string

How the discount is specified. Allowed values: `entity_level` and `item_level`.

is\_inclusive\_tax

boolean

Used to specify whether the line item rates are inclusive or exclusivr of tax.

exchange\_rate

float

Exchange rate of the currency.

recurring\_invoice\_id

string

ID of the recurring invoice from which the invoice is created.

invoiced\_estimate\_id

string

ID of the invoice from which the invoice is created.

salesperson\_name

string

Name of the salesperson. Max-length \[200\]

custom\_fields

array

Custom fields for an invoice.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

customfield\_id

long

value

string

Value of the Custom Field

line\_items

array

(Required)


Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

item\_id

string

(Required)


Search invoices by item id.

project\_id

string

ID of the Project.

time\_entry\_ids

array

IDs of the time entries associated with the project.

product\_type

string

Enter `goods` or `services` .

**For SouthAfrica Edition:** `service`, `goods`, `capital_service` and `capital_goods`

hsn\_or\_sac

string

🇮🇳

India


,🇰🇪

Kenya


,🇿🇦

South Africa


only

Add HSN/SAC code for your goods/services

sat\_item\_key\_code

string

🇲🇽

Mexico


only

Add SAT Item Key Code for your goods/services. Download the [CFDI Catalogs.](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls)

unitkey\_code

string

🇲🇽

Mexico


only

Add SAT Unit Key Code for your goods/services. Download the [CFDI Catalogs.](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls)

warehouse\_id

string

Enter warehouse ID

expense\_id

string

Add billable expense id which needs to be convert to invoice

bill\_id

string

Add billable bill id which needs to be convert to invoice

bill\_item\_id

string

Add billable bill item id which needs to be convert to invoice

expense\_receipt\_name

string

name

string

The name of the line item. Max-length \[100\]

description

string

The description of the line items. Max-length \[2000\]

item\_order

integer

The order of the line item\_order

bcy\_rate

float

base currency rate

rate

double

Rate of the line item.

quantity

float

The quantity of line item

unit

string

Unit of the line item e.g. kgs, Nos. Max-length \[100\]

discount\_amount

float

The discount amount on the line item

discount

float

Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length \[100\]

tags

array

Filter all your reports based on the tag

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

tag\_id

string

ID of the reporting tag

tag\_option\_id

string

ID of the reporting tag's option

tax\_id

string

ID of the tax.

tds\_tax\_id

string

🇲🇽

Mexico


only

ID of the TDS tax.

tax\_name

string

The name of the tax

tax\_type

string

The type of the tax

tax\_percentage

float

The percentage of tax levied

tax\_treatment\_code

string

GCConly

Specify reason for using out of scope.

Supported values for UAE are `uae_same_tax_group`, `uae_reimbursed_expense` and `uae_others`.

Supported values for Bahrain are `bahrain_same_tax_group`, `bahrain_transfer_of_concern`, `bahrain_disbursement`, `bahrain_head_to_branch_transaction`, `bahrain_warranty_repair_services` and `bahrain_others`.

Supported values for Saudi Arabia are `ksa_pvt_health`, `ksa_pvt_edu`, `ksa_reimbursed_expense` and `ksa_house_sales`.

header\_name

string

Name of the item header

salesorder\_item\_id

string

ID of the sales order line item which is invoices.

payment\_options

object

Payment options for the invoice, online payment gateways and bank accounts. Will be displayed in the pdf.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

payment\_gateways

array

Online payment gateways through which payment can be made.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

configured

boolean

Boolean check to see if a payment gateway has been configured

additional\_field1

string

Paypal payment method. Allowed Values: `standard` and `adaptive`

gateway\_name

string

Name of the payment gateway associated with the invoice. E.g. paypal, stripe.Allowed Values: `paypal`, `authorize_net`, `payflow_pro`, `stripe`, `2checkout` and `braintree`

allow\_partial\_payments

boolean

Boolean to check if partial payments are allowed for the contact

custom\_body

string

custom\_subject

string

notes

string

The notes added below expressing gratitude or for conveying some information.

terms

string

The terms added below expressing gratitude or for conveying some information.

shipping\_charge

string

Shipping charges applied to the invoice. Max-length \[100\]

adjustment

double

Adjustments made to the invoice.

adjustment\_description

string

Customize the adjustment description. E.g. Rounding off.

reason

string

tax\_authority\_id

string

🇺🇸

United States


only

ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority.

tax\_exemption\_id

string

🇮🇳

India


,🇺🇸

United States


only

ID of the tax exemption.

billing\_address\_id

string

This is the ID of the billing address you want to apply to the invoice. `Note:` You need to create a billing address with the address API and pass the address ID here.

shipping\_address\_id

string

This is the ID of the shipping address you want to apply to the invoice. `Note:` You need to create a shipping address with the address API and pass the address ID here.

avatax\_use\_code

string

Avalara Integrationonly

Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara \[standard codes\]\[1\] or enter a custom code. Max-length \[25\]

avatax\_exempt\_no

string

Avalara Integrationonly

Exemption certificate number of the customer. Max-length \[25\]

tax\_id

string

ID of the tax.

expense\_id

string

Add billable expense id which needs to be convert to invoice

salesorder\_item\_id

string

ID of the sales order line item which is invoices.

avatax\_tax\_code

string

Avalara Integrationonly

A tax code is a unique label used to group Items (products, services, or charges) together. Refer the \[link\]\[2\] for more deails. Max-length \[25\]

time\_entry\_ids

array

IDs of the time entries associated with the project.

### Query Parameters

send

Send the invoice to the contact person(s) associated with the invoice. Allowed values `true` and `false`.

ignore\_auto\_number\_generation

Ignore auto invoice number generation for this invoice. This mandates the invoice number. Allowed values `true` and `false`

Request Example

undefined

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`parameters_data='{"field1":"value1","field2":"value2"}';
headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices?organization_id=10234695"\
type: POST\
headers: headers_data\
content-type: application/json\
parameters: parameters_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"field1\":\"value1\",\"field2\":\"value2\"}");
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices?organization_id=10234695")
.post(body)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.addHeader("content-type", "application/json")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f',
    'content-type': 'application/json'
},
body: '{"field1":"value1","field2":"value2"}'
};
fetch('https://www.zohoapis.com/books/v3/invoices?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
payload = "{\"field1\":\"value1\",\"field2\":\"value2\"}"
headers = {
    'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    'content-type': "application/json"
    }
conn.request("POST", "/books/v3/invoices?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    "content-type": "application/json"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.write(JSON.stringify({field1: 'value1', field2: 'value2'}));
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "customer_id": 982000000567001,
    "currency_id": 982000000000190,
    "contact_persons": [\
        "982000000870911",\
        "982000000870915"\
    ],
    "invoice_number": "INV-00003",
    "place_of_supply": "TN",
    "vat_treatment": "string",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "gst_treatment": "business_gst",
    "gst_no": "22AAAAA0000A1Z5",
    "cfdi_usage": "acquisition_of_merchandise",
    "reference_number": " ",
    "template_id": 982000000000143,
    "date": "2013-11-17",
    "payment_terms": 15,
    "payment_terms_label": "Net 15",
    "due_date": "2013-12-03",
    "discount": 0,
    "is_discount_before_tax": true,
    "discount_type": "item_level",
    "is_inclusive_tax": false,
    "exchange_rate": 1,
    "recurring_invoice_id": " ",
    "invoiced_estimate_id": " ",
    "salesperson_name": " ",
    "custom_fields": [\
        {\
            "customfield_id": "46000000012845",\
            "value": "Normal"\
        }\
    ],
    "line_items": [\
        {\
            "item_id": 982000000030049,\
            "project_id": 90300000087378,\
            "time_entry_ids": [],\
            "product_type": "goods",\
            "hsn_or_sac": 80540,\
            "sat_item_key_code": 71121206,\
            "unitkey_code": "E48",\
            "warehouse_id": "",\
            "expense_id": " ",\
            "bill_id": " ",\
            "bill_item_id": " ",\
            "expense_receipt_name": "string",\
            "name": "Hard Drive",\
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",\
            "item_order": 1,\
            "bcy_rate": 120,\
            "rate": 120,\
            "quantity": 1,\
            "unit": " ",\
            "discount_amount": 0,\
            "discount": 0,\
            "tags": [\
                {\
                    "tag_id": 982000000009070,\
                    "tag_option_id": 982000000002670\
                }\
            ],\
            "tax_id": 982000000557028,\
            "tds_tax_id": "982000000557012",\
            "tax_name": "VAT",\
            "tax_type": "tax",\
            "tax_percentage": 12.5,\
            "tax_treatment_code": "uae_others",\
            "header_name": "Electronic devices",\
            "salesorder_item_id": " "\
        }\
    ],
    "payment_options": {
        "payment_gateways": [\
            {\
                "configured": true,\
                "additional_field1": "standard",\
                "gateway_name": "paypal"\
            }\
        ]
    },
    "allow_partial_payments": true,
    "custom_body": " ",
    "custom_subject": " ",
    "notes": "Looking forward for your business.",
    "terms": "Terms & Conditions apply",
    "shipping_charge": 0,
    "adjustment": 0,
    "adjustment_description": " ",
    "reason": " ",
    "tax_authority_id": 11149000000061052,
    "tax_exemption_id": 11149000000061054,
    "billing_address_id": "218500000000142012",
    "shipping_address_id": "218500000000142014",
    "avatax_use_code": "string",
    "avatax_exempt_no": "string",
    "tax_id": 982000000557028,
    "expense_id": " ",
    "salesorder_item_id": " ",
    "avatax_tax_code": "string",
    "time_entry_ids": []
}`

Response Example

`{
    "code": 0,
    "message": "The invoice has been created.",
    "invoice": {
        "invoice_id": 982000000567114,
        "ach_payment_initiated": false,
        "invoice_number": "INV-00003",
        "is_pre_gst": true,
        "place_of_supply": "TN",
        "gst_no": "22AAAAA0000A1Z5",
        "gst_treatment": "business_gst",
        "cfdi_usage": "acquisition_of_merchandise",
        "cfdi_reference_type": "return_of_merchandise",
        "reference_invoice_id": "132738000000126013",
        "vat_treatment": "string",
        "tax_treatment": "vat_registered",
        "is_reverse_charge_applied": true,
        "vat_reg_no": "string",
        "date": "2013-11-17",
        "status": "draft",
        "payment_terms": 15,
        "payment_terms_label": "Net 15",
        "due_date": "2013-12-03",
        "payment_expected_date": " ",
        "last_payment_date": " ",
        "reference_number": " ",
        "customer_id": 982000000567001,
        "customer_name": "Bowman & Co",
        "contact_persons": [\
            "982000000870911",\
            "982000000870915"\
        ],
        "currency_id": 982000000000190,
        "currency_code": "USD",
        "exchange_rate": 1,
        "discount": 0,
        "is_discount_before_tax": true,
        "discount_type": "item_level",
        "is_inclusive_tax": false,
        "recurring_invoice_id": " ",
        "is_viewed_by_client": false,
        "has_attachment": false,
        "client_viewed_time": "",
        "line_items": [\
            {\
                "line_item_id": 982000000567021,\
                "item_id": 982000000030049,\
                "project_id": 90300000087378,\
                "sat_item_key_code": 71121206,\
                "unitkey_code": "E48",\
                "project_name": "Sample Project",\
                "time_entry_ids": [],\
                "warehouses": [\
                    {\
                        "warehouse_id": "",\
                        "warehouse_name": "",\
                        "warehouse_stock_on_hand": ""\
                    }\
                ],\
                "item_type": "goods",\
                "product_type": "goods",\
                "expense_id": " ",\
                "expense_receipt_name": "string",\
                "name": "Hard Drive",\
                "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",\
                "item_order": 1,\
                "bcy_rate": 120,\
                "rate": 120,\
                "quantity": 1,\
                "unit": " ",\
                "discount_amount": 0,\
                "discount": 0,\
                "tags": [\
                    {\
                        "is_tag_mandatory": false,\
                        "tag_id": 982000000009070,\
                        "tag_name": "Location",\
                        "tag_option_id": 982000000002670,\
                        "tag_option_name": "USA"\
                    }\
                ],\
                "tax_id": 982000000557028,\
                "tds_tax_id": "982000000557012",\
                "tax_name": "VAT",\
                "tax_type": "tax",\
                "tax_percentage": 12.5,\
                "tax_treatment_code": "uae_others",\
                "item_total": 120,\
                "header_name": "Electronic devices",\
                "header_id": 982000000000670\
            }\
        ],
        "shipping_charge": 0,
        "adjustment": 0,
        "adjustment_description": " ",
        "sub_total": 10000,
        "tax_total": 22.6,
        "total": 10000,
        "taxes": [\
            {\
                "tax_name": "VAT",\
                "tax_amount": 19.13\
            }\
        ],
        "payment_reminder_enabled": true,
        "payment_made": 26.91,
        "credits_applied": 22.43,
        "tax_amount_withheld": 0,
        "balance": 40.6,
        "write_off_amount": 0,
        "allow_partial_payments": true,
        "price_precision": 2,
        "payment_options": {
            "payment_gateways": [\
                {\
                    "configured": true,\
                    "additional_field1": "standard",\
                    "gateway_name": "paypal"\
                }\
            ]
        },
        "is_emailed": false,
        "reminders_sent": 1,
        "last_reminder_sent_date": " ",
        "billing_address": {
            "address": "4900 Hopyard Rd, Suite 310",
            "street2": "McMillan Avenue",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600"
        },
        "shipping_address": {
            "address": "4900 Hopyard Rd, Suit 310",
            "street2": "McMillan Avenue",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 945881,
            "country": "USA",
            "fax": "+1-925-924-9600"
        },
        "notes": "Looking forward for your business.",
        "terms": "Terms & Conditions apply",
        "custom_fields": [\
            {\
                "customfield_id": "46000000012845",\
                "value": "Normal"\
            }\
        ],
        "template_id": 982000000000143,
        "template_name": "Service - Classic",
        "created_time": "2013-11-18T02:17:40-0800",
        "last_modified_time": "2013-11-18T02:02:51-0800",
        "attachment_name": " ",
        "can_send_in_mail": true,
        "salesperson_id": " ",
        "salesperson_name": " ",
        "invoice_url": "https://books.zoho.com/SecurePayment?CInvoiceID=23d84d0cf64f9a72ea0c66fded25a08c8bafd0ab508aff05323a9f80e2cd03fdc5dd568d3d6407bbda969d3e870d740b6fce549a9438c4ea"
    }
}`

## Update an invoice using a custom field's unique value

A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update an invoice by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding invoice will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing invoices, a new invoice will be created if the necessary payload details are available


`OAuth Scope : ZohoBooks.invoices.UPDATE`

### Arguments

customer\_id

string

(Required)


ID of the customer the invoice has to be created.

currency\_id

string

The currency id of the currency

contact\_persons

array

Array of contact person(s) for whom invoice has to be sent.

invoice\_number

string

Search invoices by invoice number.Variants: `invoice_number_startswith` and `invoice_number_contains`. Max-length \[100\]

place\_of\_supply

string

🇮🇳

India


,GCConly

Place where the goods/services are supplied to. (If not given, `place of contact` given for the contact will be taken)

Supported codes for UAE emirates are :

Abu Dhabi - `AB`,

Ajman - `AJ`,

Dubai - `DU`,

Fujairah - `FU`,

Ras al-Khaimah - `RA`,

Sharjah - `SH`,

Umm al-Quwain - `UM`

Supported codes for the GCC countries are :

United Arab Emirates - `AE`,

Saudi Arabia - `SA`,

Bahrain - `BH`,

Kuwait - `KW`,

Oman - `OM`,

Qatar - `QA`.

vat\_treatment

string

🇬🇧

United Kingdom


only

(Optional) VAT treatment for the invoices. VAT treatment denotes the location of the customer, if the customer resides in UK then the VAT treatment is `uk`. If the customer is in an EU country & VAT registered, you are resides in Northen Ireland and selling Goods then his VAT treatment is `eu_vat_registered`, if he resides outside of the UK then his VAT treatment is `overseas` (For Pre Brexit, this can be split as `eu_vat_registered`, `eu_vat_not_registered` and `non_eu`).

tax\_treatment

string

GCC,🇲🇽

Mexico


,🇰🇪

Kenya


,🇿🇦

South Africa


only

VAT treatment for the invoice .Choose whether the contact falls under: `vat_registered`, `vat_not_registered`, `gcc_vat_not_registered`, `gcc_vat_registered`, `non_gcc`.

`dz_vat_registered` and `dz_vat_not_registered` supported only for **UAE**.

`home_country_mexico`, `border_region_mexico`, `non_mexico` supported only for **MX**.

**For Kenya Edition:** `vat_registered` , `vat_not_registered` , `non_kenya`(A business that is located outside Kenya).

**For SouthAfrica Edition:** `vat_registered`, `vat_not_registered`, `overseas`(A business that is located outside SouthAfrica).

is\_reverse\_charge\_applied

boolean

🇿🇦

South Africa


only

(Required if customer tax treatment is `vat_registered`)

Used to specify whether the transaction is applicable for Domestic Reverse Charge (DRC) or not.

gst\_treatment

string

🇮🇳

India


only

Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are ` business_gst ` , ` business_none ` , ` overseas ` , ` consumer `.

cfdi\_usage

string

🇲🇽

Mexico


only

Choose CFDI Usage. Allowed values:

`acquisition_of_merchandise`, `return_discount_bonus`, `general_expense`, `buildings`, `furniture_office_equipment`, `transport_equipment`, `computer_equipmentdye_molds_tools`, `telephone_communication`, `satellite_communication`, `other_machinery_equipment`, `hospital_expense`, `medical_expense_disability`, `funeral_expense`, `donation`, `interest_mortage_loans`, `contribution_sar`, `medical_expense_insurance_pormium`, `school_transportation_expense`, `deposit_saving_account`, `payment_educational_service`, `no_tax_effect`, `payment`, `payroll`.

cfdi\_reference\_type

string

🇲🇽

Mexico


only

Choose CFDI Reference Type. Allowed values:

`return_of_merchandise`, `substitution_previous_cfdi`, `transfer_of_goods`, `invoice_generated_from_order`, `cfdi_for_advance`.

reference\_invoice\_id

string

🇲🇽

Mexico


only

Associate the reference invoice.

gst\_no

string

🇮🇳

India


only

15 digit GST identification number of the customer.

reference\_number

string

The reference number of the invoice

template\_id

string

ID of the pdf template associated with the invoice.

date

string

Search invoices by invoice date. Default date format is yyyy-mm-dd. ` Variants: date_start, date_end, date_before and date_after`.

payment\_terms

integer

Payment terms in days e.g. 15, 30, 60. Invoice due date will be calculated based on this. Max-length \[100\]

payment\_terms\_label

string

Used to override the default payment terms label. Default value for 15 days is "Net 15 Days". Max-length \[100\]

due\_date

string

Search invoices by due date. Default date format is yyyy-mm-dd. ` Variants: due_date_start, due_date_end, due_date_before and due_date_after `

discount

float

Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length \[100\]

is\_discount\_before\_tax

boolean

Used to specify how the discount has to applied. Either before or after the calculation of tax.

discount\_type

string

How the discount is specified. Allowed values: `entity_level` and `item_level`.

is\_inclusive\_tax

boolean

Used to specify whether the line item rates are inclusive or exclusivr of tax.

exchange\_rate

float

Exchange rate of the currency.

recurring\_invoice\_id

string

ID of the recurring invoice from which the invoice is created.

invoiced\_estimate\_id

string

ID of the invoice from which the invoice is created.

salesperson\_name

string

Name of the salesperson. Max-length \[200\]

custom\_fields

array

Custom fields for an invoice.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

customfield\_id

long

value

string

Value of the Custom Field

line\_items

array

(Required)


Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

item\_id

string

(Required)


Search invoices by item id.

project\_id

string

ID of the Project.

time\_entry\_ids

array

IDs of the time entries associated with the project.

product\_type

string

Enter `goods` or `services` .

**For SouthAfrica Edition:** `service`, `goods`, `capital_service` and `capital_goods`

hsn\_or\_sac

string

🇮🇳

India


,🇰🇪

Kenya


,🇿🇦

South Africa


only

Add HSN/SAC code for your goods/services

sat\_item\_key\_code

string

🇲🇽

Mexico


only

Add SAT Item Key Code for your goods/services. Download the [CFDI Catalogs.](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls)

unitkey\_code

string

🇲🇽

Mexico


only

Add SAT Unit Key Code for your goods/services. Download the [CFDI Catalogs.](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls)

warehouse\_id

string

Enter warehouse ID

expense\_id

string

Add billable expense id which needs to be convert to invoice

expense\_receipt\_name

string

name

string

The name of the line item. Max-length \[100\]

description

string

The description of the line items. Max-length \[2000\]

item\_order

integer

The order of the line item\_order

bcy\_rate

float

base currency rate

rate

double

Rate of the line item.

quantity

float

The quantity of line item

unit

string

Unit of the line item e.g. kgs, Nos. Max-length \[100\]

discount\_amount

float

The discount amount on the line item

tags

array

Filter all your reports based on the tag

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

tag\_id

string

ID of the reporting tag

tag\_option\_id

string

ID of the reporting tag's option

discount

float

Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length \[100\]

tax\_id

string

ID of the tax.

tds\_tax\_id

string

🇲🇽

Mexico


only

ID of the TDS tax.

tax\_name

string

The name of the tax

tax\_type

string

The type of the tax

tax\_percentage

float

The percentage of tax levied

tax\_treatment\_code

string

GCConly

Specify reason for using out of scope.

Supported values for UAE are `uae_same_tax_group`, `uae_reimbursed_expense` and `uae_others`.

Supported values for Bahrain are `bahrain_same_tax_group`, `bahrain_transfer_of_concern`, `bahrain_disbursement`, `bahrain_head_to_branch_transaction`, `bahrain_warranty_repair_services` and `bahrain_others`.

Supported values for Saudi Arabia are `ksa_pvt_health`, `ksa_pvt_edu`, `ksa_reimbursed_expense` and `ksa_house_sales`.

header\_name

string

Name of the item header

header\_id

string

ID of the item header

payment\_options

object

Payment options for the invoice, online payment gateways and bank accounts. Will be displayed in the pdf.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

payment\_gateways

array

Online payment gateways through which payment can be made.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

configured

boolean

Boolean check to see if a payment gateway has been configured

additional\_field1

string

Paypal payment method. Allowed Values: `standard` and `adaptive`

gateway\_name

string

Name of the payment gateway associated with the invoice. E.g. paypal, stripe.Allowed Values: `paypal`, `authorize_net`, `payflow_pro`, `stripe`, `2checkout` and `braintree`

allow\_partial\_payments

boolean

Boolean to check if partial payments are allowed for the contact

custom\_body

string

custom\_subject

string

notes

string

The notes added below expressing gratitude or for conveying some information.

terms

string

The terms added below expressing gratitude or for conveying some information.

shipping\_charge

string

Shipping charges applied to the invoice. Max-length \[100\]

adjustment

double

Adjustments made to the invoice.

adjustment\_description

string

Customize the adjustment description. E.g. Rounding off.

reason

string

tax\_authority\_id

string

🇺🇸

United States


only

ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority.

tax\_exemption\_id

string

🇮🇳

India


,🇺🇸

United States


only

ID of the tax exemption.

avatax\_use\_code

string

Avalara Integrationonly

Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara \[standard codes\]\[1\] or enter a custom code. Max-length \[25\]

avatax\_exempt\_no

string

Avalara Integrationonly

Exemption certificate number of the customer. Max-length \[25\]

tax\_id

string

ID of the tax.

expense\_id

string

Add billable expense id which needs to be convert to invoice

salesorder\_item\_id

string

ID of the sales order line item which is invoices.

avatax\_tax\_code

string

Avalara Integrationonly

A tax code is a unique label used to group Items (products, services, or charges) together. Refer the \[link\]\[2\] for more deails. Max-length \[25\]

line\_item\_id

string

The line item id

Request Example

undefined

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`parameters_data='{"field1":"value1","field2":"value2"}';
headers_data = Map();
headers_data.put("X-Unique-Identifier-Key", "cf_unique_cf");
headers_data.put("X-Unique-Identifier-Value", "unique Value");
headers_data.put("X-Upsert", "true");
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices?organization_id=10234695"\
type: PUT\
headers: headers_data\
content-type: application/json\
parameters: parameters_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"field1\":\"value1\",\"field2\":\"value2\"}");
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices?organization_id=10234695")
.put(body)
.addHeader("X-Unique-Identifier-Key", "cf_unique_cf")
.addHeader("X-Unique-Identifier-Value", "unique Value")
.addHeader("X-Upsert", "true")
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.addHeader("content-type", "application/json")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'PUT',
headers: {
    'X-Unique-Identifier-Key': 'cf_unique_cf',
    'X-Unique-Identifier-Value': 'unique Value',
    'X-Upsert': 'true',
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f',
    'content-type': 'application/json'
},
body: '{"field1":"value1","field2":"value2"}'
};
fetch('https://www.zohoapis.com/books/v3/invoices?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
payload = "{\"field1\":\"value1\",\"field2\":\"value2\"}"
headers = {
    'X-Unique-Identifier-Key': "cf_unique_cf",
    'X-Unique-Identifier-Value': "unique Value",
    'X-Upsert': "true",
    'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    'content-type': "application/json"
    }
conn.request("PUT", "/books/v3/invoices?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "PUT",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices?organization_id=10234695",
"headers": {
    "X-Unique-Identifier-Key": "cf_unique_cf",
    "X-Unique-Identifier-Value": "unique Value",
    "X-Upsert": "true",
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    "content-type": "application/json"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.write(JSON.stringify({field1: 'value1', field2: 'value2'}));
req.end();`

`curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/invoices?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "customer_id": 982000000567001,
    "currency_id": 982000000000190,
    "contact_persons": [\
        "982000000870911",\
        "982000000870915"\
    ],
    "invoice_number": "INV-00003",
    "place_of_supply": "TN",
    "vat_treatment": "string",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "gst_treatment": "business_gst",
    "cfdi_usage": "acquisition_of_merchandise",
    "cfdi_reference_type": "return_of_merchandise",
    "reference_invoice_id": "132738000000126013",
    "gst_no": "22AAAAA0000A1Z5",
    "reference_number": " ",
    "template_id": 982000000000143,
    "date": "2013-11-17",
    "payment_terms": 15,
    "payment_terms_label": "Net 15",
    "due_date": "2013-12-03",
    "discount": 0,
    "is_discount_before_tax": true,
    "discount_type": "item_level",
    "is_inclusive_tax": false,
    "exchange_rate": 1,
    "recurring_invoice_id": " ",
    "invoiced_estimate_id": " ",
    "salesperson_name": " ",
    "custom_fields": [\
        {\
            "customfield_id": "46000000012845",\
            "value": "Normal"\
        }\
    ],
    "line_items": [\
        {\
            "item_id": 982000000030049,\
            "project_id": 90300000087378,\
            "time_entry_ids": [],\
            "product_type": "goods",\
            "hsn_or_sac": 80540,\
            "sat_item_key_code": 71121206,\
            "unitkey_code": "E48",\
            "warehouse_id": "",\
            "expense_id": " ",\
            "expense_receipt_name": "string",\
            "name": "Hard Drive",\
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",\
            "item_order": 1,\
            "bcy_rate": 120,\
            "rate": 120,\
            "quantity": 1,\
            "unit": " ",\
            "discount_amount": 0,\
            "tags": [\
                {\
                    "tag_id": 982000000009070,\
                    "tag_option_id": 982000000002670\
                }\
            ],\
            "discount": 0,\
            "tax_id": 982000000557028,\
            "tds_tax_id": "982000000557012",\
            "tax_name": "VAT",\
            "tax_type": "tax",\
            "tax_percentage": 12.5,\
            "tax_treatment_code": "uae_others",\
            "header_name": "Electronic devices",\
            "header_id": 982000000000670\
        }\
    ],
    "payment_options": {
        "payment_gateways": [\
            {\
                "configured": true,\
                "additional_field1": "standard",\
                "gateway_name": "paypal"\
            }\
        ]
    },
    "allow_partial_payments": true,
    "custom_body": " ",
    "custom_subject": " ",
    "notes": "Looking forward for your business.",
    "terms": "Terms & Conditions apply",
    "shipping_charge": 0,
    "adjustment": 0,
    "adjustment_description": " ",
    "reason": " ",
    "tax_authority_id": 11149000000061052,
    "tax_exemption_id": 11149000000061054,
    "avatax_use_code": "string",
    "avatax_exempt_no": "string",
    "tax_id": 982000000557028,
    "expense_id": " ",
    "salesorder_item_id": " ",
    "avatax_tax_code": "string",
    "line_item_id": 982000000567021
}`

Response Example

`{
    "code": 0,
    "message": "Invoice information has been updated.",
    "invoice": {
        "invoice_id": 982000000567114,
        "ach_payment_initiated": false,
        "invoice_number": "INV-00003",
        "is_pre_gst": true,
        "place_of_supply": "TN",
        "gst_no": "22AAAAA0000A1Z5",
        "gst_treatment": "business_gst",
        "cfdi_usage": "acquisition_of_merchandise",
        "cfdi_reference_type": "return_of_merchandise",
        "reference_invoice_id": "132738000000126013",
        "vat_treatment": "string",
        "tax_treatment": "vat_registered",
        "is_reverse_charge_applied": true,
        "vat_reg_no": "string",
        "date": "2013-11-17",
        "status": "draft",
        "payment_terms": 15,
        "payment_terms_label": "Net 15",
        "due_date": "2013-12-03",
        "payment_expected_date": " ",
        "last_payment_date": " ",
        "reference_number": " ",
        "customer_id": 982000000567001,
        "customer_name": "Bowman & Co",
        "contact_persons": [\
            "982000000870911",\
            "982000000870915"\
        ],
        "currency_id": 982000000000190,
        "currency_code": "USD",
        "exchange_rate": 1,
        "discount": 0,
        "is_discount_before_tax": true,
        "discount_type": "item_level",
        "is_inclusive_tax": false,
        "recurring_invoice_id": " ",
        "is_viewed_by_client": false,
        "has_attachment": false,
        "client_viewed_time": "",
        "line_items": [\
            {\
                "line_item_id": 982000000567021,\
                "item_id": 982000000030049,\
                "project_id": 90300000087378,\
                "project_name": "Sample Project",\
                "time_entry_ids": [],\
                "warehouses": [\
                    {\
                        "warehouse_id": "",\
                        "warehouse_name": "",\
                        "warehouse_stock_on_hand": ""\
                    }\
                ],\
                "item_type": "goods",\
                "product_type": "goods",\
                "sat_item_key_code": 71121206,\
                "unitkey_code": "E48",\
                "expense_id": " ",\
                "expense_receipt_name": "string",\
                "name": "Hard Drive",\
                "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",\
                "item_order": 1,\
                "bcy_rate": 120,\
                "rate": 120,\
                "quantity": 1,\
                "unit": " ",\
                "discount_amount": 0,\
                "discount": 0,\
                "tags": [\
                    {\
                        "is_tag_mandatory": false,\
                        "tag_id": 982000000009070,\
                        "tag_name": "Location",\
                        "tag_option_id": 982000000002670,\
                        "tag_option_name": "USA"\
                    }\
                ],\
                "tax_id": 982000000557028,\
                "tds_tax_id": "982000000557012",\
                "tax_name": "VAT",\
                "tax_type": "tax",\
                "tax_percentage": 12.5,\
                "tax_treatment_code": "uae_others",\
                "item_total": 120,\
                "header_name": "Electronic devices",\
                "header_id": 982000000000670\
            }\
        ],
        "shipping_charge": 0,
        "adjustment": 0,
        "adjustment_description": " ",
        "sub_total": 10000,
        "tax_total": 22.6,
        "total": 10000,
        "taxes": [\
            {\
                "tax_name": "VAT",\
                "tax_amount": 19.13\
            }\
        ],
        "payment_reminder_enabled": true,
        "payment_made": 26.91,
        "credits_applied": 22.43,
        "tax_amount_withheld": 0,
        "balance": 40.6,
        "write_off_amount": 0,
        "allow_partial_payments": true,
        "price_precision": 2,
        "payment_options": {
            "payment_gateways": [\
                {\
                    "configured": true,\
                    "additional_field1": "standard",\
                    "gateway_name": "paypal"\
                }\
            ]
        },
        "is_emailed": false,
        "reminders_sent": 1,
        "last_reminder_sent_date": " ",
        "billing_address": {
            "address": "4900 Hopyard Rd, Suite 310",
            "street2": "McMillan Avenue",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600"
        },
        "shipping_address": {
            "address": "4900 Hopyard Rd, Suite 310",
            "street2": "McMillan Avenue",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600"
        },
        "notes": "Looking forward for your business.",
        "terms": "Terms & Conditions apply",
        "custom_fields": [\
            {\
                "customfield_id": "46000000012845",\
                "value": "Normal"\
            }\
        ],
        "template_id": 982000000000143,
        "template_name": "Service - Classic",
        "created_time": "2013-11-18T02:17:40-0800",
        "last_modified_time": "2013-11-18T02:02:51-0800",
        "attachment_name": " ",
        "can_send_in_mail": true,
        "salesperson_id": " ",
        "salesperson_name": " ",
        "invoice_url": "https://books.zoho.com/SecurePayment?CInvoiceID=23d84d0cf64f9a72ea0c66fded25a08c8bafd0ab508aff05323a9f80e2cd03fdc5dd568d3d6407bbda969d3e870d740b6fce549a9438c4ea"
    }
}`

## List invoices

List all invoices with pagination.


`OAuth Scope : ZohoBooks.invoices.READ`

### Query Parameters

invoice\_number

Search invoices by invoice number.Variants: `invoice_number_startswith` and `invoice_number_contains`. Max-length \[100\]

item\_name

Search invoices by item name.Variants: `item_name_startswith` and `item_name_contains`. Max-length \[100\]

item\_id

Search invoices by item id.

item\_description

Search invoices by item description.Variants: `item_description_startswith` and `item_description_contains`. Max-length \[100\]

reference\_number

The reference number of the invoice

customer\_name

The name of the customer. Max-length \[100\]

recurring\_invoice\_id

ID of the recurring invoice from which the invoice is created.

email

Search contacts by email id. Max-length \[100\]

total

The total amount to be paid

balance

The unpaid amount

custom\_field

Search invoices by custom fields.Variants: `custom_field_startswith` and `custom_field_contains`

date

Search invoices by invoice date. Default date format is yyyy-mm-dd. ` Variants: date_start, date_end, date_before and date_after`.

due\_date

Search invoices by due date. Default date format is yyyy-mm-dd. ` Variants: due_date_start, due_date_end, due_date_before and due_date_after `

last\_modified\_time

This filters invoices generated after the last\_modified\_time that is greater than the specified param value. Allowed format `YYYY-MM-DDTHH:MM:SS-UTC` Eg: `2018-11-18T02:02:51-0800`, `2018-11-18T02:02:51+0530`. Pass the valid UTC time of your time zone for the last 4 digits of the last\_modified\_time.

status

Search invoices by invoice status.Allowed Values: `sent`, `draft`, `overdue`, `paid`, `void`, `unpaid`, `partially_paid` and `viewed`

customer\_id

ID of the customer the invoice has to be created.

filter\_by

Filter invoices by any status or payment expected date.Allowed Values: ` Status.All`, `Status.Sent`, ` Status.Draft`, `Status.OverDue`, `Status.Paid`, `Status.Void`, `Status.Unpaid`, `Status.PartiallyPaid`, ` Status.Viewed` and `Date.PaymentExpectedDate`

search\_text

Search invoices by invoice number or purchase order or customer name. Max-length \[100\]

sort\_column

Sort invoices.Allowed Values: `customer_name`, `invoice_number`, `date`, ` due_date`, `total`, `balance` and `created_time`

zcrm\_potential\_id

Potential ID of a Deal in CRM.

response\_option

To get desired response format. There are 5 formats of responses: 0 (Includes all invoices), 1 (Includes all invoices, the number of invoices, and the sum of their total and balance amounts), 2 (Includes only the number of invoices), 3 (Includes the number of invoices and the sum of their total and balance amounts), and 4 (Includes all invoices and the sum of their total and balance amounts).

Request Example

undefined

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices?organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices?organization_id=10234695")
.get()
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'GET',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/invoices?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "invoices": [\
        {\
            "invoice_id": 982000000567114,\
            "ach_payment_initiated": false,\
            "customer_name": "Bowman & Co",\
            "customer_id": 982000000567001,\
            "status": "draft",\
            "invoice_number": "INV-00003",\
            "reference_number": " ",\
            "date": "2013-11-17",\
            "due_date": "2013-12-03",\
            "due_days": "Due in 14 day(s)",\
            "currency_id": 982000000000190,\
            "schedule_time": "",\
            "currency_code": "USD",\
            "is_viewed_by_client": false,\
            "has_attachment": false,\
            "client_viewed_time": "",\
            "total": 10000,\
            "balance": 40.6,\
            "created_time": "2013-11-18T02:17:40-0800",\
            "last_modified_time": "2013-11-18T02:02:51-0800",\
            "is_emailed": false,\
            "reminders_sent": 1,\
            "last_reminder_sent_date": " ",\
            "payment_expected_date": " ",\
            "last_payment_date": " ",\
            "custom_fields": [\
                {\
                    "customfield_id": "46000000012845",\
                    "value": "Normal"\
                }\
            ],\
            "documents": "",\
            "salesperson_id": " ",\
            "salesperson_name": " ",\
            "shipping_charge": 0,\
            "adjustment": 0,\
            "write_off_amount": 0,\
            "exchange_rate": 1\
        },\
        {...},\
        {...}\
    ],
    "page_context": [\
        {\
            "page": 1,\
            "per_page": 200,\
            "has_more_page": false,\
            "report_name": "Invoices",\
            "applied_filter": "Status.All",\
            "sort_column": "created_time",\
            "sort_order": "D",\
            "response_option": 2\
        }\
    ]
}`

## Update an invoice

Update an existing invoice. To delete a line item just remove it from the line\_items list.


`OAuth Scope : ZohoBooks.invoices.UPDATE`

### Arguments

customer\_id

string

(Required)


ID of the customer the invoice has to be created.

currency\_id

string

The currency id of the currency

contact\_persons

array

Array of contact person(s) for whom invoice has to be sent.

invoice\_number

string

Search invoices by invoice number.Variants: `invoice_number_startswith` and `invoice_number_contains`. Max-length \[100\]

place\_of\_supply

string

🇮🇳

India


,GCConly

Place where the goods/services are supplied to. (If not given, `place of contact` given for the contact will be taken)

Supported codes for UAE emirates are :

Abu Dhabi - `AB`,

Ajman - `AJ`,

Dubai - `DU`,

Fujairah - `FU`,

Ras al-Khaimah - `RA`,

Sharjah - `SH`,

Umm al-Quwain - `UM`

Supported codes for the GCC countries are :

United Arab Emirates - `AE`,

Saudi Arabia - `SA`,

Bahrain - `BH`,

Kuwait - `KW`,

Oman - `OM`,

Qatar - `QA`.

vat\_treatment

string

🇬🇧

United Kingdom


only

(Optional) VAT treatment for the invoices. VAT treatment denotes the location of the customer, if the customer resides in UK then the VAT treatment is `uk`. If the customer is in an EU country & VAT registered, you are resides in Northen Ireland and selling Goods then his VAT treatment is `eu_vat_registered`, if he resides outside of the UK then his VAT treatment is `overseas` (For Pre Brexit, this can be split as `eu_vat_registered`, `eu_vat_not_registered` and `non_eu`).

tax\_treatment

string

GCC,🇲🇽

Mexico


,🇰🇪

Kenya


,🇿🇦

South Africa


only

VAT treatment for the invoice .Choose whether the contact falls under: `vat_registered`, `vat_not_registered`, `gcc_vat_not_registered`, `gcc_vat_registered`, `non_gcc`.

`dz_vat_registered` and `dz_vat_not_registered` supported only for **UAE**.

`home_country_mexico`, `border_region_mexico`, `non_mexico` supported only for **MX**.

**For Kenya Edition:** `vat_registered` , `vat_not_registered` , `non_kenya`(A business that is located outside Kenya).

**For SouthAfrica Edition:** `vat_registered`, `vat_not_registered`, `overseas`(A business that is located outside SouthAfrica).

is\_reverse\_charge\_applied

boolean

🇿🇦

South Africa


only

(Required if customer tax treatment is `vat_registered`)

Used to specify whether the transaction is applicable for Domestic Reverse Charge (DRC) or not.

gst\_treatment

string

🇮🇳

India


only

Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are ` business_gst ` , ` business_none ` , ` overseas ` , ` consumer `.

cfdi\_usage

string

🇲🇽

Mexico


only

Choose CFDI Usage. Allowed values:

`acquisition_of_merchandise`, `return_discount_bonus`, `general_expense`, `buildings`, `furniture_office_equipment`, `transport_equipment`, `computer_equipmentdye_molds_tools`, `telephone_communication`, `satellite_communication`, `other_machinery_equipment`, `hospital_expense`, `medical_expense_disability`, `funeral_expense`, `donation`, `interest_mortage_loans`, `contribution_sar`, `medical_expense_insurance_pormium`, `school_transportation_expense`, `deposit_saving_account`, `payment_educational_service`, `no_tax_effect`, `payment`, `payroll`.

cfdi\_reference\_type

string

🇲🇽

Mexico


only

Choose CFDI Reference Type. Allowed values:

`return_of_merchandise`, `substitution_previous_cfdi`, `transfer_of_goods`, `invoice_generated_from_order`, `cfdi_for_advance`.

reference\_invoice\_id

string

🇲🇽

Mexico


only

Associate the reference invoice.

gst\_no

string

🇮🇳

India


only

15 digit GST identification number of the customer.

reference\_number

string

The reference number of the invoice

template\_id

string

ID of the pdf template associated with the invoice.

date

string

Search invoices by invoice date. Default date format is yyyy-mm-dd. ` Variants: date_start, date_end, date_before and date_after`.

payment\_terms

integer

Payment terms in days e.g. 15, 30, 60. Invoice due date will be calculated based on this. Max-length \[100\]

payment\_terms\_label

string

Used to override the default payment terms label. Default value for 15 days is "Net 15 Days". Max-length \[100\]

due\_date

string

Search invoices by due date. Default date format is yyyy-mm-dd. ` Variants: due_date_start, due_date_end, due_date_before and due_date_after `

discount

float

Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length \[100\]

is\_discount\_before\_tax

boolean

Used to specify how the discount has to applied. Either before or after the calculation of tax.

discount\_type

string

How the discount is specified. Allowed values: `entity_level` and `item_level`.

is\_inclusive\_tax

boolean

Used to specify whether the line item rates are inclusive or exclusivr of tax.

exchange\_rate

float

Exchange rate of the currency.

recurring\_invoice\_id

string

ID of the recurring invoice from which the invoice is created.

invoiced\_estimate\_id

string

ID of the invoice from which the invoice is created.

salesperson\_name

string

Name of the salesperson. Max-length \[200\]

custom\_fields

array

Custom fields for an invoice.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

customfield\_id

long

value

string

Value of the Custom Field

line\_items

array

(Required)


Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

item\_id

string

(Required)


Search invoices by item id.

project\_id

string

ID of the Project.

time\_entry\_ids

array

IDs of the time entries associated with the project.

product\_type

string

Enter `goods` or `services` .

**For SouthAfrica Edition:** `service`, `goods`, `capital_service` and `capital_goods`

hsn\_or\_sac

string

🇮🇳

India


,🇰🇪

Kenya


,🇿🇦

South Africa


only

Add HSN/SAC code for your goods/services

sat\_item\_key\_code

string

🇲🇽

Mexico


only

Add SAT Item Key Code for your goods/services. Download the [CFDI Catalogs.](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls)

unitkey\_code

string

🇲🇽

Mexico


only

Add SAT Unit Key Code for your goods/services. Download the [CFDI Catalogs.](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls)

warehouse\_id

string

Enter warehouse ID

expense\_id

string

Add billable expense id which needs to be convert to invoice

expense\_receipt\_name

string

name

string

The name of the line item. Max-length \[100\]

description

string

The description of the line items. Max-length \[2000\]

item\_order

integer

The order of the line item\_order

bcy\_rate

float

base currency rate

rate

double

Rate of the line item.

quantity

float

The quantity of line item

unit

string

Unit of the line item e.g. kgs, Nos. Max-length \[100\]

discount\_amount

float

The discount amount on the line item

tags

array

Filter all your reports based on the tag

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

tag\_id

string

ID of the reporting tag

tag\_option\_id

string

ID of the reporting tag's option

discount

float

Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length \[100\]

tax\_id

string

ID of the tax.

tds\_tax\_id

string

🇲🇽

Mexico


only

ID of the TDS tax.

tax\_name

string

The name of the tax

tax\_type

string

The type of the tax

tax\_percentage

float

The percentage of tax levied

tax\_treatment\_code

string

GCConly

Specify reason for using out of scope.

Supported values for UAE are `uae_same_tax_group`, `uae_reimbursed_expense` and `uae_others`.

Supported values for Bahrain are `bahrain_same_tax_group`, `bahrain_transfer_of_concern`, `bahrain_disbursement`, `bahrain_head_to_branch_transaction`, `bahrain_warranty_repair_services` and `bahrain_others`.

Supported values for Saudi Arabia are `ksa_pvt_health`, `ksa_pvt_edu`, `ksa_reimbursed_expense` and `ksa_house_sales`.

header\_name

string

Name of the item header

header\_id

string

ID of the item header

payment\_options

object

Payment options for the invoice, online payment gateways and bank accounts. Will be displayed in the pdf.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

payment\_gateways

array

Online payment gateways through which payment can be made.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

configured

boolean

Boolean check to see if a payment gateway has been configured

additional\_field1

string

Paypal payment method. Allowed Values: `standard` and `adaptive`

gateway\_name

string

Name of the payment gateway associated with the invoice. E.g. paypal, stripe.Allowed Values: `paypal`, `authorize_net`, `payflow_pro`, `stripe`, `2checkout` and `braintree`

allow\_partial\_payments

boolean

Boolean to check if partial payments are allowed for the contact

custom\_body

string

custom\_subject

string

notes

string

The notes added below expressing gratitude or for conveying some information.

terms

string

The terms added below expressing gratitude or for conveying some information.

shipping\_charge

string

Shipping charges applied to the invoice. Max-length \[100\]

adjustment

double

Adjustments made to the invoice.

adjustment\_description

string

Customize the adjustment description. E.g. Rounding off.

reason

string

tax\_authority\_id

string

🇺🇸

United States


only

ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority.

tax\_exemption\_id

string

🇮🇳

India


,🇺🇸

United States


only

ID of the tax exemption.

avatax\_use\_code

string

Avalara Integrationonly

Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara \[standard codes\]\[1\] or enter a custom code. Max-length \[25\]

avatax\_exempt\_no

string

Avalara Integrationonly

Exemption certificate number of the customer. Max-length \[25\]

tax\_id

string

ID of the tax.

expense\_id

string

Add billable expense id which needs to be convert to invoice

salesorder\_item\_id

string

ID of the sales order line item which is invoices.

avatax\_tax\_code

string

Avalara Integrationonly

A tax code is a unique label used to group Items (products, services, or charges) together. Refer the \[link\]\[2\] for more deails. Max-length \[25\]

line\_item\_id

string

The line item id

### Query Parameters

ignore\_auto\_number\_generation

Ignore auto invoice number generation for this invoice. This mandates the invoice number. Allowed values `true` and `false`

Request Example

undefined

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`parameters_data='{"field1":"value1","field2":"value2"}';
headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114?organization_id=10234695"\
type: PUT\
headers: headers_data\
content-type: application/json\
parameters: parameters_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"field1\":\"value1\",\"field2\":\"value2\"}");
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114?organization_id=10234695")
.put(body)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.addHeader("content-type", "application/json")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'PUT',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f',
    'content-type': 'application/json'
},
body: '{"field1":"value1","field2":"value2"}'
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
payload = "{\"field1\":\"value1\",\"field2\":\"value2\"}"
headers = {
    'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    'content-type': "application/json"
    }
conn.request("PUT", "/books/v3/invoices/982000000567114?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "PUT",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    "content-type": "application/json"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.write(JSON.stringify({field1: 'value1', field2: 'value2'}));
req.end();`

`curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "customer_id": 982000000567001,
    "currency_id": 982000000000190,
    "contact_persons": [\
        "982000000870911",\
        "982000000870915"\
    ],
    "invoice_number": "INV-00003",
    "place_of_supply": "TN",
    "vat_treatment": "string",
    "tax_treatment": "vat_registered",
    "is_reverse_charge_applied": true,
    "gst_treatment": "business_gst",
    "cfdi_usage": "acquisition_of_merchandise",
    "cfdi_reference_type": "return_of_merchandise",
    "reference_invoice_id": "132738000000126013",
    "gst_no": "22AAAAA0000A1Z5",
    "reference_number": " ",
    "template_id": 982000000000143,
    "date": "2013-11-17",
    "payment_terms": 15,
    "payment_terms_label": "Net 15",
    "due_date": "2013-12-03",
    "discount": 0,
    "is_discount_before_tax": true,
    "discount_type": "item_level",
    "is_inclusive_tax": false,
    "exchange_rate": 1,
    "recurring_invoice_id": " ",
    "invoiced_estimate_id": " ",
    "salesperson_name": " ",
    "custom_fields": [\
        {\
            "customfield_id": "46000000012845",\
            "value": "Normal"\
        }\
    ],
    "line_items": [\
        {\
            "item_id": 982000000030049,\
            "project_id": 90300000087378,\
            "time_entry_ids": [],\
            "product_type": "goods",\
            "hsn_or_sac": 80540,\
            "sat_item_key_code": 71121206,\
            "unitkey_code": "E48",\
            "warehouse_id": "",\
            "expense_id": " ",\
            "expense_receipt_name": "string",\
            "name": "Hard Drive",\
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",\
            "item_order": 1,\
            "bcy_rate": 120,\
            "rate": 120,\
            "quantity": 1,\
            "unit": " ",\
            "discount_amount": 0,\
            "tags": [\
                {\
                    "tag_id": 982000000009070,\
                    "tag_option_id": 982000000002670\
                }\
            ],\
            "discount": 0,\
            "tax_id": 982000000557028,\
            "tds_tax_id": "982000000557012",\
            "tax_name": "VAT",\
            "tax_type": "tax",\
            "tax_percentage": 12.5,\
            "tax_treatment_code": "uae_others",\
            "header_name": "Electronic devices",\
            "header_id": 982000000000670\
        }\
    ],
    "payment_options": {
        "payment_gateways": [\
            {\
                "configured": true,\
                "additional_field1": "standard",\
                "gateway_name": "paypal"\
            }\
        ]
    },
    "allow_partial_payments": true,
    "custom_body": " ",
    "custom_subject": " ",
    "notes": "Looking forward for your business.",
    "terms": "Terms & Conditions apply",
    "shipping_charge": 0,
    "adjustment": 0,
    "adjustment_description": " ",
    "reason": " ",
    "tax_authority_id": 11149000000061052,
    "tax_exemption_id": 11149000000061054,
    "avatax_use_code": "string",
    "avatax_exempt_no": "string",
    "tax_id": 982000000557028,
    "expense_id": " ",
    "salesorder_item_id": " ",
    "avatax_tax_code": "string",
    "line_item_id": 982000000567021
}`

Response Example

`{
    "code": 0,
    "message": "Invoice information has been updated.",
    "invoice": {
        "invoice_id": 982000000567114,
        "ach_payment_initiated": false,
        "invoice_number": "INV-00003",
        "is_pre_gst": true,
        "place_of_supply": "TN",
        "gst_no": "22AAAAA0000A1Z5",
        "gst_treatment": "business_gst",
        "cfdi_usage": "acquisition_of_merchandise",
        "cfdi_reference_type": "return_of_merchandise",
        "reference_invoice_id": "132738000000126013",
        "vat_treatment": "string",
        "tax_treatment": "vat_registered",
        "is_reverse_charge_applied": true,
        "vat_reg_no": "string",
        "date": "2013-11-17",
        "status": "draft",
        "payment_terms": 15,
        "payment_terms_label": "Net 15",
        "due_date": "2013-12-03",
        "payment_expected_date": " ",
        "last_payment_date": " ",
        "reference_number": " ",
        "customer_id": 982000000567001,
        "customer_name": "Bowman & Co",
        "contact_persons": [\
            "982000000870911",\
            "982000000870915"\
        ],
        "currency_id": 982000000000190,
        "currency_code": "USD",
        "exchange_rate": 1,
        "discount": 0,
        "is_discount_before_tax": true,
        "discount_type": "item_level",
        "is_inclusive_tax": false,
        "recurring_invoice_id": " ",
        "is_viewed_by_client": false,
        "has_attachment": false,
        "client_viewed_time": "",
        "line_items": [\
            {\
                "line_item_id": 982000000567021,\
                "item_id": 982000000030049,\
                "project_id": 90300000087378,\
                "project_name": "Sample Project",\
                "time_entry_ids": [],\
                "warehouses": [\
                    {\
                        "warehouse_id": "",\
                        "warehouse_name": "",\
                        "warehouse_stock_on_hand": ""\
                    }\
                ],\
                "item_type": "goods",\
                "product_type": "goods",\
                "sat_item_key_code": 71121206,\
                "unitkey_code": "E48",\
                "expense_id": " ",\
                "expense_receipt_name": "string",\
                "name": "Hard Drive",\
                "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",\
                "item_order": 1,\
                "bcy_rate": 120,\
                "rate": 120,\
                "quantity": 1,\
                "unit": " ",\
                "discount_amount": 0,\
                "discount": 0,\
                "tags": [\
                    {\
                        "is_tag_mandatory": false,\
                        "tag_id": 982000000009070,\
                        "tag_name": "Location",\
                        "tag_option_id": 982000000002670,\
                        "tag_option_name": "USA"\
                    }\
                ],\
                "tax_id": 982000000557028,\
                "tds_tax_id": "982000000557012",\
                "tax_name": "VAT",\
                "tax_type": "tax",\
                "tax_percentage": 12.5,\
                "tax_treatment_code": "uae_others",\
                "item_total": 120,\
                "header_name": "Electronic devices",\
                "header_id": 982000000000670\
            }\
        ],
        "shipping_charge": 0,
        "adjustment": 0,
        "adjustment_description": " ",
        "sub_total": 10000,
        "tax_total": 22.6,
        "total": 10000,
        "taxes": [\
            {\
                "tax_name": "VAT",\
                "tax_amount": 19.13\
            }\
        ],
        "payment_reminder_enabled": true,
        "payment_made": 26.91,
        "credits_applied": 22.43,
        "tax_amount_withheld": 0,
        "balance": 40.6,
        "write_off_amount": 0,
        "allow_partial_payments": true,
        "price_precision": 2,
        "payment_options": {
            "payment_gateways": [\
                {\
                    "configured": true,\
                    "additional_field1": "standard",\
                    "gateway_name": "paypal"\
                }\
            ]
        },
        "is_emailed": false,
        "reminders_sent": 1,
        "last_reminder_sent_date": " ",
        "billing_address": {
            "address": "4900 Hopyard Rd, Suite 310",
            "street2": "McMillan Avenue",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600"
        },
        "shipping_address": {
            "address": "4900 Hopyard Rd, Suite 310",
            "street2": "McMillan Avenue",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600"
        },
        "notes": "Looking forward for your business.",
        "terms": "Terms & Conditions apply",
        "custom_fields": [\
            {\
                "customfield_id": "46000000012845",\
                "value": "Normal"\
            }\
        ],
        "template_id": 982000000000143,
        "template_name": "Service - Classic",
        "created_time": "2013-11-18T02:17:40-0800",
        "last_modified_time": "2013-11-18T02:02:51-0800",
        "attachment_name": " ",
        "can_send_in_mail": true,
        "salesperson_id": " ",
        "salesperson_name": " ",
        "invoice_url": "https://books.zoho.com/SecurePayment?CInvoiceID=23d84d0cf64f9a72ea0c66fded25a08c8bafd0ab508aff05323a9f80e2cd03fdc5dd568d3d6407bbda969d3e870d740b6fce549a9438c4ea"
    }
}`

## Get an invoice

Get the details of an invoice.


`OAuth Scope : ZohoBooks.invoices.READ`

### Query Parameters

print

Print the exported pdf.

accept

Get the details of a particular invoice in formats such as json/ pdf/ html. Default format is json. Allowed values `json` `pdf` and `html`

Request Example

undefined

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114?organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114?organization_id=10234695")
.get()
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'GET',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/invoices/982000000567114?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "invoice": {
        "invoice_id": 982000000567114,
        "ach_payment_initiated": false,
        "invoice_number": "INV-00003",
        "is_pre_gst": true,
        "place_of_supply": "TN",
        "gst_no": "22AAAAA0000A1Z5",
        "gst_treatment": "business_gst",
        "cfdi_usage": "acquisition_of_merchandise",
        "vat_treatment": "string",
        "tax_treatment": "vat_registered",
        "is_reverse_charge_applied": true,
        "vat_reg_no": "string",
        "date": "2013-11-17",
        "status": "draft",
        "payment_terms": 15,
        "payment_terms_label": "Net 15",
        "due_date": "2013-12-03",
        "payment_expected_date": " ",
        "last_payment_date": " ",
        "reference_number": " ",
        "customer_id": 982000000567001,
        "customer_name": "Bowman & Co",
        "contact_persons": [\
            "982000000870911",\
            "982000000870915"\
        ],
        "currency_id": 982000000000190,
        "currency_code": "USD",
        "exchange_rate": 1,
        "discount": 0,
        "is_discount_before_tax": true,
        "discount_type": "item_level",
        "is_inclusive_tax": false,
        "recurring_invoice_id": " ",
        "is_viewed_by_client": false,
        "has_attachment": false,
        "client_viewed_time": "",
        "line_items": [\
            {\
                "line_item_id": 982000000567021,\
                "item_id": 982000000030049,\
                "project_id": 90300000087378,\
                "project_name": "Sample Project",\
                "time_entry_ids": [],\
                "warehouses": [\
                    {\
                        "warehouse_id": "",\
                        "warehouse_name": "",\
                        "warehouse_stock_on_hand": ""\
                    }\
                ],\
                "item_type": "goods",\
                "product_type": "goods",\
                "expense_id": " ",\
                "expense_receipt_name": "string",\
                "name": "Hard Drive",\
                "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",\
                "item_order": 1,\
                "bcy_rate": 120,\
                "rate": 120,\
                "quantity": 1,\
                "unit": " ",\
                "discount_amount": 0,\
                "discount": 0,\
                "tags": [\
                    {\
                        "is_tag_mandatory": false,\
                        "tag_id": 982000000009070,\
                        "tag_name": "Location",\
                        "tag_option_id": 982000000002670,\
                        "tag_option_name": "USA"\
                    }\
                ],\
                "tax_id": 982000000557028,\
                "tax_name": "VAT",\
                "tax_type": "tax",\
                "tax_percentage": 12.5,\
                "tax_treatment_code": "uae_others",\
                "item_total": 120,\
                "header_name": "Electronic devices",\
                "header_id": 982000000000670\
            }\
        ],
        "shipping_charge": 0,
        "adjustment": 0,
        "adjustment_description": " ",
        "sub_total": 10000,
        "tax_total": 22.6,
        "total": 10000,
        "taxes": [\
            {\
                "tax_name": "VAT",\
                "tax_amount": 19.13\
            }\
        ],
        "payment_reminder_enabled": true,
        "payment_made": 26.91,
        "credits_applied": 22.43,
        "tax_amount_withheld": 0,
        "balance": 40.6,
        "write_off_amount": 0,
        "allow_partial_payments": true,
        "price_precision": 2,
        "payment_options": {
            "payment_gateways": [\
                {\
                    "configured": true,\
                    "additional_field1": "standard",\
                    "gateway_name": "paypal"\
                }\
            ]
        },
        "is_emailed": false,
        "reminders_sent": 1,
        "last_reminder_sent_date": " ",
        "billing_address": {
            "address": "4900 Hopyard Rd, Suite 310",
            "street2": "McMillan Avenue",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600"
        },
        "shipping_address": {
            "address": "4900 Hopyard Rd, Suite 310",
            "street2": "McMillan Avenue",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600"
        },
        "notes": "Looking forward for your business.",
        "terms": "Terms & Conditions apply",
        "custom_fields": [\
            {\
                "customfield_id": "46000000012845",\
                "value": "Normal"\
            }\
        ],
        "template_id": 982000000000143,
        "template_name": "Service - Classic",
        "created_time": "2013-11-18T02:17:40-0800",
        "last_modified_time": "2013-11-18T02:02:51-0800",
        "attachment_name": " ",
        "can_send_in_mail": true,
        "salesperson_id": " ",
        "salesperson_name": " ",
        "invoice_url": "https://books.zoho.com/SecurePayment?CInvoiceID=23d84d0cf64f9a72ea0c66fded25a08c8bafd0ab508aff05323a9f80e2cd03fdc5dd568d3d6407bbda969d3e870d740b6fce549a9438c4ea"
    }
}`

## Delete an invoice

Delete an existing invoice. Invoices which have payment or credits note applied cannot be deleted.


`OAuth Scope : ZohoBooks.invoices.DELETE`

Request Example

undefined

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114?organization_id=10234695"\
type: DELETE\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114?organization_id=10234695")
.delete(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'DELETE',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("DELETE", "/books/v3/invoices/982000000567114?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "DELETE",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "The invoice has been deleted."
}`

## Mark an invoice as sent

Mark a draft invoice as sent.


`OAuth Scope : ZohoBooks.invoices.CREATE`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/status/sent?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/status/sent?organization_id=10234695")
.post(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/status/sent?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/invoices/982000000567114/status/sent?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/status/sent?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/status/sent?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "Invoice status has been changed to Sent."
}`

## Void an invoice

Mark an invoice status as void. Upon voiding, the payments and credits associated with the invoices will be unassociated and will be under customer credits.


`OAuth Scope : ZohoBooks.invoices.CREATE`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/status/void?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/status/void?organization_id=10234695")
.post(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/status/void?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/invoices/982000000567114/status/void?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/status/void?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/status/void?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "Invoice status has been changed to Void."
}`

## Mark as draft

Mark a voided invoice as draft.


`OAuth Scope : ZohoBooks.invoices.CREATE`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/status/draft?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/status/draft?organization_id=10234695")
.post(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/status/draft?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/invoices/982000000567114/status/draft?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/status/draft?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/status/draft?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "Status of invoice changed from void to draft"
}`

## Email invoices

Send invoices to your customers by email. Maximum of 10 invoices can be sent at once.


`OAuth Scope : ZohoBooks.invoices.CREATE`

### Arguments

contacts

array

Contacts for whom email or snail mail has to be sent.

contact\_id

string

(Required)


ID of the contact. Can specify if email or snail mail has to be sent for each contact.

### Query Parameters

invoice\_ids

(Required)


Comma separated invoice ids which are to be emailed.

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`parameters_data='{"field1":"value1","field2":"value2"}';
headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/email?organization_id=10234695&invoice_ids="\
type: POST\
headers: headers_data\
content-type: application/json\
parameters: parameters_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"field1\":\"value1\",\"field2\":\"value2\"}");
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/email?organization_id=10234695&invoice_ids=")
.post(body)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.addHeader("content-type", "application/json")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f',
    'content-type': 'application/json'
},
body: '{"field1":"value1","field2":"value2"}'
};
fetch('https://www.zohoapis.com/books/v3/invoices/email?organization_id=10234695&invoice_ids=', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
payload = "{\"field1\":\"value1\",\"field2\":\"value2\"}"
headers = {
    'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    'content-type': "application/json"
    }
conn.request("POST", "/books/v3/invoices/email?organization_id=10234695&invoice_ids=", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/email?organization_id=10234695&invoice_ids=",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    "content-type": "application/json"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.write(JSON.stringify({field1: 'value1', field2: 'value2'}));
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/email?organization_id=10234695&invoice_ids=' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "contacts": [\
        "string"\
    ],
    "contact_id": 460000000026049
}`

Response Example

`{
    "code": 0,
    "message": "Mission accomplished! We've sent all the invoices."
}`

## Create an instant invoice

Create an instant invoice for all the confirmed sales orders you have selected.


`OAuth Scope : ZohoBooks.invoices.CREATE`

### Arguments

salesorder\_id

string

ID of the salesorder

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`parameters_data='{"field1":"value1","field2":"value2"}';
headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/fromsalesorder"\
type: POST\
headers: headers_data\
content-type: application/json\
parameters: parameters_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"field1\":\"value1\",\"field2\":\"value2\"}");
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/fromsalesorder")
.post(body)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.addHeader("content-type", "application/json")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f',
    'content-type': 'application/json'
},
body: '{"field1":"value1","field2":"value2"}'
};
fetch('https://www.zohoapis.com/books/v3/invoices/fromsalesorder', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
payload = "{\"field1\":\"value1\",\"field2\":\"value2\"}"
headers = {
    'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    'content-type': "application/json"
    }
conn.request("POST", "/books/v3/invoices/fromsalesorder", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/fromsalesorder",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    "content-type": "application/json"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.write(JSON.stringify({field1: 'value1', field2: 'value2'}));
req.end();`

`curl --request POST \
  --url https://www.zohoapis.com/books/v3/invoices/fromsalesorder \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "salesorder_id": "2000000014088",
    "organization_id": "10234694"
}`

Response Example

`{
    "code": 0,
    "message": "The invoice has been created.",
    "invoice": {
        "invoice_id": 982000000567114,
        "ach_payment_initiated": false,
        "invoice_number": "INV-00003",
        "is_pre_gst": true,
        "place_of_supply": "TN",
        "gst_no": "22AAAAA0000A1Z5",
        "gst_treatment": "business_gst",
        "cfdi_usage": "acquisition_of_merchandise",
        "cfdi_reference_type": "return_of_merchandise",
        "reference_invoice_id": "132738000000126013",
        "vat_treatment": "string",
        "tax_treatment": "vat_registered",
        "is_reverse_charge_applied": true,
        "vat_reg_no": "string",
        "date": "2013-11-17",
        "status": "draft",
        "payment_terms": 15,
        "payment_terms_label": "Net 15",
        "due_date": "2013-12-03",
        "payment_expected_date": " ",
        "last_payment_date": " ",
        "reference_number": " ",
        "customer_id": 982000000567001,
        "customer_name": "Bowman & Co",
        "contact_persons": [\
            "982000000870911",\
            "982000000870915"\
        ],
        "currency_id": 982000000000190,
        "currency_code": "USD",
        "exchange_rate": 1,
        "discount": 0,
        "is_discount_before_tax": true,
        "discount_type": "item_level",
        "is_inclusive_tax": false,
        "recurring_invoice_id": " ",
        "is_viewed_by_client": false,
        "has_attachment": false,
        "client_viewed_time": "",
        "line_items": [\
            {\
                "line_item_id": 982000000567021,\
                "item_id": 982000000030049,\
                "project_id": 90300000087378,\
                "sat_item_key_code": 71121206,\
                "unitkey_code": "E48",\
                "project_name": "Sample Project",\
                "time_entry_ids": [],\
                "warehouses": [\
                    {\
                        "warehouse_id": "",\
                        "warehouse_name": "",\
                        "warehouse_stock_on_hand": ""\
                    }\
                ],\
                "item_type": "goods",\
                "product_type": "goods",\
                "expense_id": " ",\
                "expense_receipt_name": "string",\
                "name": "Hard Drive",\
                "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",\
                "item_order": 1,\
                "bcy_rate": 120,\
                "rate": 120,\
                "quantity": 1,\
                "unit": " ",\
                "discount_amount": 0,\
                "discount": 0,\
                "tags": [\
                    {\
                        "is_tag_mandatory": false,\
                        "tag_id": 982000000009070,\
                        "tag_name": "Location",\
                        "tag_option_id": 982000000002670,\
                        "tag_option_name": "USA"\
                    }\
                ],\
                "tax_id": 982000000557028,\
                "tds_tax_id": "982000000557012",\
                "tax_name": "VAT",\
                "tax_type": "tax",\
                "tax_percentage": 12.5,\
                "tax_treatment_code": "uae_others",\
                "item_total": 120,\
                "header_name": "Electronic devices",\
                "header_id": 982000000000670\
            }\
        ],
        "shipping_charge": 0,
        "adjustment": 0,
        "adjustment_description": " ",
        "sub_total": 10000,
        "tax_total": 22.6,
        "total": 10000,
        "taxes": [\
            {\
                "tax_name": "VAT",\
                "tax_amount": 19.13\
            }\
        ],
        "payment_reminder_enabled": true,
        "payment_made": 26.91,
        "credits_applied": 22.43,
        "tax_amount_withheld": 0,
        "balance": 40.6,
        "write_off_amount": 0,
        "allow_partial_payments": true,
        "price_precision": 2,
        "payment_options": {
            "payment_gateways": [\
                {\
                    "configured": true,\
                    "additional_field1": "standard",\
                    "gateway_name": "paypal"\
                }\
            ]
        },
        "is_emailed": false,
        "reminders_sent": 1,
        "last_reminder_sent_date": " ",
        "billing_address": {
            "address": "4900 Hopyard Rd, Suite 310",
            "street2": "McMillan Avenue",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600"
        },
        "shipping_address": {
            "address": "4900 Hopyard Rd, Suit 310",
            "street2": "McMillan Avenue",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 945881,
            "country": "USA",
            "fax": "+1-925-924-9600"
        },
        "notes": "Looking forward for your business.",
        "terms": "Terms & Conditions apply",
        "custom_fields": [\
            {\
                "customfield_id": "46000000012845",\
                "value": "Normal"\
            }\
        ],
        "template_id": 982000000000143,
        "template_name": "Service - Classic",
        "created_time": "2013-11-18T02:17:40-0800",
        "last_modified_time": "2013-11-18T02:02:51-0800",
        "attachment_name": " ",
        "can_send_in_mail": true,
        "salesperson_id": " ",
        "salesperson_name": " ",
        "salesorder_id": 2000000021993,
        "salesorder_number": "SO-00001",
        "salesorders": {
            "salesorder_id": 2000000021993,
            "salesorder_number": "SO-00001",
            "reference_number": " ",
            "crm_custom_reference_id": "",
            "salesorder_order_status": "closed",
            "total": 10000,
            "total_formatted": "₹10,000.00",
            "sub_total": 10000,
            "sub_total_formatted": "₹10,000.00",
            "date": "2013-11-17",
            "shipment_date": ""
        },
        "invoice_url": "https://books.zoho.com/SecurePayment?CInvoiceID=23d84d0cf64f9a72ea0c66fded25a08c8bafd0ab508aff05323a9f80e2cd03fdc5dd568d3d6407bbda969d3e870d740b6fce549a9438c4ea"
    }
}`

## Submit an invoice for approval

Submit an invoice for approval.


`OAuth Scope : ZohoBooks.invoices.CREATE`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/submit?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/submit?organization_id=10234695")
.post(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/submit?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/invoices/982000000567114/submit?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/submit?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/submit?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "The invoice has been submitted for approval successfully."
}`

## Approve an invoice.

Approve an invoice.


`OAuth Scope : ZohoBooks.invoices.CREATE`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/approve?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/approve?organization_id=10234695")
.post(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/approve?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/invoices/982000000567114/approve?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/approve?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/approve?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "You have approved the invoice."
}`

## Email an invoice

Email an invoice to the customer. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content.


`OAuth Scope : ZohoBooks.invoices.CREATE`

### Arguments

send\_from\_org\_email\_id

boolean

Boolean to trigger the email from the organization's email address

to\_mail\_ids

array

(Required)


Array of email address of the recipients.

cc\_mail\_ids

array

Array of email address of the recipients to be cced.

subject

string

The subject of the mail

body

string

The body of the mail

### Query Parameters

send\_customer\_statement

Send customer statement pdf a with email.

send\_attachment

Send the invoice attachment a with the email.

attachments

Files to be attached to the email

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`parameters_data='{"field1":"value1","field2":"value2"}';
headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/email?organization_id=10234695"\
type: POST\
headers: headers_data\
content-type: application/json\
parameters: parameters_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"field1\":\"value1\",\"field2\":\"value2\"}");
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/email?organization_id=10234695")
.post(body)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.addHeader("content-type", "application/json")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f',
    'content-type': 'application/json'
},
body: '{"field1":"value1","field2":"value2"}'
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/email?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
payload = "{\"field1\":\"value1\",\"field2\":\"value2\"}"
headers = {
    'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    'content-type': "application/json"
    }
conn.request("POST", "/books/v3/invoices/982000000567114/email?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/email?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    "content-type": "application/json"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.write(JSON.stringify({field1: 'value1', field2: 'value2'}));
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/email?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "send_from_org_email_id": false,
    "to_mail_ids": [\
        "willsmith@bowmanfurniture.com"\
    ],
    "cc_mail_ids": [\
        "peterparker@bowmanfurniture.com"\
    ],
    "subject": "Invoice from Zillium Inc (Invoice#: INV-00001)",
    "body": "Dear Customer,         <br><br><br><br>Thanks for your business.         <br><br><br><br>The invoice INV-00001 is attached with this email. You can choose the easy way out and <a href= https://invoice.zoho.com/SecurePayment?CInvoiceID=b9800228e011ae86abe71227bdacb3c68e1af685f647dcaed747812e0b9314635e55ac6223925675b371fcbd2d5ae3dc  >pay online for this invoice.</a>         <br><br>Here's an overview of the invoice for your reference.         <br><br><br><br>Invoice Overview:         <br><br>Invoice  : INV-00001         <br><br>Date : 05 Aug 2013         <br><br>Amount : $541.82         <br><br><br><br>It was great working with you. Looking forward to working with you again.<br><br><br>\\nRegards<br>\\nZillium Inc<br>\\n\","
}`

Response Example

`{
    "code": 0,
    "message": "Your invoice has been sent."
}`

## Get invoice email content

Get the email content of an invoice.


`OAuth Scope : ZohoBooks.invoices.READ`

### Query Parameters

email\_template\_id

Get the email content based on a specific email template. If this param is not inputted, then the content will be based on the email template associated with the customer. If no template is associated with the customer, then default template will be used.

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/email?organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/email?organization_id=10234695")
.get()
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'GET',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/email?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/invoices/982000000567114/email?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/email?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/email?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "data": {
        "bcc_mails": [\
            "string"\
        ],
        "gateways_configured": true,
        "gateways_associated": true,
        "bcc_mails_str": "",
        "body": "Dear Customer,         <br><br><br><br>Thanks for your business.         <br><br><br><br>The invoice INV-00001 is attached with this email. You can choose the easy way out and <a href= https://invoice.zoho.com/SecurePayment?CInvoiceID=b9800228e011ae86abe71227bdacb3c68e1af685f647dcaed747812e0b9314635e55ac6223925675b371fcbd2d5ae3dc  >pay online for this invoice.</a>         <br><br>Here's an overview of the invoice for your reference.         <br><br><br><br>Invoice Overview:         <br><br>Invoice  : INV-00001         <br><br>Date : 05 Aug 2013         <br><br>Amount : $541.82         <br><br><br><br>It was great working with you. Looking forward to working with you again.<br><br><br>\\nRegards<br>\\nZillium Inc<br>\\n\",",
        "documents": "",
        "customer_name": "Bowman & Co",
        "attach_pdf": true,
        "entity_id": "2000000007037",
        "cc_mails_list": [\
            {\
                "user_name": "Sujin Kumar",\
                "email": null\
            }\
        ],
        "file_name_without_extension": "INV-000004",
        "to_mails_str": "",
        "cc_mails_str": "",
        "from_email": "",
        "from_address": "",
        "deprecated_placeholders_used": [],
        "error_list": [],
        "subject": "Invoice from Zillium Inc (Invoice#: INV-00001)",
        "emailtemplates": [\
            {\
                "selected": true,\
                "name": "Default",\
                "email_template_id": "982000000000067"\
            }\
        ],
        "emailtemplate_documents": [\
            "string"\
        ],
        "to_contacts": [\
            {\
                "first_name": "Sujin",\
                "selected": true,\
                "phone": "+1-925-921-9201",\
                "email": null,\
                "last_name": "Kumar",\
                "salutation": "Mr",\
                "contact_person_id": 982000000567003,\
                "mobile": "+1-4054439562"\
            }\
        ],
        "attachment_name": " ",
        "file_name": "INV-00001.pdf",
        "from_emails": [\
            {\
                "user_name": "Sujin Kumar",\
                "selected": true,\
                "email": null,\
                "organization_contact_id": "2000000002266",\
                "is_org_email_id": true\
            }\
        ],
        "customer_id": 982000000567001
    }
}`

## Remind Customer

Remind your customer about an unpaid invoice by email. Reminder will be sent, only for the invoices which are in open or overdue status.


`OAuth Scope : ZohoBooks.invoices.CREATE`

### Arguments

to\_mail\_ids

array

Array of email address of the recipients.

cc\_mail\_ids

array

(Required)


Array of email address of the recipients to be cced.

subject

string

The subject of the mail

body

string

The body of the mail

send\_from\_org\_email\_id

boolean

Boolean to trigger the email from the organization's email address

### Query Parameters

send\_customer\_statement

Send customer statement pdf a with email.

attachments

Files to be attached to the email

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`parameters_data='{"field1":"value1","field2":"value2"}';
headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder?organization_id=10234695"\
type: POST\
headers: headers_data\
content-type: application/json\
parameters: parameters_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"field1\":\"value1\",\"field2\":\"value2\"}");
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder?organization_id=10234695")
.post(body)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.addHeader("content-type", "application/json")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f',
    'content-type': 'application/json'
},
body: '{"field1":"value1","field2":"value2"}'
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
payload = "{\"field1\":\"value1\",\"field2\":\"value2\"}"
headers = {
    'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    'content-type': "application/json"
    }
conn.request("POST", "/books/v3/invoices/982000000567114/paymentreminder?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/paymentreminder?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    "content-type": "application/json"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.write(JSON.stringify({field1: 'value1', field2: 'value2'}));
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "to_mail_ids": [\
        "willsmith@bowmanfurniture.com"\
    ],
    "cc_mail_ids": [\
        "peterparker@bowmanfurniture.com"\
    ],
    "subject": "Invoice from Zillium Inc (Invoice#: INV-00001)",
    "body": "<br>Dear Mr. Sujin,&nbsp;<br><br>You might have missed the payment date and the invoice is now overdue by&nbsp;1&nbsp;days.<br><br>----------------------------------------------------------------------------------------<br><h2>Invoice# : INV-000004 </h2>Dated : 23 Dec 2016<br>----------------------------------------------------------------------------------------<br><b>&nbsp;Due Date &nbsp; &nbsp; &nbsp; &nbsp; : &nbsp;&nbsp;23 Dec 2016</b><br><b>&nbsp;Amount &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; : &nbsp;&nbsp;$139.65</b><br>----------------------------------------------------------------------------------------<br><br><span>Not to worry at all !&nbsp;</span>View your invoice and take the easy way out by making an&nbsp;<a href=\"https://books.zoho.com/portal/zilliuminc/index#/invoices/invoice/2000000007037 \">online payment</a>.<br><br>If you have already paid, please accept our apologies and kindly ignore this payment reminder.<br><br><br>Regards,<br><br>David Sujin<br>Zillium Inc<br><br><br>",
    "send_from_org_email_id": false
}`

Response Example

`{
    "code": 0,
    "message": "Your payment reminder has been sent."
}`

## Get payment reminder mail content

Get the mail content of the payment reminder.


`OAuth Scope : ZohoBooks.invoices.READ`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder?organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder?organization_id=10234695")
.get()
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'GET',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/invoices/982000000567114/paymentreminder?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/paymentreminder?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "data": {
        "bcc_mails": [\
            "string"\
        ],
        "gateways_configured": true,
        "gateways_associated": true,
        "bcc_mails_str": "",
        "body": "<br>Dear Mr. Sujin,&nbsp;<br><br>You might have missed the payment date and the invoice is now overdue by&nbsp;1&nbsp;days.<br><br>----------------------------------------------------------------------------------------<br><h2>Invoice# : INV-000004 </h2>Dated : 23 Dec 2016<br>----------------------------------------------------------------------------------------<br><b>&nbsp;Due Date &nbsp; &nbsp; &nbsp; &nbsp; : &nbsp;&nbsp;23 Dec 2016</b><br><b>&nbsp;Amount &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; : &nbsp;&nbsp;$139.65</b><br>----------------------------------------------------------------------------------------<br><br><span>Not to worry at all !&nbsp;</span>View your invoice and take the easy way out by making an&nbsp;<a href=\"https://books.zoho.com/portal/zilliuminc/index#/invoices/invoice/2000000007037 \">online payment</a>.<br><br>If you have already paid, please accept our apologies and kindly ignore this payment reminder.<br><br><br>Regards,<br><br>David Sujin<br>Zillium Inc<br><br><br>",
        "documents": "",
        "customer_name": "Bowman & Co",
        "attach_pdf": true,
        "entity_id": "2000000007037",
        "cc_mails_list": [\
            {\
                "user_name": "Sujin Kumar",\
                "email": null\
            }\
        ],
        "file_name_without_extension": "INV-000004",
        "to_mails_str": "",
        "cc_mails_str": "",
        "from_email": "",
        "from_address": "",
        "deprecated_placeholders_used": [],
        "error_list": [],
        "subject": "Invoice from Zillium Inc (Invoice#: INV-00001)",
        "emailtemplates": [\
            {\
                "selected": true,\
                "name": "Default",\
                "email_template_id": "982000000000067"\
            }\
        ],
        "emailtemplate_documents": [\
            "string"\
        ],
        "to_contacts": [\
            {\
                "first_name": "Sujin",\
                "selected": true,\
                "phone": "+1-925-921-9201",\
                "email": null,\
                "last_name": "Kumar",\
                "salutation": "Mr",\
                "contact_person_id": 982000000567003,\
                "mobile": "+1-4054439562"\
            }\
        ],
        "attachment_name": " ",
        "file_name": "INV-00001.pdf",
        "from_emails": [\
            {\
                "user_name": "Sujin Kumar",\
                "selected": true,\
                "email": null,\
                "organization_contact_id": "2000000002266",\
                "is_org_email_id": true\
            }\
        ],
        "customer_id": 982000000567001
    }
}`

## Bulk invoice reminder

Remind your customer about an unpaid invoices by email. Reminder mail will be send, only for the invoices is in open or overdue status. Maximum 10 invoices can be reminded at once.


`OAuth Scope : ZohoBooks.invoices.CREATE`

### Query Parameters

invoice\_ids

(Required)


Array of invoice ids for which the reminder has to be sent.

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/paymentreminder?organization_id=10234695&invoice_ids="\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/paymentreminder?organization_id=10234695&invoice_ids=")
.post(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/paymentreminder?organization_id=10234695&invoice_ids=', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/invoices/paymentreminder?organization_id=10234695&invoice_ids=", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/paymentreminder?organization_id=10234695&invoice_ids=",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/paymentreminder?organization_id=10234695&invoice_ids=' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "info": {
        "email_success_info": {
            "message": "The reminders were successfully sent",
            "sent_count": 2
        },
        "email_errors_info": [\
            {\
                "message": "The reminders were successfully sent",\
                "ids": "2000000007037"\
            }\
        ],
        "code": 4083
    }
}`

## Bulk export Invoices

Maximum of 25 invoices can be exported in a single pdf.


`OAuth Scope : ZohoBooks.invoices.READ`

### Query Parameters

invoice\_ids

(Required)


Comma separated invoice ids which are to be export as pdf.

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/pdf?organization_id=10234695&invoice_ids="\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/pdf?organization_id=10234695&invoice_ids=")
.get()
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'GET',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/pdf?organization_id=10234695&invoice_ids=', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/invoices/pdf?organization_id=10234695&invoice_ids=", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/pdf?organization_id=10234695&invoice_ids=",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/pdf?organization_id=10234695&invoice_ids=' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success"
}`

## Bulk print invoices

Export invoices as pdf and print them. Maximum of 25 invoices can be printed.


`OAuth Scope : ZohoBooks.invoices.READ`

### Query Parameters

invoice\_ids

(Required)


Export invoices as pdf and print them. Maximum of 25 invoices can be printed.

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/print?organization_id=10234695&invoice_ids="\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/print?organization_id=10234695&invoice_ids=")
.get()
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'GET',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/print?organization_id=10234695&invoice_ids=', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/invoices/print?organization_id=10234695&invoice_ids=", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/print?organization_id=10234695&invoice_ids=",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/print?organization_id=10234695&invoice_ids=' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success"
}`

## Disable payment reminder

Disable automated payment reminders for an invoice.


`OAuth Scope : ZohoBooks.invoices.CREATE`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder/disable?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder/disable?organization_id=10234695")
.post(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder/disable?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/invoices/982000000567114/paymentreminder/disable?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/paymentreminder/disable?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder/disable?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "Reminders stopped."
}`

## Enable payment reminder

Enable automated payment reminders for an invoice.


`OAuth Scope : ZohoBooks.invoices.CREATE`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder/enable?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder/enable?organization_id=10234695")
.post(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder/enable?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/invoices/982000000567114/paymentreminder/enable?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/paymentreminder/enable?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/paymentreminder/enable?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "Reminders enabled."
}`

## Write off invoice

Write off the invoice balance amount of an invoice.


`OAuth Scope : ZohoBooks.invoices.CREATE`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/writeoff?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/writeoff?organization_id=10234695")
.post(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/writeoff?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/invoices/982000000567114/writeoff?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/writeoff?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/writeoff?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "Invoice has been written off"
}`

## Cancel write off

Cancel the write off amount of an invoice.


`OAuth Scope : ZohoBooks.invoices.CREATE`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/writeoff/cancel?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/writeoff/cancel?organization_id=10234695")
.post(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/writeoff/cancel?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/invoices/982000000567114/writeoff/cancel?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/writeoff/cancel?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/writeoff/cancel?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "The write off done for this invoice has been cancelled."
}`

## Update billing address

Updates the billing address for this invoice alone.


`OAuth Scope : ZohoBooks.invoices.UPDATE`

### Arguments

address

string

Billing address for the invoice

city

string

City of the customer’s billing address.

state

string

State of the customer’s billing address.

zip

string

Zip code of the customer’s billing address.

country

string

Country of the customer’s billing address.

fax

string

Customer's fax number.

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`parameters_data='{"field1":"value1","field2":"value2"}';
headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/address/billing?organization_id=10234695"\
type: PUT\
headers: headers_data\
content-type: application/json\
parameters: parameters_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"field1\":\"value1\",\"field2\":\"value2\"}");
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/address/billing?organization_id=10234695")
.put(body)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.addHeader("content-type", "application/json")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'PUT',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f',
    'content-type': 'application/json'
},
body: '{"field1":"value1","field2":"value2"}'
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/address/billing?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
payload = "{\"field1\":\"value1\",\"field2\":\"value2\"}"
headers = {
    'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    'content-type': "application/json"
    }
conn.request("PUT", "/books/v3/invoices/982000000567114/address/billing?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "PUT",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/address/billing?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    "content-type": "application/json"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.write(JSON.stringify({field1: 'value1', field2: 'value2'}));
req.end();`

`curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/address/billing?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "address": "B-1104, 11F, \nHorizon International Tower, \nNo. 6, ZhiChun Road, HaiDian District",
    "city": "Beijing",
    "state": "Beijing",
    "zip": 1000881,
    "country": "string",
    "fax": "+86-10-82637827"
}`

Response Example

`{
    "code": 0,
    "message": "Billing address updated"
}`

## Update shipping address

Updates the shipping address for this invoice alone.


`OAuth Scope : ZohoBooks.invoices.UPDATE`

### Arguments

address

string

Shipping address for the invoice

street2

string

city

string

City of the customer’s Shipping address.

state

string

State of the customer’s Shipping address.

zip

string

Zip code of the customer’s Shipping address.

country

string

Country of the customer’s Shipping address.

fax

string

Customer's fax number.

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`parameters_data='{"field1":"value1","field2":"value2"}';
headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/address/shipping?organization_id=10234695"\
type: PUT\
headers: headers_data\
content-type: application/json\
parameters: parameters_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"field1\":\"value1\",\"field2\":\"value2\"}");
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/address/shipping?organization_id=10234695")
.put(body)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.addHeader("content-type", "application/json")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'PUT',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f',
    'content-type': 'application/json'
},
body: '{"field1":"value1","field2":"value2"}'
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/address/shipping?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
payload = "{\"field1\":\"value1\",\"field2\":\"value2\"}"
headers = {
    'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    'content-type': "application/json"
    }
conn.request("PUT", "/books/v3/invoices/982000000567114/address/shipping?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "PUT",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/address/shipping?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    "content-type": "application/json"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.write(JSON.stringify({field1: 'value1', field2: 'value2'}));
req.end();`

`curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/address/shipping?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "address": "4900 Hopyard Rd, Suit 310",
    "street2": "McMillan Avenue",
    "city": "Pleasanton",
    "state": "CA",
    "zip": 945881,
    "country": "USA",
    "fax": "+1-925-924-9600"
}`

Response Example

`{
    "code": 0,
    "message": "Shipping address updated"
}`

## List invoice templates

Get all invoice pdf templates.


`OAuth Scope : ZohoBooks.invoices.READ`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/templates?organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/templates?organization_id=10234695")
.get()
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'GET',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/templates?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/invoices/templates?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/templates?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/templates?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "templates": [\
        {\
            "template_name": "Service - Classic",\
            "template_id": 982000000000143,\
            "template_type": "classic"\
        },\
        {...},\
        {...}\
    ]
}`

## Update invoice template

Update the pdf template associated with the invoice.


`OAuth Scope : ZohoBooks.invoices.UPDATE`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/templates/982000000000143?organization_id=10234695"\
type: PUT\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/templates/982000000000143?organization_id=10234695")
.put(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'PUT',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/templates/982000000000143?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("PUT", "/books/v3/invoices/982000000567114/templates/982000000000143?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "PUT",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/templates/982000000000143?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/templates/982000000000143?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "Invoice information has been updated."
}`

## List invoice payments

Get the list of payments made for an invoice.


`OAuth Scope : ZohoBooks.invoices.READ`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/payments?organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/payments?organization_id=10234695")
.get()
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'GET',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/payments?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/invoices/982000000567114/payments?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/payments?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/payments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "payments": [\
        {\
            "payment_id": "982000000567190",\
            "payment_number": 7,\
            "invoice_id": 982000000567036,\
            "invoice_payment_id": 982000000567192,\
            "payment_mode": "cash",\
            "description": " ",\
            "date": "2013-11-18",\
            "reference_number": 99782374,\
            "exchange_rate": 1,\
            "amount": 10.57,\
            "tax_amount_withheld": 0,\
            "online_transaction_id": "",\
            "is_single_invoice_payment": true\
        },\
        {...},\
        {...}\
    ]
}`

## List credits applied

Get the list of credits applied for an invoice.


`OAuth Scope : ZohoBooks.invoices.READ`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/creditsapplied?organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/creditsapplied?organization_id=10234695")
.get()
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'GET',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/creditsapplied?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/invoices/982000000567114/creditsapplied?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/creditsapplied?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/creditsapplied?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "credits": [\
        {\
            "creditnote_id": 982000000567134,\
            "creditnotes_invoice_id": "982000000567172",\
            "creditnotes_number": "CN-00001",\
            "credited_date": "2013-11-18",\
            "amount_applied": 12.2\
        },\
        {...},\
        {...}\
    ]
}`

## Apply credits

Apply the customer credits either from credit notes or excess customer payments to an invoice. Multiple credits can be applied at once.


`OAuth Scope : ZohoBooks.invoices.CREATE`

### Arguments

invoice\_payments

array

(Required)


Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

payment\_id

string

ID of the payment

amount\_applied

float

The applied amount to the creditnote

apply\_creditnotes

array

(Required)


Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

creditnote\_id

string

ID of the creditnote

amount\_applied

float

The applied amount to the creditnote

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`parameters_data='{"field1":"value1","field2":"value2"}';
headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/credits?organization_id=10234695"\
type: POST\
headers: headers_data\
content-type: application/json\
parameters: parameters_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"field1\":\"value1\",\"field2\":\"value2\"}");
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/credits?organization_id=10234695")
.post(body)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.addHeader("content-type", "application/json")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f',
    'content-type': 'application/json'
},
body: '{"field1":"value1","field2":"value2"}'
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/credits?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
payload = "{\"field1\":\"value1\",\"field2\":\"value2\"}"
headers = {
    'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    'content-type': "application/json"
    }
conn.request("POST", "/books/v3/invoices/982000000567114/credits?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/credits?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    "content-type": "application/json"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.write(JSON.stringify({field1: 'value1', field2: 'value2'}));
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/credits?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "invoice_payments": [\
        {\
            "payment_id": 982000000567190,\
            "amount_applied": 12.2\
        }\
    ],
    "apply_creditnotes": [\
        {\
            "creditnote_id": 982000000567134,\
            "amount_applied": 12.2\
        }\
    ]
}`

Response Example

`{
    "code": 0,
    "message": "Credits have been applied to the invoice(s)."
}`

## Delete a payment

Delete a payment made to an invoice.


`OAuth Scope : ZohoBooks.invoices.DELETE`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/payments/982000000567192?organization_id=10234695"\
type: DELETE\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/payments/982000000567192?organization_id=10234695")
.delete(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'DELETE',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/payments/982000000567192?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("DELETE", "/books/v3/invoices/982000000567114/payments/982000000567192?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "DELETE",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/payments/982000000567192?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/payments/982000000567192?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "The payment has been deleted."
}`

## Delete applied credit

Delete a particular credit applied to an invoice.


`OAuth Scope : ZohoBooks.invoices.DELETE`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/creditsapplied/982000000567172?organization_id=10234695"\
type: DELETE\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/creditsapplied/982000000567172?organization_id=10234695")
.delete(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'DELETE',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/creditsapplied/982000000567172?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("DELETE", "/books/v3/invoices/982000000567114/creditsapplied/982000000567172?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "DELETE",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/creditsapplied/982000000567172?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/creditsapplied/982000000567172?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "Credits applied to an invoice have been deleted."
}`

## Add attachment to an invoice

Attach a file to an invoice.


`OAuth Scope : ZohoBooks.invoices.CREATE`

### Query Parameters

can\_send\_in\_mail

True to send the attachment with the invoice when emailed.

attachment

The file to be attached.Allowed Extensions: `gif`, `png`, `jpeg`, `jpg`, `bmp` and `pdf`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695")
.post(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/invoices/982000000567114/attachment?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/attachment?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "Your file has been successfully attached to the invoice."
}`

## Update attachment preference

Set whether you want to send the attached file while emailing the invoice.


`OAuth Scope : ZohoBooks.invoices.UPDATE`

### Query Parameters

can\_send\_in\_mail

(Required)


Boolean to send the attachment with the invoice when emailed.

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695&can_send_in_mail=true"\
type: PUT\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695&can_send_in_mail=true")
.put(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'PUT',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695&can_send_in_mail=true', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("PUT", "/books/v3/invoices/982000000567114/attachment?organization_id=10234695&can_send_in_mail=true", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "PUT",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/attachment?organization_id=10234695&can_send_in_mail=true",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695&can_send_in_mail=true' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "Invoice information has been updated."
}`

## Get an invoice attachment

Returns the file attached to the invoice.


`OAuth Scope : ZohoBooks.invoices.READ`

### Query Parameters

preview

Get the thumbnail of the attachment.

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695")
.get()
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'GET',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/invoices/982000000567114/attachment?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/attachment?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success"
}`

## Delete an attachment

Delete the file attached to the invoice.


`OAuth Scope : ZohoBooks.invoices.DELETE`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695"\
type: DELETE\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695")
.delete(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'DELETE',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("DELETE", "/books/v3/invoices/982000000567114/attachment?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "DELETE",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/attachment?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/attachment?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "Your file is no longer attached to the invoice."
}`

## Delete the expense receipt

Delete the expense receipts attached to an invoice which is raised from an expense.


`OAuth Scope : ZohoBooks.invoices.DELETE`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/expenses//receipt?organization_id=10234695"\
type: DELETE\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/expenses//receipt?organization_id=10234695")
.delete(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'DELETE',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/expenses//receipt?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("DELETE", "/books/v3/invoices/expenses//receipt?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "DELETE",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/expenses//receipt?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/invoices/expenses//receipt?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "The attached expense receipt has been deleted."
}`

## Update custom field in existing invoices

Update the value of the custom field in existing invoices.


`OAuth Scope : ZohoBooks.invoices.UPDATE`

### Arguments

customfield\_id

long

value

string

Value of the Custom Field

### Query Parameters

organization\_id

(Required)


ID of the organization

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`parameters_data='{"field1":"value1","field2":"value2"}';
headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoice/982000000567114/customfields?organization_id=10234695"\
type: PUT\
headers: headers_data\
content-type: application/json\
parameters: parameters_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"field1\":\"value1\",\"field2\":\"value2\"}");
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoice/982000000567114/customfields?organization_id=10234695")
.put(body)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.addHeader("content-type", "application/json")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'PUT',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f',
    'content-type': 'application/json'
},
body: '{"field1":"value1","field2":"value2"}'
};
fetch('https://www.zohoapis.com/books/v3/invoice/982000000567114/customfields?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
payload = "{\"field1\":\"value1\",\"field2\":\"value2\"}"
headers = {
    'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    'content-type': "application/json"
    }
conn.request("PUT", "/books/v3/invoice/982000000567114/customfields?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "PUT",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoice/982000000567114/customfields?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f",
    "content-type": "application/json"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.write(JSON.stringify({field1: 'value1', field2: 'value2'}));
req.end();`

`curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/invoice/982000000567114/customfields?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`[\
    {\
        "customfield_id": "46000000012845",\
        "value": "Normal"\
    }\
]`

Response Example

`{
    "code": 0,
    "message": "Custom Fields Updated Successfully"
}`

## Add comment

Add a comment for an invoice.


`OAuth Scope : ZohoBooks.invoices.CREATE`

### Query Parameters

description

payment\_expected\_date

show\_comment\_to\_clients

Boolean to check if the comment to be shown to the clients

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/comments?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/comments?organization_id=10234695")
.post(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'POST',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/comments?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/invoices/982000000567114/comments?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/comments?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request POST \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "Comments added."
}`

## List invoice comments & history

Get the complete history and comments of an invoice.


`OAuth Scope : ZohoBooks.invoices.READ`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/comments?organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/comments?organization_id=10234695")
.get()
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'GET',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/comments?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/invoices/982000000567114/comments?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/comments?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "comments": [\
        {\
            "comment_id": 982000000567019,\
            "invoice_id": 982000000567114,\
            "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",\
            "commented_by_id": 982000000554041,\
            "commented_by": "John David",\
            "comment_type": "system",\
            "operation_type": "Added",\
            "date": "2013-11-18",\
            "date_description": "yesterday",\
            "time": "2:38 AM",\
            "transaction_id": "982000000567204",\
            "transaction_type": "invoice"\
        },\
        {...},\
        {...}\
    ]
}`

## Update comment

Update an existing comment of an invoice.


`OAuth Scope : ZohoBooks.invoices.UPDATE`

### Query Parameters

description

The comment on a invoice

show\_comment\_to\_clients

Boolean to check if the comment to be shown to the clients

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/comments/982000000567019?organization_id=10234695"\
type: PUT\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/comments/982000000567019?organization_id=10234695")
.put(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'PUT',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/comments/982000000567019?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("PUT", "/books/v3/invoices/982000000567114/comments/982000000567019?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "PUT",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/comments/982000000567019?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request PUT \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/comments/982000000567019?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "comment": {
        "comment_id": 982000000567019,
        "invoice_id": 982000000567114,
        "description": "500GB, USB 2.0 interface 1400 rpm, protective hard case.",
        "commented_by_id": 982000000554041,
        "commented_by": "John David",
        "date": "2013-11-17",
        "date_description": "yesterday",
        "time": "2:02 AM",
        "comment_type": "system"
    }
}`

## Delete a comment

Delete an invoice comment.


`OAuth Scope : ZohoBooks.invoices.DELETE`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/invoices/982000000567114/comments/982000000567019?organization_id=10234695"\
type: DELETE\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/invoices/982000000567114/comments/982000000567019?organization_id=10234695")
.delete(null)
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'DELETE',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/invoices/982000000567114/comments/982000000567019?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("DELETE", "/books/v3/invoices/982000000567114/comments/982000000567019?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "DELETE",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/invoices/982000000567114/comments/982000000567019?organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request DELETE \
  --url 'https://www.zohoapis.com/books/v3/invoices/982000000567114/comments/982000000567019?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "The comment has been deleted."
}`

## Generate payment link

This API generates a payment link for the invoice with an expiry date.


`OAuth Scope : ZohoBooks.settings.ALL`

### Query Parameters

transaction\_id

(Required)


The ID of the transaction (Invoice ID).

transaction\_type

(Required)


The type of the transaction (Invoice).

link\_type

(Required)


The type of the link (Private or Public).

expiry\_time

(Required)


The expiry time of the payment link. Supported format : `yyyy-MM-dd`

Request Example

- cURL
- Deluge
- Java
- Node.js
- Javascript
- Python

Click to copy

`headers_data = Map();
headers_data.put("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f");
response = invokeUrl
[\
url: "https://www.zohoapis.com/books/v3/share/paymentlink?transaction_id=982000000567114&transaction_type=invoice&link_type=public&expiry_time=2024-06-27&organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/share/paymentlink?transaction_id=982000000567114&transaction_type=invoice&link_type=public&expiry_time=2024-06-27&organization_id=10234695")
.get()
.addHeader("Authorization", "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f")
.build();
Response response = client.newCall(request).execute();`

`const options = {
method: 'GET',
headers: {
    Authorization: 'Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'
}
};
fetch('https://www.zohoapis.com/books/v3/share/paymentlink?transaction_id=982000000567114&transaction_type=invoice&link_type=public&expiry_time=2024-06-27&organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/share/paymentlink?transaction_id=982000000567114&transaction_type=invoice&link_type=public&expiry_time=2024-06-27&organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/share/paymentlink?transaction_id=982000000567114&transaction_type=invoice&link_type=public&expiry_time=2024-06-27&organization_id=10234695",
"headers": {
    "Authorization": "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f"
}
};
const req = http.request(options, function (res) {
const chunks = [];
res.on("data", function (chunk) {
    chunks.push(chunk);
});
res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
});
});
req.end();`

`curl --request GET \
  --url 'https://www.zohoapis.com/books/v3/share/paymentlink?transaction_id=982000000567114&transaction_type=invoice&link_type=public&expiry_time=2024-06-27&organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "data": {
        "share_link": "https://zohosecurepay.com/books/Payment/secure?CInvoiceID=2-52411db153ee1f4a9ac8ab0dec95f4711f1edb75edc7d550dd3fcb6e100852aa25a28b345d8b67fc967d69ebdba5fc240fd51fd9007c6339e4015cb6e3eadfffa489615aa926242e "
    }
}`

