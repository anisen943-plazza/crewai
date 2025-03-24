### Step 1: Registering New Client

You will have to first register your application with Zoho's Developer console in order get your `Client ID` and `Client Secret`.

To register your application, go to [https://accounts.zoho.com/developerconsole](https://accounts.zoho.com/developerconsole) and click on `Add Client ID`. Provide the required details to register your application.

On successful registration, you will be provided with a set of OAuth 2.0 credentials such as a ` Client ID ` and ` Client Secret ` that are known to both Zoho and your application. Do not share this credentials anywhere.

### Step 2: Generating Grant Token

Redirect to the following authorization URL with the given params

` https://accounts.zoho.com/oauth/v2/auth?`

| Parameter | Description |
| --- | --- |
| scope \* | SCOPE for which the token to be generated. Multiple scopes can be given which has to be separated by commas. Ex : ` ZohoBooks.fullaccess.all` |
| client\_id \* | Client ID obtained during Client Registration |
| state | An opaque string that is round-tripped in the protocol; ie., whatever value given to this will be passed back to you. |
| response\_type \* | `code` |
| redirect\_uri \* | One of the redirect URI given in above step. This param should be same redirect url mentioned while registering the Client |
| access\_type | The allowed values are `offline` and `online`. The `online` access\_type gives your application only the access\_token which is valid for one hour. The `offline` access\_type will give the application an access\_token as well as a refresh\_token. By default it is taken as `online` |
| prompt | Prompts for user consent each time your app tries to access user credentials. Ex: `Consent` |

_Note:_ Fields with `*` are mandatory

On this request, you will be shown with a "user consent page".

Upon clicking “Accept”, Zoho will redirect to the given redirect\_uri with `code` and `state` param. This code value is mandatory to get the access token in the next step and this code is valid for 60 seconds.

On clicking “Deny”, the server returns an error

Request Example

Click to copy

`
https://accounts.zoho.com/oauth/v2/auth?scope=ZohoBooks.invoices.CREATE,ZohoBooks.invoices.READ,ZohoBooks.invoices.UPDATE,ZohoBooks.invoices.DELETE&client_id=1000.0SRSxxxxxxxxxxxxxxxxxxxx239V&state=testing&response_type=code&redirect_uri=http://www.zoho.com/books&access_type=offline
        `

### Step 3: Generate Access and Refresh Token

After getting `code` from the above step, make a POST request for the following URL with given params, to generate the `access_token`.

`https://accounts.zoho.com/oauth/v2/token?`

| Parameter | Description |
| --- | --- |
| code\* | `code` which is obtained in the above step |
| client\_id\* | Client ID obtained during Client Registration |
| client\_secret\* | Client secret obtained during Client Registration |
| redirect\_uri\* | This param should be same redirect url mentioned while adding Client |
| grant\_type\* | `authorization_code` |
| scope | SCOPE for which token to be generated. Ex : ` ZohoBooks.fullaccess.all`. Multiple scopes has to be separated by commas. |
| state | An opaque string that is round-tripped in the protocol; that is to say, value will be passed back to you. |

_Note:_ Fields with `*` are mandatory

In the response, you will get both `access_token` and `refresh_token`.

1\. The `access_token` will expire after a particular period (as given in `expires_in` param in the response).

2\. The `refresh_token` is permanent and will be used to regenerate new `access_token`, if the current access token is expired.

_Note:_ Each time a re-consent page is accepted, a new refresh token is generated. The maximum limit is 20 refresh tokens per user. If this limit is crossed, the first refresh token is automatically deleted to accommodate the latest one. This is done irrespective of whether the first refresh token is in use or not.

Request Example

Click to copy

`
https://accounts.zoho.com/oauth/v2/token?code=1000.dd7exxxxxxxxxxxxxxxxxxxxxxxx9bb8.b6c0xxxxxxxxxxxxxxxxxxxxxxxxdca4&client_id=1000.0SRSxxxxxxxxxxxxxxxxxxxx239V&client_secret=fb01xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx8abf&redirect_uri=http://www.zoho.com/books&grant_type=authorization_code
        `

### Step 4: Generate Access Token From Refresh Token

Access Tokens have limited validity. In most general cases the access tokens expire in one hour. Until then, the access token has unlimited usage. Once it expires, your app will have to use the refresh token to request for a new access token. Redirect to the following POST URL with the given params to get a new access token

`https://accounts.zoho.com/oauth/v2/token?`

| Parameter | Description |
| --- | --- |
| refresh\_token | REFRESH TOKEN which is obtained in the above step |
| client\_id | Client ID obtained during Client Registration |
| client\_secret | Client secret obtained during Client Registration |
| redirect\_uri | This param should be same redirect url mentioned while registering Client |
| grant\_type | `refresh_token` |

Request Example

Click to copy

`
https://accounts.zoho.com/oauth/v2/token?refresh_token=1000.8ecdxxxxxxxxxxxxxxxxxxxxx5cb7.4638xxxxxxxxxxxxxxxxxxxxxxebdc&client_id=1000.0SRSxxxxxxxxxxxxxxxxxxxx239V&client_secret=fb01xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx8abf&redirect_uri=http://www.zoho.com/books&grant_type=refresh_token
        `

### Step 5: Revoking a Refresh Token

To revoke a refresh token, call the following POST URL with the given params

`https://accounts.zoho.com/oauth/v2/token/revoke?`

| Parameter | Description |
| --- | --- |
| token | REFRESH TOKEN which is to be revoked |

Request Example

Click to copy

`
https://accounts.zoho.com/oauth/v2/token/revoke?token=1000.8ecdxxxxxxxxxxxxxxxxxxxxxxxx5cb7.4638xxxxxxxxxxxxxxxxxxxxxxxxebdc
        `

### Step 6: Calling An API

Access Token can be passed only in header and cannot be passed in the request param.

- Header name should be `Authorization`
- Header value should be `Zoho-oauthtoken {access_token}`