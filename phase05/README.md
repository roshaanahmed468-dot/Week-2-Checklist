# Phase 05 — Errors, Timeouts & Rate Limits

## Task 21 — Why a timeout is necessary

Without a timeout, `requests.get()` waits indefinitely if the server never responds (for example,
a stalled connection or an overloaded server). The program would hang and could never recover. A
timeout sets a limit, so the client gives up after the set number of seconds and handles the failure.
`api_client.py` uses `timeout=TIMEOUT_SECONDS` (default 10 seconds, set with `API_TIMEOUT`).

The test in `phase05/api_client.py` calls `/slow/3` with a 1-second limit. The output is
`Timeout: no response within 1 seconds.` instead of a hang.

## Task 22 — Failure categories

| Case                  | How it is detected                              | Output                                  |
|-----------------------|-------------------------------------------------|-----------------------------------------|
| Successful request    | status 2xx                                      | `Success. Status Code: 200`             |
| API error             | status 4xx/5xx                                  | `Request failed.`, status code, meaning |
| Timeout               | `requests.exceptions.Timeout`                   | `Timeout: no response within …`         |
| Network/request fail  | `ConnectionError` or other `RequestException`   | `Network failure: could not connect…`   |

## Task 23 — Rate Limiting

1. **What is a rate limit?** A cap on how many requests a client may send in a time window (e.g. 100 per minute).
2. **Why do APIs impose them?** To protect server capacity, keep service fair for all users, prevent abuse and
   brute-force attempts, and control cost.
3. **What does HTTP 429 mean?** "Too Many Requests": the client has exceeded the limit. The
   response often includes a `Retry-After` header saying when to try again.
4. **Why can an automated program generate too many requests?** A loop, a retry bug, or a
   process running in parallel can fire hundreds of requests in seconds, far faster than a person clicking.
   Without a delay or a limit in the code, it hits the cap quickly.
5. **Why does this matter for agentic systems?** An AI agent may call tools repeatedly while it plans,
   retries, or explores. Each tool call can be an API request. Without rate handling, one agent
   can exhaust a quota, get blocked, or cause repeated failures. Agents need to back off on 429,
   respect `Retry-After`, and limit how many calls they make.

The final project implements this: `_request()` retries 429 responses up to three times with
exponential backoff (1 s, 2 s, 4 s).

## Status-code tests

Captured in `evidence/logs/phase05_output.txt`: 404, 400, 401, 429, 500, timeout, network failure,
and success.
