"""Phase 04 — Authentication, API keys & secure configuration (Tasks 16–18).

The API key is read from the environment (loaded from a local .env file).
It is never written in this source file.
"""
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()  # reads .env in the current folder, if present

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")


def mask(secret):
    """Show only the first 4 characters so logs never reveal the full key."""
    if not secret:
        return "<not set>"
    return secret[:4] + "*" * max(len(secret) - 4, 0)


def build_auth_headers(token):
    """Task 17: build the header in the pattern  Authorization: Bearer TOKEN."""
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }


def show_request_config(headers):
    """Print a sanitized view of the request configuration (token masked)."""
    safe = dict(headers)
    safe["Authorization"] = "Bearer " + mask(API_KEY)
    print("Request configuration (sanitized):")
    print("  URL:    ", BASE_URL)
    for name, value in safe.items():
        print(f"  {name}: {value}")
    print()


def get_with_auth(path):
    if not API_KEY:
        print("ERROR: API_KEY is not set. Create a .env file (see .env.example).")
        sys.exit(1)
    headers = build_auth_headers(API_KEY)
    show_request_config(headers)
    response = requests.get(f"{BASE_URL}{path}", headers=headers, timeout=10)
    print(f"GET {path} -> status {response.status_code}")
    return response


if __name__ == "__main__":
    # JSONPlaceholder ignores the header; the mock server's /secure route checks it.
    r = get_with_auth("/posts/1")
    print("Body:", r.text[:120], "...\n")
    if os.getenv("API_BASE_URL", "").startswith("http://127.0.0.1"):
        r2 = get_with_auth("/secure/posts/1")
        print("Protected route body:", r2.text[:120])
