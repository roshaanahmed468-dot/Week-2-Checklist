
# Task 24 — Define an API Tool

## Tool Name
get_post

## Description
Retrieves a specific post from the JSONPlaceholder API using its post ID.

## HTTP Method
GET

## Endpoint
https://jsonplaceholder.typicode.com/posts/{post_id}

## Required Inputs
- post_id: The ID of the post to retrieve.

## Optional Inputs
- None

## Expected Output
- id: The post ID.
- title: The post title.
- body: The post content.
- userId: The ID of the user who created the post.

## Possible Errors
- 404: The requested post was not found.
- 429: Too many requests were sent.
- 500: An internal server error occurred.
- Timeout: The API did not respond within the allowed time.
- Network failure: The client could not connect to the API.

## Authentication Required
No. JSONPlaceholder allows this public endpoint to be accessed without an API key or authentication token.
