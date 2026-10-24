
# Task 02 — Identify the Client, API and Server

## Communication Diagram

```text
+---------+       +---------+       +---------+
| Browser | ----> |   API   | ----> |  Server |
| Client  |       | Endpoint|       |         |
+---------+       +---------+       +---------+
     ^                                  |
     |                                  |
     +---------- JSON Response <--------+
```

## Component Labels

1. **Browser (Client):** Sends a request to access a resource.
2. **API:** Provides the endpoint through which the client requests data.
3. **Server:** Processes the request and provides the requested data.
4. **Response:** Contains the returned data, such as a JSON object.

## Written Explanation

When the browser requests `/posts/1`, it sends an HTTP GET request to the API endpoint. The server processes the request and retrieves the data for post ID 1. The server returns an HTTP response containing the post data in JSON format. The browser displays the returned JSON data to the user.
