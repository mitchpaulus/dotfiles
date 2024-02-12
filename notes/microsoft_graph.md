# Microsoft Graph

The hot new way to integrate with Office 365 data.

## Tennant Id

Can get from [Azure portal](https://portal.azure.com) -> Azure Active Directory.
Is a UUID. Typically represents our company.


## Video

[An introduction to Microsoft Graph for developers - Part I - Getting started - October 2019](https://www.youtube.com/watch?v=EBbnpFdB92A)

12:00 Delve is built on Microsoft Graph
12:37 Office.com is also built on Microsoft Graph
16:09 5 Steps to first graph app
17:48 Graph Explorer



## Getting Email Attachments

https://docs.microsoft.com/en-us/graph/api/attachment-get?view=graph-rest-1.0&tabs=http#example-1-get-the-properties-of-a-file-attachment

> You can append the path segment `/$value` to get the raw contents of a file or item attachment.

```
GET https://graph.microsoft.com/v1.0/me/messages/AAMkAGUzY5QKjAAA=/attachments/AAMkAGUzY5QKjAAABEgAQAMkpJI_X-LBFgvrv1PlZYd8=/$value
```

## SDKs


Microsoft.Graph - Contains the models and request builders for accessing the v1.0 endpoint with the fluent API.
Microsoft.Graph has a dependency on Microsoft.Graph.Core.

Microsoft.Graph.Beta - Contains the models and request builders for accessing the beta endpoint with the fluent API.
Microsoft.Graph.Beta has a dependency on Microsoft.Graph.Core.

Microsoft.Graph.Core - The core library for making calls to Microsoft Graph.

Microsoft.Graph.Auth - Provides an authentication scenario-based wrapper of the Microsoft Authentication Library (MSAL) for use with the Microsoft Graph SDK.
Microsoft.Graph.Auth has a dependency on Microsoft.Graph.Core.


## Chats

- Listing chats: <https://learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0&tabs=http>

```
params = {
    '$expand': 'members',
    '$filter': "chatType eq \'oneOnOne\'",
    '$top': '50'
}
```

Users my account can see: <https://graph.microsoft.com/v1.0/users>

Content type is either `html` or `text` for chat messages.
<https://learn.microsoft.com/en-us/graph/api/resources/itembody?view=graph-rest-1.0>

- Listing messages: <https://learn.microsoft.com/en-us/graph/api/chat-list-messages?view=graph-rest-1.0&tabs=http>

```
GET /me/chats/{chat-id}/messages
GET /users/{user-id | user-principal-name}/chats/{chat-id}/messages
GET /chats/{chat-id}/messages

Name	Description
$top	Controls the number of items per response. Maximum allowed $top value is 50.
$orderby	Currently supports the lastModifiedDateTime (default) and createdDateTime properties in descending order. The ascending order is currently not supported.
$filter	Sets the date range filter for the lastModifiedDateTime and createdDateTime properties.
        The lastModifiedDateTime property supports the gt and lt operators.
        The createdDateTime property supports the lt operator.
        You can only filter results if the request URL contains the $orderby and $filter query parameters configured for the same property;
        otherwise, the $filter query option is ignored.
```

## Calendar

Calendar View: <https://learn.microsoft.com/en-us/graph/api/calendar-list-calendarview?view=graph-rest-1.0&tabs=http>.
That helps take care of recurring events and such.

```
GET /me/calendar/calendarView?startDateTime={start_datetime}&endDateTime={end_datetime}
GET /users/{id | userPrincipalName}/calendar/calendarView?startDateTime={start_datetime}&endDateTime={end_datetime}
```

## Share Link

<https://learn.microsoft.com/en-us/graph/api/driveitem-createlink?view=graph-rest-1.0&tabs=http>


## API Reference

<https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0&preserve-view=true>
