
# Task 10 — Investigate HTTP Status Codes

## Status Code Table

| Status Code | Meaning | Test |
|---|---|---|
| 200 | OK — request successful | GET /posts/1 |
| 201 | Created — resource creation confirmed | POST /posts |
| 404 | Not Found — resource not found | GET /posts/9999 |

## Explanation

A successful HTTP response indicates that the request was processed successfully according to the returned status code.

Status code 200 indicates a successful request. Status code 201 indicates that a resource was created. Status code 404 indicates that the requested resource could not be found.

Therefore, a successful response and a resource-not-found response have different meanings.
