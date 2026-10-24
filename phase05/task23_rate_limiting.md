
# Task 23 — Investigate Rate Limiting

## 1. What is a rate limit?

A rate limit is a restriction on how many API requests a client can make during a specific period of time.

## 2. Why do APIs impose rate limits?

APIs use rate limits to prevent excessive requests, protect server resources, maintain performance, and provide fair access to users.

## 3. What does HTTP 429 mean?

HTTP status code 429 means "Too Many Requests." It indicates that a client has sent too many requests within a given period.

## 4. Why can an automated program generate too many requests?

An automated program may send too many requests because of loops, frequent polling, repeated retries, or incorrectly configured automation.

## 5. Why is rate limiting especially important for agentic systems?

Agentic systems can perform repeated API calls automatically while completing multi-step tasks. Without proper limits, an agent may send excessive requests, waste resources, trigger API restrictions, or overload a service.
