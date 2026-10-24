# Phase 01 — API & Client-Server Fundamentals

## Task 01 — Explore an API Using a Browser

Endpoint: `https://jsonplaceholder.typicode.com/posts/1`

| Field  | Value (post /1)                                                                 |
|--------|----------------------------------------------------------------------------------|
| userId | 1                                                                                |
| id     | 1                                                                                |
| title  | sunt aut facere repellat provident occaecati excepturi optio reprehenderit       |
| body   | quia et suscipit / suscipit recusandae consequuntur expedita et cum / reprehenderit molestiae ut ut quas totam / nostrum rerum est autem sunt rem eveniet architecto |

The response is a JSON object with four fields: `userId`, `id`, `title`, `body`.

**Why the response changes between /1, /2 and /3:** the path segment after `/posts/` is a
resource identifier. Each URL points to a different post in the same `posts` collection, so the
server looks up a different record and returns that record's values. `id` matches the number in
the URL, and `title`/`body` differ because they are different posts. `userId` may stay the same
(posts 1–3 all belong to user 1) because several posts can share one author.

## Task 02 — Identify the Client, API and Server

```
 ┌─────────┐   GET /posts/1    ┌─────────┐   looks up record   ┌──────────┐
 │ Browser │ ────────────────► │   API   │ ──────────────────► │  Server  │
 │(Client) │                   │(endpoint│                     │ (database│
 │         │ ◄──────────────── │ /posts/1)│ ◄────────────────── │ + logic) │
 └─────────┘  200 OK + JSON    └─────────┘   post record        └──────────┘
   Browser → API → Server → Response
```

- **Client:** the browser, which sends the request.
- **API:** the interface (URL + rules) that exposes the `posts` resource.
- **Server:** the machine that stores the data and produces the response.

When the browser requests `/posts/1`, it sends an HTTP GET request to the JSONPlaceholder host.
The API routes the request to the post with `id` 1. The server finds that record and returns it as
JSON with status `200 OK`. The browser then displays the JSON text.

## Task 03 — Identify API Resources

| Endpoint     | Resource | Specific Resource? |
|--------------|----------|--------------------|
| /posts       | posts    | No (the collection of all posts) |
| /posts/1     | posts    | Yes (post with id 1) |
| /posts/2     | posts    | Yes (post with id 2) |

## Evidence
- `evidence/task01_posts_1.png`, `task01_posts_2.png`, `task01_posts_3.png`: see the note in `evidence/README.md`.
