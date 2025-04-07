# Asana REST API Documentation

## Overview

The Asana API is a RESTful interface for interacting with the Asana platform, providing comprehensive access to Asana's project management and collaboration features.

### Base URL
`https://app.asana.com/api/1.0`

## Key Features

- RESTful design
- JSON request/response support
- Standard HTTP methods
- Predictable resource-oriented URLs

## Authentication

Asana provides several authentication methods for accessing its API:

### 1. Personal Access Token (PAT)

- Quickest and simplest authentication method
- Long-lived tokens providing API access
- Provides same permissions as the generating user
- Best for:
  - Scripts
  - Simple apps without multiple user logins

### PAT Attribution
- API actions are attributed to the token's creator
- Can create a separate "bot" account to avoid personal attribution

### 2. Service Account

- Enterprise-tier feature
- Created by Asana super admins
- Provides complete access to all organizational data
- Ideal for:
  - Data backups
  - Organizational management
  - Automated administrative tasks
  - Comprehensive integrations

### 3. OAuth

- Open-standard authentication protocol
- Allows multiple users to sign in
- More complex implementation
- Provides enhanced security and features
- Best for apps requiring multi-user access

### 4. OpenID Connect (OIDC)

- Authentication protocol built on OAuth 2.0
- Enables users to log in using Asana credentials
- Facilitates single sign-on across multiple platforms

> Note: View-only license users have limited API access. Check user permissions using the workspace membership endpoint.

## Core Resources and Endpoints

### Tasks API

Tasks represent work items that can be assigned, tracked, and organized within projects and workspaces.

#### Task Object Structure

**Key Properties**:
- `gid`: Globally unique identifier
- `name`: Task name
- `resource_subtype`: Task type (e.g., `default_task`, `milestone`, `approval`)
- `assignee`: User assigned to the task
- `due_on`: Task due date
- `completed`: Boolean indicating task completion status
- `custom_fields`: Custom field values applied to the task

#### Available Task Endpoints

1. **Get Tasks**
   - `GET /tasks`: Retrieve multiple tasks
   - `GET /tasks/{task_gid}`: Get a specific task

2. **Create Task**
   - `POST /tasks`: Create a new task
   - Supports adding to projects, setting assignees, custom fields

3. **Update Task**
   - `PUT /tasks/{task_gid}`: Modify task details

4. **Delete Task**
   - `DELETE /tasks/{task_gid}`: Remove a task

5. **Related Task Actions**
   - Add/Remove Projects
   - Add/Remove Tags
   - Add/Remove Followers
   - Create Subtasks
   - Set Task Dependencies
   - Search Tasks

#### Example Task Object

```json
{
  "gid": "12345",
  "name": "Buy catnip",
  "assignee": {
    "name": "Greg Sanchez"
  },
  "due_on": "2019-09-15",
  "completed": false
}
```

### Projects API

A project in Asana represents "a prioritized list of tasks or a board with columns of tasks represented as cards".

#### Project Object Structure

**Key Fields**:
- `gid`: Globally unique identifier
- `name`: Project name
- `workspace`: Associated workspace
- `team`: Shared team
- `owner`: Project creator
- `archived`: Project completion status
- `privacy_setting`: Access level (e.g., `public_to_workspace`, `private`)

#### Key Project Endpoints

1. **Get Projects**
   - `GET /projects`: Retrieve multiple projects
   - Parameters:
     - Workspace filter
     - Team filter
     - Pagination options

2. **Create Project**
   - `POST /projects`
   - Required fields:
     - `name`
     - `workspace`

3. **Update Project**
   - `PUT /projects/{project_gid}`
   - Updatable fields:
     - `name`
     - `notes`
     - `owner`
     - `team`

4. **Delete Project**
   - `DELETE /projects/{project_gid}`

5. **Project-Specific Operations**
   - Add/remove members
   - Add/remove custom fields
   - Add/remove followers
   - Create project from template

### Users API

The Users API allows interaction with user accounts in Asana.

#### User Object Properties

**UserCompact**:
- `gid`: Globally unique identifier (string)
- `resource_type`: Base type of resource (string)
- `name`: User's name (string)

**User (Extended Properties)**:
- `email`: User's email address (string)
- `photo`: Profile photo in various sizes (object/null)
- `workspaces`: Accessible workspaces/organizations (array)

#### User Endpoints

- `GET /users`: Get multiple users
- `GET /users/{user_gid}`: Get a specific user
- `GET /users/{user_gid}/favorites`: Get user's favorites
- `GET /teams/{team_gid}/users`: Get users in a team
- `GET /workspaces/{workspace_gid}/users`: Get users in a workspace/organization

#### Notes
- Special identifier `me` can refer to the current authenticated user
- Email and name are read-only except for the authenticated user
- Profile photos available in multiple sizes (21, 27, 36, 60, 128, 1024 pixels)

### Attachments API

An attachment in Asana represents a file attached to a task.

#### Attachment Types

**AttachmentCompact**:
- `gid`: Globally unique identifier (string)
- `resource_type`: Base resource type (string)
- `name`: File name (string)
- `resource_subtype`: Hosting service (string)

**Valid Hosting Services**:
- `asana`
- `dropbox`
- `gdrive`
- `onedrive`
- `box`
- `vimeo`
- `external`

**Attachment (Full Object)**:
- `connected_to_app`: Whether attachment is connected to requesting app (boolean)
- `created_at`: Creation timestamp
- `download_url`: URL containing attachment content
- `host`: Attachment hosting service
- `parent`: Associated task details
- `permanent_url`: Persistent attachment URL
- `size`: Attachment size in bytes
- `view_url`: User-friendly attachment viewing URL

**Note**: Download URLs may be temporarily valid and should be retrieved on-demand.

## Additional Resources

- **Workspaces**
- **Teams**
- **Sections**
- **Custom Fields**
- **Tags**
- **Goals**
- **Portfolios**
- **Webhooks**
- **Events API**
- **Batch API**

## Best Practices

- Use compact representations for efficiency
- Customize responses using input/output options
- Refer to the official documentation for implementation details

## Additional Resources

- [Developer Forum](https://forum.asana.com/c/api/24)
- [Guides](https://developers.asana.com/docs/overview)
- [Changelog](https://developers.asana.com/docs/change-log)