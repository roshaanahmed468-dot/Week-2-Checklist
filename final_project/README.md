
# Complete API Client

## Project Overview
This project demonstrates API communication, JSON processing, HTTP status-code handling, timeout handling, and network-error handling using Python.

## API Details
- API: JSONPlaceholder
- Endpoint: https://jsonplaceholder.typicode.com/posts/{post_id}
- HTTP Method: GET
- Authentication: Not required
- Response Format: JSON

## Requirements
- Python 3
- Requests library

## Installation
Run this command from the API-Lab folder:

    python -m pip install -r final_project/requirements.txt

## How to Run
Run this command from the API-Lab folder:

    python final_project/src/api_client.py

Enter a positive post ID when prompted.

## JSON Processing
The application extracts and displays:
- Post ID
- User ID
- Title
- Body

## Error Handling
The application handles:
- HTTP 404: Resource not found
- HTTP 401: Unauthorized access
- HTTP 429: Too many requests
- HTTP 5xx: Server errors
- Request timeout
- Connection errors
- Other request errors
- Invalid user input

## Authentication and Security
JSONPlaceholder does not require authentication for this public endpoint. No API key is needed.

If an API requiring authentication is used in the future, credentials should be stored in environment variables rather than hardcoded.

## Rate Limiting
The application detects HTTP 429 and advises the user to wait. It does not automatically retry requests.

## Testing
1. Post ID 2: HTTP 200; post details displayed.
2. Post ID 9999: HTTP 404; resource-not-found message displayed.
