# Using Slack APIs | Slack

The Slack developer docs are moving! We've been working hard at building out a new docs experience at [docs.slack.dev](https://docs.slack.dev/) — now in beta! You can start using the new docs today, but we'll keep the content on both sites up to date during the transition.

[Learn more](https://api.slack.com/changelog/2024-12-api-site-migration)

# Using Slack APIs

Every [Slack app](https://api.slack.com/docs/apps) and [workflow automation](https://api.slack.com/automation) has access to a range of APIs that provide access to read, write, and update many types of data in Slack.

Read on to learn about our core APIs, and discover how to use them to make magic.

* * *

## Web API

The Web API supplies a collection of [HTTP methods](https://api.slack.com/methods) that underpin the majority of Slack app functionality.

With over 100 methods available, it's impossible to explain _everything_ that's possible with the Web API, but we're sure there's one right for your app.

Our [Web API](https://api.slack.com/web) guide explains the basic process of interacting with these methods. Once you've read up on that, dive into the [list of available methods](https://api.slack.com/methods).

* * *

## Events API

The Events API is a streamlined way to build apps that respond to activities in Slack.

Subscribe to the [events](https://api.slack.com/events) you want from a range of possibilities. Build a [Slack app](https://api.slack.com/start/apps) that can [react to those events](https://api.slack.com/interactivity#responses) usefully.

Tell us where to send the events you carefully select and we'll push them to your app securely. We'll even retry when things don't work out.

Read our [Events API](https://api.slack.com/events-api) guide to learn how to subscribe to and handle events.

Check out our [Event delivery](https://api.slack.com/apis/event-delivery) guide to explore your options with how to receive event payloads: via a public HTTP URL or using the magic of WebSocket via Socket Mode.

If you don't wish to expose a public, static HTTP endpoint to communicate with Slack, [Socket Mode](https://api.slack.com/apis/connections/socket) can help.

* * *

## Other APIs

Beyond the Web and Events APIs, we have a range of other niche APIs that are suitable for specific types of apps.

- [**Admin APIs**](https://api.slack.com/enterprise/managing) are a subset of Web APIs that are geared towards automating and simplifying the administration of Slack organizations.
- [**SCIM APIs**](https://api.slack.com/enterprise/scim) are available for user provisioning and management.
- [**Audit Logs APIs**](https://api.slack.com/enterprise/audit-logs) are tailored for building security information and event management tools.
- The [**Status API**](https://api.slack.com/docs/slack-status) provides a programmatic way to monitor the health of the Slack product.
- [**RTM**](https://api.slack.com/rtm) is an outmoded API that provides WebSocket access to some of the same functionality as the Web and Events APIs. We list it here for completeness even though it has been deprecated.

![Slack Technologies Company Logo](https://cdn.cookielaw.org/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/1ce30484-b023-4ff1-a118-3a9dc53fce45/f83dd0bf-3d5c-47ca-b065-8f247adfeacd/rsz_slack_rgb.png)

## Privacy Preference Center

We use three kinds of cookies on our websites: required, functional, and advertising. You can choose whether functional and advertising cookies apply. Click on the different cookie categories to find out more about each category and to change the default settings. [More information](https://slack.com/cookie-policy)

Allow All

### Manage Consent Preferences

#### Required Cookies

Always Active

Required cookies are necessary for basic website functionality. Some examples include: session cookies needed to transmit the website, authentication cookies, and security cookies.

Cookies Details‎

#### Functional Cookies

Functional Cookies

Functional cookies enhance functions, performance, and services on the website. Some examples include: cookies used to analyze site traffic, cookies used for market research, and cookies used to display advertising that is not directed to a particular individual.

Cookies Details‎

#### Advertising Cookies

Advertising Cookies

Advertising cookies track activity across websites in order to understand a viewer’s interests, and direct them specific marketing. Some examples include: cookies used for remarketing, or interest-based advertising.

Cookies Details‎

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

# User presence and status | Slack

The Slack developer docs are moving! We've been working hard at building out a new docs experience at [docs.slack.dev](https://docs.slack.dev/) — now in beta! You can start using the new docs today, but we'll keep the content on both sites up to date during the transition.

[Learn more](https://api.slack.com/changelog/2024-12-api-site-migration)

# User presence and status

Slack users can toggle whether they are marked active or away. They can also set their own custom status, informing their workspace not only that they are _at lunch_, but exactly what they are eating.

## Custom status

![A set custom status as it appears within a conversation](https://a.slack-edge.com/80588/img/api/custom_status_in_message.png)

Users can declare their status by selecting a custom emoji icon and string of text to represent their "current status" — maybe they're in another office, on the good old telephone, sailing, vacationing in the sticks, or possibly eaten by a grue.

Some users want to fly the freak flag and use this space to wax poetic while others won't touch the stuff, or only in the most perfunctory way.

We encourage developers to embrace all the ways users and workspaces enjoy utilizing custom status. Slack is where workplay happens.

Custom status is part of a user's profile and setting status requires the `users.profile:write` scope. At this time, bot users do not have a user profile and do not have a status.

Admins on paid teams may also set a user's status by passing the `user` parameter to the [`users.profile.set`](https://api.slack.com/methods/users.profile.set) method.

### Reading statuses

Determine a user's currently set custom status by consulting their profile. You'll find profiles attached to user objects returned by [`users.list`](https://api.slack.com/methods/users.list) and [`users.info`](https://api.slack.com/methods/users.info). Both methods require the `users:read` OAuth scope.

More directly retrieve status for a specific user with [`users.profile.get`](https://api.slack.com/methods/users.profile.get) with the `users.profile:read` scope.

A user's custom status is represented by the `status_text`, `status_emoji`, and `status_expiration` profile attributes.

- `status_text` \- a string of no more than 100 characters; does not support markup or other formatting, like user mentions. May contain `:emoji:` references.
- `status_emoji` \- a string corresponding to an emoji installed on the workspace. Animated emoji will appear frozen. When clearing the attribute, a default emoji (currently `💬` / `:speech_balloon:`) will be selected for the user.
- `status_expiration` \- an integer specifying seconds since the epoch, more commonly known as "UNIX time". When it becomes this time, the status will be reset. When `0` or omitted, the status does not expire.

To be notified when status and other profile fields change, subscribe to [`user_change`](https://api.slack.com/events/user_change) events in the [Events API](https://api.slack.com/events-api) or use the [RTM API](https://api.slack.com/rtm) to stream and monitor.

### Writing custom statuses

Set a user's custom status by using their access token with [`users.profile.set`](https://api.slack.com/methods/users.profile.set) and the `users.profile:write` scope.

You'll need to provide the `profile` parameter a URL-encoded JSON string containing at least the `status_text` attribute.

For example, to set a non-expiring custom status of `riding a train` with an emoji set to this idyllic scene: `🚞`, build a JSON payload like this:

```json hljs
Copy{
    "status_text": "riding a train",
    "status_emoji": ":mountain_railway:",
    "status_expiration": 0
}

```

Next, place the custom status fields within the user's `profile` and use [`users.profile.set`](https://api.slack.com/methods/users.profile.set). In this example, we're posting with JSON and using a user token :

```http hljs
CopyPOST /api/users.profile.set
Host: slack.com
Content-type: application/json; charset=utf-8
Authorization: Bearer xoxp_secret_token
{
    "profile": {
        "status_text": "riding a train",
        "status_emoji": ":mountain_railway:",
        "status_expiration": 0
    }
}

```

As with other profile fields, these fields may be set on their own or while updating multiple profile fields.

To unset a user's custom status, set both `status_text` and `status_emoji` to empty strings: `""`.

When sending a `application/x-www-form-urlencoded`-based HTTP POST instead, you must provide the `profile` parameter as a URL-encoded string of JSON. We recommend using `application/json` to avoid any encoding errors.

### Expiring custom statuses

Automatically expire a custom status by setting `status_expiration` to an integer-based Unix timestamp, like `1532627506`.

For example, to set a custom status of `🚞 riding the train home` and have it expire on July 26th, 2018 at 17:51:46 UTC, construct this JSON payload:

```json hljs
Copy{
    "status_text": "riding the train home",
    "status_emoji": ":mountain_railway:",
    "status_expiration": 1532627506
}

```

That's how to sync status with calendars, cubicles, conference calls, and bathroom stalls.

* * *

## User presence

A user can have one of two possible presence values, `active` or `away`. A user
is active if they have at least one client connected to Slack, and they are not
marked as "away". There are two ways a user can be marked as away: automatic
and manual.

### Automatic away

The Slack message servers will automatically detect activity in the client. After 10 minutes with no activity, the user is automatically marked as `away`. There is some additional nuance to that dependent on the client, explained in detail in our [Help Center](https://slack.com/help/articles/201864558#desktop-3).

These auto-away rules do not apply to [Bot Users](https://api.slack.com/bot-users).

### Manual away

An application can call [`users.setPresence`](https://api.slack.com/methods/users.setPresence)
to manually mark a user as `away` or `auto`. A manual status set using this
method will persist between connections.

A manual `away` status set using this method overrides the automatic presence
determined by the message server.

Setting presence back to `auto` indicates that the automatic status should be used instead. There's no way to force a user status to `active`.

## Bot presence

[Bot users](https://api.slack.com/bot-users) have their own form of being present on Slack.

When marked `away`, bots will have a grey circle next to their name. Many users interpret this demarcation to mean your bot is not currently available.

And when they are `active`, bots will have a green dot there. Users have been known to consider your green dot a badge of conversational readiness.

It's either/or. `away` or `active`. Grey or green (or maybe grey and orange — the color of the active dot may vary when [different Slack client themes](https://slack.com/intl/en-ie/help/articles/205166337-Change-your-Slack-theme) are used).

Please don't use presence to telegraph Morse code or teach your bot to speak the binary language of moisture vaporators. Use [`chat.postMessage`](https://api.slack.com/methods/chat.postMessage) for that.

### Events API bots

If your bot user runs on the [Events API](https://api.slack.com/apis/connections/events-api), you can only toggle your bot's `active` or `away` status by [managing your app](https://api.slack.com/apps) and its _Bot Users_ panel, or for apps published in the Slack Marketplace, on the _Live App Settings_ panel.

![Toggling bot user presence for the events API](https://a.slack-edge.com/80588/img/api/events-api-bot-presence.png)

When set to _Off_, your bot user is only marked as online if it's connected to the RTM API.

When set to _On_, your bot user will be marked as _active_ and present. That green dot is all yours. Just toggle back _Off_ again to be marked _away_.

Your bot user's [profile](https://api.slack.com/methods/users.profile.get) will include a `always_active` field set to `true`. Counter-intuitively, your bot's `presence` field will remain `away`. That's the bad news.

The good news is that `always_active` will be interpreted by Slack clients as if the bot user's presence were `active`. Yes, you're awarded that green dot.

### RTM bots

If your bot user runs on the [RTM API](https://api.slack.com/rtm), your bot will be marked `active` to users whenever connected to the RTM API.

Bots cannot set their presence to `active` with [`users.setPresence`](https://api.slack.com/methods/users.setPresence). RTM bots _can_ use it to set it to `away`. Or you can always automatically mark your bot as `away` by disconnecting from your websocket.

## Determining user presence

**RTM API Presence is now only available via subscription.**
As of January 2018, [`presence_change`](https://api.slack.com/events/presence_change) events are not dispatched without [_presence subscriptions_](https://api.slack.com/docs/presence-and-status) established with [`presence_sub`](https://api.slack.com/events/presence_sub). Relatedly, current user presence status is no longer communicated in [`rtm.start`](https://api.slack.com/methods/rtm.start). [Learn more](https://api.slack.com/changelog/2018-01-prese).

### Presence subscriptions over RTM

Presence subscriptions are required to track `presence_change` events over RTM.

Subscribe to `presence_change` events for specific users by sending a [`presence_sub`](https://api.slack.com/events/presence_sub) event into the websocket.

For instance, to subscribe to `presence_change` events for users `U123456` and `W123456`, write the following JSON blob into an established websocket:

```json hljs
Copy{
    "type": "presence_sub",
    "ids": [\
        "U123456",\
        "W123456"\
    ]
}

```

The message server will respond with `presence_change` events indicating the current presence state of any users added to the presence subscription.

Here's what you need to know about presence subscriptions:

- You must declare your entire list of user IDs to subscribe to in _**each**_ request.

  - Add users by appending them to your array of `ids`.
  - Remove users by removing them from your array of `ids`.
- Subscribing to all user's presence events requires specifying every user's ID. This is not recommended, especially on large workspaces.
  - For best results, limit subscriptions to only those users you absolutely need presence information for. 500 users is a good maximum.
- Presence subscriptions work best with [batched](https://api.slack.com/apis/presence-and-status#batching) `presence_change` events.
- Upon connecting, your app will have no presence subscriptions.
- Presence subscriptions only last the duration of a websocket session. Disconnecting means needing to subscribe again.
- By specifying an [Enterprise Grid](https://api.slack.com/enterprise-grid) user ID belonging to a user on another workspace within the same Enterprise Grid, your app can subscribe to cross-workspace `presence_change` events.

Presence subscriptions are now effectively required, as of January 2018. [Learn more](https://api.slack.com/changelog/2018-01-presence-present-and-future).

`presence_sub` is rate limited and there are upper bounds to the amount of data posted in a single event.

### Presence querying with the RTM API

Writing a [`presence_query`](https://api.slack.com/events/presence_query) event to the WebSocket will perform a query operation for a list of up to 500 user IDs.

To look up users `U123456` and `W123456`, send a query like:

```json hljs
Copy{
    "type": "presence_query",
    "ids": [\
        "U123456",\
        "W123456"\
    ]
}

```

In response, you'll receive [`presence_change`](https://api.slack.com/events/presence_change) events for the matching users.

`presence_query` is rate limited and there are upper bounds to the amount of data posted in a single event.

### Presence querying with the Web API

When using our [Web API](https://api.slack.com/web), you can call the
[`users.getPresence`](https://api.slack.com/methods/users.getPresence) method to get the user's
current presence value.

### Presence subscriptions over Events API

Presence-related events cannot be tracked using the [Events API](https://api.slack.com/events-api) at this time.

### Batched presence events

Traditionally, using the [Real Time Messaging API](https://api.slack.com/rtm) the initial call to
[`rtm.start`](https://api.slack.com/methods/rtm.start) or [`rtm.connect`](https://api.slack.com/methods/rtm.connect) would include the current presence value for every member of your workspace. If their presence value changes after that, a [`presence_change`](https://api.slack.com/events/presence_change) event would be sent.

Now presence events must be batched together into a special version of the `presence_change` event that includes a `users` array instead of a singular `user` field. You must enable this new behavior by passing the `batch_presence_aware=1` parameter to `rtm.start` or `rtm.connect`. `presence_change` events will otherwise no longer dispatch after November 15, 2017.

Initial presence state is no longer described when connecting to [`rtm.start`](https://api.slack.com/methods/rtm.start).

**[Which API is right for me?](https://api.slack.com/docs?ref=unit)**

We'll help you [make decisions](https://api.slack.com/docs?ref=unit) based on your goals and our capabilities.

![Slack Technologies Company Logo](https://cdn.cookielaw.org/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/1ce30484-b023-4ff1-a118-3a9dc53fce45/f83dd0bf-3d5c-47ca-b065-8f247adfeacd/rsz_slack_rgb.png)

## Privacy Preference Center

We use three kinds of cookies on our websites: required, functional, and advertising. You can choose whether functional and advertising cookies apply. Click on the different cookie categories to find out more about each category and to change the default settings. [More information](https://slack.com/cookie-policy)

Allow All

### Manage Consent Preferences

#### Required Cookies

Always Active

Required cookies are necessary for basic website functionality. Some examples include: session cookies needed to transmit the website, authentication cookies, and security cookies.

Cookies Details‎

#### Functional Cookies

Functional Cookies

Functional cookies enhance functions, performance, and services on the website. Some examples include: cookies used to analyze site traffic, cookies used for market research, and cookies used to display advertising that is not directed to a particular individual.

Cookies Details‎

#### Advertising Cookies

Advertising Cookies

Advertising cookies track activity across websites in order to understand a viewer’s interests, and direct them specific marketing. Some examples include: cookies used for remarketing, or interest-based advertising.

Cookies Details‎

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

# Using Slack Connect API methods | Slack

The Slack developer docs are moving! We've been working hard at building out a new docs experience at [docs.slack.dev](https://docs.slack.dev/) — now in beta! You can start using the new docs today, but we'll keep the content on both sites up to date during the transition.

[Learn more](https://api.slack.com/changelog/2024-12-api-site-migration)

# Using Slack Connect API methods

[Slack Connect](https://api.slack.com/apis/channels-between-orgs) allows users between different workspaces and organizations to work together on Slack.

Slack Connect API methods offer capabilities for managing and automating your Slack Connect processes. Here's some of the ways these API methods can empower you:

✨ Invite users from external organizations to new channels and accept Slack Connect channel invitations when installed on the target workspace.

✨ Integrate Slack Connect management into your onboarding and offboarding processes. Automatically invite new partners and collaborators, or disconnect from those who are leaving.

✨ Schedule regular audits and maintenance tasks to keep your Slack Connect connections current and secure. Automate the disconnection of outdated or unnecessary connections.

Read on for more details and use cases.

* * *

## Creating an app to interact with Slack Connect

You can use Slack Connect API methods within both workflow apps and granular bot apps. They are set up differently, however.

To create a workflow app, head to the [Deno Slack SDK quickstart](https://api.slack.com/automation/quickstart). We also recommend reading our [Governing Slack Connect invites](https://api.slack.com/automation/governing-slack-connect-invites) guide for an example on using Slack Connect API methods, scopes, and events with the Deno Slack SDK and the Slack CLI.

Scopes are given to workflow apps within the [App manifest](https://api.slack.com/automation/manifest). Workflow apps can't subscribe to events, but can have an [event trigger](https://api.slack.com/automation/triggers/event) for some events. All the events listed on this page have corresponding event triggers.

To create a granular bot app, head to the [quickstart](https://api.slack.com/quickstart) guide and [create a new app](https://api.slack.com/apps?new_app=1). Scopes are given to granular bot apps within the _App Settings_. Granular bots can subscribe to events within the _Events API_ section of the _App Settings_ page.

* * *

## Managing your app's Slack Connect invitations

Your app can be invited to a Slack Connect Channel. Use the [`shared_channel_invite_received`](https://api.slack.com/events/shared_channel_invite_received) event to be notified when suitors call.

The `shared_channel_invite_received` event is fired when a shared channel invite was sent. This event will fire **only** if the [`conversations.inviteShared`](https://api.slack.com/methods/conversations.inviteShared) API method is called to invite an app to a Slack Connect channel.

### Accept invitations

In order for your app to _act_ upon the invite, it'll need to have the proper scopes:

- [`conversations.connect:read`](https://api.slack.com/scopes/conversations.connect:read) — This scope allows your app to handle events when your app is invited to a Slack Connect channel.
- [`conversations.connect:write`](https://api.slack.com/scopes/conversations.connect:write) — This scope allows your app to send and accept invitations to Slack Connect and receive events when invitations are accepted.

Use the [`conversations.acceptSharedInvite`](https://api.slack.com/methods/conversations.acceptSharedInvite) method to accept an invite to a Slack Connect channel. You'll have the option to name the channel if the channel hasn't already been created yet by passing the `channel_name` parameter. Provide the invitation ID from the [`shared_channel_invite_received`](https://api.slack.com/events/shared_channel_invite_received) event response.

You can also use the `free_trial_accepted` parameter to start a free trial for your workspace in order to use Slack Connect, as long as you're eligible.

* * *

## Inviting users to Slack Connect channels

Your app can invite users from external organizations to a channel, turning the channel into a Slack Connect channel in the process.

It'll need the proper scope:

- [`conversations.connect:write`](https://api.slack.com/scopes/conversations.connect:write) — This scope allows your app to send and accept invitations to Slack Connect and receive events when invitations are accepted.

Then use the [`conversations.inviteShared`](https://api.slack.com/methods/conversations.inviteShared) method to invite users via email or via user ID.

If your app is already installed on the target organization, you can invite it directly and therefore automate both inviting and accepting invitations in order to connect two or more organizations.

Your app does **not** need to handle approval of Slack Connect in order to invite users. You can invite users and then wait for manual approval by Admins if that approval is necessary on your workspace or the target workspace.

Many workspaces require **approval** by an Admin for Slack Connect channels (in addition to a user accepting an invitation). Alternatively, you can manage approval of the channel invitations.

* * *

## Managing workspace invitations

Since many workspaces require Admin approval for the creation of Slack Connect channels, your app can manage that task, with the help of an installing user who grants your app a user token. If the installing user has the authority to manage Slack Connect approval, you're good to go — your app can make use of that authority in the user's stead.

The following events help you stay on top of workspace invitations.

- [`shared_channel_invite_accepted`](https://api.slack.com/events/shared_channel_invite_accepted) — This event notifies your app when an invite sent by your workspace or organization has been accepted.
- [`shared_channel_invite_approved`](https://api.slack.com/events/shared_channel_invite_approved) — This event notifies your app when an invitation has been approved.
- [`shared_channel_invite_declined`](https://api.slack.com/events/shared_channel_invite_declined) — This event notifies your app when an invitation has been declined.

In order for your app to _act_ upon the the invitations, it'll need to have the proper scope:

- [`conversations.connect:manage`](https://api.slack.com/scopes/conversations.connect:manage) — This scope allows your app to approve, decline, or list Slack Connect invitations. Since approval requires more authority than accepting invitations, apps with this feature can only be installed by a workspace owner or admin.

### Approve invitations

With the `conversations.connect:manage` scope, your app can call the [`conversations.approveSharedInvite`](https://api.slack.com/methods/conversations.approveSharedInvite) method to approve a pending invitation. Provide the invitation ID from the [`shared_channel_invite_accepted`](https://api.slack.com/events/shared_channel_invite_accepted) event response.

You can approve from the perspective of the originating organization _or_ the target organization, depending on where your app is installed.

### Decline invitations

You can also decline pending invitations with the [`conversations.declineSharedInvite`](https://api.slack.com/methods/conversations.declineSharedInvite) method. Provide the invitation ID from the [`shared_channel_invite_accepted`](https://api.slack.com/events/shared_channel_invite_accepted) event response.

### List invitations

To list shared channel invites that have been generated or received but have not been approved by all parties, use the [`conversations.listConnectInvites`](https://api.slack.com/methods/conversations.listConnectInvites) method. If your app is installed at the organization level, you'll be able to list all the pending invitations in all workspaces, but you can also specify a particular channel.

### Governing invitations

You can choose to add an approval step to the Slack Connect process before invitations are sent to external people.

We have a dedicated guide on automating the governing of Slack Connect invitations! Visit the [Governing Slack Connect invites](https://api.slack.com/automation/governing-slack-connect-invites) page for all the details.

If you choose to apply automation rules before channel invitations are sent, you can listen for the [`shared_channel_invite_requested`](https://api.slack.com/events/shared_channel_invite_requested) event. You can also list all the requests needing approval before being sent with the [`conversations.requestSharedInvite.list`](https://api.slack.com/methods/conversations.requestSharedInvite.list) method.

When enabled, external user invitations will not be sent until they are approved to send. To approve an invitation to be sent, use the [`conversations.requestSharedInvite.approve`](https://api.slack.com/methods/conversations.requestSharedInvite.approve) API method. To deny an invitation to be sent use the [`conversations.requestSharedInvite.deny`](https://api.slack.com/methods/conversations.requestSharedInvite.deny) API method.

* * *

## Viewing connected organizations and users

You can use Slack Connect API methods to find information on connected organizations and users. The relevant methods will require a Slack Connect specific scope: the [`conversations.connect:manage`](https://api.slack.com/scopes/conversations.connect:manage) scope.

To view details about external teams connected via Slack Connect, use the [`team.externalTeams.list`](https://api.slack.com/methods/team.externalTeams.list) method.

To look up if a specific user is on Slack (and is also [discoverable](https://slack.com/help/articles/5535749574803-Manage-Slack-Connect-discoverability-for-your-organization)), use the [`users.discoverableContacts.lookup`](https://api.slack.com/methods/users.discoverableContacts.lookup) method.

* * *

## Setting Slack Connect channels posting permissions

Slack Connect channels have two types of posting permissions:

- _Permission only to post_
- _Permission to post, invite, and more_

You can pick the permission level using the [`conversations.externalInvitePermissions.set`](https://api.slack.com/methods/conversations.externalInvitePermissions.set) method. Be sure to provide your app the [`conversations.connect:manage`](https://api.slack.com/scopes/conversations.connect:manage) scope.

* * *

## Disconnecting a Slack Connect channel

Your app can disconnect Slack Connect channels. It'll need the proper _Admin_ scope:

- [`admin.conversations:write`](https://api.slack.com/scopes/admin.conversations:write) — This scopes allows your app to start new conversations, modify conversations and modify channel details.

Then use the [`admin.conversations.disconnectShared`](https://api.slack.com/methods/admin.conversations.disconnectShared) method to disconnect the Slack Connect channel.

### Disconnect all Slack Connect channels from another organization

To sever all ties with another organization, you can disconnect all Slack Connect channels and direct messages (DMs) from that organization.

You'll need the proper `write` scopes for all relevant message types, alongside the [`conversations.connect:manage`](https://api.slack.com/scopes/conversations.connect:manage) scope.

Then use the [`team.externalTeams.disconnect`](https://api.slack.com/methods/team.externalTeams.disconnect) method and say goodbye.

**Gone, but not forgotten**

Disconnecting from an organization ends all communication, but depending on permissions, still allows access to conversation history. Refer to [this help center article](https://slack.com/help/articles/360063030933-Slack-Connect--Disconnect-from-an-organization-) for the expected behavior of disconnecting conversations.

![Slack Technologies Company Logo](https://cdn.cookielaw.org/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/1ce30484-b023-4ff1-a118-3a9dc53fce45/f83dd0bf-3d5c-47ca-b065-8f247adfeacd/rsz_slack_rgb.png)

## Privacy Preference Center

We use three kinds of cookies on our websites: required, functional, and advertising. You can choose whether functional and advertising cookies apply. Click on the different cookie categories to find out more about each category and to change the default settings. [More information](https://slack.com/cookie-policy)

Allow All

### Manage Consent Preferences

#### Required Cookies

Always Active

Required cookies are necessary for basic website functionality. Some examples include: session cookies needed to transmit the website, authentication cookies, and security cookies.

Cookies Details‎

#### Functional Cookies

Functional Cookies

Functional cookies enhance functions, performance, and services on the website. Some examples include: cookies used to analyze site traffic, cookies used for market research, and cookies used to display advertising that is not directed to a particular individual.

Cookies Details‎

#### Advertising Cookies

Advertising Cookies

Advertising cookies track activity across websites in order to understand a viewer’s interests, and direct them specific marketing. Some examples include: cookies used for remarketing, or interest-based advertising.

Cookies Details‎

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

# Socket Mode | Slack

The Slack developer docs are moving! We've been working hard at building out a new docs experience at [docs.slack.dev](https://docs.slack.dev/) — now in beta! You can start using the new docs today, but we'll keep the content on both sites up to date during the transition.

[Learn more](https://api.slack.com/changelog/2024-12-api-site-migration)

# Socket Mode

Socket Mode allows your app to use [the Events API](https://api.slack.com/apis/connections/events-api) and [interactive features](https://api.slack.com/interactivity)— _without_ exposing a public HTTP **Request URL**.

Instead of sending payloads to a public endpoint, Slack will use a [WebSocket URL](https://tools.ietf.org/html/rfc6455) to communicate with your app. WebSockets use a bidirectional stateful protocol with low latency to communicate between two parties—in this case, Slack and your app.

Unlike a public HTTP endpoint, the WebSocket URL you listen to is not static. The URL is created at runtime by calling the [`apps.connections.open`](https://api.slack.com/methods/apps.connections.open) method, and it refreshes regularly.

Socket Mode helps developers working behind a corporate firewall, or who have other security concerns that don't allow exposing a static HTTP endpoint.

You can still switch between a direct HTTP endpoint and Socket Mode at any time in the [app settings](https://api.slack.com/apps).

We recommend [using our Bolt frameworks or SDKs for Java, Javascript, or Python](https://api.slack.com/apis/connections/socket#sdks) to handle the details of Socket Mode. The process is streamlined, and you get access to all the other pleasant features of our SDKs.

Apps using Socket Mode are **not** currently allowed in the public Slack Marketplace.

Socket Mode is **only** available for apps using [granular permissions](https://api.slack.com/quickstart). If you created your app on or after December of 2019, good news: your app already uses the new permissions. Otherwise, you may have to [migrate](https://api.slack.com/authentication/migration) your classic app to use granular permissions before turning on Socket Mode.

* * *

## Setting up an app for Socket Mode

App setup for Socket Mode has three steps:

1. [Create an app](https://api.slack.com/apis/socket-mode#creating)
2. [Toggle on Socket Mode](https://api.slack.com/apis/socket-mode#toggling)
3. [Generate an app-level token](https://api.slack.com/apis/socket-mode#token)

### 1\. Create an app

If you don't have one already, you'll need to create a Slack app:

[Create a Slack app](https://api.slack.com/apps?new_app=1&ref=bolt_start_hub)

Fill out your **App Name** and select the Development Workspace where you'll play around and build your app.

Socket Mode apps currently can't be listed in the Slack Marketplace. If you'd like to distribute your Socket Mode app to your entire Enterprise Grid organization, you can [make your app deployable organization-wide](https://api.slack.com/enterprise/apps).

#### Creating an app with a manifest

You can [create an app through a manifest](https://api.slack.com/reference/manifests) and turn on Socket Mode by configuring a few options. Below is a YAML example which includes adding a bot user with the [`app_mentions:read`](https://api.slack.com/scopes/chat:write.customize) scope and subscribing to the [`app_mention`](https://api.slack.com/events/app_mention) event subscription:

```yaml
Copy_metadata:
  major_version: 1
display_information:
  name: Demo App
features:
  bot_user:
    display_name: Demo App
    always_online: false
oauth_config:
  scopes:
    bot:
      - app_mentions:read
settings:
  event_subscriptions:
    bot_events:
      - app_mention
  org_deploy_enabled: false
  socket_mode_enabled: true
  is_hosted: false
  token_rotation_enabled: false

```

### 2\. Toggle on Socket Mode

In your [app settings](https://api.slack.com/apps), navigate to the **Socket Mode** section. Toggle the **Enable Socket Mode** button to turn on receiving payloads via WebSockets.

Socket Mode can be toggled on or off whenever you'd like. When you toggle Socket Mode on, you'll **only** receive events and interactive payloads over your WebSocket connections—not over HTTP.

If your app is actively receiving events when you toggle Socket Mode on, you may lose events until you establish a connection to your WebSocket URL.

At this point, you can subscribe to some events in the **Event Subscriptions** section of your app settings. A favorite is the [`app_mention`](https://api.slack.com/events/app_mention) event.

When using Socket Mode, your app does not need a Request UR to use the [Events API](https://api.slack.com/apis/connections/events-api). Your app's connection to the WebSocket replaces the need for Slack to dispatch to a Request URL.

### 3\. Generate an app-level token

When you toggle Socket Mode on, the app settings will guide you through obtaining an app-level token if you haven't created one.

You can also create or generate an app-level token manually. Under **Basic Information**, scroll to the **App-level tokens** section and click the button to generate an [app-level token](https://api.slack.com/concepts/token-types#app).

Your app-level token allows your app, either directly or with an SDK, to generate a WebSocket URL for communication with Slack via the [`apps.connections.open`](https://api.slack.com/methods/apps.connections.open) method.

You're finished with setting up your app for Socket Mode. The rest can be handled by [using the Slack SDKs](https://api.slack.com/apis/socket-mode#sdks). Or, you can [implement the Socket Mode protocol yourself](https://api.slack.com/apis/socket-mode#implementing).

* * *

## Using Socket Mode with Bolt SDKs

Socket Mode is automatically supported by each of our frameworks and SDKs.

The only thing you need to do is set your app-level token as an environment variable:

```hljs bash
Copyexport SLACK_APP_TOKEN='xapp-***'

```

Now you can lean on the [Bolt framework](https://api.slack.com/tools/bolt) for [Javascript](https://api.slack.com/tools/bolt-js), [Java](https://api.slack.com/tools/bolt-java), or [Python](https://api.slack.com/tools/bolt-python) to take care of the rest.

Here's some code to get your app running in Socket Mode using Bolt:

Capturing events using Socket Mode

Java

JavaScript

Python

Java

```hljs apiDocs__codeCopyPanel java

Copypackage hello;

import com.slack.api.bolt.App;
import com.slack.api.bolt.AppConfig;
import com.slack.api.bolt.socket_mode.SocketModeApp;
import com.slack.api.model.event.AppMentionEvent;

// Required dependencies:
// implementation("com.slack.api:bolt-socket-mode:(latest version)")
// implementation("org.glassfish.tyrus.bundles:tyrus-standalone-client:1.17")
public class MyApp {

  public static void main(String[] args) throws Exception {
    String botToken = System.getenv("SLACK_BOT_TOKEN");
    App app = new App(AppConfig.builder().singleTeamBotToken(botToken).build());
    String appToken = System.getenv("SLACK_APP_TOKEN");
    SocketModeApp socketModeApp = new SocketModeApp(appToken, app);
    socketModeApp.start();
  }
}
```

[Powered by Bolt for Java](https://slack.dev/bolt-java)

JavaScript

```hljs javascript

Code to initialize Bolt app
// Require the Node Slack SDK package (github.com/slackapi/node-slack-sdk)
const { WebClient, LogLevel } = require("@slack/web-api");

// WebClient instantiates a client that can call API methods
// When using Bolt, you can use either `app.client` or the `client` passed to listeners.
const client = new WebClient("xoxb-your-token", {
  // LogLevel can be imported and used to make debugging simpler
  logLevel: LogLevel.DEBUG
});

Copyconst { App } = require('@slack/bolt');

const app = new App({
  token: process.env.BOT_TOKEN,
  appToken: process.env.SLACK_APP_TOKEN,
  socketMode: true,
});

(async () => {
  await app.start();
  console.log('⚡️ Bolt app started');
})();
```

[Powered by Bolt for JavaScript](https://slack.dev/bolt-js)

Python

```hljs apiDocs__codeCopyPanel python

Copyimport os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
```

[Powered by Bolt for Python](https://slack.dev/bolt-python)

If a Bolt SDK suits your goals, then you're ready to to continue developing your app as normal! No need to follow the rest of this guide.

* * *

## Implementing Socket Mode without Bolt

If you prefer to implement the Socket Mode protocol yourself, read on.

You'll need a library or programming language that supports the [WebSocket](https://tools.ietf.org/html/rfc6455) protocol.

Connections refresh regularly. You should be ready to receive and connect to new WebSocket URLs as quickly as possible to maintain service.

### 1\. Call the `apps.connections.open` endpoint

Call the [`apps.connections.open`](https://api.slack.com/methods/apps.connections.open) endpoint with your app-level token to receive a WebSocket URL:

```hljs bash
Copycurl -X POST "https://slack.com/api/apps.connections.open" \
-H "Content-type: application/x-www-form-urlencoded" \
-H "Authorization: Bearer xapp-1-123"

```

Remember to send the token in the `Authorization` header, not as a parameter.

You'll receive a URL in response:

```hljs json
Copy{
    "ok": true,
    "url": "wss:\/\/wss.slack.com\/link\/?ticket=1234-5678"
}

```

You'll notice that, with Socket Mode turned on, your app settings doesn't require or even allow you to enter a **Request URL**. That's because this WebSocket URL replaces the public Request URL that Slack would have sent payloads to.

You can turn off Socket Mode **at any time** to return to the direct HTTP protocol for events and interactive features. If you've already set a **Request URL**, it'll be saved for later once you enter Socket Mode. When you turn Socket Mode off, the Request URL will be used once again to receive events.

* * *

### 2\. Connect to the WebSocket

Use your WebSocket library to connect to the URL specified in the above response.

Here's an example in Javascript:

```hljs javascript
Copyif (response.ok) {
  let wssUrl = response.url;
  let socket = new WebSocket(wssUrl);

  socket.onopen = function(e) {
    // connection established
  }

  socket.onmessage = function(event) {
    // application received message
  }
}

```

One helpful trick: you can append `&debug_reconnects=true` to your WebSocket URL when you connect to it in order to make the connection time significantly shorter (360 seconds). That way, you can test and debug reconnects without waiting around.

After you connect to the WebSocket, Slack will send a `hello` message:

```hljs bash
Copy{
    "type": "hello",
    "connection_info": {
        "app_id": "A1234"
    },
    "num_connections": 1,
    "debug_info": {
        "host": "applink-….",
        "started" "2020-10-11 12:12:12.120",
        "build_number": 54,
        "approximate_connection_time": 3600
    }
}

```

The `approximate_connection_time` (in seconds) can be used to estimate how long the connection will persist until Slack refreshes it.

### Using multiple connections

Socket Mode allows your app to maintain _up to 10_ open WebSocket connections at the same time.

When multiple connections are active, each payload may be sent to _any_ of the connections. It's best not to assume any particular pattern for how payloads will be distributed across multiple open connections.

There are a few reasons to make use of multiple active connections:

- If you'd like to handle a scheduled connection restart gracefully, you can generate an additional connection before the restart occurs.
- If you're having trouble keeping up with a large throughput of events from one connection, multiple connections can allow you to load balance.
- If you'd like to gracefully restart your app's services, you can use multiple connections for temporary active-active redundancy.

* * *

### 3\. Handle disconnects gracefully

Expect disconnects to your WebSocket connection. These may happen when you toggle off Socket Mode in the app settings, or for other reasons.

Here's a disconnect message you'll receive if you toggle off Socket Mode:

```hljs json
Copy{
  "type": "disconnect",
  "reason": "link_disabled",
  "debug_info": {
    "host": "wss-111.slack.com"
  }
}

```

No matter what, you'll need to handle connection refreshes once every few hours.

You may receive a warning about 10 seconds before the disconnect:

```hljs json
Copy{
  "type": "disconnect",
  "reason": "warning",
  "debug_info": {
    "host": "wss-111.slack.com"
  }
}

```

Even if you don't receive a warning, you'll still want to expect a `refresh_requested` message:

```hljs json
Copy{
  "type" : "disconnect",
  "reason": "refresh_requested",
  "debug_info": {
    "host": "wss-111.slack.com"
  }
}

```

You may want to use [multiple connections](https://api.slack.com/apis/socket-mode#connections) in order to maintain uptime during a connection restart.

* * *

### 4\. Receive events

Event payloads sent to your app via Socket Mode are identical to the typical [Events API](https://api.slack.com/apis/connections/events-api) payloads, with some additional metadata:

```hljs json
Copy{
  "payload": <event_payload>,
  "envelope_id": <unique_identifier_string>,
  "type": <event_type_enum>,
  "accepts_response_payload": <accepts_response_payload_bool>
}

```

You can use the `accepts_response_payload` to determine whether a response can include additional information.

Your app still needs to acknowledge receiving _each event_ so that Slack knows whether to retry.

### 5\. Acknowledge events

While acknowledging each event is required, there's no need to verify or validate inbound events, because you're receiving the events over a pre-authenticated WebSocket. Note that this is a different pattern from receiving events directly over HTTP, where validation is required for each event.

Use the `envelope_id` field in the object you receive from your WebSocket to send a response back to Slack acknowledging that you've received the event:

```hljs json
Copy{
    "envelope_id": <$unique_identifier_string>,
    "payload": <$payload_shape> // optional
}

```

* * *

## Using interactive features

[Interactive features](https://api.slack.com/interactivity) also send payloads as normal to your app—along with additional metadata specific to Socket Mode. Here's the general structure to expect:

```hljs json
Copy{
  "payload": <interactive_component_payload>,
  "envelope_id": <unique_identifier_string>,
  "type": <event_type_enum>,
  "accepts_response_payload": <accepts_response_payload_bool>
}

```

See below for specific examples on the following:

- [Slash commands](https://api.slack.com/apis/socket-mode#command)
- [Block Kit buttons](https://api.slack.com/apis/socket-mode#button)
- [App Home interactions](https://api.slack.com/apis/socket-mode#home)
- [Modals](https://api.slack.com/apis/socket-mode#modal)
- [Dynamic menus](https://api.slack.com/apis/socket-mode#menu)

### Slash commands

Here's what's sent:

```hljs json
Copy{
  "payload": {
    "token": "bHKJ2n9AW6Ju3MjciOHfbA1b",
    "team_id": "T123ABC456",
    "team_domain": "maria",
    "channel_id": "C123ABC456",
    "channel_name": "general",
    "user_id": "U123ABC456",
    "user_name": "rainer",
    "command": "/randorilke",
    "text": "",
    "response_url": "https://rilke.slack.com/commands/T0SNL8S4S/37053613554/YMB2ZESDLNjNLqSFZ1quhNAh",
    "trigger_id": "37053613634.26768298162.440952c06ef4de2653466a48fe495f93"
  },
  "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545",
  "type": "slash_commands",
  "accepts_response_payload": true
}

```

Here's an example response from your app:

```hljs json
Copy{
  "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545",
  "payload": {
    "blocks": [\
      {\
        "type": "section",\
        "text": {\
          "type": "mrkdwn",\
          "text": "Book of Hours"\
        }\
      },\
      {\
        "type": "section",\
        "text": {\
          "type": "mrkdwn",\
          "text": "Duino Elegies"\
        }\
      }\
    ]
  }
}

```

### Block Kit buttons

Here's what your app receives:

```hljs bash
Copy{
  "payload": {
    "type": "block_actions",
    "team": {
      "id": "T123ABC456",
      "domain": "Duino"
    },
    "user": {
      "id": "U123ABC456",
      "username": "RMR",
      "team_id": "T123ABC456"
    },
    "api_app_id": "AABA1ABCD",
    "token": "9s8d9as89d8as9d8as989",
    "container": {
      "type": "message_attachment",
      "message_ts": "1548261231.000200",
      "attachment_id": 1,
      "channel_id": "C123ABC456",
      "is_ephemeral": false,
      "is_app_unfurl": false
    },
    "trigger_id": "12321423423.333649436676.d8c1bb837935619ccad0f624c448ffb3",
    "channel": {
      "id": "C123ABC456",
      "name": "review-updates"
    },
    "message": {
      "bot_id": "B123ABC456",
      "type": "message",
      "text": "Who if I cried out would hear me.",
      "user": "U123ABC456",
      "ts": "1548261231.000200",
      ...
    },
    "response_url": "https://hooks.slack.com/actions/AABA1ABCD/1232321423432/D09sSasdasdAS9091209",
    "actions": [{\
      "action_id": "WaXA",\
      "block_id": "=qXel",\
      "text": {\
        "type": "plain_text",\
        "text": "View",\
        "emoji": true\
      },\
      "value": "click_me_123",\
      "type": "button",\
      "action_ts": "1548426417.840180"\
    }]
  },
  "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545",
  "type": "interactive",
  "accepts_response_payload": true
}

```

Here's an example response from your app:

```hljs json
Copy{
  "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545"
}

```

### App Home interactions

Here's what your app receives:

```hljs bash
Copy{
  "payload": {
    "type": "app_home_opened",
    "user": "U123ABC456",
    "channel": "C123ABC456",
    "event_ts": "1515449522000016",
    "tab": "home",
    "view": {
      "id": "V123ABC456",
      "team_id": "T123ABC456",
      "type": "home",
      "blocks": [\
        ...\
      ],
      "private_metadata": "",
      "callback_id": "",
      "state":{
        ...
      },
      "hash":"1231232323.12321312",
      "clear_on_close": false,
      "notify_on_close": false,
      "root_view_id": "V123ABC456",
      "app_id": "A123ABC456",
      "external_id": "",
      "app_installed_team_id": "T123ABC456",
      "bot_id": "B123ABC456"
    }
  }
  "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545",
  "type": "events_api",
  "accepts_response_payload": false
}

```

Here's an example response from your app:

```hljs json
Copy{
  "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545"
}

```

Here's what your app receives:

```hljs bash
Copy{
  "payload": {
    "type": "view_submission",
    "team": { ... },
    "user": { ... },
    "view": {
      "id": "V123ABC456",
      "type": "modal",
      "title": { ... },
      "submit": { ... },
      "blocks": [ ... ],
      "private_metadata": "shhh-its-secret",
      "callback_id": "modal-with-inputs",
      "state": {
        "values": {
          "multi-line": {
            "ml-value": {
              "type": "plain_text_input",
              "value": "Archaic torso of Apollo"
            }
          }
        }
      },
      "hash": "156663117.cd33ad1f"
    }
  },
  "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545",
  "type": "interactive",
  "accepts_response_payload": true
}

```

Here's an example response from your app:

```hljs json
Copy{
  "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545",
  "payload": {
    "response_action": "update",
    "view": {
      "type": "modal",
      "callback_id": "updated-view-id",
      "title": {
        "type": "plain_text",
        "text": "Updated view"
      },
      "blocks": [{\
        "type": "section",\
        "text": {\
          "type": "plain_text",\
          "text": "You must change your life."\
        }\
      }]
    }
  }
}

```

### Dynamic menus

Here's what your app receives:

```hljs json
Copy{
  "payload": {
    "type": "block_suggestion",
    "user": {
      "id": "U123ABC456",
      "name": "panther"
    },
    "team": {
      "id": "T123ABC456",
      "domain": "rilke"
    },
    "block_id": "search-block",
    "action_id": "seach-action",
    "value": "an",
    "view": {"id": "V111", "type": "modal", "callback_id": "view-id"}
  },
  "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545",
  "type": "interactive",
  "accepts_response_payload": true
}

```

Here's an example response from your app:

```hljs json
Copy{
  "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545",
  "payload": {
    "options": [\
      {\
        "text": {\
          "type": "plain_text",\
          "text": "Give me your hand"\
        },\
        "value": "AI-2323"\
      },\
      {\
        "text": {\
          "type": "plain_text",\
          "text": "Beauty and terror"\
        },\
        "value": "SUPPORT-42"\
      }\
    ]
  }
}

```

![Slack Technologies Company Logo](https://cdn.cookielaw.org/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/1ce30484-b023-4ff1-a118-3a9dc53fce45/f83dd0bf-3d5c-47ca-b065-8f247adfeacd/rsz_slack_rgb.png)

## Privacy Preference Center

We use three kinds of cookies on our websites: required, functional, and advertising. You can choose whether functional and advertising cookies apply. Click on the different cookie categories to find out more about each category and to change the default settings. [More information](https://slack.com/cookie-policy)

Allow All

### Manage Consent Preferences

#### Required Cookies

Always Active

Required cookies are necessary for basic website functionality. Some examples include: session cookies needed to transmit the website, authentication cookies, and security cookies.

Cookies Details‎

#### Functional Cookies

Functional Cookies

Functional cookies enhance functions, performance, and services on the website. Some examples include: cookies used to analyze site traffic, cookies used for market research, and cookies used to display advertising that is not directed to a particular individual.

Cookies Details‎

#### Advertising Cookies

Advertising Cookies

Advertising cookies track activity across websites in order to understand a viewer’s interests, and direct them specific marketing. Some examples include: cookies used for remarketing, or interest-based advertising.

Cookies Details‎

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

# Rate Limits | Slack

The Slack developer docs are moving! We've been working hard at building out a new docs experience at [docs.slack.dev](https://docs.slack.dev/) — now in beta! You can start using the new docs today, but we'll keep the content on both sites up to date during the transition.

[Learn more](https://api.slack.com/changelog/2024-12-api-site-migration)

# Rate Limits

Slack platform features and APIs rely on rate limits to help provide a predictably pleasant experience for users.

The details of how and when rate limiting works _differs_ between features. This article gives an overview of the rate limits you're likely to encounter for Slack platform features, and then notes how the limits apply to each feature.

## Overview

Broadly, you'll encounter limits like these, applied on a " _per API method per app per workspace_" basis.

| Feature/API | Limit | Notes |
| --- | --- | --- |
| Web API Tier 1 | 1+ per minute | Access tier 1 methods infrequently. A small amount of burst behavior is tolerated. |
| Web API Tier 2 | 20+ per minute | Most methods allow at least 20 requests per minute, while allowing for occasional bursts of more requests. |
| Web API Tier 3 | 50+ per minute | Tier 3 methods allow a larger number of requests and are typically attached to methods with paginating collections of conversations or users. Sporadic bursts are welcome. |
| Web API Tier 4 | 100+ per minute | Enjoy a large request quota for Tier 4 methods, including generous burst behavior. |
| Web API Special Tier | _Varies_ | Rate limiting conditions are unique for methods with this tier. For example, [`chat.postMessage`](https://api.slack.com/methods/chat.postMessage) generally allows posting one message per second per channel, while also maintaining a workspace-wide limit. Consult the method's documentation to better understand its rate limiting conditions. |
| Posting messages | 1 per second | Short bursts >1 allowed. If you attempt bursts, there is no guarantee that messages will be stored or displayed to users. If the burst exceeds available limits, users will see an error message indicating that some messages from your app are not being displayed. |
| Incoming webhooks | 1 per second | Short bursts >1 allowed. |
| Events API events | 30,000 deliveries per hour per workspace | Larger bursts are sometimes allowed. |
| Workflow triggers: event triggers | 10,000 per hour |  |
| Workflow triggers: webhook triggers | 10 per minute |  |

Read on for more details on how rate limits are applied to different Slack features and APIs.

## Burst limiting

You'll see mentions of burst tolerance in the chart above; burst limits are similar to rate limits. While a rate limit defines the maximum requests allowed in a specific timeframe (typically per minute), a burst limit defines the maximum rate of requests allowed concurrently.

Slack does not share precise burst limits externally, because these numbers are subject to change and we don't want you to to build your app with a specific burst capacity in mind only to have to change it later. However, we do recommend you design your apps with a limit of 1 request per second for any given API call, knowing that we'll allow it to go over this limit as long as this is only a temporary burst.

"Why even have burst limits?" you might ask. Slack is primarily a communication tool for humans. We try to detect apps acting spammy, unintentionally or not, and quiet them down to avoid hindering users' ability to communicate and use their workspace's archive.

* * *

## Web API rate limiting

Your app's requests to the [Web API](https://api.slack.com/web) are evaluated per method, per workspace. Rate limit windows are per minute.

Each [Web API method](https://api.slack.com/methods) is assigned one of four _rate limit tiers_, listed [above](https://api.slack.com/apis/rate-limits#overview). Tier 1 accepts the fewest requests and Tier 4 the most. There's also a `special` tier for rate-limiting behavior that's unique to a method.

All Slack plans receive the same rate limit tier for each method.

The _Facts_ section of each method's reference documentation will indicate its rate limit tier. Check out the [`conversations.list` documentation](https://api.slack.com/methods/conversations.list) for an example of a Tier 2 method. Each tier's limits are subject to change.

### Pagination limitation

For methods supporting [cursored pagination](https://api.slack.com/docs/pagination), the rate limit given applies when you're _using_ pagination. If you're not, you'll receive stricter rate limits—for example, you'll be allowed to make fewer requests if you attempt to fetch all of [`users.list`](https://api.slack.com/methods/users.list) without pagination.

## Responding to rate limiting conditions

If you exceed a rate limit when using any of our HTTP-based APIs (including incoming webhooks), Slack will return a `HTTP 429 Too Many Requests` error, and a `Retry-After` HTTP header containing the number of seconds until you can retry.

For example, if your app exceeds the rate limit of `conversations.info`, you might receive a raw HTTP response like this:

```nohighlight
CopyHTTP/1.1 429 Too Many Requests
Retry-After: 30

```

This response instructs your app to wait 30 seconds before attempting to call `conversations.info` with any [token](https://api.slack.com/docs/token-types) awarded to your app from this workspace. By evaluating the `Retry-After` header you can wait for the indicated number of seconds before retrying the same request or continuing to use that method for this workspace.

Calls to other methods on behalf of this workspace are not restricted. Calls to the same method for other workspaces for this app are also not restricted.

## Limits when posting messages

In general, apps may post no more than one message per second per channel, whether a message is posted via [`chat.postMessage`](https://api.slack.com/methods/chat.postMessage), an incoming webhook, or one of the many other ways to send messages in to Slack. We allow bursts over that limit for short periods. However, if your app continues to exceed its allowance over longer periods of time, we will begin rate limiting.

If you go over these limits while using the [Real Time Messaging API](https://api.slack.com/rtm) you will receive an error message as a reply. If you continue to send messages, your app will be disconnected. Continuing to send messages after exceeding a rate limit runs the risk of your app being permanently disabled.

What if your app requires a higher volume of messaging? Other services provide an interface for logging, searching, aggregating, and archiving messages at higher throughputs. These include [Papertrail](https://papertrailapp.com/), [Loggly](https://www.loggly.com/), [Splunk](http://www.splunk.com/) and [LogStash](http://logstash.net/).

## Profile update rate limits

Update a user's profile, including custom status, sparingly. Special [rate limit](https://api.slack.com/docs/rate-limits) rules apply when updating profile data with [`users.profile.set`](https://api.slack.com/methods/users.profile.set). A token may update a single user's profile no more than **10** times per minute. And a single token may only set **30** user profiles per minute. Some burst behavior is allowed.

## Events API

Event deliveries to your server via the Events API are rate limited to 30,000 deliveries per workspace per hour.

When a workspace generates more than 30,000 events, you'll receive an informative event called [`app_rate_limited`](https://api.slack.com/events/app_rate_limited), describing the workspace and timestamp when rate limiting began.

```json hljs
Copy{
    "token": "Jhj5dZrVaK7ZwHHjRyZWjbDl",
    "type": "app_rate_limited",
    "team_id": "T123456",
    "minute_rate_limited": 1518467820,
    "api_app_id": "A123456"
}

```

Learn more about [Events API rate limiting](https://api.slack.com/events-api#rate_limiting) and our tolerance for [delivery failures](https://api.slack.com/events-api#failure_limits).

## RTM APIs (legacy)

### Message delivery

Message delivery to your app is not rate limited over RTM. You'll receive every event the connecting token is allowed to see. You may receive more events than you can come up with, so we recommend decoupling your processing of events from the receiving of them.

### Posting messages

Rate limits _do_ apply to posting messages or other write events to the Real Time Messaging websocket. Please limit writes to 1 per second.

If you sustain writes beyond these limits when using our [Real Time Messaging API](https://api.slack.com/rtm) you will receive an [error message](https://api.slack.com/rtm#errors) as a reply. If you continue to send messages your app will be disconnected.

The message server will disconnect any client that sends a message longer than
16 kilobytes. This includes all parts of the message, including JSON syntax,
not just the message text. Clients should limit messages sent to channels to
4000 characters, which will always be under 16k bytes even with a message
comprised solely of non-BMP Unicode characters at 4 bytes each. If the message
is longer a client should prompt to split the message into multiple messages,
create a snippet or create a post.

### Obtaining websocket URLs

Rate limits also apply to the [`rtm.start`](https://api.slack.com/methods/rtm.start) and [`rtm.connect`](https://api.slack.com/methods/rtm.connect) methods for obtaining the URL needed to connect to a websocket.

Limit requests to these methods to no more than 1 per minute, with some bursting behavior allowed. If you enter rate limit conditions when trying to fetch websocket URLs, you won't be able to reconnect until the window passes.

## Other functionality

We reserve the right to rate limit other functionality to prevent abuse, spam, denial-of-service attacks, or other security issues. Where possible we'll return a descriptive error message, but the nature of this type of rate limiting often prevents us from providing more information.

Recommended reading

- [Using the Slack Web API](https://api.slack.com/web)
- [Block Kit](https://api.slack.com/block-kit)

**[Build custom workflow builder steps with Bolt SDKs](https://api.slack.com/tutorials/tracks/bolt-custom-function?ref=unit)**

Learn how to use our Bolt for Javascript SDK and Bolt for Python SDK to build functions for your team.

![Slack Technologies Company Logo](https://cdn.cookielaw.org/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/1ce30484-b023-4ff1-a118-3a9dc53fce45/f83dd0bf-3d5c-47ca-b065-8f247adfeacd/rsz_slack_rgb.png)

## Privacy Preference Center

We use three kinds of cookies on our websites: required, functional, and advertising. You can choose whether functional and advertising cookies apply. Click on the different cookie categories to find out more about each category and to change the default settings. [More information](https://slack.com/cookie-policy)

Allow All

### Manage Consent Preferences

#### Required Cookies

Always Active

Required cookies are necessary for basic website functionality. Some examples include: session cookies needed to transmit the website, authentication cookies, and security cookies.

Cookies Details‎

#### Functional Cookies

Functional Cookies

Functional cookies enhance functions, performance, and services on the website. Some examples include: cookies used to analyze site traffic, cookies used for market research, and cookies used to display advertising that is not directed to a particular individual.

Cookies Details‎

#### Advertising Cookies

Advertising Cookies

Advertising cookies track activity across websites in order to understand a viewer’s interests, and direct them specific marketing. Some examples include: cookies used for remarketing, or interest-based advertising.

Cookies Details‎

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

[iframe](https://csxd.contentsquare.net/uxa/xdframe-single-domain-1.2.0.html?pid=5540)

# Slack Connect: working with channels between organizations | Slack

The Slack developer docs are moving! We've been working hard at building out a new docs experience at [docs.slack.dev](https://docs.slack.dev/) — now in beta! You can start using the new docs today, but we'll keep the content on both sites up to date during the transition.

[Learn more](https://api.slack.com/changelog/2024-12-api-site-migration)

# Slack Connect: working with channels between organizations

![Shared Channels allows you to collaborate with an external org!](https://a.slack-edge.com/80588/img/api/shared_channel_head@2x.png)

With Slack Connect, channels connect you to people working at other companies and organizations.

The [Conversation APIs](https://api.slack.com/docs/conversations-api) manages most of the complexity for you. While many apps, bots, and other integrations should continue to work with channels that have members from multiple workspaces and organizations, [you may face unexpected quirks](https://api.slack.com/apis/channels-between-orgs#what_to_expect).

If you'd like to directly manage Slack Connect for your organization using an app, check out our documentation on the [Slack Connect APIs](https://api.slack.com/apis/connect). Otherwise, read on to learn how to ensure your app handles Slack Connect gracefully.

## What is Slack Connect?

In Slack Connect, a channel is a bridge between teams that need to work together. Teams use Slack Connect to communicate between workspaces and organizations. Slack Connect allows users of different organizations to chat, share files, and use apps in the same way they communicate with their more immediate colleagues in their own workspace.

## How channels between organizations work

### Messages and files

All workspaces involved in a connected channel can read and send messages, share files, and access the history of shared channels.

### Channel settings

A connected channel may have different settings for each workspace it's party to.

- Channel names may differ. What's one workspace's `#do-stuff` is another workspace's `#do-nothing`. It's best to make no assumptions about channel names and stick only with IDs.
- One workspace might set the channel as private, while the other workspace may set the same channel as public.
- Data retention settings may differ between teams.

With all these differences in channel type settings, you **must** use the new [Conversations API](https://api.slack.com/docs/conversations-api) instead of existing APIs such as `channels.` _, `ims.`_ \`, and `groups.*`

## Technical considerations

Be on the lookout for minor differences in channel, message, user, team and related objects. When a channel can hold multiple teams within it, you'll naturally encounter messages and users originating from other teams.

### Detecting when a channel has members from multiple workspaces or organizations

Your app can learn when channels become shared and unshared with another team by subscribing to the [`channel_shared`](https://api.slack.com/events/channel_shared) and [`channel_unshared`](https://api.slack.com/events/channel_unshared) events in the **Event Subscriptions** tab in your **Apps** page.

To receive all shared events for channels or groups in a workspace, your app will need the `channels:read` or `groups:read` scopes respectively. To receive only shared events for channels and groups your bot user is in, your app just needs the `bot` scope.

Both shared events contain the ID of the channel itself, in addition to the team that the channel was shared or unshared with as follows:

```json hljs
Copy{
    "type": "channel_shared",
    "connected_team_id": "T123ABC456",
    "channel": "C123ABC456",
    "event_ts": "1565722340.000000"
}

```

It may be helpful for your app to note the `connected_team_id`, as it will begin receiving messages and events from users on that external team.

### External members

Your app will receive messages and events from users on external teams. Information about these users will be different than users on the workspace where your app is installed.

![A stranger in shared channels](https://a.slack-edge.com/3efc0/img/api/shared_channels_stranger@2x.png)

_An external member. In their profile, a member from an external team will be marked with a square status indicator next to the username._

- **External members** are members on the other team that your application shares channel membership with.
- **Strangers** are external members on the other team that your application does _not_ have a shared channel in common; you can find out about these members when the other team mentions them in the shared channel or shares one of their messages or files in the shared channel.

The user type object (returned by methods such as [`users.info`](https://api.slack.com/methods/users.info)) provides additional information to identify external members, while withholding some information your app may expect. External members are also returned in the [`conversations.members`](https://api.slack.com/methods/conversations.members) API response.

- If the user is a stranger who isn't in any shared channels, the `is_stranger` flag is set `true`.
- Both the [`users:read.email`](https://api.slack.com/scopes/users:read.email) and [`users:read`](https://api.slack.com/scopes/users:read) OAuth scopes are required to access the `email` field in [user objects](https://api.slack.com/types/user) returned by the [`users.info`](https://api.slack.com/methods/users.info) and [`users.list`](https://api.slack.com/methods/users.list) API methods. [Learn more](https://api.slack.com/changelog/2017-04-narrowing-email-access).
- For external members and strangers, their profile data will not contain any locale information, even if you pass the `include_locale` flag.

Here's an example of a response from [`users.info`](https://api.slack.com/methods/users.info):

```json hljs
Copy{
    "ok": true,
    "user": {
        "id": "U123ABC456",
        "team_id": "T123ABC456",
        "name": "rex",
        "real_name": "Devon Rex",
        "profile": {
            "image_24": "https:\/\/.../11662770033.jpg",
            "team": "T123ABC456",
            "display_name": "eshellstrop"
            // all that other stuff
        },
        "is_stranger": true
    }
}

```

When you specify a user, you need to use a user's `id` instead of their `username`. With the new [name-tagging](https://api.slack.com/apis/changelog/2017-09-the-one-about-usernames) feature, the `username` attribute cannot be relied upon as a unique identifier, and will not work with "foreign" users via the API. For example, you cannot use [`chat.postMessage`](https://api.slack.com/methods/chat.postMessage) with a `username` set to a foreign user.

A bot user is able to DM users on all connected workspaces, as long as users are in a shared channel together.

### Same channel, different setting

When a channel gains members from another workspace or organization via Slack Connect, the channel ID may change depending on its setting.

If the channel is set to private, the ID prefix may change from `G` to `C` (e.g. `G1234567890` becomes `C1234567890`) when it's shared. Subscribe to the [`channel_id_changed` event](https://api.slack.com/events/channel_id_changed) to determine when a private channel's ID has changed because a share has been initiated.

Since each team in the channel can independently decide whether the channel is public or private on their end, there are some changes with the APIs too:

- The `conversations.*` methods accept any type of channel.
- The channel type object now includes the channel type info (public, private, and so forth).
- The [`conversations.info`](https://api.slack.com/methods/conversations.info) method will provide additional information on the workspaces connected to the shared channel and the ID of the host workspace.

The channel type object (returned by methods such as [`conversations.info`](https://api.slack.com/methods/conversations.info)) tells you additional channel information. If the channel is shared externally (i.e. not just between multiple workspaces in your Grid organization), `is_ext_shared` is set to true. If it is a private channel or a group DM channel, the properties `is_private` or `is_mpim` are set to `true`, respectively.

Use the `is_ext_shared`, < `is_private`, and `is_mpim` flags **_exclusively_** to determine the privacy and type of a given channel. Beware of `is_shared`, which also includes channels shared between multiple workspaces in the same organization.

Example response from `conversations.list`:

```json hljs
Copy{
    "ok": true,
    "channels": [\
        {\
            "id": "C123ABC456",\
            "name": "product-qa",\
            "is_channel": true,\
            "created": 1491332036,\
            "creator": "U123ABC456",\
            "is_archived": false,\
            "is_general": false,\
            "is_shared": true,\
            "is_ext_shared": true,\
            "is_org_shared": false,\
            "is_member": false,\
            "is_private": true,\
            "is_mpim": false,\
            "members": [\
                "U123ABC456",\
                "U222222222"\
            ],\
             ...\
        },\
        { ...  },\
    ]
}

```

### Channels between organizations that are converted back to a single-organization channel

When a channel between organizations or workspaces is unshared by the host workspace, each workspace can still access channel history for all previous messages and activity. However, the channel in the disconnected workspace will be assigned a new ID, while the host workspace keeps the original channel ID.

### Private channels between organizations

Channels between organizations and workspaces can be made private on a per-workspace basis. For instance, a public channel on one workspace can be shared with a private channel on another workspace. Use the [Conversations API](https://api.slack.com/docs/conversations-api) methods to work with the channels and to accurately determine their privacy.

When a workspace's private shared channel becomes unshared, its channel ID remains `C`-prefixed ( _i.e._ `C1234567890` does _not_ change back to `G1234567890`) although the channel is still private—making channel prefix an unreliable indicator in determining privacy.

## Design considerations

The most important technical requirement for supporting Slack Connect is that you must use the [Conversations API](https://api.slack.com/docs/conversations-api) to properly interact with channels that have been shared.

Next, we'll talk about design considerations for your app as it supports Slack Connect. Here's a quick set of questions to ask about your app before you should consider it compatible with Slack Connect:

1. Does your app provide access to sensitive, internal data? You must ask for confirmation before sharing this information to an external partner.
2. Does your app have a slash command, shortcut, or message action? Be prepared to share an explanatory message about how this action can only be invoked by users from the workspace that installed the app.
3. Does your app have interactive elements? Consider who should be able to interact with those elements (such as buttons and dropdown menus). Check that the originating user is part of the `authorized_users` property in the interaction payload to ensure they're part of the installing authorization.

If your app doesn't behave as expected, especially if it shares sensitive data to external parties, you may lose user trust, and you'll likely have your app uninstalled. Test your app thoroughly before you describe it as compatible with Slack Connect.

## Behavior to expect

An app compatible with Slack Connect needs to account for authorization and installation differences among workspaces where it's installed. If your app is installed on a workspace that shares a channel with another workspace, your app could be authorized in one workspace but not authorized in the other. Likewise, an app that can be installed into multiple workspaces will need to implement functionality that understands which workspace to operate in and to receive information from.

The following are additional guidelines to consider while building an app that can exist across channels and workspaces:

### Channels don't belong to a single workspace

A shared channel doesn't belong to a single workspace. If you need to look up a token or user to respond to an event, look at the `authorized_users` property.

The `authorized_users` property is an array that contains a set of one or more users who are authorized to view the event. A user can be a bot user or a human user who installed the app. For each user in the `authorized_users` property:

- the app has a valid, correctly scoped token associated with that user, and
- the event happened inside a channel that the authorized user was a member of.

The `team_id` property on the event's [outer payload](https://api.slack.com/apis/connections/events-api#events-JSON) will mirror the first element in the `authorized_users` array. If you need a complete list of every authorized user for an event, you can use
[apps.event.authorizations.list](https://api.slack.com/apis/methods/apps.event.authorizations.list).

### Beware sharing users' data

As a rule of thumb, your app should default to exposing less information in shared channels to protect your users' data.

Bot users are accessible to all users on the workspace where your app is installed, and any external members in a channel between organizations where your bot is also present.

When an external member messages you, the [event payload](https://api.slack.com/apis/connections/events-api#events-JSON) will contain a `team_id` property that indicates the workspace where the message came from. This property is identical to the first element of the `authorized_users` property, which is a set of one or more bot users or human users who installed the app. These users are authorized to see the event.

If your app typically shares sensitive information, make sure to change its behavior for external members.

### Slash commands are not shared

Slash commands and message actions are _not_ shared — they are limited only to the team that has installed the app to their team workspace. Another team must install the app independently in order to be able to use them.

When your app is initiated by a slash command or message action, only the team that installed your app can invoke it, but external members can still see any information posted into channel as a result. For example, let's say _Catnip inc._ has installed a polling app that is initiated with a command `/poll`. Users in the _Catnip inc._ can initiate a poll, while _Woof inc._ can only vote on the poll, and cannot create a new poll.

### App unfurls may surprise you

[`link_shared`](https://api.slack.com/events/link_shared) events are **not** delivered when an _external_ member shares a link that matches your app's unfurling domain, unless the app is installed in their workspace.

### Not all workspaces support Slack Connect

Slack Connect channels are not available to all free workspaces. If your app builds with the assumption that a workspace or organization uses Slack Connect, it may not be available to all end users and workspaces.

### More than one workspace may be connected

Slack Connect channels can connect up to 250 organizations.

### You may have multiple bot copies

If your app is installed on multiple workspaces that share a Slack Connect channel, you may have multiple app homes and multiple bot copies. Right now, we don't distinguish that a given app “belongs” to a particular workspace.

### Beware of changing IDs on channels when a share is initiated

The moment a channel share is _initiated_, `G`-encoded private channels will have their ID immediately changed to be `C`-encoded— **even if the channel is never successfully shared** with an external org.

You'll want to subscribe to the new [`channel_id_changed` event](https://api.slack.com/events/channel_id_changed), which marks when a private channel's ID has changed due to being shared:

```hljs bash
Copy    "event": {
      "type": "channel_id_changed",
      "old_channel_id": "G123ABC456",
      "new_channel_id": "C123ABC456",
      "event_ts": "1612206778.000000"
    }

```

### Beware of frozen and disconnected channels

A conversation can be archived and _frozen_ when an organization is disconnected from another with Slack Connect.

You may see a `"frozen_reason": "connection_severed"` in a Conversation object returned from the [Conversations API](https://api.slack.com/docs/conversations-api). The ID of a disconnected channel will change if your organization was invited to share it—i.e., your organization is not the host. The host organization retains the original channel and original ID, while the invited organization get a copy of the channel that is assigned a new ID.

Your app will receive a `channel_not_found` error if you try to query the API with the original channel ID.

### There's currently no way to find all channels shared with a specific external organization

Unfortunately, the [`conversations.list` method](https://api.slack.com/methods/conversations.list) does not include `connected_team_ids`.

### Beware of `is_shared`

The property `is_shared` on a [conversation object](https://api.slack.com/types/conversation) means the channel is shared with one or more workspaces. But beware: these can be internal workspaces (as with multi-workspace channels in Enterprise Grid) or external workspaces (as with Slack Connect).

Look for `is_ext_shared` and `is_org_shared` to learn which kind of shared channel you're viewing.

### Determining whether a user is external must be done implicitly

Look for the `is_stranger` field in [`user` objects](https://api.slack.com/types/user). If it's `true`, your app does not share a channel with the user. If it's `false`, but the `team` associated with the user is not the installing team for your app, the user is external and your app **does** share a channel with them.

In other words, there is no single property to substantiate if the user is external or not: you must deduce it from a combination of the `is_stranger` and the `team_id` property.

### Additional check required to access file info ( `check_file_info`)

When uploaded into a Slack Connect channel, [file object](https://api.slack.com/types/file) properties are not immediately accessible to apps listening via the Events API or RTM API. Instead, the payload will contain a file object with the key-value pair `"file_access": "check_file_info"` meaning that further action is required from your app in order to view an uploaded file's metadata.

```json hljs
Copy    "files": [\
        {\
          "id": "F123ABC456",\
          "mode": "file_access",\
          "file_access": "check_file_info",\
          "created": 0,\
          "timestamp": 0,\
          "user": ""\
        }\
      ]

```

This behavior is only observed for files uploaded into Slack Connect channels and occurs regardless of which workspace the uploader is a member of. Files uploaded into local conversations that send events to your app will contain the full file object. That said, expect this behavior even in local channels if the file was first uploaded into a Slack Connect channel before being shared to a local channel.

When your app is presented with the instruction to check file info, you should make a request to [`files.info`](https://api.slack.com/methods/files.info) if you need to access the full file object.

When accessing conversation files and messages using [`conversations.history`](https://api.slack.com/methods/conversations.history) or [`conversations.replies`](https://api.slack.com/methods/conversations.replies), full file objects are returned. Similarly, listing files with [`files.list`](https://api.slack.com/methods/files.list), using the [Discovery API](https://slack.com/help/articles/360002079527), or [exporting your workspace data](https://slack.com/help/articles/201658943) will also always return full file objects.

It is only when file events are pushed to your app that you will need an additional API call to view a file's properties.

## Support strategies by feature

| API | Support strategies |
| --- | --- |
| Events API | Support events originated from external users in shared channels.<br> <br>No duplicated event triggering between shared channels.<br> <br>To see which teams the event is delivered, look for the values of the `authed_teams` property for the response. |
| Web API | Support external users in shared channels. Some user-related actions will not be permissible due to their external nature.<br> <br>Use `users.info` to retrieve additional information on cross-team user ID not found in `users.list`. |
| Incoming webhooks | Messages from incoming webhooks are visible to all members of a shared channel.<br> <br>Incoming webhooks can send DMs only to users on installed teams. |
| Slash commands | Slash commands can be only invoked by users belonging to the workspace your app is installed.<br> <br>Turn on entity resolution for mentioned users allowing you to identity them by id, including on foreign teams. |
| Message actions | Message actions can only be invoked by users belonging to the workspace your app is installed. |
| Interactive messages | Handle action invocation by users from other teams, and let them know if an action is not permissible due to their external nature. |
| Unfurls | When a user on the installing workspace posts a link in the shared channel, the link should be unfurled for the entire channel unless there is a privacy concern. |
| RTM | Support users from other workspace in shared channels where appropriate.<br> <br>Message deliveries are duplicated in shared channels when installed on multiple joined workspaces due to the multiple socket connections. |
| Bot users 🤖 | Bot users can DM all local users in the workspace they are installed in and external users with a common shared channel. |

## Conversations API

Developing with channels between organizations and workspaces requires using the new Web API methods from the [Conversations API](https://api.slack.com/docs/conversations-api).

## Requesting a sandbox

Building properly for channels between workspaces and organizations requires experiencing the unique constraints and opportunities yourself. If you don't already have access to workspaces with the proper plan level to grant access to channels between organizations, please complete the form below to request a sandbox.

[Request a sandbox](https://api.slack.com/go/sandbox)

## Troubleshooting and known issues

We're still working on Slack Connect. It's likely you'll run into a bug or two. The following are some that we know about.

#### 🚧 MPIM events tell little lies about channel types

In a multiparty direct message channel ("MPIM") with a foreign user, events like [`member_joined_channel`](https://api.slack.com/events/member_joined_channel) and [`member_left_channel`](https://api.slack.com/events/member_left_channel) may dispatch an incorrect value for `channel_type`.

#### 🚧 IM Object format is not yet consistent

IM formats may differ from other channel objects for a while. We're working towards making all objects the same format.

#### 🚧 Select menus may be inconsistent

Default select menus ( [`users_select`](https://api.slack.com/reference/messaging/block-elements#users_select), [`conversations_select`](https://api.slack.com/reference/messaging/block-elements#conversations_select), and [`channels_select`](https://api.slack.com/reference/messaging/block-elements#channel_select)) may display unexpected options in shared channels.

Next steps

- [Using Slack Connect API methods](https://api.slack.com/apis/connect)

![Slack Technologies Company Logo](https://cdn.cookielaw.org/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/1ce30484-b023-4ff1-a118-3a9dc53fce45/f83dd0bf-3d5c-47ca-b065-8f247adfeacd/rsz_slack_rgb.png)

## Privacy Preference Center

We use three kinds of cookies on our websites: required, functional, and advertising. You can choose whether functional and advertising cookies apply. Click on the different cookie categories to find out more about each category and to change the default settings. [More information](https://slack.com/cookie-policy)

Allow All

### Manage Consent Preferences

#### Required Cookies

Always Active

Required cookies are necessary for basic website functionality. Some examples include: session cookies needed to transmit the website, authentication cookies, and security cookies.

Cookies Details‎

#### Functional Cookies

Functional Cookies

Functional cookies enhance functions, performance, and services on the website. Some examples include: cookies used to analyze site traffic, cookies used for market research, and cookies used to display advertising that is not directed to a particular individual.

Cookies Details‎

#### Advertising Cookies

Advertising Cookies

Advertising cookies track activity across websites in order to understand a viewer’s interests, and direct them specific marketing. Some examples include: cookies used for remarketing, or interest-based advertising.

Cookies Details‎

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

# Using the Calls API | Slack

The Slack developer docs are moving! We've been working hard at building out a new docs experience at [docs.slack.dev](https://docs.slack.dev/) — now in beta! You can start using the new docs today, but we'll keep the content on both sites up to date during the transition.

[Learn more](https://api.slack.com/changelog/2024-12-api-site-migration)

# Using the Calls API

You can integrate your calls with Slack so that they're more interactive, less intrusive, and easier for users to join.

Your call app will appear in the Slack client natively, under the Call icon, if you choose.

Whenever someone starts or shares a call, it appears in Slack with all the bells and whistles: a list of participants, a join button, and information about the call.

## Overview

The Calls API provides a way for your call app to tell Slack about the calls you're making between users.

It's important to know that Slack doesn't make the call. The API allows you to do your work and include your call, pleasantly and productively, within the Slack client. In exchange, Slack allows users to start, end, and enter your Calls from inside Slack.

To make things clearer, when we refer to your app's 3rd-party call, we'll use a lowercase "c". The full Call inside Slack will be capitalized.

Slack also shows off your call natively, with lists of participants, a join button, and metadata.

![Image of a call object generated from a link](https://a.slack-edge.com/80588/img/api/calls_link_shared.png)

There are two ways for your app to integrate with Slack so that users can initiate and deal with Calls within Slack.

One way for a user to initiate your app is via a slash command, for example, by typing `/mycallapp` into the message composer. The other way for a user to initiate your app is directly via the Call icon.

These two interaction patterns work the same for your app. Once you decide on one or the other, only the [app setup](https://api.slack.com/apis/calls#setup) is different. The payloads you receive are the same, and the way that you use the API methods to inform Slack about your calls remains the same as well.

## App setup

Users of non-partnered apps will need to initiate Calls using a [slash command](https://api.slack.com/interactivity/slash-commands).

To get started, [create your Slack app](https://api.slack.com/apps). Under the **Add features and functionality** header, select the **Slash Commands** button and then **Create a New Command**. Setting up your slash command app here is exactly the same as documented in the [slash command documentation](https://api.slack.com/interactivity/slash-commands).

Don't worry too much about the Request URL (the URL where Slack will send information about users interacting with calls to your app). You can change that later. You can also change the name of the command later.

You'll need two scopes for interacting with calls:

- [`calls:read`](https://api.slack.com/scopes/calls:read)
- [`calls:write`](https://api.slack.com/scopes/calls:write)

Request these two scopes under the **OAuth & Permissions** sidebar (scroll down to the **Scopes** section). Then click the **Install App to Workspace** button. You're all ready to work with Calls.

## Call functions: dialing to hanging up and everything in between

If you want to give users a smartphone for their calling needs, there are several different features you'll want to provide. Initiating and rejecting a Call are the starting point, but far more can happen.

The five main actions that a smart Call app has to handle are: [initiation of a Call](https://api.slack.com/apis/calls#initiation), [unfurling a link to a Call](https://api.slack.com/apis/calls#unfurling), [responding to a rejected Call](https://api.slack.com/apis/calls#rejection), [updating Call info and adding/removing participants](https://api.slack.com/apis/calls#updating), and finally [hanging up a Call](https://api.slack.com/apis/calls#ending).

Next, we'll go through each in a bit more detail, starting with [Call initiation](https://api.slack.com/apis/calls#initiation).

### Responding to a Call initiation

When a user initiates a call with your app, either by using a slash command or the Call icon, Slack sends a payload to your app.

For example, if the call is initiated with the Call icon, your app might receive the following in an HTTP POST request:

```json hljs
Copy{
    "token": "<verification token>",
    "team_id": "T123ABC456",
    "team_domain": "my-team",
    "channel_id": "C123ABC456",
    "channel_name": "test",
    "user_id" : "U123ABC456",
    "user_name": "mattjones",
    "response_url":"https://slack.com/callback/123xyz",
    "type": "video"
}

```

If the call is initiated with a slash command (e.g., `/mycall`), expect a normal [slash command payload](https://api.slack.com/interactivity/slash-commands#app_command_handling) sent to your app instead.

In turn, your app makes two responses—maybe three, if you include posting the Call to a channel afterward.

#### 1\. Immediate response

First up is an immediate, synchronous response within 3 seconds. This quick acknowledgement tells Slack where to send the calling user, and only applies when a user starts a call from a Call button—not a slash command.

Post your response to the `response_url` indicated in the payload you receive. If you're implementing a calls slash command, the `response_url` isn't needed: see the [register the call with Slack](https://api.slack.com/apis/calls#register_call) and [post the Call to channel](https://api.slack.com/apis/calls#post_to_channel) steps.

In reference to the example above, you'd therefore respond by pinging `https://slack.com/callback/123xyz` with:

```json hljs
Copy{
    "response_type":"call",
    "call_initiation_url":"https://join.call.com/123456",
    "desktop_protocol_call_initiation_url": "call://join&room_id=123456"
}

```

The specified `call_initiation_url` will be automatically opened for the initiating user in a separate window.

Sometimes, you might prefer to use a custom URL scheme to launch your app in desktop directly. If you wish, include the `desktop_protocol_call_initiation_url` optional field, representing the URL that will be used to launch your calls app directly. If you don't include it, Slack will fallback by launching `call_initiation_url` in a new browser window.

You'll always need to include the regular `call_initiation_url` in case a user doesn't have, or doesn't want, your app to be launched in desktop.

A `type` might be included in the payload sent to your app to indicate whether the call should be `audio` or `video`. For `video`, you don't need to do anything special except make sure your initiation URL begins a video. For `audio`, you'll receive a `phone_number`, and you'll want to make use of that in your response to Slack.

Example response:

```json hljs
Copy{
    "response_type": "audio",
    "call_initiation_url": "https://your_company_url/...",
    "desktop_protocol_call_initiation_url": "your_call_app_url://+1-202-555-0145"
}

```

#### 2\. Register the call with Slack

After you've made your quick response to Slack with a redirect `call_initiation_url`, you'll want to actually register the details of the call with Slack. Use the [`calls.add`](https://api.slack.com/methods/calls.add) method to add the Call to Slack.

You'll receive an `id` from Slack in the response. Make sure you store the Call's `id`, since you'll need it to reference the call if you want to [update](https://api.slack.com/apis/calls#updating) or [end](https://api.slack.com/apis/calls#ending) the Call.

#### 3\. Post the Call to channel

As a courtesy, post the Call to channel so the people in it know about the Call. Use the [`chat.postMessage`](https://api.slack.com/methods/chat.postMessage) method with a `call` block:

```json hljs
Copy"blocks": [\
    {\
        "type": "call",\
        "call_id": "R123",\
    }\
]

```

Your app might not have permission to post to private channels, multi-party direct messages, or direct messages in order to post a call block via the usual [chat.postMessage](https://api.slack.com/methods/chat.postMessage) method. In that case, use the `in_channel` slash command response type. This posts a message directly to the channel the slash command request originated from, and can include a `call` block:

```json hljs
Copy{
    "response_type": "in_channel",
    "text": "A new call was started by <name of call provider>",
    "blocks": [{\
        "type": "call",\
        "call_id": "R123",\
    }]
}

```

#### The `users` parameter

When you register a Call with the [`calls.add`](https://api.slack.com/methods/calls.add) method, add participants with the [`calls.participants.add`](https://api.slack.com/methods/calls.participants.add) method, or remove them with the [`calls.participants.remove`](https://api.slack.com/methods/calls.participants.remove) method, you'll notice a `users` parameter.

Each method requires `user` objects to include either a `slack_id` or `external_id`, or both.

A `slack_id` is the `id` of the user in Slack—you might receive this when interacting with any Slack API method, such as the [`conversations.members`](https://api.slack.com/methods/conversations.members) method. An `external_id` may be used if you don't know the `slack_id` for your users. In this case, `external_id` is a unique id created by your app for your users.

Here's an example `users` array containing two users identified in those two distinct ways:

```json hljs
Copy[\
    {\
        "slack_id": "U123ABC456",\
    },\
    {\
        "external_id": "54321678",\
        "display_name": "Kim Possible",\
        "avatar_url": "https://callmebeepme.com/users/avatar1234.jpg"\
    }\
]

```

If you aren't using the `application/json` Content-type, remember to encode `users` appropriately for the Content-type you send.

### Unfurling a link to a Call

Subscribe to the [`link_shared`](https://api.slack.com/events/link_shared) and [`call_rejected`](https://api.slack.com/events/call_rejected) events in your [app settings page](https://api.slack.com/apps) under **Event Subscriptions**, if you haven't already. Reinstall your app afterward.

Slack notifies your app with a `link_shared` event whenever a link from a specified domain (i.e., your app's domain representing calls) is shared.

Similar to [Call initiation](https://api.slack.com/apis/calls#initiation), your app should respond to the `link_shared` event with the [`calls.add`](https://api.slack.com/methods/calls.add) method to register the call. You'll receive an `id` from Slack in the response. Make sure you store the Call's `id`, since you'll need it to reference the call here and elsewhere.

In this case, you'll then invoke the [`chat.unfurl`](https://api.slack.com/methods/chat.unfurl) method. That way, you unfurl a Call in channel, already populated with the Call's duration and participants.

Here's an example call to `chat.unfurl`, supplying a `call_id` received from `calls.add`:

```json hljs
Copy{
    "token": "xxxx-xxxxxxxxx-xxxx",
    "channel": "C123ABC456",
    "ts": "12345.6789",
    "unfurls": {
        "https:\/\/url.to\/your\/call": {
            "blocks": [{\
                "type": "call",\
                "call_id": "Rxxx"\
            }]
        }
    }
}

```

### Responding to a rejected Call

Slack notifies your app with a `call_rejected` event whenever a Call is rejected by an invited user. Here's an example payload your app might receive:

```json hljs
Copy{
    "token": "12345FVmRUzNDOAuy4BiWh",
    "team_id": "T123ABC456",
    "api_app_id": "B123ABC456",
    "event": {
        "type": "call_rejected",
        "call_id": "RL731AVEF",
        "user_id": "U123ABC456",
        "channel_id": "D123ABC456",
        "external_unique_id": "123-456-7890"
    },
    "type": "event_callback",
    "event_id": "Ev123ABC456",
    "event_time": 1563448153,
    "authed_users": ["U123ABC456"]
}

```

Your app can then choose to handle the rejected call according to its own logic.

### Updating a Call and its participants

Use the [`calls.update` method](https://api.slack.com/methods/calls.update) to update a Call's `title`, `join_url`, or `desktop_app_join_url`.

Use the [`calls.participants.add`](https://api.slack.com/methods/calls.participants.add) method and the [`calls.participants.remove`](https://api.slack.com/methods/calls.participants.remove) method to add or remove participants.

The Call object in channel will update automatically with any of these changes.

### Hanging up a Call

When a call ends, update the Call object in Slack by calling the [`calls.end`](https://api.slack.com/methods/calls.end) method.

![Image of a call that has ended](https://a.slack-edge.com/80588/img/api/calls_end.png)

![Slack Technologies Company Logo](https://cdn.cookielaw.org/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/1ce30484-b023-4ff1-a118-3a9dc53fce45/f83dd0bf-3d5c-47ca-b065-8f247adfeacd/rsz_slack_rgb.png)

## Privacy Preference Center

We use three kinds of cookies on our websites: required, functional, and advertising. You can choose whether functional and advertising cookies apply. Click on the different cookie categories to find out more about each category and to change the default settings. [More information](https://slack.com/cookie-policy)

Allow All

### Manage Consent Preferences

#### Required Cookies

Always Active

Required cookies are necessary for basic website functionality. Some examples include: session cookies needed to transmit the website, authentication cookies, and security cookies.

Cookies Details‎

#### Functional Cookies

Functional Cookies

Functional cookies enhance functions, performance, and services on the website. Some examples include: cookies used to analyze site traffic, cookies used for market research, and cookies used to display advertising that is not directed to a particular individual.

Cookies Details‎

#### Advertising Cookies

Advertising Cookies

Advertising cookies track activity across websites in order to understand a viewer’s interests, and direct them specific marketing. Some examples include: cookies used for remarketing, or interest-based advertising.

Cookies Details‎

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

# Events API | Slack

The Slack developer docs are moving! We've been working hard at building out a new docs experience at [docs.slack.dev](https://docs.slack.dev/) — now in beta! You can start using the new docs today, but we'll keep the content on both sites up to date during the transition.

[Learn more](https://api.slack.com/changelog/2024-12-api-site-migration)

# Events API

The Events API is a streamlined way to build apps and bots that respond to activities in Slack. When you use the Events API, _Slack_ calls _you_.

You have two options: you can either use [Socket Mode](https://api.slack.com/apis/socket-mode) or you can designate a public [HTTP endpoint](https://api.slack.com/apis/http) that your app listens on, choose what events to subscribe to, and _voilà_: Slack sends the appropriate events to you. Learn more about the differences between Socket Mode and HTTP [here](https://api.slack.com/apis/event-delivery).

All you need is a [Slack app](https://api.slack.com/slack-apps) and a secure place for us to send your [events](https://api.slack.com/events/api). With the Events API, you can do the following:

- Tell Slack where to send your [event types](https://api.slack.com/events/api) and we'll deliver them with grace, security, and respect. We'll even retry when things don't work out. The [event types](https://api.slack.com/events/api) sent to you are directly tied to the [OAuth permission scopes](https://api.slack.com/docs/oauth-scopes) awarded as users install your Slack app.
- Subscribe to only the [event types](https://api.slack.com/events/api) you want; don't worry about the ones you don't need.
- Subscribe your Slack apps to events related to channels and direct messages they are party to. Build bots without a bothersome bevy of [Real Time Messaging (RTM) API](https://api.slack.com/rtm) WebSockets.

## Overview

Many apps built using the Events API will follow the same abstract event-driven sequence:

1. A user creates a circumstance that triggers an event subscription to your application.
2. Your server receives a payload of JSON describing that event.
3. Your server acknowledges receipt of the event.
4. Your business logic decides what to do about that event.
5. Your server carries out that decision.

If your app is a bot listening to messages with specific trigger phrases, that event loop may play out something like the following:

1. Members send messages in a channel the bot belongs to—the #random channel. The messages are about lots of things, but some of them contain today's secret word.
2. Your server receives a [`message.channels`](https://api.slack.com/events/message.channels) event, as per its bot subscription and membership in the #random channel.
3. Your server responds with a swift and confident HTTP 200 OK.
4. Your bot is trained to listen for today's secret word, and having found it, decides to send a message to the channel, encouraging everyone to keep that word secret.
5. Your server uses [`chat.postMessage`](https://api.slack.com/methods/chat.postMessage) from the Web API to post that message to #random.

Using the Web API with the Events API empowers your app or bot to do much more than just listen and reply to messages.

Let's get started!

* * *

## Preparing your app to use the Events API

The Events API is recommended over the [RTM API](https://api.slack.com/rtm) for most use cases. If you're already familiar with HTTP and are comfortable maintaining your own server, handling the request and response cycle of the Events API should be familiar. If the world of web APIs is new to you, the Events API is a great next step after mastering [incoming webhooks](https://api.slack.com/messaging/webhooks) or the [Web API](https://api.slack.com/web).

### Is the Events API right for your app?

Before starting, you may want to make a few early decisions about your application architecture and approach to consuming events. The Events API is best used in conjunction with other platform features.

One way to use the Events API is as an alternative to opening WebSocket connections to the [RTM API](https://api.slack.com/rtm). Why choose the Events API over the legacy RTM API? Instead of maintaining one or more long-lived connections for each workspace an application is connected to, you can set up one or more endpoints on your own servers to receive events atomically in near real-time. For more information, refer to [Events API FAQ](https://api.slack.com/faq#events_api).

Some developers may want to use the Events API as a kind of redundancy for their existing WebSocket connections. Other developers will use the Events API to receive information around the workspaces and users they are acting on behalf, to improve their [slash commands](https://api.slack.com/slash-commands), [bot users](https://api.slack.com/bot-users), [notifications](https://api.slack.com/docs/messages), or other capabilities. With [app events](https://api.slack.com/apis/events-api#app_events), you can track app uninstallation, token revocation, Enterprise Grid migration, and more. Handle anything else your app does by using [incoming webhooks](https://api.slack.com/messaging/webhooks) and other write-based [web API methods](https://api.slack.com/methods).

### Permission model

The Events API leverages Slack's existing [object-driven OAuth scope system](https://api.slack.com/docs/oauth-scopes) to control access to events. For example, if your app has access to files through the `files:read` scope, you can choose to subscribe to any or none of the file-related events such as [`file_created`](https://api.slack.com/events/file_created) and [`file_deleted`](https://api.slack.com/events/file_deleted).

You will only receive events that users who have authorized your app can "see" on their workspace (that is, if a user authorizes access to private channel history, you'll only see the activity in private channels they are a member of, not all private channels across the workspace).

[Bot users](https://api.slack.com/bot-users) may also subscribe to events on their own behalf. The `bot` scope requested when workspaces install your bot covers events access for both the Events API and the [Real Time Messaging API](https://api.slack.com/rtm).

## Subscribing to event types

To begin working with the Events API, you'll need to create a [Slack app](https://api.slack.com/slack-apps) if you haven't already. While managing your application, find the **Event Subscriptions** setting and use the toggle to turn it on.

![The on switch for the Events API](https://a.slack-edge.com/80588/img/api/events_api_turn_it_on.png)

After a little more configuration, you'll be able to select all the [event types](https://api.slack.com/events/api) you want to subscribe to.

Before continuing on to choosing event subscriptions, you will need to choose to use either Socket Mode or an HTTP request URL. For more information on the differences between them, refer to [Exploring HTTP vs Socket Mode](https://api.slack.com/apis/event-delivery).

To set up your app to use Socket Mode, refer to the [Socket Mode](https://api.slack.com/apis/socket-mode) guide.
To set up your app to use HTTP request URLs, refer to the [HTTP](https://api.slack.com/apis/http) guide.

### Choosing event subscriptions

After configuring and validating either Socket Mode or your request URL, it's time to subscribe to the [event types](https://api.slack.com/events/api) you find fascinating, useful, or necessary.

![The event subscription configuration process](https://a.slack-edge.com/80588/img/api/event_subscriptions.png)

The subscription manager is split into two sections:

- Team Events: these are the events that require a corresponding OAuth scope, and are perspectival to a member installing your application.
- Bot Events: subscribe to events on behalf of your application's [bot user](https://api.slack.com/bot-users), no additional scopes beyond `bot` required. As with workspace events, you'll only receive events perspectival to your bot user.

Some event types are not available in bot user subscriptions. Consult a specific event's documentation page for information on whether that event is supported for bot users.

### Activating subscriptions

The Events API is backed by the same [OAuth permission scoping system](https://api.slack.com/docs/oauth-scopes) powering your [Slack App](https://api.slack.com/slack-apps).

If workspaces have already installed your application, your request URL will soon begin receiving your configured event subscriptions.

For any workspaces that have yet to install your application, you'll need to request the specific OAuth scopes corresponding to the [event types](https://api.slack.com/events/api) you're subscribing to. If you're working on behalf of a [bot user](https://api.slack.com/bot-users), you'll need your bot installed the typical way, using the `bot` OAuth scope.

Authorize users for your Event Consumer app through the standard [OAuth flow](https://api.slack.com/authentication). Be sure to include all of the necessary scopes for the events your app wants to receive. Consult our index of the [available event types with corresponding OAuth scopes](https://api.slack.com/events/api).

With all this due preparation out of the way, it's time to receive and handle all those event subscriptions.

## Receiving events

Your Request URL will receive a request for each event matching your subscriptions. One request, one event.

You may want to consider the number of workspaces you serve, the number of users on those workspaces, their volume of messages, and other activity to evaluate how many requests your Request URL may receive and scale accordingly.

### Events dispatched as JSON

When an event in your subscription occurs in an authorized user's account, we'll send an HTTP POST request to your Request URL. The event will be in the `Content-Type: application/json` format:

```json hljs
Copy{
    "type": "event_callback",
    "token": "XXYYZZ",
    "team_id": "T123ABC456",
    "api_app_id": "A123ABC456",
    "event": {
        "type": "name_of_event",
        "event_ts": "1234567890.123456",
        "user": "U123ABC456",
        ...
    },
    "event_context": "EC123ABC456",
    "event_id": "Ev123ABC456",
    "event_time": 1234567890,
    "authorizations": [\
        {\
            "enterprise_id": "E123ABC456",\
            "team_id": "T123ABC456",\
            "user_id": "U123ABC456",\
            "is_bot": false,\
            "is_enterprise_install": false,\
        }\
    ],
    "is_ext_shared_channel": false,
    "context_team_id": "T123ABC456",
    "context_enterprise_id": null
}

```

The `token` and `api_app_id` fields help you identify the validity and intended destination of the request, respectively.

The `authorized_users` property is an array that contains a set of one or more users
who are authorized to view the event. A user can be a bot user or a human user who
installed the app. For each user in the `authorized_users` property:

- the app has a valid, correctly scoped token associated with that user, and
- the event happened inside a channel that the authorized user was a member of.

The `team_id` property on the event's [outer payload](https://api.slack.com/apis/connections/events-api#events-JSON) will mirror the first element in the `authorized_users` array. If you need a complete list of every authorized user for an event, you can use
[apps.event.authorizations.list](https://api.slack.com/apis/methods/apps.event.authorizations.list).

The `event` attribute contains a JSON hash for the corresponding [event type](https://api.slack.com/events/api). The event wrapper is an event envelope of sorts, and the event field represents the contents of that envelope. Learn more about [the event wrapper](https://api.slack.com/types/event), including its JSON schema.

### Callback field overview

Also referred to as the "outer event", or the JSON object containing the event that happened itself:

| Field | Type | Description |
| --- | --- | --- |
| `token` | String | The shared-private callback token that authenticates this callback to the application as having come from Slack. Match this against what you were given when the subscription was created. If it does not match, do not process the event and discard it. Example: `JhjZd2rVax7ZwH7jRYyWjbDl` |
| `team_id` | String | The unique identifier for the workspace/team where this event occurred. Example: `T461EG9ZZ` |
| `api_app_id` | String | The unique identifier for the application this event is intended for. Your application's ID can be found in the URL of the your application console. If your Request URL manages multiple applications, use this field along with the `token` field to validate and route incoming requests. Example: `A4ZFV49KK` |
| `event` | [Event type](https://api.slack.com/apis/connections/events-api#event_type_structure) | Contains the inner set of fields representing the event that's happening. [Examples below.](https://api.slack.com/apis/connections/events-api#event_type_structure) |
| `type` | String | This reflects the type of callback you're receiving. Typically, that is `event_callback`. You may encounter `url_verification` during the configuration process. The `event` field's "inner event" will also contain a `type` field indicating which [event type](https://api.slack.com/events/api) lurks within ( [below](https://api.slack.com/apis/connections/events-api#event_type_structure)). |
| `authorizations` | Object | An installation of your app. Installations are defined by a combination of the installing Enterprise Grid org, workspace, and user (represented by `enterprise_id`, `team_id`, and `user_id` inside this field)—note that installations may only have one or two, not all three, defined. `authorizations` describes _one_ of the installations that this event is visible to. You'll receive a single event for a piece of data intended for multiple users in a workspace, rather than a message per user. Use [`apps.event.authorizations.list`](https://api.slack.com/methods/apps.event.authorizations.list) to retrieve additional authorizations. |
| `event_context` | String | An identifier for this specific event. This field can be used with the [`apps.event.authorizations.list`](https://api.slack.com/methods/apps.event.authorizations.list) method to obtain a full list of installations of your app for which this event is visible. |
| `event_id` | String | A unique identifier for this specific event, globally unique across all workspaces. |
| `event_time` | Integer | The epoch timestamp in seconds indicating when this event was dispatched. |

### Event type structure

The structure of [event types](https://api.slack.com/events/api) vary from type to type, depending on the kind of action or [object type](https://api.slack.com/types) they represent. The Events API allows you to tolerate minor changes in [event type](https://api.slack.com/events/api) and [object type](https://api.slack.com/types) structures, and to expect additional fields you haven't encountered before or fields that are only conditionally present.

If you're already familiar with the [RTM API](https://api.slack.com/rtm), you'll find that the inner `event` structure is identical to corresponding events, but are wrapped in a kind of event envelope in the callbacks we send to your event Request URL:

| Field | Type | Description |
| --- | --- | --- |
| `type` | String | The specific name of the event described by its adjacent fields. This field is included with every inner event type. Examples: `reaction_added`, `message.channels`, `team_join` |
| `event_ts` | String | The timestamp of the event. The combination of `event_ts`, `team_id`, `user_id`, or `channel_id` is intended to be unique. This field is included with every inner event type. Example: `1469470591.759709` |
| `user` | String | The user ID belonging to the [user](https://api.slack.com/types/user) that incited this action. Not included in all events as not all events are controlled by users. See the top-level callback object's `authed_users` if you need to calculate event visibility by user. Example: `U061F7AUR` |
| `ts` | String | The timestamp of what the event describes, which may occur slightly prior to the event being dispatched as described by `event_ts`. The combination of `ts`, `team_id`, `user_id`, or `channel_id` is intended to be unique. Example: `1469470591.759709` |
| `item` | String | Data specific to the underlying [object type](https://api.slack.com/types) being described. Often you'll encounter abbreviated versions of full objects. For instance, when [file objects](https://api.slack.com/types/file) are referenced, only the file's ID is presented. See each individual [event type](https://api.slack.com/events/api) for more detail. |

If multiple users on one workspace have installed your app and can "see" the same event, we will send _one_ event and include a list of users to whom this event is "visible" in the `authed_users` field. For example, if a file was uploaded to a channel that two of your authorized users were party to, we would stream the `file_uploaded` event once and indicate both of those users in the `authed_users` array.

Here's a full example of a dispatched event for [reaction\_added](https://api.slack.com/events/reaction_added):

```json hljs
Copy{
    "token": "z26uFbvR1xHJEdHE1OQiO6t8",
    "team_id": "T123ABC456",
    "api_app_id": "A123ABC456",
    "event": {
        "type": "reaction_added",
        "user": "U123ABC456",
        "item": {
            "type": "message",
            "channel": "C123ABC456",
            "ts": "1464196127.000002"
        },
        "reaction": "slightly_smiling_face",
        "item_user": "U222222222",
        "event_ts": "1465244570.336841"
    },
    "type": "event_callback",
    "authed_users": [\
        "U123ABC456"\
    ],
    "authorizations": [\
        {\
            "enterprise_id": "E123ABC456",\
            "team_id": "T123ABC456",\
            "user_id": "U123ABC456",\
            "is_bot": false\
        }\
    ],
    "event_id": "Ev123ABC456",
    "event_context": "EC123ABC456",
    "event_time": 1234567890
}

```

* * *

## Authorizations

Previously, the Events API included a [_full list_ of `authed_users`](https://api.slack.com/events-api#receiving_events), and sometimes `authed_teams`, with every event. These fields displayed who the event is visible to. For example, if your app has been installed by two users in a workspace, and the app listens for the [`file_shared` event](https://api.slack.com/events/file_shared), your app might receive an event with `authed_users` containing those two users.

Now, `authed_users` and `authed_teams` [**are deprecated**](https://api.slack.com/changelog/2020-09-15-events-api-truncate-authed-users). Events will contain a single, compact `authorizations` field that shows one installation of your app that the event is visible to. In other words, lists of authorizations will be truncated to one element.

Expect a new outer payload on events that looks similar to this one:

```json hljs
Copy{
    "token": "z26uFbvR1xHJEdHE1OQiO6t8",
    "team_id": "T123ABC456",
    "api_app_id": "A123ABC456",
    "event": {
        "type": "reaction_added",
        "user": "U123ABC456",
        "item": {
            "type": "message",
            "channel": "C123ABC456",
            "ts": "1464196127.000002"
        },
        "reaction": "slightly_smiling_face",
        "item_user": "U123ABC456",
        "event_ts": "1465244570.336841"
    },
    "type": "event_callback",
    "authed_users": [\
        "U222222222"\
    ],
    "authed_teams": [\
        "T123ABC456"\
    ],
    "authorizations": [\
        {\
            "enterprise_id": "E123ABC456",\
            "team_id": "T123ABC456",\
            "user_id": "U123ABC456",\
            "is_bot": false\
        }\
    ],
    "event_context": "EC123ABC456",
    "event_id": "Ev123ABC456",
    "event_time": 1234567890
}

```

If there's more than one installing party that your app is keeping track of, it's best not to rely on the single party listed in `authorizations` to be any particular one.

To get a _full list_ of who can see events, call the [`apps.event.authorizations.list` method](https://api.slack.com/methods/apps.event.authorizations.list) after obtaining an [app-level token](https://api.slack.com/concepts/token-types#app). [Read more on the changes here](https://api.slack.com/changelog/2020-09-15-events-api-truncate-authed-users); they have taken effect for existing apps as of February 24, 2021.

Not all events provide an `event_context`. [Read more about the events where `event_context` is not applicable, and view a full list of those events](https://api.slack.com/changelog/2020-09-15-events-api-truncate-authed-users#no_context). Newly created apps are _automatically_ opted into the new form of events: a single, truncated `authorizations` field with one authorization shown.

You can also use the [`apps.event.authorizations.list` method](https://api.slack.com/methods/apps.event.authorizations.list) immediately, without yet opting in to the event payload changes. These changes allow Slack to increase the performance of the Events API, delivering events faster.

* * *

## Responding to events

Your app should respond to the event request with an HTTP 2xx _within three seconds_. If it does not, we'll consider the event delivery attempt failed. After a failure, we'll retry three times, backing off exponentially. Some best practices are to:

- Maintain a response success rate of at least 5% of events per 60 minutes to prevent automatic disabling.
- Respond to events with an HTTP 200 OK as soon as you can.
- Avoid actually processing and reacting to events within the same process.
- Implement a queue to handle inbound events after they are received.

What you do with events depends on what your application or service does.

Maybe it'll trigger you to send a message using [`chat.postMessage`](https://api.slack.com/methods/chat.postMessage). Maybe you'll update a leaderboard. Maybe you'll update a piece of data you're storing. Maybe you'll change the world or just decide to do nothing at all.

### Rate limiting

We don't want to flood your servers with events it can't handle.

Event deliveries currently max out at 30,000 per workspace _per app_ per 60 minutes. If your app would receive more than one workspace's 30,000 events in a 60 minute window, you'll receive [`app_rate_limited`](https://api.slack.com/events/app_rate_limited) events describing the conditions every minute.

When rate limited, your Request URL will receive a special app event, [`app_rate_limited`](https://api.slack.com/events/app_rate_limited).

```json hljs
Copy{
	"token": "Jhj5dZrVaK7ZwHHjRyZWjbDl",
	"type": "app_rate_limited",
	"team_id": "T123ABC456",
	"minute_rate_limited": 1518467820,
	"api_app_id": "A123ABC456"
}

```

**Field guide**

- `token`: the same shared token used to verify other events in the Events API
- `type`: this specific event type, `app_rate_limited`
- `minute_rate_limited`: a rounded epoch time value indicating the minute your application became rate limited for this workspace. `1518467820` is at 2018-02-12 20:37:00 UTC.
- `team_id`: subscriptions between your app and the workspace with this ID are being rate limited
- `api_app_id`: your application's ID, especially useful if you have multiple applications working with the Events API

You'll receive these callbacks for each of the minutes you are rate limited for that workspace.

* * *

## Error handling

As Slack sends your request URL events, we ask that you return an HTTP 200 OK for each event you successfully receive. You may respond with an HTTP 301 or 302 and we'll follow up to two redirects in our quest for you to provide us an HTTP 200 success code. Respond with success conditions to at least 5% of the events delivered to your app or your app will risk being temporarily disabled.

Once you've repaired your ability to handle events, re-enable subscriptions by visiting Slack app management, selecting your app, and following the prompts. You'll need to go to **Live App Settings** if your app is part of the Slack Marketplace.

### Failure conditions

We consider any of these scenarios a single failure condition:

- We are unable to negotiate or validate your server's SSL certificate.
- We wait longer than _3 seconds_ to receive a valid response from your server.
- We encounter more than 2 HTTP redirects to follow.
- We receive any other response than an HTTP 200-series response (besides allowed redirects mentioned above).

While we limit the number of failure conditions we'll tolerate over time, we also gracefully retry sending your events according to an exponential backoff strategy.

Maintain a successful response rate of 5% or above to avoid automatic event delivery disabling. Apps receiving less than 1,000 events per hour will not be automatically disabled.

### Retries

We'll knock knock knock on your server's door, retrying a failed request up to _3 times_ in a gradually increasing timetable:

1. The first retry will be sent nearly immediately.
2. The second retry will be attempted after 1 minute.
3. The third and final retry will be sent after 5 minutes.

With each retry attempt, you'll also be given a `x-slack-retry-num` HTTP header indicating the attempt number: `1`, `2`, or `3`. Retries count against the [failure limits](https://api.slack.com/apis/events-api#failure_limits) mentioned below.

We'll tell you why we're retrying the request in the `x-slack-retry-reason` HTTP header. These possible values describe their inciting events:

- `http_timeout`: Your server took longer than 3 seconds to respond to the previous event delivery attempt.
- `too_many_redirects`: We'll follow you down the rabbit hole of HTTP redirects only so far. If we encounter more than 2, we'll retry the request in hopes it won't be that many this time.
- `connection_failed`: We just couldn't seem to connect to your server. Maybe we couldn't find it in DNS or maybe your host is unreachable.
- `ssl_error`: We couldn't verify the veracity of your SSL certificate. Find tips on producing valid SSL certificates [here](https://api.slack.com/faq#why_does_slack_never_reach_my_slash_command_url).
- `http_error`: We encountered an HTTP status code that was not in the HTTP 200 OK range. Maybe the request was forbidden. Or you rate limited _us_. Or the document just could not be found. So we're trying again in case that's all rectified now.
- `unknown_error`: We didn't anticipate this condition arising, but prepared for it nonetheless. For some reason it didn't work; we don't know why yet.

### Turning retries off

If your server is having trouble handling our requests or you'd rather we not retry failed deliveries, provide an HTTP header in your responses indicating that you'd prefer no further attempts. Provide us this HTTP header and value as part of your non-200 OK response:

```http hljs
Copyx-slack-no-retry: 1

```

By presenting this header, we'll understand it to mean you'd rather this specific event not be re-delivered. Other event deliveries will remain unaffected.

### Failure limits

If you're responding with errors, we won't keep sending events to your servers forever.

When your application enters any combination of these [failure conditions](https://api.slack.com/apis/events-api#failure_conditions) for more than _95% of delivery attempts_ within 60 minutes, your application's event subscriptions will be temporarily disabled.

We'll also send you, the Slack app's creator and owner, an email alerting you to the situation. You'll have the opportunity to re-enable deliveries when you're ready.

### Resuming event deliveries

Manually re-enable event subscriptions by visiting your application's settings. If your app is part of the Slack Marketplace, use your **Live App Settings** instead of your development app.

* * *

## Change management

Inevitably, the status of your subscriptions will change. New workspaces will sign up for your application. Installing users may leave a workspace. Maybe you make some tweaks to your subscriptions or incite users to request a different set of OAuth scopes.

Beyond your app being disabled, there are a few different types of changes that will affect which events your app is receiving.

### App installation

When a user installs your app, you'll immediately begin receiving events for them based on your subscription.

Your application's granted OAuth scopes dictate which events in your subscription you receive.

If you've configured your subscription to receive [`reaction_added`](https://api.slack.com/events/reaction_added), [`reaction_removed`](https://api.slack.com/events/reaction_removed), and [`file_created`](https://api.slack.com/events/file_created) events, you won't receive all three unless you request the `reactions:read` and `files:read` scopes from the user. For example, If you'd only requested `files:read`, you'll only receive [`file_created`](https://api.slack.com/events/file_created) events and not [`reaction_added`](https://api.slack.com/events/reaction_added) or [`reaction_removed`](https://api.slack.com/events/reaction_removed).

### App revocation

If a user uninstalls your app (or the tokens issued to your app are revoked), events for that user will immediately stop being sent to your app.

### Modifying events in your subscription

If you modify your subscription through the application management interface, the modifications will _immediately_ take effect.

Depending on the modification, the event types, and OAuth scopes you've been requesting from users, a few different things can happen:

- **Adding event subscriptions you already have scopes for**: For example, you've been requesting `files:read` from users and decide to add the `file_created` event. Because you already have access to this resource (files), you'll begin receiving `file_created` events as soon as you update your subscription.
- **Adding event subscriptions you aren't yet scoped for**: For example, you've been requesting `channels:read` from users and decide to add the `file_created` event. Because you _don't_ have access to this resource (files), you won't receive `file_created` events immediately. You must send your existing users through the OAuth flow again, requesting the `files:read` scope. You'll begin to receive `file_created` events for each user _after_ they authorize `files:read` for your app.
- **Removing event subscriptions, regardless of granted scopes**: Events will immediately stop being sent for all users who have installed your app. Their OAuth scopes and authorizations will not be affected. If you weren't granted the permission scopes for the removed event subscription, then nothing really changes. You weren't receiving those events anyway and you won't be receiving them now either.

* * *

## Presence

Bot users using the Events API exclusively must toggle their [presence](https://api.slack.com/docs/presence#bot_presence) status. To toggle your bot user's presence when connected exclusively to the Events API, visit your [app management console](https://api.slack.com/apps)'s **Bot Users** tab.

![Toggling bot user presence for the events API](https://a.slack-edge.com/80588/img/api/events-api-bot-presence.png)

Learn more about the [nuances of bot user presence](https://api.slack.com/docs/presence#bot_presence).

* * *

## Event types compatible with the Events API

[Browse all available events here](https://api.slack.com/events).

Want to browse the list of events and even some of their properties programmatically? Check out our [AsyncAPI spec for the Events API](https://github.com/slackapi/slack-api-specs).

* * *

## Monitoring your app's lifecycle with app events

Your application has a life of its own. You build it, cultivate it, maintain it, and improve it. But still, stuff happens to your app in the wild. Tokens get revoked, workspaces accidentally uninstall it, and sometimes teams grow up and become part of a massive [Enterprise Grid](https://api.slack.com/enterprise-grid).

Building an integration for Enterprise Grid workspaces? Consult the [Enterprise Grid](https://api.slack.com/enterprise-grid) docs for notes on Events API usage and shared channels.

Sophisticated apps want to know what's happening, to situationally respond, tidy up data messes, pause and resume activity, or to help you contemplate the many-folded nuances of building invaluable social software. Your app is interesting, wouldn't you like to subscribe to its newsletter?

Subscriptions to app events require no special [OAuth scopes](https://api.slack.com/docs/oauth-scopes); just subscribe to the events you're interested in and you'll receive them as appropriate for each workspace your app is installed on.

**[Platform changelog](https://api.slack.com/changelog?ref=unit)**

Learn about our newest features and advancements

![Slack Technologies Company Logo](https://cdn.cookielaw.org/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/1ce30484-b023-4ff1-a118-3a9dc53fce45/f83dd0bf-3d5c-47ca-b065-8f247adfeacd/rsz_slack_rgb.png)

## Privacy Preference Center

We use three kinds of cookies on our websites: required, functional, and advertising. You can choose whether functional and advertising cookies apply. Click on the different cookie categories to find out more about each category and to change the default settings. [More information](https://slack.com/cookie-policy)

Allow All

### Manage Consent Preferences

#### Required Cookies

Always Active

Required cookies are necessary for basic website functionality. Some examples include: session cookies needed to transmit the website, authentication cookies, and security cookies.

Cookies Details‎

#### Functional Cookies

Functional Cookies

Functional cookies enhance functions, performance, and services on the website. Some examples include: cookies used to analyze site traffic, cookies used for market research, and cookies used to display advertising that is not directed to a particular individual.

Cookies Details‎

#### Advertising Cookies

Advertising Cookies

Advertising cookies track activity across websites in order to understand a viewer’s interests, and direct them specific marketing. Some examples include: cookies used for remarketing, or interest-based advertising.

Cookies Details‎

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

# Checking up on Slack with the Slack Status API | Slack

The Slack developer docs are moving! We've been working hard at building out a new docs experience at [docs.slack.dev](https://docs.slack.dev/) — now in beta! You can start using the new docs today, but we'll keep the content on both sites up to date during the transition.

[Learn more](https://api.slack.com/changelog/2024-12-api-site-migration)

# Checking up on Slack with the Slack Status API

The Slack Status API describes the health of the Slack product. When there's an incident, outage, or maintenance, the Slack Status API reflects all the information we have on the issue, including which features of Slack are affected and detailed updates over time.

## Atom and RSS Feed

Receive updates on the health of Slack services by subscribing to our Atom or RSS feeds. Use your favorite subscription tool to subscribe to `https://slack-status.com/feed/atom` or `https://slack-status.com/feed/rss`. You could even use the `/feed` command in Slack to subscribe to our Status feed — but it might not work if some parts of Slack are unavailable. An outside feed reader might be a better choice.

Note that many readers check for updates only a few times an hour. Set your feed reader to poll for updates often (for example, once a minute) if you need to be notified immediately of a Slack issue.

## API reference

Slack offers two API endpoints to describe its status. Use the `https://slack-status.com/api/v2.0.0/current` endpoint to check for active incidents. Use the `https://slack-status.com/api/v2.0.0/history` endpoint to learn about past incidents. Both are unauthenticated: you can even open these API endpoints directly in your browser. [Try it](https://slack-status.com/api/v2.0.0/current).

You can also find either endpoint with a cURL command:

```hljs javascript
Copycurl https://slack-status.com/api/v2.0.0/current
curl https://slack-status.com/api/v2.0.0/history

```

### Version 2.0.0

#### Current Status API

The `current` endpoint returns a JSON object containing a `status` field. When all is well, the `status` will be "ok", and the response will be brief. Here's a sample "ok" response.

```json hljs
Copy
{
    "status":"ok",
    "active_incidents": [],
    "date_created":"2018-09-07T18:34:15-07:00",
    "date_updated":"2018-09-07T18:34:15-07:00"
}

```

If there's an incident, outage, or planned maintenance, you'll receive a richer JSON response containing a title that describes the issue, a time updated, and affected services. Here's a sample JSON response describing an issue with email forwarding:

```json hljs
Copy
  {
    "status": "active",
    "date_created": "2019-04-09T07:35:46-07:00",
    "date_updated": "2019-04-09T07:35:46-07:00",
    "active_incidents": [\
      {\
        "id": "546",\
        "date_created": "2018-09-07T14:35:00-07:00",\
        "date_updated": "2018-09-07T18:34:15-07:00",\
        "title": "Slack’s forwarding email feature is failing for some customers",\
        "type": "incident",\
        "status": "active",\
        "url": "https://slack-status.com/2018-09/7dea1cd14cd0f657",\
        "services": [\
          "Apps/Integrations/APIs"\
        ],\
        "notes": [\
          {\
            "date_created": "2018-09-07T18:34:15-07:00",\
            "body": "Technical Summary:\r\nOn September 7th at 2:35pm PT, we received reports that emails were failing to deliver to Slack forwarding addresses. We identified that this was the result of an expired certificate used to verify requests sent from our email provider. At 4:55pm PT, we deployed an update that corrected this and fixed the problem. Unfortunately any email sent to a forwarding address during this time is not retrievable and will need to be re-sent."\
          }\
        ],\
      },\
      ...\
    ]
  }

```

Here's more detail on each of the fields in the response:

- `id` \- A unique ID for the issue.
- `date_created` \- The timestamp when incident response or maintenance began.
- `date_updated` \- The timestamp when incident response or maintenance was most recently updated.
- `title` \- A short description of what's happening.
- `type` \- The type of issue we're experiencing. The options are "incident", "notice", or "outage".
- `status` \- We use status "ok" when all is well. Otherwise, the `status` field is "active" when the issue has not yet been resolved, and "resolved" when the issue has been resolved. The status may also be "scheduled," "completed," or "cancelled" in the case of planned maintenance.
- `url` \- A web URL tracking this incident. The information displayed is the same as in the API endpoint.
- `services` \- An array that lists the Slack services affected. We use these service names:

  - "Login/SSO"
  - "Messaging"
  - "Notifications"
  - "Search"
  - "Workspace/Org Administration"
  - "Canvases"
  - "Connectivity"
  - "Files"
  - "Huddles"
  - "Apps/Integrations/APIs"
  - "Workflows"
- `notes` \- An array of notes with additional specifics and updates.

In version 2.0.0, the current API endpoint displays all active incidents. If you don't pass a version, the API endpoint defaults to version 1.0.0, which only displays one incident at a time. If there are multiple incidents, it displays the most urgent one according to Slack internal incident ranking. If there are no active incidents, it'll display the most recent incident that was updated within the last hour. If no incidents have been reported or updated in the last hour, the endpoint returns the terse "ok" response.

#### History API

The `history` endpoint returns a list of all past Slack issues. Each object in the response array is an incident like the ones returned by the `current` endpoint. As with the `current` endpoint, you can expect the following fields for each issue:

- `id` \- A unique ID for the issue.
- `date_created` \- The timestamp when incident response or maintenance began.
- `date_updated` \- The timestamp when incident response or maintenance was most recently updated.
- `title` \- A short description of the issue.
- `type` \- The type of issue we experienced. The options are "incident", "notice", or "outage".
- `status` \- We use status "ok" when all is well. Otherwise, the `status` field is "active" when the issue has not yet been resolved, and "resolved" when the issue has been resolved. The status may also be "scheduled," "completed," or "cancelled" in the case of planned maintenance.
- `url` \- A web URL for this incident. The information displayed is the same as in the API endpoint.
- `services` \- An array that lists the Slack services affected. Current and past service names can include the following:

  - "Login/SSO"
  - "Messaging"
  - "Notifications"
  - "Search"
  - "Workspace/Org Administration"
  - "Connections"
  - "Files"
  - "Huddles"
  - "Apps/Integrations/APIs"
  - "Workflows"
  - "Posts/Files"
  - "Calls"
  - "Link Previews"
- `notes` \- An array of notes with additional specifics and updates.

### Version 1.0.0

Version 1.0.0 of the Slack Status API endpoints can be found at both `https://slack-status.com/api/v1.0.0/current` and `https://slack-status.com/api/current`. The information returned is similar to version 2.0.0, except that the `current` endpoint shows only one incident at a time. If there are multiple incidents, the endpoint displays the most urgent one according to Slack internal incident ranking. If there are no active incidents, it'll display the most recent incident that was updated within the last hour. If no incidents have been reported or updated in the last hour, the endpoint returns the terse "ok" response.

## Best practices

- Use the most recent version of the API endpoint ( `v2.0.0`).
- Call the `current` endpoint as frequently or infrequently as you need to in order to respond to issues with Slack; if you need to be notified immediately of an incident, consider polling the `current` endpoint once a minute. Polling more frequently than that isn't recommended.
- If you rely on a specific feature of Slack heavily, check the `services` field of an incident to verify that the feature is working as usual. For example, if your app doesn't use Huddles, but does rely on messaging, consider filtering for incidents that contain "Messaging" in the `services` array, and ignoring alerts that only affect "Huddles".

**[Which API is right for me?](https://api.slack.com/docs?ref=unit)**

We'll help you [make decisions](https://api.slack.com/docs?ref=unit) based on your goals and our capabilities.

![Slack Technologies Company Logo](https://cdn.cookielaw.org/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/1ce30484-b023-4ff1-a118-3a9dc53fce45/f83dd0bf-3d5c-47ca-b065-8f247adfeacd/rsz_slack_rgb.png)

## Privacy Preference Center

We use three kinds of cookies on our websites: required, functional, and advertising. You can choose whether functional and advertising cookies apply. Click on the different cookie categories to find out more about each category and to change the default settings. [More information](https://slack.com/cookie-policy)

Allow All

### Manage Consent Preferences

#### Required Cookies

Always Active

Required cookies are necessary for basic website functionality. Some examples include: session cookies needed to transmit the website, authentication cookies, and security cookies.

Cookies Details‎

#### Functional Cookies

Functional Cookies

Functional cookies enhance functions, performance, and services on the website. Some examples include: cookies used to analyze site traffic, cookies used for market research, and cookies used to display advertising that is not directed to a particular individual.

Cookies Details‎

#### Advertising Cookies

Advertising Cookies

Advertising cookies track activity across websites in order to understand a viewer’s interests, and direct them specific marketing. Some examples include: cookies used for remarketing, or interest-based advertising.

Cookies Details‎

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

# Paginating through collections | Slack

The Slack developer docs are moving! We've been working hard at building out a new docs experience at [docs.slack.dev](https://docs.slack.dev/) — now in beta! You can start using the new docs today, but we'll keep the content on both sites up to date during the transition.

[Learn more](https://api.slack.com/changelog/2024-12-api-site-migration)

# Paginating through collections

Throughout the Slack platform, you'll encounter collections of _things_. Lists of users. Arrays of channels. A pride of lion emoji.

When you call an [API method](https://api.slack.com/methods) to retrieve most of these collections, they're returned to you in portions. Check out more detail below on pagination in API methods, including how to use them and which methods follow the pattern.

Most methods that support pagination use a cursor-based approach. However, some older methods use varied versions of pagination. The individual documentation for each API method is your source of truth for which pattern the method follows.

## Cursor-based pagination

For larger collections like channel and user lists, Slack API methods return results using a cursor-based approach.

Cursors are like pointers. Pointers point at things: they reference a specific iota, a place in the list where your last request left off. They help avoid loading an entire set just to give you a slice.

A cursor-paginated method returns two things: a portion of the total set of results, and a **cursor** that points to the next portion of the results.

Cursor-based pagination is spreading across the platform quickly and is mandatory on some methods.

Please paginate along with us.

### Just the facts

- Cursor-paginated methods accept `cursor` and `limit` parameters.
- If you don't pass a `cursor` parameter, but **do** pass a `limit` parameter, the default value retrieves the first portion (or "page") of results.
- Paginated responses include a top-level `response_metadata` object that includes a `next_cursor` _when there are additional results to be retrieved_.
- On your next call to the same method, set the `cursor` parameter equal to the `next_cursor` value you received on the last request to retrieve the next portion of the collection.
- An empty, null, or non-existent `next_cursor` in the response indicates no further results.
- The `limit` parameter sets a _maximum_ number of results to return per call.
- Provide sensible `limit` values. We recommend `100`- `200` results at a time.
- The `limit` parameter maximum is `1000` and subject to change and may vary per method.
- It's possible to receive _fewer_ results than your specified `limit`, even when there are additional results to retrieve. Avoid the temptation to check the size of results against the limit to conclude the results have been completely returned. Instead, check the `next_cursor` value in the `response_metadata` object to make sure that it's empty, null, or non-existent.

### Walkthrough

When accessing the first virtual page of a paginated collection — for instance making a [`users.list`](https://api.slack.com/methods/users.list) request for the first time — you'll receive a `response_metadata` attribute containing a cursor for your next request.

Here's an example request to `users.list`, where we limit our list of users to `2` users per "page", making it easier to test on a workspace with a low number of users.

```http hljs
CopyGET https://slack.com/api/users.list
Authorization: Bearer xoxb-1234-5678-90123

```

In return, we get our typical `users.list` response, limited to `2` results. Skip down to the bottom to see the `response_metadata`, containing cursor information on the next page of results.

```json hljs
Copy{
    "ok": true,
    "members": [\
        {\
            "id": "USLACKBOT",\
            "team_id": "T0123ABC456",\
            "name": "slackbot",\
            "deleted": false,\
            "color": "757575",\
            "real_name": "slackbot",\
            "tz": null,\
            "tz_label": "Pacific Daylight Time",\
            "tz_offset": -25200,\
            "profile": {\
                "first_name": "slackbot",\
                "last_name": "",\
                "image_24": "https:\/\/a.slack-edge.com...png",\
                "image_32": "https:\/\/a.slack-edge.com...png",\
                "image_48": "https:\/\/a.slack-edge.com...png",\
                "image_72": "https:\/\/a.slack-edge.com...png",\
                "image_192": "https:\/\/a.slack-edge.com...png",\
                "image_512": "https:\/\/a.slack-edge.com...png",\
                "avatar_hash": "sv1444671949",\
                "always_active": true,\
                "real_name": "slackbot",\
                "real_name_normalized": "slackbot",\
                "fields": null\
            },\
            "is_admin": false,\
            "is_owner": false,\
            "is_primary_owner": false,\
            "is_restricted": false,\
            "is_ultra_restricted": false,\
            "is_bot": false,\
            "updated": 0\
        },\
        {\
            "id": "W0123ABC456",\
            "team_id": "T0123ABC456",\
            "name": "glinda",\
            "deleted": false,\
            "color": "9f69e7",\
            "real_name": "Glinda Southgood",\
            "tz": "America\/Los_Angeles",\
            "tz_label": "Pacific Daylight Time",\
            "tz_offset": -25200,\
            "profile": {\
                "avatar_hash": "8fbdd10b41c6",\
                "image_24": "https:\/\/a.slack-edge.com...png",\
                "image_32": "https:\/\/a.slack-edge.com...png",\
                "image_48": "https:\/\/a.slack-edge.com...png",\
                "image_72": "https:\/\/a.slack-edge.com...png",\
                "image_192": "https:\/\/a.slack-edge.com...png",\
                "image_512": "https:\/\/a.slack-edge.com...png",\
                "image_1024": "https:\/\/a.slack-edge.com...png",\
                "image_original": "https:\/\/a.slack-edge.com...png",\
                "first_name": "Glinda",\
                "last_name": "Southgood",\
                "title": "Glinda the Good",\
                "phone": "",\
                "skype": "",\
                "real_name": "Glinda Southgood",\
                "real_name_normalized": "Glinda Southgood",\
                "email": "glenda@south.oz.coven"\
            },\
            "is_admin": true,\
            "is_owner": true,\
            "is_primary_owner": true,\
            "is_restricted": false,\
            "is_ultra_restricted": false,\
            "is_bot": false,\
            "updated": 1480527098,\
            "has_2fa": false\
        }\
    ],
    "cache_ts": 1498777272,
    "response_metadata": {
        "next_cursor": "dXNlcjpVMEc5V0ZYTlo="
    }
}

```

Within `response_metadata` you'll note `next_cursor`, a string pointing at the next page of results. To retrieve the next page of results, provide this value as the `cursor` parameter to the paginated method.

Cursor strings typically end with the `=` character. When presenting this value as a URL or POST parameter, it _must_ be encoded as `%3D`.

We issue our request for the next page of no more than 2 results like this:

```http hljs
CopyGET https://slack.com/api/users.list?limit=2&cursor=dXNlcjpVMEc5V0ZYTlo%3D
Authorization: Bearer xoxb-1234-5678-90123

```

And ( _spoiler alert_): we only get one result back. This workspace actually only has three users. We've reached the end of our pagination journey and there are no more results to retrieve. Our `next_cursor` becomes but an empty string:

```json hljs
Copy{
    "ok": true
    "members": [\
        // that one last member\
    ],
    "cache_ts": 1498777272,
    "response_metadata": {
        "next_cursor": ""
    }
}

```

You'll know that there are no further results to retrieve when a `next_cursor` field contains an empty string ( `""`). You're not even paginating at all if you receive no `response_metadata` or its `next_cursor` value.

Cursors expire and are meant to be used within a reasonable amount of time. You should have no trouble pausing between [rate limiting](https://api.slack.com/docs/rate-limits) windows, but do not persist cursors for hours or days.

Enhanced rate limiting conditions are provided when using cursor-based pagination.

### Error conditions

Currently, the only error specific to pagination that you might encounter is:

- `invalid_cursor` \- Returned when navigating a paginated collection and providing a `cursor` value that just does not compute — either it's gibberish, somehow encoded wrong, or of too great a vintage.

Invalid `limit` values are currently magically adjusted to something sensible. We recommend providing reasonable values for best results, as with most parameters.

### Methods supporting cursor-based pagination

We're adding cursor-based pagination to almost every collection-yielding method.

Today, cursor-based pagination is supported by these methods:

- [`conversations.history`](https://api.slack.com/methods/conversations.history)
- [`conversations.list`](https://api.slack.com/methods/conversations.list)
- [`conversations.members`](https://api.slack.com/methods/conversations.members)
- [`conversations.replies`](https://api.slack.com/methods/conversations.replies)
- [`files.info`](https://api.slack.com/methods/files.info)
- [`reactions.list`](https://api.slack.com/methods/reactions.list)
- [`stars.list`](https://api.slack.com/methods/stars.list)
- [`users.list`](https://api.slack.com/methods/users.list)
- [`groups.list`](https://api.slack.com/methods/groups.list) ( _deprecated_)
- [`im.list`](https://api.slack.com/methods/im.list) ( _deprecated_)
- [`mpim.list`](https://api.slack.com/methods/mpim.list) ( _deprecated_)

* * *

## Classic pagination

You'll find a variety of other _pseudo_ and _real_ pagination schemes through a few other Web API methods.

Each of those API methods detail their pagination strategy.

### Timeline methods

These methods are more positional than page oriented and allow you to navigate through time with `oldest`, `latest`, and a special `inclusive` parameter.

They're all deprecated too!

- `channels.history`
- `groups.history`
- `im.history`
- `mpim.history`

### Traditional paging

These methods use some form of archaic numeric-based `page` and `count` or other limiting parameters.

- [`files.list`](https://api.slack.com/methods/files.list)
- [`search.all`](https://api.slack.com/methods/search.all)
- [`search.files`](https://api.slack.com/methods/search.files)
- [`search.messages`](https://api.slack.com/methods/search.messages)

![Slack Technologies Company Logo](https://cdn.cookielaw.org/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/1ce30484-b023-4ff1-a118-3a9dc53fce45/f83dd0bf-3d5c-47ca-b065-8f247adfeacd/rsz_slack_rgb.png)

## Privacy Preference Center

We use three kinds of cookies on our websites: required, functional, and advertising. You can choose whether functional and advertising cookies apply. Click on the different cookie categories to find out more about each category and to change the default settings. [More information](https://slack.com/cookie-policy)

Allow All

### Manage Consent Preferences

#### Required Cookies

Always Active

Required cookies are necessary for basic website functionality. Some examples include: session cookies needed to transmit the website, authentication cookies, and security cookies.

Cookies Details‎

#### Functional Cookies

Functional Cookies

Functional cookies enhance functions, performance, and services on the website. Some examples include: cookies used to analyze site traffic, cookies used for market research, and cookies used to display advertising that is not directed to a particular individual.

Cookies Details‎

#### Advertising Cookies

Advertising Cookies

Advertising cookies track activity across websites in order to understand a viewer’s interests, and direct them specific marketing. Some examples include: cookies used for remarketing, or interest-based advertising.

Cookies Details‎

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

# Exploring HTTP vs Socket Mode | Slack

The Slack developer docs are moving! We've been working hard at building out a new docs experience at [docs.slack.dev](https://docs.slack.dev/) — now in beta! You can start using the new docs today, but we'll keep the content on both sites up to date during the transition.

[Learn more](https://api.slack.com/changelog/2024-12-api-site-migration)

# Exploring HTTP vs Socket Mode

In the course of your journey to create a Slack app, you will likely want to use the [Events API](https://api.slack.com/apis/events-api), [slash commands](https://api.slack.com/interactivity/slash-commands), [interactivity](https://api.slack.com/interactivity/handling), or [shortcuts](https://api.slack.com/interactivity/shortcuts) to enable your app to respond to messages and handle interactive events happening in Slack. To do so, you will choose to receive event payloads via HTTP requests or WebSocket messages. Each protocol has its pros and cons, which we will explain here.

## What is a web protocol?

Put simply, a web protocol is a set of rules that computers use to communicate over the internet. What this means in terms of a Slack app is how information is sent from the Slack client (end user) to the app and back: how it exchanges information. For Slack apps, this can happen either over HTTP or WebSocket (the use of which is known as Socket Mode in the [app settings](https://api.slack.com/apps)). WebSocket and HTTP are both web communication protocols, but they have different use cases and characteristics.

Here is a side-by-side comparison of the two.

| Feature | HTTP | WebSocket |
| --- | --- | --- |
| Messaging pattern | Request-response | Bi-directional |
| Protocol | Stateless | Stateful |
| Scalability | Scales well horizontally | Challenging to scale due to stateful nature. Slack limits the number of concurrent WebSocket connections to 10 per app. |
| Bidirectional updates | No | Yes |
| Connection length | Short-lived | Long-lived |

## HTTP

HTTP is a protocol that follows a request-response pattern between clients and servers. A short-lived connection to the server is opened for each request, then closed once the request is complete. Within each response, the server provides the client with the requested content as well as information about the request (metadata). HTTP uses half-duplex communication, which means only one party can communicate at a time. Because each request contains all necessary information, it is simpler (compared to using WebSocket) to route requests through proxies to carry out other operations, like caching and encryption.

HTTP communication is stateless: it does not keep track of connections and requests. HTTP is well-suited for static content and standard API requests, like the ones used by Slack apps. In terms of reliability, short-lived connections—like stateless HTTP connections—are inherently more reliable than long-lived connections.

The downside of HTTP that app developers part of a corporation run into is that they cannot expose a public HTTP endpoint due to the firewall because it is a security concern. Another disadvantage to HTTP is that the client opens an ephemeral connection and sends metadata for each request, which incurs a small overhead.

## WebSocket

WebSocket is a protocol that allows for simultaneous two-way communication over the same connection in realtime. This means the server can push realtime updates as soon as they become available instead of waiting to respond to a request from the client. Unlike HTTP, WebSocket is a full-duplex communication protocol.

Because of its low latency and persistent connections, WebSocket is best for applications that require real-time, two-way communication, like online gaming, chat apps, and live updates. Socket Mode in Slack is a great option if you're building an on-premise integration, have no ability to receive external HTTP requests, or want data feed redundancy by opening additional WebSocket connections.

However, WebSocket is stateful, making it more difficult to scale. It also uses long-lived connections that over time could be subject to a network partition or other transient events causing disconnects. Additionally, the socket server backend recycles containers serving connections every now and then, leading to occassional reliability issues. To have the highest possible reliability for application connectivity, we recommend using HTTP for production applications.

## Which to use when

For its convenience, ease of setup, and ability to work behind a firewall, we recommend using Socket Mode when developing your app and using it locally. Once deployed and published for use in a team setting, we recommend using HTTP request URLs. If your production app does not need to use Socket Mode, we recommend sticking with HTTP for the sake of simplicity. There are less moving parts and less complexity for your app to worry about managing. Socket mode is fully supported for distributed apps. However, if you intend to submit your app to be available for use in the [Slack Marketplace](https://api.slack.com/marketplace), using HTTP is a requirement.

Alternatively, if it is a requirement that you work behind a firewall and do not have the ability to expose HTTP endpoints, Socket Mode is there for you. As long as you do not intend to submit your app to the Slack Marketplace and actively maintain your connection to us, Socket Mode is a reliable option.

* * *

## Implementation

Support for both HTTP and WebSocket is built into the [Slack Bolt frameworks](https://tools.slack.dev/). They can also be configured without the use of SDKs.

### HTTP resources

Read more about setting up your app with HTTP [here](https://api.slack.com/apis/http). To explore the Bolt SDK documentation on creating an app with HTTP, refer to the [Bolt for Python guide here](https://tools.slack.dev/bolt-python/tutorial/getting-started-http) and the [Bolt for JavaScript guide here](https://tools.slack.dev/bolt-js/tutorial/getting-started-http/).

### Socket Mode resources

Read more about setting up your app with Socket Mode [here](https://api.slack.com/apis/socket-mode). To explore the Bolt SDK documentation on creating an app with Socket Mode, refer to the [Bolt for Python guide here](https://tools.slack.dev/bolt-python/getting-started) and the [Bolt for JavaScript guide here](https://tools.slack.dev/bolt-js/getting-started).

![Slack Technologies Company Logo](https://cdn.cookielaw.org/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/1ce30484-b023-4ff1-a118-3a9dc53fce45/f83dd0bf-3d5c-47ca-b065-8f247adfeacd/rsz_slack_rgb.png)

## Privacy Preference Center

We use three kinds of cookies on our websites: required, functional, and advertising. You can choose whether functional and advertising cookies apply. Click on the different cookie categories to find out more about each category and to change the default settings. [More information](https://slack.com/cookie-policy)

Allow All

### Manage Consent Preferences

#### Required Cookies

Always Active

Required cookies are necessary for basic website functionality. Some examples include: session cookies needed to transmit the website, authentication cookies, and security cookies.

Cookies Details‎

#### Functional Cookies

Functional Cookies

Functional cookies enhance functions, performance, and services on the website. Some examples include: cookies used to analyze site traffic, cookies used for market research, and cookies used to display advertising that is not directed to a particular individual.

Cookies Details‎

#### Advertising Cookies

Advertising Cookies

Advertising cookies track activity across websites in order to understand a viewer’s interests, and direct them specific marketing. Some examples include: cookies used for remarketing, or interest-based advertising.

Cookies Details‎

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

# Slack Connect API reference | Slack

The Slack developer docs are moving! We've been working hard at building out a new docs experience at [docs.slack.dev](https://docs.slack.dev/) — now in beta! You can start using the new docs today, but we'll keep the content on both sites up to date during the transition.

[Learn more](https://api.slack.com/changelog/2024-12-api-site-migration)

# Slack Connect API reference

[Slack Connect](https://api.slack.com/apis/channels-between-orgs) allows users between different workspaces and organizations to work together on Slack.

Below is a list of Slack Connect-related scopes, methods and events. For information on how to use these components together to address common use cases, see our [Using Slack Connect API methods](https://api.slack.com/apis/connect) guide.

## Scopes

| Scope | Description |
| --- | --- |
| [`conversations.connect:read`](https://api.slack.com/scopes/conversations.connect:read) | Receive Slack Connect invite events sent to the channels your slack app is in. |
| [`conversations.connect:write`](https://api.slack.com/scopes/conversations.connect:write) | Create Slack Connect invitations for channels that your slack app has been added to, and accept invitations sent to your slack app. |
| [`conversations.connect:manage`](https://api.slack.com/scopes/conversations.connect:manage) | Allows your slack app to manage Slack Connect channels, and approve, decline, and list Slack Connect invitations. Since approval requires more authority than accepting invitations, apps with this feature can only be installed by a workspace owner or admin. |

## Methods

| Method | Description |
| --- | --- |
| [`admin.conversations.disconnectShared`](https://api.slack.com/methods/admin.conversations.disconnectShared) | Disconnect a connected channel from one or more workspaces. |
| [`conversations.acceptSharedInvite`](https://api.slack.com/methods/conversations.acceptSharedInvite) | Accepts an invitation to a Slack Connect channel. |
| [`conversations.approveSharedInvite`](https://api.slack.com/methods/conversations.approveSharedInvite) | Approves an invitation to a Slack Connect channel |
| [`conversations.declineSharedInvite`](https://api.slack.com/methods/conversations.declineSharedInvite) | Declines a Slack Connect channel invite. |
| [`conversations.externalInvitePermissions.set`](https://api.slack.com/methods/conversations.externalInvitePermissions.set) | Upgrade or downgrade Slack Connect channel permissions between "can post only" and "can post and invite". |
| [`conversations.inviteShared`](https://api.slack.com/methods/conversations.inviteShared) | Sends an invitation to a Slack Connect channel. |
| [`conversations.listConnectInvites`](https://api.slack.com/methods/conversations.listConnectInvites) | Lists shared channel invites that have been generated or received but have not been approved by all parties. |
| [`conversations.requestSharedInvite.approve`](https://api.slack.com/methods/conversations.requestSharedInvite.approve) | Approves a request to add an external user to a channel and sends them a Slack Connect invite. |
| [`conversations.requestSharedInvite.deny`](https://api.slack.com/methods/conversations.requestSharedInvite.deny) | Denies a request to invite an external user to a channel. |
| [`conversations.requestSharedInvite.list`](https://api.slack.com/methods/conversations.requestSharedInvite.list) | Lists requests to add external users to channels with ability to filter. |
| [`team.externalTeams.disconnect`](https://api.slack.com/methods/team.externalTeams.disconnect) | Disconnects all Slack Connect channels and direct messages (DMs) from an external organization. |
| [`team.externalTeams.list`](https://api.slack.com/methods/team.externalTeams.list) | Returns a list of all the external teams connected and details about the connection. |
| [`users.discoverableContacts.lookup`](https://api.slack.com/methods/users.discoverableContacts.lookup) | Look up an email address to see if someone is [discoverable](https://slack.com/help/articles/5535749574803-Manage-Slack-Connect-discoverability-for-your-organization) on Slack. |

## Events

| Method | Description |
| --- | --- |
| [`shared_channel_invite_accepted`](https://api.slack.com/events/shared_channel_invite_accepted) | A shared channel invite was accepted. |
| [`shared_channel_invite_approved`](https://api.slack.com/events/shared_channel_invite_approved) | A shared channel invite was approved. |
| [`shared_channel_invite_declined`](https://api.slack.com/events/shared_channel_invite_declined) | A shared channel invite was declined. |
| [`shared_channel_invite_received`](https://api.slack.com/events/shared_channel_invite_received) | A shared channel invite was sent to a Slack user. |
| [`shared_channel_invite_requested`](https://api.slack.com/events/shared_channel_invite_requested) | A shared channel invite was sent to a Slack user. |

**[Bits and bobs for the Deno developer](https://github.com/slack-samples/deno-code-snippets)**

These [TypeScript code snippets](https://github.com/slack-samples/deno-code-snippets) help you work with canvases, authentication, forms, connectors, and more.

![Slack Technologies Company Logo](https://cdn.cookielaw.org/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/1ce30484-b023-4ff1-a118-3a9dc53fce45/f83dd0bf-3d5c-47ca-b065-8f247adfeacd/rsz_slack_rgb.png)

## Privacy Preference Center

We use three kinds of cookies on our websites: required, functional, and advertising. You can choose whether functional and advertising cookies apply. Click on the different cookie categories to find out more about each category and to change the default settings. [More information](https://slack.com/cookie-policy)

Allow All

### Manage Consent Preferences

#### Required Cookies

Always Active

Required cookies are necessary for basic website functionality. Some examples include: session cookies needed to transmit the website, authentication cookies, and security cookies.

Cookies Details‎

#### Functional Cookies

Functional Cookies

Functional cookies enhance functions, performance, and services on the website. Some examples include: cookies used to analyze site traffic, cookies used for market research, and cookies used to display advertising that is not directed to a particular individual.

Cookies Details‎

#### Advertising Cookies

Advertising Cookies

Advertising cookies track activity across websites in order to understand a viewer’s interests, and direct them specific marketing. Some examples include: cookies used for remarketing, or interest-based advertising.

Cookies Details‎

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

# There's been a glitch… | Slack

![](https://a.slack-edge.com/80588/img/404/marrakesh-meadow-80.jpg)

# There’s been a glitch…

We’re not quite sure what went wrong. You can go back, or try looking on our [Help Center](http://get.slack.help/hc/en-us) if you need a hand.

# Conversations API | Slack

The Slack developer docs are moving! We've been working hard at building out a new docs experience at [docs.slack.dev](https://docs.slack.dev/) — now in beta! You can start using the new docs today, but we'll keep the content on both sites up to date during the transition.

[Learn more](https://api.slack.com/changelog/2024-12-api-site-migration)

# Conversations API

_Public channels, private channels, DMs... They're all conversations!_

The Slack Conversations API provides you with a unified interface to work with all the channel-like things encountered in Slack: public channels, private channels, direct messages, group direct messages, [shared channels](https://api.slack.com/shared-channels), and so on.

Use this [API family](https://api.slack.com/methods#conversations) to [review history](https://api.slack.com/methods/conversations.history), [create](https://api.slack.com/methods/conversations.create) or [archive](https://api.slack.com/methods/conversations.archive) channels, [invite](https://api.slack.com/methods/conversations.invite) team members, [set conversation topics](https://api.slack.com/methods/conversations.setTopic) and [purpose](https://api.slack.com/methods/conversations.setPurpose), and more — no matter what type of conversation you're working with.

The types of channels you interface with in the Conversations API are governed by corresponding [permission scopes](https://api.slack.com/scopes). For example; to retrieve details about a public channel, you'll need [`channels:read`](https://api.slack.com/scopes/channels:read). For details about a private channel, you'll need [`groups:read`](https://api.slack.com/scopes/groups:read).

## Using the Conversations API

Before the Conversations API, you needed to use different methods from multiple "family trees" to achieve the same thing depending on the _type_ of channel you were working with.

For example, to list direct messages you had to call the `im.list` method, but for public channels you had to call the `channels.list` method. Many different objects and shapes represented the same type of timeline message container at their core. These methods are now [deprecated](https://api.slack.com/apis/changelog/2020-01-deprecating-antecedents-to-the-conversations-api).

In the new model, use `conversations.*` methods to access anything channel-like. For example, the [`conversation.list`](https://api.slack.com/methods/conversations.list) method returns information on public, private, and direct message channels, when accessed with the appropriate [permission scopes](https://api.slack.com/scopes).

## Conversations API methods

| Method & Description | Description |
| --- | --- |
| [conversations.acceptSharedInvite](https://api.slack.com/methods/conversations.acceptSharedInvite) <br>Accepts an invitation to a Slack Connect channel. | Accepts an invitation to a Slack Connect channel. |
| [conversations.approveSharedInvite](https://api.slack.com/methods/conversations.approveSharedInvite) <br>Approves an invitation to a Slack Connect channel | Approves an invitation to a Slack Connect channel |
| [conversations.archive](https://api.slack.com/methods/conversations.archive) <br>Archives a conversation. | Archives a conversation. |
| [conversations.canvases.create](https://api.slack.com/methods/conversations.canvases.create) <br>Create a channel canvas for a channel | Create a channel canvas for a channel |
| [conversations.close](https://api.slack.com/methods/conversations.close) <br>Closes a direct message or multi-person direct message. | Closes a direct message or multi-person direct message. |
| [conversations.create](https://api.slack.com/methods/conversations.create) <br>Initiates a public or private channel-based conversation | Initiates a public or private channel-based conversation |
| [conversations.declineSharedInvite](https://api.slack.com/methods/conversations.declineSharedInvite) <br>Declines a Slack Connect channel invite. | Declines a Slack Connect channel invite. |
| [conversations.externalInvitePermissions.set](https://api.slack.com/methods/conversations.externalInvitePermissions.set) <br>Upgrade or downgrade Slack Connect channel permissions between 'can post only' and 'can post and invite'. | Upgrade or downgrade Slack Connect channel permissions between 'can post only' and 'can post and invite'. |
| [conversations.history](https://api.slack.com/methods/conversations.history) <br>Fetches a conversation's history of messages and events. | Fetches a conversation's history of messages and events. |
| [conversations.info](https://api.slack.com/methods/conversations.info) <br>Retrieve information about a conversation. | Retrieve information about a conversation. |
| [conversations.invite](https://api.slack.com/methods/conversations.invite) <br>Invites users to a channel. | Invites users to a channel. |
| [conversations.inviteShared](https://api.slack.com/methods/conversations.inviteShared) <br>Sends an invitation to a Slack Connect channel | Sends an invitation to a Slack Connect channel |
| [conversations.join](https://api.slack.com/methods/conversations.join) <br>Joins an existing conversation. | Joins an existing conversation. |
| [conversations.kick](https://api.slack.com/methods/conversations.kick) <br>Removes a user from a conversation. | Removes a user from a conversation. |
| [conversations.leave](https://api.slack.com/methods/conversations.leave) <br>Leaves a conversation. | Leaves a conversation. |
| [conversations.list](https://api.slack.com/methods/conversations.list) <br>Lists all channels in a Slack team. | Lists all channels in a Slack team. |
| [conversations.listConnectInvites](https://api.slack.com/methods/conversations.listConnectInvites) <br>Lists shared channel invites that have been generated or received but have not been approved by all parties | Lists shared channel invites that have been generated or received but have not been approved by all parties |
| [conversations.mark](https://api.slack.com/methods/conversations.mark) <br>Sets the read cursor in a channel. | Sets the read cursor in a channel. |
| [conversations.members](https://api.slack.com/methods/conversations.members) <br>Retrieve members of a conversation. | Retrieve members of a conversation. |
| [conversations.open](https://api.slack.com/methods/conversations.open) <br>Opens or resumes a direct message or multi-person direct message. | Opens or resumes a direct message or multi-person direct message. |
| [conversations.rename](https://api.slack.com/methods/conversations.rename) <br>Renames a conversation. | Renames a conversation. |
| [conversations.replies](https://api.slack.com/methods/conversations.replies) <br>Retrieve a thread of messages posted to a conversation | Retrieve a thread of messages posted to a conversation |
| [conversations.requestSharedInvite.approve](https://api.slack.com/methods/conversations.requestSharedInvite.approve) <br>Approves a request to add an external user to a channel and sends them a Slack Connect invite | Approves a request to add an external user to a channel and sends them a Slack Connect invite |
| [conversations.requestSharedInvite.deny](https://api.slack.com/methods/conversations.requestSharedInvite.deny) <br>Denies a request to invite an external user to a channel | Denies a request to invite an external user to a channel |
| [conversations.requestSharedInvite.list](https://api.slack.com/methods/conversations.requestSharedInvite.list) <br>Lists requests to add external users to channels with ability to filter. | Lists requests to add external users to channels with ability to filter. |
| [conversations.setPurpose](https://api.slack.com/methods/conversations.setPurpose) <br>Sets the channel description. | Sets the channel description. |
| [conversations.setTopic](https://api.slack.com/methods/conversations.setTopic) <br>Sets the topic for a conversation. | Sets the topic for a conversation. |
| [conversations.unarchive](https://api.slack.com/methods/conversations.unarchive) <br>Reverses conversation archival. | Reverses conversation archival. |
| [users.conversations](https://api.slack.com/methods/users.conversations) <br>List conversations the calling user may access. | List conversations the calling user may access. |

## Working with Shared Channels

Each channel has a unique-to-the-team ID that begins with a single letter prefix: either `C`, `G`, or `D`.

When a channel is shared across teams (see [Slack Connect: working with channels between organizations](https://api.slack.com/shared-channels)), the prefix of the channel ID may be changed, e.g. a private channel with ID `G0987654321` may become ID `C0987654321`.

This is one reason you should use the `conversations` methods instead of the previous API methods! You cannot rely on a private shared channel's unique ID remaining constant during its entire lifetime.

The channel type object tells you additional channel information. If the channel is shared, `is_shared` is set to `true`. If it is a private channel or a group DM channel, the properties `is_private` or `is_mpim` are set to `true`.

### The conversational booleans

Some of the most important fields in [conversation objects](https://api.slack.com/types/conversation) are the booleans indicating what kind of conversation/channel it is and how private it is. For a list of these booleans, refer to [conversation-related booleans](https://api.slack.com/types/conversation#booleans).

## Conversation membership

Discover who is party to a conversation with [`conversations.members`](https://api.slack.com/methods/conversations.members), a paginated method allowing you to safely navigate through very large (or tiny) collections of users.

## Permission scopes

Your app's scopes act as a filter. They sort out the conversations you don't have access to, guaranteeing that Conversations API methods only return the conversations your app should see.

### Scopes for classic apps

All Conversations API endpoints still accept _multiple_ scopes and filter access to channels based on the provided token's scope. If you have a scope that allowed you to use a deprecated conversation method, that scope will work with the Conversations API equivalent.

For instance, [`conversations.list`](https://api.slack.com/methods/conversations.list) accepts [`channels:read`](https://api.slack.com/scopes/channels:read), [`groups:read`](https://api.slack.com/scopes/groups:read), [`mpim:read`](https://api.slack.com/scopes/mpim:read), and [`im:read`](https://api.slack.com/scopes/im:read).

If you only have `channels:read`, then `conversations.list` will only return public channels and all the related methods will only deal with public channels. If you have both `channels:read` and `im:read`, then methods will only return public channels and DMs, and so on.

### Scopes for workspace apps (deprecated)

Workspace apps were [retired in August 2021](https://api.slack.com/changelog/2021-03-workspace-apps-to-retire-in-august-2021).

## Pagination

The Conversations API uses our [cursor-based pagination model](https://api.slack.com/docs/pagination), improving the performance of requests over large sets of data.

Just set a `limit` on your first request, include the `next_cursor` found in `response_metadata` in the response as the `cursor` parameter in your next request and you're paginating with ease on the conversational trapeze. Unlike older methods, the Conversations API is paginated _by default_.

### Inconsistent page size is a feature, not a bug

Keep in mind that it's possible to receive fewer results than your specified `limit`, even when there are additional results to retrieve. Maybe you'll even receive 0 results but still have a `next_cursor` with 4 more waiting in the wings.

When looking up MPIMs using the `conversations.list`, you are likely to get far fewer results than requested number with a `next_cursor` value, although `next_cursor` will continue to indicate when more results await. For example, when requesting 100 MPIMs, it may return only 5.

## Known issues

#### 🚧 Channel IDs can become unstable in certain situations

There are a few circumstances where channel IDs might change within a workspace. You can use [`conversations.list`](https://api.slack.com/methods/conversations.list) regularly to monitor change for known `#channel` names if ID stability is important to you.

In the future, we'll mitigate this unexpected transition with appropriate [Events API](https://api.slack.com/events-api) events or other solutions.

#### 🚧 MPIM events and channel types

In a Multiparty Direct Message Channel (MPIM) with a foreign user, events like [`member_joined_channel`](https://api.slack.com/events/member_joined_channel) and [`member_left_channel`](https://api.slack.com/events/member_left_channel) may dispatch an incorrect value for `channel_type`.

#### 🚧 IM object format is not yet consistent

IM formats may differ from other channel objects. We're working towards making all objects the same format. You may notice `members` lists that aren't meant to be there. These are almost all cleared up!

#### 🚧 Unsharing channels

When a channel becomes unshared, [`conversations.history`](https://api.slack.com/methods/conversations.history) access for the channel may become unreliable.

Recommended reading

- [Block Kit](https://api.slack.com/block-kit)
- [Messaging for Slack apps](https://api.slack.com/messaging)
- [Using the Slack Web API](https://api.slack.com/web)

Next steps

- [Creating interactive messages](https://api.slack.com/messaging/interactivity)

# HTTP Request URLs | Slack

The Slack developer docs are moving! We've been working hard at building out a new docs experience at [docs.slack.dev](https://docs.slack.dev/) — now in beta! You can start using the new docs today, but we'll keep the content on both sites up to date during the transition.

[Learn more](https://api.slack.com/changelog/2024-12-api-site-migration)

# HTTP Request URLs

Once you've weighed the pros and cons and [made the decision to use HTTP](https://api.slack.com/apis/event-delivery) in your app, you will need to set up and verify your request URL. This guide will show you how to set this up.

## Handling app installation and authentication with Request URLs

Request URLs operate similarly to [slash command](https://api.slack.com/slash-commands) invocation URLs in that they receive an HTTP POST containing data in response to activity. In the Events API, your Events API request URL is the target location where all of the events your application is subscribed to will be delivered, regardless of the workspace or event type.

Since your application will have only one Events API request URL, you'll need to do any additional dispatch or routing server-side after receiving event data.

Your request URL will receive JSON-based payloads containing wrapped [event types](https://api.slack.com/events/api). The volume of events will vary depending on the events you subscribe to and the size and activity of the workspaces that install your application.

Your request URL might receive _many_ events and requests. Consider decoupling your ingestion of events from the processing and reaction to them. Review the Events API guide section on [rate limiting](https://api.slack.com/apis/events-api#rate_limiting) to better understand the maximum event volume you may receive.

### Request URL configuration and verification

After you create your app, navigate to the [app settings page](https://api.slack.com/apps) and select your app to view its settings. In the **Event Subscriptions** section, toggle the feature on. This will reveal a field where you should enter your request URL.

Your Event request URL must be confirmed before saving this form. If your server takes some time to "wake up" and your initial attempt at URL verification fails due to a timeout, use the **Retry** button to attempt verification again. Careful, request URLs are case-sensitive.

### URL verification handshake

The events sent to your request URL may contain sensitive information associated with the workspaces having approved your Slack app. To ensure that events are being delivered to a server under your direct control, we must verify your ownership by issuing you a challenge request.

After you've completed typing your URL, we'll dispatch an HTTP POST to your request URL. We'll verify your SSL certificate and we'll send a `application/json` POST body containing three fields:

```json hljs
Copy{
    "token": "Jhj5dZrVaK7ZwHHjRyZWjbDl",
    "challenge": "3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P",
    "type": "url_verification"
}

```

This event does not require a specific OAuth scope or subscription. You'll automatically receive it whenever configuring an [Events API](https://api.slack.com/apis/events-api) request URL. The attributes Slack sends include:

- `token`: This deprecated verification token is proof that the request is coming from Slack on behalf of your application. You'll find this value in the **App Credentials** section of the **Basic Information** of your [app settings](https://api.slack.com/apps). Verifying this value is more important when working with real events after this verification sequence has been completed. When responding to real events, always use the [more secure signing secret process](https://api.slack.com/docs/verifying-requests-from-slack) to verify Slack requests' authenticity.
- `challenge`: a randomly generated string produced by Slack. The purpose for sending this string is that you'll respond to this request with a response body containing this value.
- `type`: this payload is similarly formatted to other event types you'll encounter in the Events API. To help you differentiate URL verification requests form other event types, we inform you that this is of the `url_verification` variety.

### Respond to the challenge

Once you receive the event, complete the sequence by responding with HTTP 200 and the `challenge` attribute value.

Responses can be sent in plaintext:

```http hljs
CopyHTTP 200 OK
Content-type: text/plain
3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P

```

Alternatively, if you're feeling more formal, respond with `application/x-www-form-urlencoded` and a named `challenge` parameter:

```http hljs
CopyHTTP 200 OK
Content-type: application/x-www-form-urlencoded
challenge=3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P

```

Or if you feel like showing off, respond with `application/json`:

```http hljs
CopyHTTP 200 OK
Content-type: application/json
{"challenge":"3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P"}

```

Once URL verification is complete, you'll see a green check mark celebrating your victory.

![Finally, you win the game of URL verification.](https://a.slack-edge.com/80588/img/api/event_url_verification.png)

If you receive an error from your server, a timeout, or other exceptional condition occurs, you'll see error messages that will hopefully help you understand what's amiss before you try again.

![https://internal-intranet-links-will-not-work-here.local/sorry won't work so a different URL will need to be given before retrying](https://a.slack-edge.com/80588/img/api/event_url_verification_failure.png)

Especially when working with large workspaces, many workspaces, or subscribing to a large number of events, de-coupling the processing of and reaction to events is key. With this challenging handshake complete, you're ready to open up our [event type catalog](https://api.slack.com/events/api) and decide which events to subscribe to.

## Next steps

Now that you've set up your app to use HTTP request URLs, explore the [Events API](https://api.slack.com/apis/events-api) guide to learn how to subscribe to, receive, and handle events. Also be sure to check out the [Interactivity](https://api.slack.com/interactivity/handling) guide, including [Shortcuts](https://api.slack.com/interactivity/shortcuts) and [Slash commands](https://api.slack.com/interactivity/slash-commands) for additional ways to customize your app.

![Slack Technologies Company Logo](https://cdn.cookielaw.org/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/1ce30484-b023-4ff1-a118-3a9dc53fce45/f83dd0bf-3d5c-47ca-b065-8f247adfeacd/rsz_slack_rgb.png)

## Privacy Preference Center

We use three kinds of cookies on our websites: required, functional, and advertising. You can choose whether functional and advertising cookies apply. Click on the different cookie categories to find out more about each category and to change the default settings. [More information](https://slack.com/cookie-policy)

Allow All

### Manage Consent Preferences

#### Required Cookies

Always Active

Required cookies are necessary for basic website functionality. Some examples include: session cookies needed to transmit the website, authentication cookies, and security cookies.

Cookies Details‎

#### Functional Cookies

Functional Cookies

Functional cookies enhance functions, performance, and services on the website. Some examples include: cookies used to analyze site traffic, cookies used for market research, and cookies used to display advertising that is not directed to a particular individual.

Cookies Details‎

#### Advertising Cookies

Advertising Cookies

Advertising cookies track activity across websites in order to understand a viewer’s interests, and direct them specific marketing. Some examples include: cookies used for remarketing, or interest-based advertising.

Cookies Details‎

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

# There's been a glitch… | Slack

![](https://a.slack-edge.com/80588/img/404/marrakesh-meadow-80.jpg)

# There’s been a glitch…

We’re not quite sure what went wrong. You can go back, or try looking on our [Help Center](http://get.slack.help/hc/en-us) if you need a hand.

# There's been a glitch… | Slack

![](https://a.slack-edge.com/80588/img/404/marrakesh-meadow-80.jpg)

# There’s been a glitch…

We’re not quite sure what went wrong. You can go back, or try looking on our [Help Center](http://get.slack.help/hc/en-us) if you need a hand.

