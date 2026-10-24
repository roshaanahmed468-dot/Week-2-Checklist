"""Phase 05 — Errors, timeouts & rate limits (Tasks 19–23)."""
import os

import requests
from requests.exceptions import ConnectionError as ReqConnectionError
from requests.exceptions import RequestException, Timeout

BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
TIMEOUT_SECONDS = float(os.getenv("API_TIMEOUT", "10"))

STATUS_MESSAGES = {
    400: "Bad request: the data sent is invalid. Check the request body.",
    401: "Unauthorized: credentials are missing or invalid.",
    403: "Forbidden: the credentials are valid but not allowed to do this.",
    404: "Resource not found.",
    429: "Rate limit exceeded: too many requests. Wait before retrying.",
    500: "Server error: the API failed. Try again later.",
}


def handle_response(response):
    """Task 20: give each status code category its own message."""
    code = response.status_code
    if 200 <= code < 300:
        print(f"Success. Status Code: {code}")
        return response.json() if response.content else {}
    message = STATUS_MESSAGES.get(code, "Unexpected HTTP error.")
    print("Request failed.")
    print(f"Status Code: {code}")
    print(message)
    return None


def safe_get(path, base_url=None):
    """Tasks 19, 21, 22: handle success, API error, timeout and network failure."""
    url = f"{base_url or BASE_URL}{path}"
    try:
        response = requests.get(url, timeout=TIMEOUT_SECONDS)   # Task 21: timeout
    except Timeout:
        print(f"Timeout: no response within {TIMEOUT_SECONDS:g} seconds.")
        return None
    except ReqConnectionError:
        print("Network failure: could not connect to the server.")
        return None
    except RequestException as exc:
        print(f"Request failed: {exc}")
        return None
    return handle_response(response)


def demo():
    print("=== Task 19: 404 (resource does not exist) ===")
    safe_get("/posts/999")
    print("\n=== Task 20: other HTTP status categories ===")
    for code in (400, 401, 429, 500):
        print(f"-- {code}")
        safe_get(f"/status/{code}")
    print("\n=== Task 21: timeout (server takes 3s, limit is 1s) ===")
    global TIMEOUT_SECONDS
    old_timeout = TIMEOUT_SECONDS
    TIMEOUT_SECONDS = 1
    safe_get("/slow/3")
    TIMEOUT_SECONDS = old_timeout
    print("\n=== Task 22: network failure (unreachable host) ===")
    safe_get("/posts/1", base_url="http://nonexistent.invalid")
    print("\n=== Success for comparison ===")
    post = safe_get("/posts/1")
    if post:
        print("Title:", post["title"])


if __name__ == "__main__":
    demo()
