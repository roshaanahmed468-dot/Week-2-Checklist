# Phase 02 — HTTP Requests, Responses & REST

## Task 04 — Analyze a URL

URL: `https://api.example.com/students/101`

| # | Part                | Value             |
|---|---------------------|-------------------|
| 1 | Protocol            | `https`           |
| 2 | Host                | `api.example.com` |
| 3 | Path                | `/students/101`   |
| 4 | Resource            | `students`        |
| 5 | Resource identifier | `101`             |

## Task 05 — REST API Operation Table

| Operation             | HTTP Method | Endpoint      |
|-----------------------|-------------|---------------|
| Retrieve all students | GET         | /students     |
| Create a student      | POST        | /students     |
| Retrieve student 101  | GET         | /students/101 |
| Update student 101    | PUT         | /students/101 |
| Delete student 101    | DELETE      | /students/101 |

**Why different methods?** HTTP methods describe the *action* on a resource. GET reads data
without changing it, POST creates a new resource in a collection, PUT replaces or updates an
existing resource identified by its URL, and DELETE removes it. The URL names *what* is acted on;
the method says *what to do* with it. The same URL (`/students/101`) therefore supports several
operations depending on the method.

## Task 06 — GET Requests

| Endpoint | Method | Status | Response body (summary)                                   |
|----------|--------|--------|-----------------------------------------------------------|
| /posts/1 | GET    | 200    | `{"userId":1,"id":1,"title":"sunt aut facere…","body":"quia et suscipit…"}` |
| /posts/2 | GET    | 200    | `{"userId":1,"id":2,"title":"qui est esse","body":"est rerum tempore…"}`    |
| /posts/3 | GET    | 200    | `{"userId":1,"id":3,"title":"ea molestias quasi…","body":"et iusto sed…"}`  |

## Task 07 — POST (create)

- Method: `POST`
- Endpoint: `https://jsonplaceholder.typicode.com/posts`
- Request body:
```json
{ "title": "My API Lab", "body": "Testing POST request", "userId": 1 }
```
- Status code: `201 Created`
- Response body:
```json
{ "title": "My API Lab", "body": "Testing POST request", "userId": 1, "id": 101 }
```
JSONPlaceholder is a fake API, so it returns `id: 101` but does not store the post.

## Task 08 — PUT (update)

- Method: `PUT`
- Endpoint: `/posts/1`
- Request body:
```json
{ "id": 1, "title": "Updated by API Lab", "body": "Updated body text", "userId": 1 }
```
- Status code: `200 OK`
- Response: the same JSON that was sent, confirming the replacement.

## Task 09 — DELETE

- Method: `DELETE`
- Endpoint: `/posts/1`
- Status code: `200 OK`
- Response body: `{}`

DELETE is intended to remove the resource identified by the URL (here, post 1) from the server.
On a real service, later GETs on `/posts/1` should return 404. JSONPlaceholder reports success
but does not really delete anything, so the removal is simulated.

## Task 10 — HTTP Status Codes

| Status | Meaning                              | Your test     |
|--------|--------------------------------------|---------------|
| 200    | OK: request succeeded, body returned | GET /posts/1  |
| 201    | Created: a new resource was created  | POST /posts   |
| 404    | Not Found: no resource at this URL   | GET /posts/999 |

**Difference:** a successful request (2xx) means the server found or completed the operation, and
the response body contains the result. A 404 means the request was valid but the requested
resource does not exist, so there is nothing to return. Both are valid HTTP responses; only the
2xx code means the operation succeeded.
