# Phase 06 — Tool Specification: `get_post`

## Task 24 — Define an API Tool

- **Tool Name:** `get_post`
- **Description:** Retrieves a single post from the JSONPlaceholder API using its numeric ID.
- **HTTP Method:** `GET`
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts/{post_id}`
- **Required Inputs:** `post_id` (integer, 1 or greater)
- **Optional Inputs:** none (the client sets a 10-second timeout)
- **Expected Output:** JSON object with `id`, `userId`, `title`, `body`
- **Possible Errors:** 404 (post does not exist), 429 (rate limit), 500 (server error), timeout, network failure
- **Authentication Required:** No (public API)

## Task 25 — Agent Tool Interface

```
Tool: get_post
Purpose:
  Retrieve a post using its ID.
Input:
  post_id: integer (required, >= 1)
Output:
  id: integer
  userId: integer
  title: string
  body: string
Possible Errors:
  404      -> "Post not found"; the agent should ask for a different ID.
  429      -> "Rate limited"; the agent should wait and retry later.
  500      -> "Server error"; the agent may retry once.
  Timeout  -> "Request timed out"; the agent may retry.
```

**Design note:** an agent does not call HTTP directly. It sees only the tool name, description
and input schema, and decides when to call it. Clear descriptions, typed inputs and short,
readable error messages let the agent recover from failures instead of guessing.
This phase only defines the tool; no AI agent is built here.
