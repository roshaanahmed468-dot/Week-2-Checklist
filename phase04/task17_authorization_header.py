
import requests

# Demo token only — not a real credential
token = "TOKEN"

# Construct the Authorization header
headers = {
    "Authorization": "Bearer " + token
}

# Display the sanitized request configuration
print("Authorization Header:", headers["Authorization"])

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    print("Request Method: GET")
    print("Endpoint:", url)
    print("Status Code:", response.status_code)

except requests.exceptions.RequestException as error:
    print("Request error:", error)
