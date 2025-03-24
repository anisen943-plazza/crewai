# Contacts

The list of contacts created.

End Points


Create a Contact


[POST  \\
\\
\\
/contacts](https://www.zoho.com/books/api/v3/contacts/#create-a-contact)

Update a contact using a custom field's unique value


[PUT   \\
\\
\\
/contacts](https://www.zoho.com/books/api/v3/contacts/#update-a-contact-using-a-custom-fields-unique-value)

List Contacts


[GET   \\
\\
\\
/contacts](https://www.zoho.com/books/api/v3/contacts/#list-contacts)

Update a Contact


[PUT   \\
\\
\\
/contacts/{contact\_id}](https://www.zoho.com/books/api/v3/contacts/#update-a-contact)

Get Contact


[GET   \\
\\
\\
/contacts/{contact\_id}](https://www.zoho.com/books/api/v3/contacts/#get-contact)

Delete a Contact


[DELETE\\
\\
\\
/contacts/{contact\_id}](https://www.zoho.com/books/api/v3/contacts/#delete-a-contact)

Mark as Active


[POST  \\
\\
\\
/contacts/{contact\_id}/active](https://www.zoho.com/books/api/v3/contacts/#mark-as-active)

Mark as Inactive


[POST  \\
\\
\\
/contacts/{contact\_id}/inactive](https://www.zoho.com/books/api/v3/contacts/#mark-as-inactive)

Enable Portal Access


[POST  \\
\\
\\
/contacts/{contact\_id}/portal/enable](https://www.zoho.com/books/api/v3/contacts/#enable-portal-access)

Enable Payment Reminders


[POST  \\
\\
\\
/contacts/{contact\_id}/paymentreminder/enable](https://www.zoho.com/books/api/v3/contacts/#enable-payment-reminders)

Disable Payment Reminders


[POST  \\
\\
\\
/contacts/{contact\_id}/paymentreminder/disable](https://www.zoho.com/books/api/v3/contacts/#disable-payment-reminders)

Email Statement


[POST  \\
\\
\\
/contacts/{contact\_id}/statements/email](https://www.zoho.com/books/api/v3/contacts/#email-statement)

Get Statement Mail Content


[GET   \\
\\
\\
/contacts/{contact\_id}/statements/email](https://www.zoho.com/books/api/v3/contacts/#get-statement-mail-content)

Email Contact


[POST  \\
\\
\\
/contacts/{contact\_id}/email](https://www.zoho.com/books/api/v3/contacts/#email-contact)

List Comments


[GET   \\
\\
\\
/contacts/{contact\_id}/comments](https://www.zoho.com/books/api/v3/contacts/#list-comments)

Add Additional Address


[POST  \\
\\
\\
/contacts/{contact\_id}/address](https://www.zoho.com/books/api/v3/contacts/#add-additional-address)

Get Contact Addresses


[GET   \\
\\
\\
/contacts/{contact\_id}/address](https://www.zoho.com/books/api/v3/contacts/#get-contact-addresses)

Edit Additional Address


[PUT   \\
\\
\\
/contacts/{contact\_id}/address/{address\_id}](https://www.zoho.com/books/api/v3/contacts/#edit-additional-address)

Delete Additional Address


[DELETE\\
\\
\\
/contacts/{contact\_id}/address/{address\_id}](https://www.zoho.com/books/api/v3/contacts/#delete-additional-address)

List Refunds


[GET   \\
\\
\\
/contacts/{contact\_id}/refunds](https://www.zoho.com/books/api/v3/contacts/#list-refunds)

Track 1099


[POST  \\
\\
\\
/contacts/{contact\_id}/track1099](https://www.zoho.com/books/api/v3/contacts/#track-1099)

Untrack 1099


[POST  \\
\\
\\
/contacts/{contact\_id}/untrack1099](https://www.zoho.com/books/api/v3/contacts/#untrack-1099)

### Attribute

contact\_id

string

ID of the contact

contact\_name

string

Display Name of the contact. Max-length \[200\]

company\_name

string

Company Name of the contact. Max-length \[200\]

has\_transaction

boolean

unavailable

contact\_type

string

Contact type of the contact

customer\_sub\_type

string

Type of the customer

credit\_limit

double

Credit limit for a customer

is\_portal\_enabled

boolean

To enable client portal for the contact. Allowed value is `true` and `false`.

language\_code

string

language of a contact. allowed values `de,en,es,fr,it,ja,nl,pt,pt_br,sv,zh,en_gb`

is\_taxable

boolean

🇺🇸

United States


,🇨🇦

Canada


,🇦🇺

Australia


,🇮🇳

India


,🇲🇽

Mexico


,🇰🇪

Kenya


,🇿🇦

South Africa


only

Boolean to track the taxability of the customer.

tax\_id

string

🇮🇳

India


,🇺🇸

United States


only

ID of the tax or tax group that can be collected from the contact. Tax can be given only if `is_taxable` is `true`.

tds\_tax\_id

string

🇲🇽

Mexico


only

ID of the TDS tax.

tax\_name

string

🇮🇳

India


only

Enter tax name

tax\_percentage

double

Enter tax percentage.

tax\_authority\_id

string

🇺🇸

United States


only

ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority.

tax\_exemption\_id

string

🇺🇸

United States


,🇨🇦

Canada


,🇦🇺

Australia


,🇮🇳

India


only

ID of the tax exemption.

tax\_authority\_name

string

Enter tax authority name.

tax\_exemption\_code

string

🇺🇸

United States


,🇨🇦

Canada


,🇦🇺

Australia


,🇮🇳

India


only

Enter tax exemption code

place\_of\_contact

string

🇮🇳

India


only

Location of the contact. (This node identifies the place of supply and source of supply when invoices/bills are raised for the customer/vendor respectively. This is not applicable for Overseas contacts)

gst\_no

string

🇮🇳

India


only

15 digit GST identification number of the customer/vendor.

vat\_treatment

string

🇬🇧

United Kingdom


only

VAT treatment of the contact.Allowed Values:

`uk` (A business that is located in the UK.),

`eu_vat_registered` (A business that is reg for VAT and trade goods between Northern Ireland and EU. This node is available only for organizations enabled for NI protocal in VAT Settings.) and

`overseas` (A business that is located outside UK. Pre Brexit, this was split as `eu_vat_registered`, `eu_vat_not_registered` and `non_eu` ).

tax\_treatment

string

GCC,🇲🇽

Mexico


,🇰🇪

Kenya


,🇿🇦

South Africa


only

VAT treatment of the contact.

Allowed Values: `vat_registered`, `vat_not_registered`, `gcc_vat_not_registered`, `gcc_vat_registered`, `non_gcc`, `dz_vat_registered` and `dz_vat_not_registered`

`home_country_mexico` (A business that is located within MX)

`border_region_mexico` (A business that is located in the northern and southern border regions in MX)

`non_mexico` (A business that is located outside MX).

**For Kenya Edition:** `vat_registered` , `vat_not_registered` , `non_kenya`(A business that is located outside Kenya).

**For SouthAfrica Edition:** `vat_registered`, `vat_not_registered`, `overseas`(A business that is located outside SouthAfrica).

tax\_exemption\_certificate\_number

string

🇰🇪

Kenya


only

Tax Exemption Certificate number is issued by the Kenya Revenue Authority (KRA) to organizations or individuals who qualify for tax exemption

tax\_regime

string

🇲🇽

Mexico


only

Tax Regime of the contact.Allowed Values: `general_legal_person`, `legal_entities_non_profit`, `resident_abroad`, `production_cooperative_societies`, `agricultural_livestock`, `optional_group_of_companies`, `coordinated`, `simplified_trust`, `wages_salaries_income`, `lease`, `property_disposal_acquisition`, `other_income`, `resident_abroad`, `divident_income`, `individual_business_professional`, `interest_income`, `income_obtaining_price`, `no_tax_obligation`, `tax_incorporation`, `income_through_technology_platform`, `simplified_trust`.

legal\_name

string

🇲🇽

Mexico


only

Legal Name of the contact.

is\_tds\_registered

boolean

🇲🇽

Mexico


only

Boolean to check if tax is registered.

gst\_treatment

string

🇮🇳

India


only

Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are ` business_gst ` , ` business_none ` , ` overseas ` , ` consumer `.

is\_linked\_with\_zohocrm

boolean

unavailable

website

string

Website of the contact.

owner\_id

string

**For Customer Only :** If a contact is assigned to any particular user, that user can manage transactions for the contact.

primary\_contact\_id

string

unavailable

payment\_terms

integer

Net payment term for the customer.

payment\_terms\_label

string

Label for the paymet due details.

currency\_id

string

Currency ID of the customer's currency.

currency\_code

string

Currency code of the currency in which the customer wants to pay. If currency\_code is not specified here, the currency chosen in your Zoho Subscriptions organization will be used for billing. currency\_id and currency\_symbol are set automatically in accordance to the currency\_code.

currency\_symbol

string

Symbol of the currency of the contact\_type

opening\_balance\_amount

double

Opening balance amount for a contact.

exchange\_rate

double

Exchange rate for the opening balance.

outstanding\_receivable\_amount

integer

defintion unavailable

outstanding\_receivable\_amount\_bcy

integer

defintion unavailable

unused\_credits\_receivable\_amount

integer

defintion unavailable

unused\_credits\_receivable\_amount\_bcy

integer

defintion unavailable

status

string

The status of the contact.

payment\_reminder\_enabled

boolean

defintion unavailable

custom\_fields

array

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

index

integer

Index of the custom field. It can hold any value from 1 to 10.

value

string

Value of the custom field.

label

string

Label of the custom field.

billing\_address

object

Billing address of the contact.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

attention

string

address

string

Max-length \[500\]

street2

string

state\_code

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

phone

string

Search contacts by phone number of the contact person. Variants: `phone_startswith` and `phone_contains`

shipping\_address

object

Customer's shipping address object.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

attention

string

address

string

Max-length \[500\]

street2

string

state\_code

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

phone

string

Search contacts by phone number of the contact person. Variants: `phone_startswith` and `phone_contains`

facebook

string

Facebook profile account. max-length \[100\]

twitter

string

Twitter account. max-length \[100\]

contact\_persons

array

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

contact\_person\_id

string

ID of the contact person

salutation

string

Salutation for the contact

first\_name

string

Max-length \[100\]

last\_name

string

Max-length \[100\]

email

string

Email address of the contact person.

phone

string

Search contacts by phone number of the contact person. Variants: `phone_startswith` and `phone_contains`

mobile

string

Search contacts by mobile number of the contact person.

designation

string

Designation for the contact person.

department

string

Department for the contact person.

skype

string

Skype details for the contact person.

is\_primary\_contact

boolean

To mark contact person as primary for contact. Allowed value is `true` only.

enable\_portal

boolean

To enable client portal for the primary contact. Allowed value is `true` and `false`.

default\_templates

object

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

invoice\_template\_id

string

Default invoice template id used for this contact while creating invoice.

estimate\_template\_id

string

Default estimate template id used for this contact while creating estimate.

creditnote\_template\_id

string

Default credit note template id used for this contact while creating credit note.

purchaseorder\_template\_id

string

Default purchase order template id used for this contact while creating purchase order(for Vendors only).

salesorder\_template\_id

string

Default sales order template id used for this contact while creating sales order.

retainerinvoice\_template\_id

string

Default retainer invoice template id used for this contact while creating retainer invoice.

paymentthankyou\_template\_id

string

Default payment thankyou template id used for this contact while sending payment thankyou note.

retainerinvoice\_paymentthankyou\_template\_id

string

Default retainer invoice paymnet thankyou template id used for this contact while sending payment thankyou note for retainer invoice.

invoice\_email\_template\_id

string

Default invoice email template id used for this contact while sending invoices.

estimate\_email\_template\_id

string

Default estimate email template id used for this contact while sending estimates.

creditnote\_email\_template\_id

string

Default credit note email template id used for this contact while sending credit notes.

purchaseorder\_email\_template\_id

string

Default purchase order template id used for this contact while creating purchase order(for Vendors only).

salesorder\_email\_template\_id

string

Default sales order template id used for this contact while creating sales order.

retainerinvoice\_email\_template\_id

string

Default retainer invoice template id used for this contact while creating retainer invoice.

paymentthankyou\_email\_template\_id

string

Default payment thankyou template id used for this contact while sending payment thankyou note.

retainerinvoice\_paymentthankyou\_email\_template\_id

string

Default retainer invoice paymnet thankyou template id used for this contact while sending payment thankyou note for retainer invoice.

notes

string

Commennts about the payment made by the contact.

created\_time

string

Time at which the contact was created.

last\_modified\_time

string

Time at which the contact was modified

Example

`{
    "contact_id": 460000000026049,
    "contact_name": "Bowman and Co",
    "company_name": "Bowman and Co",
    "has_transaction": true,
    "contact_type": "customer",
    "customer_sub_type": "business",
    "credit_limit": 1000,
    "is_portal_enabled": true,
    "language_code": "string",
    "is_taxable": true,
    "tax_id": 11149000000061058,
    "tds_tax_id": "982000000557012",
    "tax_name": "CGST",
    "tax_percentage": 12,
    "tax_authority_id": 11149000000061052,
    "tax_exemption_id": 11149000000061054,
    "tax_authority_name": "string",
    "tax_exemption_code": "string",
    "place_of_contact": "TN",
    "gst_no": "22AAAAA0000A1Z5",
    "vat_treatment": "string",
    "tax_treatment": "string",
    "tax_exemption_certificate_number": "KRAEXM0043310521",
    "tax_regime": "general_legal_person",
    "legal_name": "ESCUELA KEMPER URGATE",
    "is_tds_registered": true,
    "gst_treatment": "business_gst",
    "is_linked_with_zohocrm": false,
    "website": "www.bowmanfurniture.com",
    "owner_id": 460000000016051,
    "primary_contact_id": 460000000026051,
    "payment_terms": 15,
    "payment_terms_label": "Net 15",
    "currency_id": 460000000000097,
    "currency_code": "USD",
    "currency_symbol": "$",
    "opening_balance_amount": 1200,
    "exchange_rate": 1,
    "outstanding_receivable_amount": 250,
    "outstanding_receivable_amount_bcy": 250,
    "unused_credits_receivable_amount": 1369.66,
    "unused_credits_receivable_amount_bcy": 1369.66,
    "status": "active",
    "payment_reminder_enabled": true,
    "custom_fields": [\
        {\
            "index": 1,\
            "value": "GBGD078",\
            "label": "VAT ID"\
        }\
    ],
    "billing_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "shipping_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "facebook": "zoho",
    "twitter": "zoho",
    "contact_persons": [\
        {\
            "contact_person_id": 460000000026051,\
            "salutation": "Mr",\
            "first_name": "Will",\
            "last_name": "Smith",\
            "email": "willsmith@bowmanfurniture.com",\
            "phone": "+1-925-921-9201",\
            "mobile": "+1-4054439562",\
            "designation": "Sales Executive",\
            "department": "Sales and Marketing",\
            "skype": "Zoho",\
            "is_primary_contact": true,\
            "enable_portal": true\
        }\
    ],
    "default_templates": {
        "invoice_template_id": 460000000052069,
        "estimate_template_id": 460000000000179,
        "creditnote_template_id": 460000000000211,
        "purchaseorder_template_id": 460000000000213,
        "salesorder_template_id": 460000000000214,
        "retainerinvoice_template_id": 460000000000215,
        "paymentthankyou_template_id": 460000000000216,
        "retainerinvoice_paymentthankyou_template_id": 460000000000217,
        "invoice_email_template_id": 460000000052071,
        "estimate_email_template_id": 460000000052073,
        "creditnote_email_template_id": 460000000052075,
        "purchaseorder_email_template_id": 460000000000218,
        "salesorder_email_template_id": 460000000000219,
        "retainerinvoice_email_template_id": 460000000000220,
        "paymentthankyou_email_template_id": 460000000000221,
        "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
    },
    "notes": "Payment option : Through check",
    "created_time": "2013-08-05T12:06:10+0530",
    "last_modified_time": "2013-10-07T18:24:51+0530"
}`

## Create a Contact

Create a contact with given information.


`OAuth Scope : ZohoBooks.contacts.CREATE`

### Arguments

contact\_name

string

(Required)


Display Name of the contact. Max-length \[200\]

company\_name

string

Company Name of the contact. Max-length \[200\]

website

string

Website of the contact.

language\_code

string

language of a contact. allowed values `de,en,es,fr,it,ja,nl,pt,pt_br,sv,zh,en_gb`

contact\_type

string

Contact type of the contact

customer\_sub\_type

string

Type of the customer

credit\_limit

double

Credit limit for a customer

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

is\_portal\_enabled

boolean

To enable client portal for the contact. Allowed value is `true` and `false`.

currency\_id

string

Currency ID of the customer's currency.

payment\_terms

integer

Net payment term for the customer.

payment\_terms\_label

string

Label for the paymet due details.

notes

string

Commennts about the payment made by the contact.

billing\_address

object

Billing address of the contact.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

attention

string

address

string

Max-length \[500\]

street2

string

state\_code

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

phone

string

Search contacts by phone number of the contact person. Variants: `phone_startswith` and `phone_contains`

shipping\_address

object

Customer's shipping address object.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

attention

string

address

string

Max-length \[500\]

street2

string

state\_code

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

phone

string

Search contacts by phone number of the contact person. Variants: `phone_startswith` and `phone_contains`

contact\_persons

array

, default is Contact persons of a contact.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

salutation

string

Salutation for the contact

first\_name

string

Max-length \[100\]

last\_name

string

Max-length \[100\]

email

string

Email address of the contact person.

phone

string

Search contacts by phone number of the contact person. Variants: `phone_startswith` and `phone_contains`

mobile

string

Search contacts by mobile number of the contact person.

designation

string

Designation for the contact person.

department

string

Department for the contact person.

skype

string

Skype details for the contact person.

is\_primary\_contact

boolean

To mark contact person as primary for contact. Allowed value is `true` only.

enable\_portal

boolean

To enable client portal for the primary contact. Allowed value is `true` and `false`.

default\_templates

object

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

invoice\_template\_id

string

Default invoice template id used for this contact while creating invoice.

estimate\_template\_id

string

Default estimate template id used for this contact while creating estimate.

creditnote\_template\_id

string

Default credit note template id used for this contact while creating credit note.

purchaseorder\_template\_id

string

Default purchase order template id used for this contact while creating purchase order(for Vendors only).

salesorder\_template\_id

string

Default sales order template id used for this contact while creating sales order.

retainerinvoice\_template\_id

string

Default retainer invoice template id used for this contact while creating retainer invoice.

paymentthankyou\_template\_id

string

Default payment thankyou template id used for this contact while sending payment thankyou note.

retainerinvoice\_paymentthankyou\_template\_id

string

Default retainer invoice paymnet thankyou template id used for this contact while sending payment thankyou note for retainer invoice.

invoice\_email\_template\_id

string

Default invoice email template id used for this contact while sending invoices.

estimate\_email\_template\_id

string

Default estimate email template id used for this contact while sending estimates.

creditnote\_email\_template\_id

string

Default credit note email template id used for this contact while sending credit notes.

purchaseorder\_email\_template\_id

string

Default purchase order template id used for this contact while creating purchase order(for Vendors only).

salesorder\_email\_template\_id

string

Default sales order template id used for this contact while creating sales order.

retainerinvoice\_email\_template\_id

string

Default retainer invoice template id used for this contact while creating retainer invoice.

paymentthankyou\_email\_template\_id

string

Default payment thankyou template id used for this contact while sending payment thankyou note.

retainerinvoice\_paymentthankyou\_email\_template\_id

string

Default retainer invoice paymnet thankyou template id used for this contact while sending payment thankyou note for retainer invoice.

custom\_fields

array

Custom fields of the contact.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

index

integer

Index of the custom field. It can hold any value from 1 to 10.

value

string

Value of the custom field.

opening\_balance\_amount

double

Opening balance amount for a contact.

exchange\_rate

double

Exchange rate for the opening balance.

vat\_reg\_no

string

🇬🇧

United Kingdom


,Avalara Integrationonly

**For UK Edition:** VAT Registration number of a contact with length should be between 2 and 12 characters.

**For Avalara:** If you are doing sales in the European Union (EU) then provide VAT Registration Number of your customers here. This is used to calculate VAT for B2B sales, from Avalara.

owner\_id

string

**For Customer Only :** If a contact is assigned to any particular user, that user can manage transactions for the contact.

tax\_reg\_no

string

GCC,🇲🇽

Mexico


,🇰🇪

Kenya


,🇿🇦

South Africa


only

**For GCC Edition:** 15 digit Tax Registration number of a contact with Tax treatment as `vat_registered`, `gcc_vat_registered`, `dz_vat_registered`.

**For Mexico Edition:** 12 digit Tax Registration number of a contact with Tax treatment as

`home_country_mexico`, `border_region_mexico`, `non_mexico`.

Consumers generic RFC: `XAXX010101000`, Overseas generic RFC: `XEXX010101000`.

**For Kenya Edition:** 11 digit Tax Registration number of a contact with Tax treatment as `vat_registered`

**For SouthAfrica Edition:** 10 digit Tax Registration number of a contact with Tax treatment as `vat_registered`

tax\_exemption\_certificate\_number

string

🇰🇪

Kenya


only

Tax Exemption Certificate number is issued by the Kenya Revenue Authority (KRA) to organizations or individuals who qualify for tax exemption

country\_code

string

🇬🇧

United Kingdom


,GCC,Avalara Integrationonly

**For UK Edition:** Two letter country code of a contact

**For Avalara:** Two letter country code for the customer country, if your customer is not in US. Refer \[AvaTax Codes for Countries and States\]\[2\].

**For GCC Editions :** Two Letter country code for the GCC Country or the UAE emirate of the contact which will be considered as **place of supply**.

Supported codes for UAE emirates are :

Abu Dhabi - `AB`,

Ajman - `AJ`,

Dubai - `DU`,

Fujairah - `FU`,

Ras al-Khaimah - `RA`,

Sharjah - `SH`,

Umm al-Quwain - `UM`.

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

VAT treatment of the contact.Allowed Values:

`uk` (A business that is located in the UK.),

`eu_vat_registered` (A business that is reg for VAT and trade goods between Northern Ireland and EU. This node is available only for organizations enabled for NI protocal in VAT Settings.) and

`overseas` (A business that is located outside UK. Pre Brexit, this was split as `eu_vat_registered`, `eu_vat_not_registered` and `non_eu` ).

tax\_treatment

string

GCC,🇲🇽

Mexico


,🇰🇪

Kenya


,🇿🇦

South Africa


only

VAT treatment of the contact.

Allowed Values: `vat_registered`, `vat_not_registered`, `gcc_vat_not_registered`, `gcc_vat_registered`, `non_gcc`, `dz_vat_registered` and `dz_vat_not_registered`

`home_country_mexico` (A business that is located within MX)

`border_region_mexico` (A business that is located in the northern and southern border regions in MX)

`non_mexico` (A business that is located outside MX).

**For Kenya Edition:** `vat_registered` , `vat_not_registered` , `non_kenya`(A business that is located outside Kenya).

**For SouthAfrica Edition:** `vat_registered`, `vat_not_registered`, `overseas`(A business that is located outside SouthAfrica).

tax\_regime

string

🇲🇽

Mexico


only

Tax Regime of the contact.Allowed Values: `general_legal_person`, `legal_entities_non_profit`, `resident_abroad`, `production_cooperative_societies`, `agricultural_livestock`, `optional_group_of_companies`, `coordinated`, `simplified_trust`, `wages_salaries_income`, `lease`, `property_disposal_acquisition`, `other_income`, `resident_abroad`, `divident_income`, `individual_business_professional`, `interest_income`, `income_obtaining_price`, `no_tax_obligation`, `tax_incorporation`, `income_through_technology_platform`, `simplified_trust`.

legal\_name

string

🇲🇽

Mexico


only

Legal Name of the contact.

is\_tds\_registered

boolean

🇲🇽

Mexico


only

Boolean to check if tax is registered.

place\_of\_contact

string

🇮🇳

India


only

Location of the contact. (This node identifies the place of supply and source of supply when invoices/bills are raised for the customer/vendor respectively. This is not applicable for Overseas contacts)

gst\_no

string

🇮🇳

India


only

15 digit GST identification number of the customer/vendor.

gst\_treatment

string

🇮🇳

India


only

Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are ` business_gst ` , ` business_none ` , ` overseas ` , ` consumer `.

tax\_authority\_name

string

Enter tax authority name.

avatax\_exempt\_no

string

Avalara Integrationonly

Exemption certificate number of the customer.

avatax\_use\_code

string

Avalara Integrationonly

Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara \[standard codes\]\[1\] or enter a custom code.

tax\_exemption\_id

string

🇺🇸

United States


,🇨🇦

Canada


,🇦🇺

Australia


,🇮🇳

India


only

ID of the tax exemption.

tax\_exemption\_code

string

🇺🇸

United States


,🇨🇦

Canada


,🇦🇺

Australia


,🇮🇳

India


only

Enter tax exemption code

tax\_authority\_id

string

🇺🇸

United States


only

ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority.

tax\_id

string

🇮🇳

India


,🇺🇸

United States


only

ID of the tax or tax group that can be collected from the contact. Tax can be given only if `is_taxable` is `true`.

tds\_tax\_id

string

🇲🇽

Mexico


only

ID of the TDS tax.

is\_taxable

boolean

🇺🇸

United States


,🇨🇦

Canada


,🇦🇺

Australia


,🇮🇳

India


,🇲🇽

Mexico


,🇰🇪

Kenya


,🇿🇦

South Africa


only

Boolean to track the taxability of the customer.

facebook

string

Facebook profile account. max-length \[100\]

twitter

string

Twitter account. max-length \[100\]

track\_1099

boolean

🇺🇸

United States


only

Boolean to track a contact for 1099 reporting.

tax\_id\_type

string

🇺🇸

United States


only

Tax ID type of the contact, it can be SSN, ATIN, ITIN or EIN.

tax\_id\_value

string

🇺🇸

United States


only

Tax ID of the contact.

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts?organization_id=10234695"\
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
.url("https://www.zohoapis.com/books/v3/contacts?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts?organization_id=10234695', options)
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
conn.request("POST", "/books/v3/contacts?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "contact_name": "Bowman and Co",
    "company_name": "Bowman and Co",
    "website": "www.bowmanfurniture.com",
    "language_code": "string",
    "contact_type": "customer",
    "customer_sub_type": "business",
    "credit_limit": 1000,
    "tags": [\
        {\
            "tag_id": 462000000009070,\
            "tag_option_id": 462000000002670\
        }\
    ],
    "is_portal_enabled": true,
    "currency_id": 460000000000097,
    "payment_terms": 15,
    "payment_terms_label": "Net 15",
    "notes": "Payment option : Through check",
    "billing_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "shipping_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "contact_persons": "Contact persons of a contact.",
    "default_templates": {
        "invoice_template_id": 460000000052069,
        "estimate_template_id": 460000000000179,
        "creditnote_template_id": 460000000000211,
        "purchaseorder_template_id": 460000000000213,
        "salesorder_template_id": 460000000000214,
        "retainerinvoice_template_id": 460000000000215,
        "paymentthankyou_template_id": 460000000000216,
        "retainerinvoice_paymentthankyou_template_id": 460000000000217,
        "invoice_email_template_id": 460000000052071,
        "estimate_email_template_id": 460000000052073,
        "creditnote_email_template_id": 460000000052075,
        "purchaseorder_email_template_id": 460000000000218,
        "salesorder_email_template_id": 460000000000219,
        "retainerinvoice_email_template_id": 460000000000220,
        "paymentthankyou_email_template_id": 460000000000221,
        "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
    },
    "custom_fields": [\
        {\
            "index": 1,\
            "value": "GBGD078"\
        }\
    ],
    "opening_balance_amount": 1200,
    "exchange_rate": 1,
    "vat_reg_no": "string",
    "owner_id": 460000000016051,
    "tax_reg_no": 12345678912345,
    "tax_exemption_certificate_number": "KRAEXM0043310521",
    "country_code": "string",
    "vat_treatment": "string",
    "tax_treatment": "string",
    "tax_regime": "general_legal_person",
    "legal_name": "ESCUELA KEMPER URGATE",
    "is_tds_registered": true,
    "place_of_contact": "TN",
    "gst_no": "22AAAAA0000A1Z5",
    "gst_treatment": "business_gst",
    "tax_authority_name": "string",
    "avatax_exempt_no": "string",
    "avatax_use_code": "string",
    "tax_exemption_id": 11149000000061054,
    "tax_exemption_code": "string",
    "tax_authority_id": 11149000000061052,
    "tax_id": 11149000000061058,
    "tds_tax_id": "982000000557012",
    "is_taxable": true,
    "facebook": "zoho",
    "twitter": "zoho",
    "track_1099": true,
    "tax_id_type": "string",
    "tax_id_value": "string"
}`

Response Example

`{
    "code": 0,
    "message": "The contact has been created",
    "contact": {
        "contact_id": 460000000026049,
        "contact_name": "Bowman and Co",
        "company_name": "Bowman and Co",
        "has_transaction": true,
        "contact_type": "customer",
        "customer_sub_type": "business",
        "credit_limit": 1000,
        "is_portal_enabled": true,
        "language_code": "string",
        "is_taxable": true,
        "tax_id": 11149000000061058,
        "tds_tax_id": "982000000557012",
        "tax_name": "CGST",
        "tax_percentage": 12,
        "tax_authority_id": 11149000000061052,
        "tax_exemption_id": 11149000000061054,
        "tax_authority_name": "string",
        "tax_exemption_code": "string",
        "place_of_contact": "TN",
        "gst_no": "22AAAAA0000A1Z5",
        "vat_treatment": "string",
        "tax_treatment": "string",
        "tax_exemption_certificate_number": "KRAEXM0043310521",
        "tax_regime": "general_legal_person",
        "legal_name": "ESCUELA KEMPER URGATE",
        "is_tds_registered": true,
        "gst_treatment": "business_gst",
        "is_linked_with_zohocrm": false,
        "website": "www.bowmanfurniture.com",
        "owner_id": 460000000016051,
        "primary_contact_id": 460000000026051,
        "payment_terms": 15,
        "payment_terms_label": "Net 15",
        "currency_id": 460000000000097,
        "currency_code": "USD",
        "currency_symbol": "$",
        "opening_balance_amount": 1200,
        "exchange_rate": 1,
        "outstanding_receivable_amount": 250,
        "outstanding_receivable_amount_bcy": 250,
        "unused_credits_receivable_amount": 1369.66,
        "unused_credits_receivable_amount_bcy": 1369.66,
        "status": "active",
        "payment_reminder_enabled": true,
        "custom_fields": [\
            {\
                "index": 1,\
                "value": "GBGD078",\
                "label": "VAT ID"\
            }\
        ],
        "billing_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "shipping_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "facebook": "zoho",
        "twitter": "zoho",
        "contact_persons": [\
            {\
                "contact_person_id": 460000000026051,\
                "salutation": "Mr",\
                "first_name": "Will",\
                "last_name": "Smith",\
                "email": "willsmith@bowmanfurniture.com",\
                "phone": "+1-925-921-9201",\
                "mobile": "+1-4054439562",\
                "designation": "Sales Executive",\
                "department": "Sales and Marketing",\
                "skype": "Zoho",\
                "is_primary_contact": true,\
                "enable_portal": true\
            }\
        ],
        "default_templates": {
            "invoice_template_id": 460000000052069,
            "estimate_template_id": 460000000000179,
            "creditnote_template_id": 460000000000211,
            "purchaseorder_template_id": 460000000000213,
            "salesorder_template_id": 460000000000214,
            "retainerinvoice_template_id": 460000000000215,
            "paymentthankyou_template_id": 460000000000216,
            "retainerinvoice_paymentthankyou_template_id": 460000000000217,
            "invoice_email_template_id": 460000000052071,
            "estimate_email_template_id": 460000000052073,
            "creditnote_email_template_id": 460000000052075,
            "purchaseorder_email_template_id": 460000000000218,
            "salesorder_email_template_id": 460000000000219,
            "retainerinvoice_email_template_id": 460000000000220,
            "paymentthankyou_email_template_id": 460000000000221,
            "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
        },
        "notes": "Payment option : Through check",
        "created_time": "2013-08-05T12:06:10+0530",
        "last_modified_time": "2013-10-07T18:24:51+0530"
    }
}`

## Update a contact using a custom field's unique value

A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update a contact by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding contact will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing contacts, a new contact will be created if the necessary payload details are available


`OAuth Scope : ZohoBooks.contacts.UPDATE`

### Arguments

contact\_name

string

(Required)


Display Name of the contact. Max-length \[200\]

company\_name

string

Company Name of the contact. Max-length \[200\]

payment\_terms

integer

Net payment term for the customer.

payment\_terms\_label

string

Label for the paymet due details.

contact\_type

string

Contact type of the contact

customer\_sub\_type

string

Type of the customer

currency\_id

string

Currency ID of the customer's currency.

opening\_balance\_amount

double

Opening balance amount for a contact.

exchange\_rate

double

Exchange rate for the opening balance.

credit\_limit

double

Credit limit for a customer

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

website

string

Website of the contact.

owner\_id

string

**For Customer Only :** If a contact is assigned to any particular user, that user can manage transactions for the contact.

custom\_fields

array

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

index

integer

Index of the custom field. It can hold any value from 1 to 10.

value

string

Value of the custom field.

label

string

Label of the custom field.

billing\_address

object

Billing address of the contact.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

attention

string

address

string

Max-length \[500\]

street2

string

state\_code

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

phone

string

Search contacts by phone number of the contact person. Variants: `phone_startswith` and `phone_contains`

shipping\_address

object

Customer's shipping address object.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

attention

string

address

string

Max-length \[500\]

street2

string

state\_code

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

phone

string

Search contacts by phone number of the contact person. Variants: `phone_startswith` and `phone_contains`

contact\_persons

array

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

contact\_person\_id

string

ID of the contact person. For an existing contact person, pass the `contact_person_id`.

salutation

string

Salutation for the contact

first\_name

string

Max-length \[100\]

last\_name

string

Max-length \[100\]

email

string

Email address of the contact person.

phone

string

Search contacts by phone number of the contact person. Variants: `phone_startswith` and `phone_contains`

mobile

string

Search contacts by mobile number of the contact person.

designation

string

Designation for the contact person.

department

string

Department for the contact person.

skype

string

Skype details for the contact person.

is\_primary\_contact

boolean

To mark contact person as primary for contact. Allowed value is `true` only.

enable\_portal

boolean

To enable client portal for the primary contact. Allowed value is `true` and `false`.

default\_templates

object

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

invoice\_template\_id

string

Default invoice template id used for this contact while creating invoice.

estimate\_template\_id

string

Default estimate template id used for this contact while creating estimate.

creditnote\_template\_id

string

Default credit note template id used for this contact while creating credit note.

purchaseorder\_template\_id

string

Default purchase order template id used for this contact while creating purchase order(for Vendors only).

salesorder\_template\_id

string

Default sales order template id used for this contact while creating sales order.

retainerinvoice\_template\_id

string

Default retainer invoice template id used for this contact while creating retainer invoice.

paymentthankyou\_template\_id

string

Default payment thankyou template id used for this contact while sending payment thankyou note.

retainerinvoice\_paymentthankyou\_template\_id

string

Default retainer invoice paymnet thankyou template id used for this contact while sending payment thankyou note for retainer invoice.

invoice\_email\_template\_id

string

Default invoice email template id used for this contact while sending invoices.

estimate\_email\_template\_id

string

Default estimate email template id used for this contact while sending estimates.

creditnote\_email\_template\_id

string

Default credit note email template id used for this contact while sending credit notes.

purchaseorder\_email\_template\_id

string

Default purchase order template id used for this contact while creating purchase order(for Vendors only).

salesorder\_email\_template\_id

string

Default sales order template id used for this contact while creating sales order.

retainerinvoice\_email\_template\_id

string

Default retainer invoice template id used for this contact while creating retainer invoice.

paymentthankyou\_email\_template\_id

string

Default payment thankyou template id used for this contact while sending payment thankyou note.

retainerinvoice\_paymentthankyou\_email\_template\_id

string

Default retainer invoice paymnet thankyou template id used for this contact while sending payment thankyou note for retainer invoice.

notes

string

Commennts about the payment made by the contact.

vat\_reg\_no

string

🇬🇧

United Kingdom


,Avalara Integrationonly

**For UK Edition:** VAT Registration number of a contact with length should be between 2 and 12 characters.

**For Avalara:** If you are doing sales in the European Union (EU) then provide VAT Registration Number of your customers here. This is used to calculate VAT for B2B sales, from Avalara.

tax\_reg\_no

string

GCC,🇲🇽

Mexico


,🇰🇪

Kenya


,🇿🇦

South Africa


only

**For GCC Edition:** 15 digit Tax Registration number of a contact with Tax treatment as `vat_registered`, `gcc_vat_registered`, `dz_vat_registered`.

**For Mexico Edition:** 12 digit Tax Registration number of a contact with Tax treatment as

`home_country_mexico`, `border_region_mexico`, `non_mexico`.

Consumers generic RFC: `XAXX010101000`, Overseas generic RFC: `XEXX010101000`.

**For Kenya Edition:** 11 digit Tax Registration number of a contact with Tax treatment as `vat_registered`

**For SouthAfrica Edition:** 10 digit Tax Registration number of a contact with Tax treatment as `vat_registered`

country\_code

string

🇬🇧

United Kingdom


,GCC,Avalara Integrationonly

**For UK Edition:** Two letter country code of a contact

**For Avalara:** Two letter country code for the customer country, if your customer is not in US. Refer \[AvaTax Codes for Countries and States\]\[2\].

**For GCC Editions :** Two Letter country code for the GCC Country or the UAE emirate of the contact which will be considered as **place of supply**.

Supported codes for UAE emirates are :

Abu Dhabi - `AB`,

Ajman - `AJ`,

Dubai - `DU`,

Fujairah - `FU`,

Ras al-Khaimah - `RA`,

Sharjah - `SH`,

Umm al-Quwain - `UM`.

Supported codes for the GCC countries are :

United Arab Emirates - `AE`,

Saudi Arabia - `SA`,

Bahrain - `BH`,

Kuwait - `KW`,

Oman - `OM`,

Qatar - `QA`.

tax\_treatment

string

GCC,🇲🇽

Mexico


,🇰🇪

Kenya


,🇿🇦

South Africa


only

VAT treatment of the contact.

Allowed Values: `vat_registered`, `vat_not_registered`, `gcc_vat_not_registered`, `gcc_vat_registered`, `non_gcc`, `dz_vat_registered` and `dz_vat_not_registered`

`home_country_mexico` (A business that is located within MX)

`border_region_mexico` (A business that is located in the northern and southern border regions in MX)

`non_mexico` (A business that is located outside MX).

**For Kenya Edition:** `vat_registered` , `vat_not_registered` , `non_kenya`(A business that is located outside Kenya).

**For SouthAfrica Edition:** `vat_registered`, `vat_not_registered`, `overseas`(A business that is located outside SouthAfrica).

tax\_exemption\_certificate\_number

string

🇰🇪

Kenya


only

Tax Exemption Certificate number is issued by the Kenya Revenue Authority (KRA) to organizations or individuals who qualify for tax exemption

tax\_regime

string

🇲🇽

Mexico


only

Tax Regime of the contact.Allowed Values: `general_legal_person`, `legal_entities_non_profit`, `resident_abroad`, `production_cooperative_societies`, `agricultural_livestock`, `optional_group_of_companies`, `coordinated`, `simplified_trust`, `wages_salaries_income`, `lease`, `property_disposal_acquisition`, `other_income`, `resident_abroad`, `divident_income`, `individual_business_professional`, `interest_income`, `income_obtaining_price`, `no_tax_obligation`, `tax_incorporation`, `income_through_technology_platform`, `simplified_trust`.

legal\_name

string

🇲🇽

Mexico


only

Legal Name of the contact.

is\_tds\_registered

boolean

🇲🇽

Mexico


only

Boolean to check if tax is registered.

vat\_treatment

string

🇬🇧

United Kingdom


only

VAT treatment of the contact.Allowed Values:

`uk` (A business that is located in the UK.),

`eu_vat_registered` (A business that is reg for VAT and trade goods between Northern Ireland and EU. This node is available only for organizations enabled for NI protocal in VAT Settings.) and

`overseas` (A business that is located outside UK. Pre Brexit, this was split as `eu_vat_registered`, `eu_vat_not_registered` and `non_eu` ).

place\_of\_contact

string

🇮🇳

India


only

Location of the contact. (This node identifies the place of supply and source of supply when invoices/bills are raised for the customer/vendor respectively. This is not applicable for Overseas contacts)

gst\_no

string

🇮🇳

India


only

15 digit GST identification number of the customer/vendor.

gst\_treatment

string

🇮🇳

India


only

Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are ` business_gst ` , ` business_none ` , ` overseas ` , ` consumer `.

tax\_authority\_name

string

Enter tax authority name.

avatax\_exempt\_no

string

Avalara Integrationonly

Exemption certificate number of the customer.

avatax\_use\_code

string

Avalara Integrationonly

Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara \[standard codes\]\[1\] or enter a custom code.

tax\_exemption\_id

string

🇺🇸

United States


,🇨🇦

Canada


,🇦🇺

Australia


,🇮🇳

India


only

ID of the tax exemption.

tax\_exemption\_code

string

🇺🇸

United States


,🇨🇦

Canada


,🇦🇺

Australia


,🇮🇳

India


only

Enter tax exemption code

tax\_authority\_id

string

🇺🇸

United States


only

ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority.

tax\_id

string

🇮🇳

India


,🇺🇸

United States


only

ID of the tax or tax group that can be collected from the contact. Tax can be given only if `is_taxable` is `true`.

is\_taxable

boolean

🇺🇸

United States


,🇨🇦

Canada


,🇦🇺

Australia


,🇮🇳

India


,🇲🇽

Mexico


,🇰🇪

Kenya


,🇿🇦

South Africa


only

Boolean to track the taxability of the customer.

facebook

string

Facebook profile account. max-length \[100\]

twitter

string

Twitter account. max-length \[100\]

track\_1099

boolean

🇺🇸

United States


only

Boolean to track a contact for 1099 reporting.

tax\_id\_type

string

🇺🇸

United States


only

Tax ID type of the contact, it can be SSN, ATIN, ITIN or EIN.

tax\_id\_value

string

🇺🇸

United States


only

Tax ID of the contact.

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts?organization_id=10234695"\
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
.url("https://www.zohoapis.com/books/v3/contacts?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts?organization_id=10234695', options)
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
conn.request("PUT", "/books/v3/contacts?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "PUT",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'X-Unique-Identifier-Key: cf_unique_cf' \
  --header 'X-Unique-Identifier-Value: unique Value' \
  --header 'X-Upsert: true' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "contact_name": "Bowman and Co",
    "company_name": "Bowman and Co",
    "payment_terms": 15,
    "payment_terms_label": "Net 15",
    "contact_type": "customer",
    "customer_sub_type": "business",
    "currency_id": 460000000000097,
    "opening_balance_amount": 1200,
    "exchange_rate": 1,
    "credit_limit": 1000,
    "tags": [\
        {\
            "tag_id": 462000000009070,\
            "tag_option_id": 462000000002670\
        }\
    ],
    "website": "www.bowmanfurniture.com",
    "owner_id": 460000000016051,
    "custom_fields": [\
        {\
            "index": 1,\
            "value": "GBGD078",\
            "label": "VAT ID"\
        }\
    ],
    "billing_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "shipping_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "contact_persons": [\
        {\
            "contact_person_id": 460000000026051,\
            "salutation": "Mr",\
            "first_name": "Will",\
            "last_name": "Smith",\
            "email": "willsmith@bowmanfurniture.com",\
            "phone": "+1-925-921-9201",\
            "mobile": "+1-4054439562",\
            "designation": "Sales Executive",\
            "department": "Sales and Marketing",\
            "skype": "Zoho",\
            "is_primary_contact": true,\
            "enable_portal": true\
        }\
    ],
    "default_templates": {
        "invoice_template_id": 460000000052069,
        "estimate_template_id": 460000000000179,
        "creditnote_template_id": 460000000000211,
        "purchaseorder_template_id": 460000000000213,
        "salesorder_template_id": 460000000000214,
        "retainerinvoice_template_id": 460000000000215,
        "paymentthankyou_template_id": 460000000000216,
        "retainerinvoice_paymentthankyou_template_id": 460000000000217,
        "invoice_email_template_id": 460000000052071,
        "estimate_email_template_id": 460000000052073,
        "creditnote_email_template_id": 460000000052075,
        "purchaseorder_email_template_id": 460000000000218,
        "salesorder_email_template_id": 460000000000219,
        "retainerinvoice_email_template_id": 460000000000220,
        "paymentthankyou_email_template_id": 460000000000221,
        "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
    },
    "notes": "Payment option : Through check",
    "vat_reg_no": "string",
    "tax_reg_no": 12345678912345,
    "country_code": "string",
    "tax_treatment": "string",
    "tax_exemption_certificate_number": "KRAEXM0043310521",
    "tax_regime": "general_legal_person",
    "legal_name": "ESCUELA KEMPER URGATE",
    "is_tds_registered": true,
    "vat_treatment": "string",
    "place_of_contact": "TN",
    "gst_no": "22AAAAA0000A1Z5",
    "gst_treatment": "business_gst",
    "tax_authority_name": "string",
    "avatax_exempt_no": "string",
    "avatax_use_code": "string",
    "tax_exemption_id": 11149000000061054,
    "tax_exemption_code": "string",
    "tax_authority_id": 11149000000061052,
    "tax_id": 11149000000061058,
    "is_taxable": true,
    "facebook": "zoho",
    "twitter": "zoho",
    "track_1099": true,
    "tax_id_type": "string",
    "tax_id_value": "string"
}`

Response Example

`{
    "code": 0,
    "message": "Contact has been updated successfully",
    "contact": {
        "contact_id": 460000000026049,
        "contact_name": "Bowman and Co",
        "company_name": "Bowman and Co",
        "has_transaction": true,
        "contact_type": "customer",
        "customer_sub_type": "business",
        "credit_limit": 1000,
        "is_taxable": true,
        "tax_id": 11149000000061058,
        "tax_name": "CGST",
        "tax_percentage": 12,
        "tax_authority_id": 11149000000061052,
        "tax_exemption_id": 11149000000061054,
        "tax_authority_name": "string",
        "tax_exemption_code": "string",
        "place_of_contact": "TN",
        "gst_no": "22AAAAA0000A1Z5",
        "tax_treatment": "string",
        "tax_regime": "general_legal_person",
        "legal_name": "ESCUELA KEMPER URGATE",
        "is_tds_registered": true,
        "vat_treatment": "string",
        "gst_treatment": "business_gst",
        "is_linked_with_zohocrm": false,
        "website": "www.bowmanfurniture.com",
        "owner_id": 460000000016051,
        "primary_contact_id": 460000000026051,
        "payment_terms": 15,
        "payment_terms_label": "Net 15",
        "currency_id": 460000000000097,
        "currency_code": "USD",
        "currency_symbol": "$",
        "opening_balance_amount": 1200,
        "exchange_rate": 1,
        "outstanding_receivable_amount": 250,
        "outstanding_receivable_amount_bcy": 250,
        "unused_credits_receivable_amount": 1369.66,
        "unused_credits_receivable_amount_bcy": 1369.66,
        "status": "active",
        "payment_reminder_enabled": true,
        "custom_fields": [\
            {\
                "index": 1,\
                "value": "GBGD078",\
                "label": "VAT ID"\
            }\
        ],
        "billing_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "shipping_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "facebook": "zoho",
        "twitter": "zoho",
        "contact_persons": [\
            {\
                "contact_person_id": 460000000026051,\
                "salutation": "Mr",\
                "first_name": "Will",\
                "last_name": "Smith",\
                "email": "willsmith@bowmanfurniture.com",\
                "phone": "+1-925-921-9201",\
                "mobile": "+1-4054439562",\
                "designation": "Sales Executive",\
                "department": "Sales and Marketing",\
                "skype": "Zoho",\
                "is_primary_contact": true,\
                "enable_portal": true\
            }\
        ],
        "default_templates": {
            "invoice_template_id": 460000000052069,
            "estimate_template_id": 460000000000179,
            "creditnote_template_id": 460000000000211,
            "purchaseorder_template_id": 460000000000213,
            "salesorder_template_id": 460000000000214,
            "retainerinvoice_template_id": 460000000000215,
            "paymentthankyou_template_id": 460000000000216,
            "retainerinvoice_paymentthankyou_template_id": 460000000000217,
            "invoice_email_template_id": 460000000052071,
            "estimate_email_template_id": 460000000052073,
            "creditnote_email_template_id": 460000000052075,
            "purchaseorder_email_template_id": 460000000000218,
            "salesorder_email_template_id": 460000000000219,
            "retainerinvoice_email_template_id": 460000000000220,
            "paymentthankyou_email_template_id": 460000000000221,
            "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
        },
        "notes": "Payment option : Through check",
        "created_time": "2013-08-05T12:06:10+0530",
        "last_modified_time": "2013-10-07T18:24:51+0530"
    }
}`

## List Contacts

List all contacts with pagination.


`OAuth Scope : ZohoBooks.contacts.READ`

### Query Parameters

contact\_name

Search contacts by contact name. Max-length \[100\] Variants: `contact_name_startswith` and `contact_name_contains`. Max-length \[100\]

company\_name

Search contacts by company name. Max-length \[100\] Variants: `company_name_startswith` and `company_name_contains`

first\_name

Search contacts by first name of the contact person. Max-length \[100\] Variants: `first_name_startswith` and `first_name_contains`

last\_name

Search contacts by last name of the contact person. Max-length \[100\] Variants: `last_name_startswith` and `last_name_contains`

address

Search contacts by any of the address fields. Max-length \[100\] Variants: `address_startswith` and `address_contains`

email

Search contacts by email of the contact person. Max-length \[100\] Variants: `email_startswith` and `email_contains`

phone

Search contacts by phone number of the contact person. Max-length \[100\] Variants: `phone_startswith` and `phone_contains`

filter\_by

Filter contacts by status. Allowed Values: `Status.All, Status.Active, Status.Inactive, Status.Duplicate and Status.Crm`

search\_text

Search contacts by contact name or notes. Max-length \[100\]

sort\_column

Sort contacts. Allowed Values: `contact_name, first_name, last_name, email, outstanding_receivable_amount, created_time and last_modified_time`

zcrm\_contact\_id

CRM Contact ID for the contact.

zcrm\_account\_id

CRM Account ID for the contact.

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts?organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/contacts?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/contacts?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "contacts": [\
        {\
            "contact_id": 460000000026049,\
            "contact_name": "Bowman and Co",\
            "company_name": "Bowman and Co",\
            "contact_type": "customer",\
            "status": "active",\
            "payment_terms": 15,\
            "payment_terms_label": "Net 15",\
            "currency_id": 460000000000097,\
            "currency_code": "USD",\
            "outstanding_receivable_amount": 250,\
            "unused_credits_receivable_amount": 1369.66,\
            "first_name": "Will",\
            "last_name": "Smith",\
            "email": "willsmith@bowmanfurniture.com",\
            "phone": "+1-925-921-9201",\
            "mobile": "+1-4054439562",\
            "created_time": "2013-08-05T12:06:10+0530",\
            "last_modified_time": "2013-10-07T18:24:51+0530"\
        },\
        {...},\
        {...}\
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "applied_filter": "Status.All",
        "sort_column": "contact_name",
        "sort_order": "D"
    }
}`

## Update a Contact

Update an existing contact. To delete a contact person, remove it from the contact\_persons list.


`OAuth Scope : ZohoBooks.contacts.UPDATE`

### Arguments

contact\_name

string

(Required)


Display Name of the contact. Max-length \[200\]

company\_name

string

Company Name of the contact. Max-length \[200\]

payment\_terms

integer

Net payment term for the customer.

payment\_terms\_label

string

Label for the paymet due details.

contact\_type

string

Contact type of the contact

customer\_sub\_type

string

Type of the customer

currency\_id

string

Currency ID of the customer's currency.

opening\_balance\_amount

double

Opening balance amount for a contact.

exchange\_rate

double

Exchange rate for the opening balance.

credit\_limit

double

Credit limit for a customer

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

website

string

Website of the contact.

owner\_id

string

**For Customer Only :** If a contact is assigned to any particular user, that user can manage transactions for the contact.

custom\_fields

array

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

index

integer

Index of the custom field. It can hold any value from 1 to 10.

value

string

Value of the custom field.

label

string

Label of the custom field.

billing\_address

object

Billing address of the contact.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

attention

string

address

string

Max-length \[500\]

street2

string

state\_code

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

phone

string

Search contacts by phone number of the contact person. Variants: `phone_startswith` and `phone_contains`

shipping\_address

object

Customer's shipping address object.

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

attention

string

address

string

Max-length \[500\]

street2

string

state\_code

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

phone

string

Search contacts by phone number of the contact person. Variants: `phone_startswith` and `phone_contains`

contact\_persons

array

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

contact\_person\_id

string

ID of the contact person. For an existing contact person, pass the `contact_person_id`.

salutation

string

Salutation for the contact

first\_name

string

Max-length \[100\]

last\_name

string

Max-length \[100\]

email

string

Email address of the contact person.

phone

string

Search contacts by phone number of the contact person. Variants: `phone_startswith` and `phone_contains`

mobile

string

Search contacts by mobile number of the contact person.

designation

string

Designation for the contact person.

department

string

Department for the contact person.

skype

string

Skype details for the contact person.

is\_primary\_contact

boolean

To mark contact person as primary for contact. Allowed value is `true` only.

enable\_portal

boolean

To enable client portal for the primary contact. Allowed value is `true` and `false`.

default\_templates

object

Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

invoice\_template\_id

string

Default invoice template id used for this contact while creating invoice.

estimate\_template\_id

string

Default estimate template id used for this contact while creating estimate.

creditnote\_template\_id

string

Default credit note template id used for this contact while creating credit note.

purchaseorder\_template\_id

string

Default purchase order template id used for this contact while creating purchase order(for Vendors only).

salesorder\_template\_id

string

Default sales order template id used for this contact while creating sales order.

retainerinvoice\_template\_id

string

Default retainer invoice template id used for this contact while creating retainer invoice.

paymentthankyou\_template\_id

string

Default payment thankyou template id used for this contact while sending payment thankyou note.

retainerinvoice\_paymentthankyou\_template\_id

string

Default retainer invoice paymnet thankyou template id used for this contact while sending payment thankyou note for retainer invoice.

invoice\_email\_template\_id

string

Default invoice email template id used for this contact while sending invoices.

estimate\_email\_template\_id

string

Default estimate email template id used for this contact while sending estimates.

creditnote\_email\_template\_id

string

Default credit note email template id used for this contact while sending credit notes.

purchaseorder\_email\_template\_id

string

Default purchase order template id used for this contact while creating purchase order(for Vendors only).

salesorder\_email\_template\_id

string

Default sales order template id used for this contact while creating sales order.

retainerinvoice\_email\_template\_id

string

Default retainer invoice template id used for this contact while creating retainer invoice.

paymentthankyou\_email\_template\_id

string

Default payment thankyou template id used for this contact while sending payment thankyou note.

retainerinvoice\_paymentthankyou\_email\_template\_id

string

Default retainer invoice paymnet thankyou template id used for this contact while sending payment thankyou note for retainer invoice.

notes

string

Commennts about the payment made by the contact.

vat\_reg\_no

string

🇬🇧

United Kingdom


,Avalara Integrationonly

**For UK Edition:** VAT Registration number of a contact with length should be between 2 and 12 characters.

**For Avalara:** If you are doing sales in the European Union (EU) then provide VAT Registration Number of your customers here. This is used to calculate VAT for B2B sales, from Avalara.

tax\_reg\_no

string

GCC,🇲🇽

Mexico


,🇰🇪

Kenya


,🇿🇦

South Africa


only

**For GCC Edition:** 15 digit Tax Registration number of a contact with Tax treatment as `vat_registered`, `gcc_vat_registered`, `dz_vat_registered`.

**For Mexico Edition:** 12 digit Tax Registration number of a contact with Tax treatment as

`home_country_mexico`, `border_region_mexico`, `non_mexico`.

Consumers generic RFC: `XAXX010101000`, Overseas generic RFC: `XEXX010101000`.

**For Kenya Edition:** 11 digit Tax Registration number of a contact with Tax treatment as `vat_registered`

**For SouthAfrica Edition:** 10 digit Tax Registration number of a contact with Tax treatment as `vat_registered`

country\_code

string

🇬🇧

United Kingdom


,GCC,Avalara Integrationonly

**For UK Edition:** Two letter country code of a contact

**For Avalara:** Two letter country code for the customer country, if your customer is not in US. Refer \[AvaTax Codes for Countries and States\]\[2\].

**For GCC Editions :** Two Letter country code for the GCC Country or the UAE emirate of the contact which will be considered as **place of supply**.

Supported codes for UAE emirates are :

Abu Dhabi - `AB`,

Ajman - `AJ`,

Dubai - `DU`,

Fujairah - `FU`,

Ras al-Khaimah - `RA`,

Sharjah - `SH`,

Umm al-Quwain - `UM`.

Supported codes for the GCC countries are :

United Arab Emirates - `AE`,

Saudi Arabia - `SA`,

Bahrain - `BH`,

Kuwait - `KW`,

Oman - `OM`,

Qatar - `QA`.

tax\_treatment

string

GCC,🇲🇽

Mexico


,🇰🇪

Kenya


,🇿🇦

South Africa


only

VAT treatment of the contact.

Allowed Values: `vat_registered`, `vat_not_registered`, `gcc_vat_not_registered`, `gcc_vat_registered`, `non_gcc`, `dz_vat_registered` and `dz_vat_not_registered`

`home_country_mexico` (A business that is located within MX)

`border_region_mexico` (A business that is located in the northern and southern border regions in MX)

`non_mexico` (A business that is located outside MX).

**For Kenya Edition:** `vat_registered` , `vat_not_registered` , `non_kenya`(A business that is located outside Kenya).

**For SouthAfrica Edition:** `vat_registered`, `vat_not_registered`, `overseas`(A business that is located outside SouthAfrica).

tax\_exemption\_certificate\_number

string

🇰🇪

Kenya


only

Tax Exemption Certificate number is issued by the Kenya Revenue Authority (KRA) to organizations or individuals who qualify for tax exemption

tax\_regime

string

🇲🇽

Mexico


only

Tax Regime of the contact.Allowed Values: `general_legal_person`, `legal_entities_non_profit`, `resident_abroad`, `production_cooperative_societies`, `agricultural_livestock`, `optional_group_of_companies`, `coordinated`, `simplified_trust`, `wages_salaries_income`, `lease`, `property_disposal_acquisition`, `other_income`, `resident_abroad`, `divident_income`, `individual_business_professional`, `interest_income`, `income_obtaining_price`, `no_tax_obligation`, `tax_incorporation`, `income_through_technology_platform`, `simplified_trust`.

legal\_name

string

🇲🇽

Mexico


only

Legal Name of the contact.

is\_tds\_registered

boolean

🇲🇽

Mexico


only

Boolean to check if tax is registered.

vat\_treatment

string

🇬🇧

United Kingdom


only

VAT treatment of the contact.Allowed Values:

`uk` (A business that is located in the UK.),

`eu_vat_registered` (A business that is reg for VAT and trade goods between Northern Ireland and EU. This node is available only for organizations enabled for NI protocal in VAT Settings.) and

`overseas` (A business that is located outside UK. Pre Brexit, this was split as `eu_vat_registered`, `eu_vat_not_registered` and `non_eu` ).

place\_of\_contact

string

🇮🇳

India


only

Location of the contact. (This node identifies the place of supply and source of supply when invoices/bills are raised for the customer/vendor respectively. This is not applicable for Overseas contacts)

gst\_no

string

🇮🇳

India


only

15 digit GST identification number of the customer/vendor.

gst\_treatment

string

🇮🇳

India


only

Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are ` business_gst ` , ` business_none ` , ` overseas ` , ` consumer `.

tax\_authority\_name

string

Enter tax authority name.

avatax\_exempt\_no

string

Avalara Integrationonly

Exemption certificate number of the customer.

avatax\_use\_code

string

Avalara Integrationonly

Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara \[standard codes\]\[1\] or enter a custom code.

tax\_exemption\_id

string

🇺🇸

United States


,🇨🇦

Canada


,🇦🇺

Australia


,🇮🇳

India


only

ID of the tax exemption.

tax\_exemption\_code

string

🇺🇸

United States


,🇨🇦

Canada


,🇦🇺

Australia


,🇮🇳

India


only

Enter tax exemption code

tax\_authority\_id

string

🇺🇸

United States


only

ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority.

tax\_id

string

🇮🇳

India


,🇺🇸

United States


only

ID of the tax or tax group that can be collected from the contact. Tax can be given only if `is_taxable` is `true`.

is\_taxable

boolean

🇺🇸

United States


,🇨🇦

Canada


,🇦🇺

Australia


,🇮🇳

India


,🇲🇽

Mexico


,🇰🇪

Kenya


,🇿🇦

South Africa


only

Boolean to track the taxability of the customer.

facebook

string

Facebook profile account. max-length \[100\]

twitter

string

Twitter account. max-length \[100\]

track\_1099

boolean

🇺🇸

United States


only

Boolean to track a contact for 1099 reporting.

tax\_id\_type

string

🇺🇸

United States


only

Tax ID type of the contact, it can be SSN, ATIN, ITIN or EIN.

tax\_id\_value

string

🇺🇸

United States


only

Tax ID of the contact.

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049?organization_id=10234695"\
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
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049?organization_id=10234695', options)
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
conn.request("PUT", "/books/v3/contacts/460000000026049?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "PUT",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "contact_name": "Bowman and Co",
    "company_name": "Bowman and Co",
    "payment_terms": 15,
    "payment_terms_label": "Net 15",
    "contact_type": "customer",
    "customer_sub_type": "business",
    "currency_id": 460000000000097,
    "opening_balance_amount": 1200,
    "exchange_rate": 1,
    "credit_limit": 1000,
    "tags": [\
        {\
            "tag_id": 462000000009070,\
            "tag_option_id": 462000000002670\
        }\
    ],
    "website": "www.bowmanfurniture.com",
    "owner_id": 460000000016051,
    "custom_fields": [\
        {\
            "index": 1,\
            "value": "GBGD078",\
            "label": "VAT ID"\
        }\
    ],
    "billing_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "shipping_address": {
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "state_code": "CA",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    },
    "contact_persons": [\
        {\
            "contact_person_id": 460000000026051,\
            "salutation": "Mr",\
            "first_name": "Will",\
            "last_name": "Smith",\
            "email": "willsmith@bowmanfurniture.com",\
            "phone": "+1-925-921-9201",\
            "mobile": "+1-4054439562",\
            "designation": "Sales Executive",\
            "department": "Sales and Marketing",\
            "skype": "Zoho",\
            "is_primary_contact": true,\
            "enable_portal": true\
        }\
    ],
    "default_templates": {
        "invoice_template_id": 460000000052069,
        "estimate_template_id": 460000000000179,
        "creditnote_template_id": 460000000000211,
        "purchaseorder_template_id": 460000000000213,
        "salesorder_template_id": 460000000000214,
        "retainerinvoice_template_id": 460000000000215,
        "paymentthankyou_template_id": 460000000000216,
        "retainerinvoice_paymentthankyou_template_id": 460000000000217,
        "invoice_email_template_id": 460000000052071,
        "estimate_email_template_id": 460000000052073,
        "creditnote_email_template_id": 460000000052075,
        "purchaseorder_email_template_id": 460000000000218,
        "salesorder_email_template_id": 460000000000219,
        "retainerinvoice_email_template_id": 460000000000220,
        "paymentthankyou_email_template_id": 460000000000221,
        "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
    },
    "notes": "Payment option : Through check",
    "vat_reg_no": "string",
    "tax_reg_no": 12345678912345,
    "country_code": "string",
    "tax_treatment": "string",
    "tax_exemption_certificate_number": "KRAEXM0043310521",
    "tax_regime": "general_legal_person",
    "legal_name": "ESCUELA KEMPER URGATE",
    "is_tds_registered": true,
    "vat_treatment": "string",
    "place_of_contact": "TN",
    "gst_no": "22AAAAA0000A1Z5",
    "gst_treatment": "business_gst",
    "tax_authority_name": "string",
    "avatax_exempt_no": "string",
    "avatax_use_code": "string",
    "tax_exemption_id": 11149000000061054,
    "tax_exemption_code": "string",
    "tax_authority_id": 11149000000061052,
    "tax_id": 11149000000061058,
    "is_taxable": true,
    "facebook": "zoho",
    "twitter": "zoho",
    "track_1099": true,
    "tax_id_type": "string",
    "tax_id_value": "string"
}`

Response Example

`{
    "code": 0,
    "message": "Contact has been updated successfully",
    "contact": {
        "contact_id": 460000000026049,
        "contact_name": "Bowman and Co",
        "company_name": "Bowman and Co",
        "has_transaction": true,
        "contact_type": "customer",
        "customer_sub_type": "business",
        "credit_limit": 1000,
        "is_taxable": true,
        "tax_id": 11149000000061058,
        "tax_name": "CGST",
        "tax_percentage": 12,
        "tax_authority_id": 11149000000061052,
        "tax_exemption_id": 11149000000061054,
        "tax_authority_name": "string",
        "tax_exemption_code": "string",
        "place_of_contact": "TN",
        "gst_no": "22AAAAA0000A1Z5",
        "tax_treatment": "string",
        "tax_regime": "general_legal_person",
        "legal_name": "ESCUELA KEMPER URGATE",
        "is_tds_registered": true,
        "vat_treatment": "string",
        "gst_treatment": "business_gst",
        "is_linked_with_zohocrm": false,
        "website": "www.bowmanfurniture.com",
        "owner_id": 460000000016051,
        "primary_contact_id": 460000000026051,
        "payment_terms": 15,
        "payment_terms_label": "Net 15",
        "currency_id": 460000000000097,
        "currency_code": "USD",
        "currency_symbol": "$",
        "opening_balance_amount": 1200,
        "exchange_rate": 1,
        "outstanding_receivable_amount": 250,
        "outstanding_receivable_amount_bcy": 250,
        "unused_credits_receivable_amount": 1369.66,
        "unused_credits_receivable_amount_bcy": 1369.66,
        "status": "active",
        "payment_reminder_enabled": true,
        "custom_fields": [\
            {\
                "index": 1,\
                "value": "GBGD078",\
                "label": "VAT ID"\
            }\
        ],
        "billing_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "shipping_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "facebook": "zoho",
        "twitter": "zoho",
        "contact_persons": [\
            {\
                "contact_person_id": 460000000026051,\
                "salutation": "Mr",\
                "first_name": "Will",\
                "last_name": "Smith",\
                "email": "willsmith@bowmanfurniture.com",\
                "phone": "+1-925-921-9201",\
                "mobile": "+1-4054439562",\
                "designation": "Sales Executive",\
                "department": "Sales and Marketing",\
                "skype": "Zoho",\
                "is_primary_contact": true,\
                "enable_portal": true\
            }\
        ],
        "default_templates": {
            "invoice_template_id": 460000000052069,
            "estimate_template_id": 460000000000179,
            "creditnote_template_id": 460000000000211,
            "purchaseorder_template_id": 460000000000213,
            "salesorder_template_id": 460000000000214,
            "retainerinvoice_template_id": 460000000000215,
            "paymentthankyou_template_id": 460000000000216,
            "retainerinvoice_paymentthankyou_template_id": 460000000000217,
            "invoice_email_template_id": 460000000052071,
            "estimate_email_template_id": 460000000052073,
            "creditnote_email_template_id": 460000000052075,
            "purchaseorder_email_template_id": 460000000000218,
            "salesorder_email_template_id": 460000000000219,
            "retainerinvoice_email_template_id": 460000000000220,
            "paymentthankyou_email_template_id": 460000000000221,
            "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
        },
        "notes": "Payment option : Through check",
        "created_time": "2013-08-05T12:06:10+0530",
        "last_modified_time": "2013-10-07T18:24:51+0530"
    }
}`

## Get Contact

Get details of a contact.


`OAuth Scope : ZohoBooks.contacts.READ`

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049?organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/contacts/460000000026049?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "contact": {
        "contact_id": 460000000026049,
        "contact_name": "Bowman and Co",
        "company_name": "Bowman and Co",
        "has_transaction": true,
        "contact_type": "customer",
        "customer_sub_type": "business",
        "credit_limit": 1000,
        "is_taxable": true,
        "tax_id": 11149000000061058,
        "tax_name": "CGST",
        "tax_percentage": 12,
        "tax_authority_id": 11149000000061052,
        "tax_exemption_id": 11149000000061054,
        "tax_authority_name": "string",
        "tax_exemption_code": "string",
        "place_of_contact": "TN",
        "gst_no": "22AAAAA0000A1Z5",
        "tax_treatment": "string",
        "tax_regime": "general_legal_person",
        "legal_name": "ESCUELA KEMPER URGATE",
        "is_tds_registered": true,
        "vat_treatment": "string",
        "gst_treatment": "business_gst",
        "is_linked_with_zohocrm": false,
        "website": "www.bowmanfurniture.com",
        "owner_id": 460000000016051,
        "primary_contact_id": 460000000026051,
        "payment_terms": 15,
        "payment_terms_label": "Net 15",
        "currency_id": 460000000000097,
        "currency_code": "USD",
        "currency_symbol": "$",
        "opening_balance_amount": 1200,
        "exchange_rate": 1,
        "outstanding_receivable_amount": 250,
        "outstanding_receivable_amount_bcy": 250,
        "unused_credits_receivable_amount": 1369.66,
        "unused_credits_receivable_amount_bcy": 1369.66,
        "status": "active",
        "facebook": "zoho",
        "twitter": "zoho",
        "payment_reminder_enabled": true,
        "custom_fields": [\
            {\
                "index": 1,\
                "value": "GBGD078",\
                "label": "VAT ID"\
            }\
        ],
        "billing_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "shipping_address": {
            "attention": "Mr.John",
            "address": "4900 Hopyard Rd",
            "street2": "Suite 310",
            "state_code": "CA",
            "city": "Pleasanton",
            "state": "CA",
            "zip": 94588,
            "country": "U.S.A",
            "fax": "+1-925-924-9600",
            "phone": "+1-925-921-9201"
        },
        "contact_persons": [\
            {\
                "contact_person_id": 460000000026051,\
                "salutation": "Mr",\
                "first_name": "Will",\
                "last_name": "Smith",\
                "email": "willsmith@bowmanfurniture.com",\
                "phone": "+1-925-921-9201",\
                "mobile": "+1-4054439562",\
                "designation": "Sales Executive",\
                "department": "Sales and Marketing",\
                "skype": "Zoho",\
                "is_primary_contact": true,\
                "enable_portal": true\
            }\
        ],
        "default_templates": {
            "invoice_template_id": 460000000052069,
            "estimate_template_id": 460000000000179,
            "creditnote_template_id": 460000000000211,
            "purchaseorder_template_id": 460000000000213,
            "salesorder_template_id": 460000000000214,
            "retainerinvoice_template_id": 460000000000215,
            "paymentthankyou_template_id": 460000000000216,
            "retainerinvoice_paymentthankyou_template_id": 460000000000217,
            "invoice_email_template_id": 460000000052071,
            "estimate_email_template_id": 460000000052073,
            "creditnote_email_template_id": 460000000052075,
            "purchaseorder_email_template_id": 460000000000218,
            "salesorder_email_template_id": 460000000000219,
            "retainerinvoice_email_template_id": 460000000000220,
            "paymentthankyou_email_template_id": 460000000000221,
            "retainerinvoice_paymentthankyou_email_template_id": 460000000000222
        },
        "notes": "Payment option : Through check",
        "created_time": "2013-08-05T12:06:10+0530",
        "last_modified_time": "2013-10-07T18:24:51+0530"
    }
}`

## Delete a Contact

Delete an existing contact.


`OAuth Scope : ZohoBooks.contacts.DELETE`

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049?organization_id=10234695"\
type: DELETE\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("DELETE", "/books/v3/contacts/460000000026049?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "DELETE",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "The contact has been deleted."
}`

## Mark as Active

Mark a contact as active.


`OAuth Scope : ZohoBooks.contacts.CREATE`

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/active?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/active?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/active?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/contacts/460000000026049/active?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/active?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/active?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "The contact has been marked as active."
}`

## Mark as Inactive

Mark a contact as inactive.


`OAuth Scope : ZohoBooks.contacts.CREATE`

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/inactive?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/inactive?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/inactive?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/contacts/460000000026049/inactive?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/inactive?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/inactive?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "The contact has been marked as inactive."
}`

## Enable Portal Access

Enable portal access for a contact.


`OAuth Scope : ZohoBooks.contacts.CREATE`

### Arguments

contact\_persons

array

(Required)


Show Sub-Attributes![arrow](https://www.zoho.com/books/api/v3/images/dropdown-arrow.svg)

contact\_person\_id

string

ID of the contact person

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/portal/enable?organization_id=10234695"\
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
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/portal/enable?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/portal/enable?organization_id=10234695', options)
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
conn.request("POST", "/books/v3/contacts/460000000026049/portal/enable?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/portal/enable?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/portal/enable?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "contact_persons": [\
        {\
            "contact_person_id": 460000000026051\
        }\
    ]
}`

Response Example

`{
    "code": 0,
    "message": "Client Portal preferences have been updated"
}`

## Enable Payment Reminders

Enable automated payment reminders for a contact.


`OAuth Scope : ZohoBooks.contacts.CREATE`

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/paymentreminder/enable?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/paymentreminder/enable?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/paymentreminder/enable?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/contacts/460000000026049/paymentreminder/enable?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/paymentreminder/enable?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/paymentreminder/enable?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "All reminders associated with this contact have been enabled."
}`

## Disable Payment Reminders

Disable automated payment reminders for a contact.


`OAuth Scope : ZohoBooks.contacts.CREATE`

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/paymentreminder/disable?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/paymentreminder/disable?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/paymentreminder/disable?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/contacts/460000000026049/paymentreminder/disable?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/paymentreminder/disable?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/paymentreminder/disable?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "All reminders associated with this contact have been stopped."
}`

## Email Statement

Email statement to the contact. If JSONString is not inputted, mail will be sent with the default mail content.


`OAuth Scope : ZohoBooks.contacts.CREATE`

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

(Required)


Subject of an email has to be sent. Max-length \[1000\]

body

string

(Required)


Body of an email has to be sent. Max-length \[5000\]

### Query Parameters

start\_date

If start\_date and end\_date are not given, current month's statement will be sent to contact. Date format \[yyyy-mm-dd\]

end\_date

End date for the statement. Date format \[yyyy-mm-dd\]

multipart\_or\_formdata

Files to be attached along with the statement.

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/statements/email?organization_id=10234695"\
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
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/statements/email?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/statements/email?organization_id=10234695', options)
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
conn.request("POST", "/books/v3/contacts/460000000026049/statements/email?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/statements/email?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/statements/email?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "send_from_org_email_id": true,
    "to_mail_ids": [\
        "willsmith@bowmanfurniture.com"\
    ],
    "cc_mail_ids": [\
        "peterparker@bowmanfurniture.com"\
    ],
    "subject": "Statement of transactions with Zillium Inc",
    "body": "Dear Customer,     <br/>We have attached with this email a list of all your transactions with us for the period 01 Sep 2013 to 30 Sep 2013. You can write to us or call us if you need any assistance or clarifications.     <br/>Thanks for your business.<br/>Regards<br/>Zillium Inc"
}`

Response Example

`{
    "code": 0,
    "message": "Statement has been sent to the Customer."
}`

## Get Statement Mail Content

Get the statement mail content.


`OAuth Scope : ZohoBooks.contacts.READ`

### Query Parameters

start\_date

If start\_date and end\_date are not given, current month's statement will be sent to contact. Date format \[yyyy-mm-dd\]

end\_date

End date for the statement. Date format \[yyyy-mm-dd\]

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/statements/email?organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/statements/email?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/statements/email?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/contacts/460000000026049/statements/email?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/statements/email?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/statements/email?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "data": {
        "body": "Dear Customer,     <br/>We have attached with this email a list of all your transactions with us for the period 01 Sep 2013 to 30 Sep 2013. You can write to us or call us if you need any assistance or clarifications.     <br/>Thanks for your business.<br/>Regards<br/>Zillium Inc",
        "subject": "Statement of transactions with Zillium Inc",
        "to_contacts": [\
            {\
                "first_name": "Will",\
                "selected": true,\
                "phone": "+1-925-921-9201",\
                "email": "willsmith@bowmanfurniture.com",\
                "contact_person_id": 460000000026051,\
                "last_name": "Smith",\
                "salutation": "Mr",\
                "mobile": "+1-4054439562"\
            }\
        ],
        "file_name": "statement_BowmanandCo.pdf",
        "from_emails": [\
            {\
                "user_name": "John Smith",\
                "selected": true,\
                "email": "willsmith@bowmanfurniture.com"\
            }\
        ],
        "contact_id": 460000000026049
    }
}`

## Email Contact

Send email to contact.


`OAuth Scope : ZohoBooks.contacts.CREATE`

### Arguments

to\_mail\_ids

array

(Required)


Array of email address of the recipients.

subject

string

(Required)


Subject of an email has to be sent. Max-length \[1000\]

body

string

(Required)


Body of an email has to be sent. Max-length \[5000\]

attachments

binary

Files to be attached to the email. It has to be sent in multipart/formdata

### Query Parameters

send\_customer\_statement

Send customer statement pdf with email.

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/email?organization_id=10234695"\
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
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/email?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/email?organization_id=10234695', options)
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
conn.request("POST", "/books/v3/contacts/460000000026049/email?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/email?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/email?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "to_mail_ids": [\
        "willsmith@bowmanfurniture.com"\
    ],
    "subject": "Welcome to Zillium Inc .",
    "body": "Dear Customer,     <br/>We have attached with this email a list of all your transactions with us for the period 01 Sep 2013 to 30 Sep 2013. You can write to us or call us if you need any assistance or clarifications.     <br/>Thanks for your business.<br/>Regards<br/>Zillium Inc",
    "attachments": "string"
}`

Response Example

`{
    "code": 0,
    "message": "Email has been sent."
}`

## List Comments

List recent activities of a contact.


`OAuth Scope : ZohoBooks.contacts.READ`

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/comments?organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/comments?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/comments?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/contacts/460000000026049/comments?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/comments?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/comments?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "contact_comments": [\
        {\
            "comment_id": 460000000053131,\
            "contact_id": 460000000026049,\
            "contact_name": "Bowman and Co",\
            "description": "",\
            "commented_by_id": 460000000024003,\
            "commented_by": "John David",\
            "date": "2013-11-19",\
            "date_description": "4 days ago",\
            "time": "6:03 PM",\
            "transaction_id": 460000000053123,\
            "transaction_type": "customer_payment",\
            "is_entity_deleted": false,\
            "operation_type": "added"\
        },\
        {...},\
        {...}\
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "applied_filter": "Status.All",
        "sort_column": "contact_name",
        "sort_order": "D"
    }
}`

## Add Additional Address

Add an additional address for a contact using the arguments below.


`OAuth Scope : ZohoBooks.contacts.CREATE`

### Arguments

attention

string

address

string

Max-length \[500\]

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

phone

string

phone number of the contact person.

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/address?organization_id=10234695"\
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
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/address?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/address?organization_id=10234695', options)
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
conn.request("POST", "/books/v3/contacts/460000000026049/address?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/address?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/address?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "attention": "Mr.John",
    "address": "4900 Hopyard Rd",
    "street2": "Suite 310",
    "city": "Pleasanton",
    "state": "CA",
    "zip": 94588,
    "country": "U.S.A",
    "fax": "+1-925-924-9600",
    "phone": "+1-925-921-9201"
}`

Response Example

`{
    "code": 0,
    "message": "The address has been created.",
    "address_info": {
        "address_id": 1053791000000186000,
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    }
}`

## Get Contact Addresses

Get addresses of a contact including its Shipping Address, Billing Address and other additional addresses.


`OAuth Scope : ZohoBooks.contacts.READ`

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/address?organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/address?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/address?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/contacts/460000000026049/address?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/address?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/address?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "addresses": [\
        {\
            "address_id": 1053791000000186000,\
            "attention": "Mr.John",\
            "address": "4900 Hopyard Rd",\
            "street2": "Suite 310",\
            "city": "Pleasanton",\
            "state": "CA",\
            "zip": 94588,\
            "country": "U.S.A",\
            "fax": "+1-925-924-9600",\
            "phone": "+1-925-921-9201"\
        },\
        {...},\
        {...}\
    ]
}`

## Edit Additional Address

Edit the additional address of a contact using the arguments below.


`OAuth Scope : ZohoBooks.contacts.UPDATE`

### Arguments

attention

string

address

string

Max-length \[500\]

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

phone

string

phone number of the contact person.

address\_id

string

(Required)


Address id of the address

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/address/1053791000000186000?organization_id=10234695"\
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
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/address/1053791000000186000?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/address/1053791000000186000?organization_id=10234695', options)
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
conn.request("PUT", "/books/v3/contacts/460000000026049/address/1053791000000186000?organization_id=10234695", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "PUT",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/address/1053791000000186000?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/address/1053791000000186000?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f' \
  --header 'content-type: application/json' \
  --data '{"field1":"value1","field2":"value2"}'`

Body Parameters

Click to copy

`{
    "attention": "Mr.John",
    "address": "4900 Hopyard Rd",
    "street2": "Suite 310",
    "city": "Pleasanton",
    "state": "CA",
    "zip": 94588,
    "country": "U.S.A",
    "fax": "+1-925-924-9600",
    "phone": "+1-925-921-9201",
    "address_id": 1053791000000186000
}`

Response Example

`{
    "code": 0,
    "message": "The address has been updated.",
    "address_info": {
        "address_id": 1053791000000186000,
        "attention": "Mr.John",
        "address": "4900 Hopyard Rd",
        "street2": "Suite 310",
        "city": "Pleasanton",
        "state": "CA",
        "zip": 94588,
        "country": "U.S.A",
        "fax": "+1-925-924-9600",
        "phone": "+1-925-921-9201"
    }
}`

## Delete Additional Address

Delete the additional address of a contact.


`OAuth Scope : ZohoBooks.contacts.DELETE`

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/address/1053791000000186000?organization_id=10234695"\
type: DELETE\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/address/1053791000000186000?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/address/1053791000000186000?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("DELETE", "/books/v3/contacts/460000000026049/address/1053791000000186000?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "DELETE",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/address/1053791000000186000?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/address/1053791000000186000?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "The address has been deleted."
}`

## List Refunds

List the refund history of a contact.


`OAuth Scope : ZohoBooks.contacts.READ`

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/refunds?organization_id=10234695"\
type: GET\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/refunds?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/refunds?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("GET", "/books/v3/contacts/460000000026049/refunds?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "GET",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/refunds?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/refunds?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "success",
    "creditnote_refunds": [\
        {\
            "creditnote_refund_id": 982000000567158,\
            "creditnote_id": 982000000567134,\
            "date": "2013-11-19",\
            "refund_mode": "cash",\
            "reference_number": 782364,\
            "creditnote_number": "CN-00001",\
            "customer_name": "Bowman & Co",\
            "description": "gf",\
            "amount_bcy": 57.15,\
            "amount_fcy": 57.15\
        },\
        {...},\
        {...}\
    ],
    "page_context": {
        "page": 1,
        "per_page": 200,
        "has_more_page": false,
        "report_name": "Credit Notes Refund",
        "sort_column": "date",
        "sort_order": "D"
    }
}`

## Track 1099

Track a contact for 1099 reporting: (Note: This API is only available when the organization's country is U.S.A).


`OAuth Scope : ZohoBooks.contacts.CREATE`

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/track1099?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/track1099?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/track1099?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/contacts/460000000026049/track1099?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/track1099?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/track1099?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "1099 tracking is enabled."
}`

## Untrack 1099

Use this API to stop tracking payments to a vendor for 1099 reporting. (Note: This API is only available when the organization's country is U.S.A).


`OAuth Scope : ZohoBooks.contacts.CREATE`

Request Example

cURL

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
url: "https://www.zohoapis.com/books/v3/contacts/460000000026049/untrack1099?organization_id=10234695"\
type: POST\
headers: headers_data\
connection: <connection_name>\
]
info response;`

`OkHttpClient client = new OkHttpClient();
Request request = new Request.Builder()
.url("https://www.zohoapis.com/books/v3/contacts/460000000026049/untrack1099?organization_id=10234695")
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
fetch('https://www.zohoapis.com/books/v3/contacts/460000000026049/untrack1099?organization_id=10234695', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));`

`import http.client
conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = { 'Authorization': "Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f" }
conn.request("POST", "/books/v3/contacts/460000000026049/untrack1099?organization_id=10234695", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))`

`const http = require("https");
const options = {
"method": "POST",
"hostname": "www.zohoapis.com",
"port": null,
"path": "/books/v3/contacts/460000000026049/untrack1099?organization_id=10234695",
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
  --url 'https://www.zohoapis.com/books/v3/contacts/460000000026049/untrack1099?organization_id=10234695' \
  --header 'Authorization: Zoho-oauthtoken 1000.41d9xxxxxxxxxxxxxxxxxxxxxxxxc2d1.8fccxxxxxxxxxxxxxxxxxxxxxxxx125f'`

Response Example

`{
    "code": 0,
    "message": "1099 tracking is disabled."
}`

