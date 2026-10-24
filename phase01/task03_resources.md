
# Task 03 — Identify API Resources

## API Resource Comparison

| Endpoint | Resource | Specific Resource? |
|---|---|---|
| /posts | Collection of posts | No |
| /posts/1 | Individual post | Yes |
| /posts/2 | Individual post | Yes |

## Explanation

The `/posts` endpoint returns a collection of posts.
The `/posts/1` endpoint returns the specific post with ID 1.
The `/posts/2` endpoint returns the specific post with ID 2.

The `/posts` endpoint identifies the collection, while the endpoints containing an ID identify individual resources.
