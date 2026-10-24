# Task 16 — Public vs Protected API

## Comparison Table

| Feature | Public API | Protected API |
|---|---|---|
| Credentials Required | May not require credentials | Usually requires an API key, token, or other authentication |
| Purpose of Authentication | Authentication may not be necessary for basic access | To verify the identity or permissions of the requester |
| Example | JSONPlaceholder API | An API that requires an API key or access token |
| Authentication Mechanism | No authentication, or optional API key | API key, Bearer token, or OAuth token |
| Invalid Credentials | Not applicable if authentication is not required; access may still be restricted by other rules | The server may return HTTP 401 Unauthorized or HTTP 403 Forbidden |

## Explanation

A public API allows users to access its available resources without necessarily providing credentials. A protected API requires authentication or authorization before allowing access to certain resources.

Authentication helps a service verify who is making a request, while authorization determines what that requester is allowed to access. API keys and Bearer tokens are examples of credentials that can be sent with API requests.

If credentials are missing or invalid, a protected API may reject the request. The exact response depends on the API's security rules.