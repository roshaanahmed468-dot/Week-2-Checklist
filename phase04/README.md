# Phase 04 — Authentication, API Keys & Secure Configuration

## Task 16 — Public vs Protected API

| Aspect                 | Public API                                   | Protected API                                       |
|------------------------|----------------------------------------------|-----------------------------------------------------|
| Credentials required?  | No. Anyone can send a request.               | Yes. A key or token must be sent with each request. |
| Why authentication?    | Not needed; data is open.                    | Identifies the caller, limits who can read or change data, and enables usage tracking and billing. |
| Example mechanism      | None (JSONPlaceholder `/posts`)              | `Authorization: Bearer <token>` header, or an `X-API-Key` header. |
| Invalid credentials    | Not applicable; requests succeed.            | The server returns **401 Unauthorized** (missing or invalid credentials) or **403 Forbidden** (valid credentials, not allowed). The request is rejected and no data is returned. |

## Task 17 — Authorization Header

`build_auth_headers(token)` in `api_client.py` builds:

```
Authorization: Bearer <TOKEN>
Accept: application/json
```

The token is never printed in full. `show_request_config()` masks it and prints the sanitized
configuration. Captured output is in `evidence/logs/phase04_output.txt`. The test token used during
testing was a dummy value, not a real credential.

## Task 18 — Move Credentials to `.env`

1. `.env.example` is committed with a placeholder: `API_KEY=your_key_here`.
2. The real `.env` (created locally, not committed) holds the key.
3. `load_dotenv()` loads it, and `os.getenv("API_KEY")` reads it. The key is never written in the Python source.
4. `.gitignore` contains `.env`. `evidence/logs/task18_gitignore_check.txt` shows
   `git check-ignore` matching `.env`, and `git status` does not list it.

**Never submit your real key.** Only `.env.example` belongs in the repository.
