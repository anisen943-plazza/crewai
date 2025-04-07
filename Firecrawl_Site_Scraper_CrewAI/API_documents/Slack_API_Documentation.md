# Slack API Documentation

## Web API Methods

Popular method groups include:
- appsauth
- chat
- conversations
- files
- reactions
- reminders
- teams
- users
- usergroups
- views

### Method Examples
- [`admin.analytics.getFile`](https://api.slack.com/methods/admin.analytics.getFile): Retrieve analytics data for a given date, presented as a compressed JSON file.
- [`admin.apps.activities.list`](https://api.slack.com/methods/admin.apps.activities.list): Get logs for a specified team/org.

## Using the Slack Web API

The Slack Web API is an interface for querying information _from_ and enacting change _in_ a Slack workspace. Use it for individual queries or as part of a more complex tapestry of platform features in a [Slack app](https://api.slack.com/docs/apps).

- [Web API Methods](https://api.slack.com/methods)
- For a quick setup, this tutorial teaches you [how to quickly get and use a Slack API bot token](https://api.slack.com/tutorials/tracks/getting-a-token).

### Basic Overview
- The Web API is not a REST API but works using HTTP RPC-style methods.
- Use HTTPS, SSL, and TLS v1.2 or above for API methods.
- Methods require a series of arguments to dictate functionality and can be sent as GET, POST parameters, or as application/json.

### Errors specific to passing JSON
If JSON is invalid:
- `invalid_json`
- `json_not_object`

All Web API responses will contain a JSON object with a boolean property `ok` indicating success or failure.

### Authentication
Authenticate your requests using a [bearer token](https://api.slack.com/docs/token-types). Register your application to obtain credentials via [OAuth 2.0](https://api.slack.com/authentication/oauth-v2).

## Authentication and Installation

Slack uses OAuth 2.0 for installing apps and handling permissions:
- [Creating an app](https://api.slack.com/authentication/basics)
- [Installing with OAuth](https://api.slack.com/authentication/oauth-v2)

### Permissions
- Tokens are crucial for accessing APIs.
- Scope requests for granular access points and data.

### Security
- Token rotation and request verification are key for maintaining security.

## Block Kit

Block Kit is a UI framework to create visually rich messages. Components can be customized and rearranged to create a tailored user experience.

**Build and Prototype Visually**  
[Block Kit Builder](https://app.slack.com/block-kit-builder) enables quick composition and previewing of blocks.

### Reference Guides
- **Blocks**: Includes Action, Context, Divider, Image, etc.
- **Block Elements**: Includes Buttons, Checkboxes, Select menus, etc.

### Tools Built by Slack

Tools include libraries and tools by Slack:
| Tool | Works with |
| --- | --- |
| [**Block Kit Builder**](https://app.slack.com/block-kit-builder) | JSON |

For more resources, check out [Slack GitHub](https://github.com/slackapi) and explore community tools on the [Slack Community page](https://api.slack.com/community).

![Slack Technologies Company Logo](https://cdn.cookielaw.org/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/1ce30484-b023-4ff1-a118-3a9dc53fce45/f83dd0bf-3d5c-47ca-b065-8f247adfeacd/rsz_slack_rgb.png)

## Privacy Preference Center

### Required Cookies
Always Active: Essential for basic functionality.

### Manage Consent Preferences
You can toggle functional and advertising cookie preferences. [Learn More](https://slack.com/cookie-policy).
```