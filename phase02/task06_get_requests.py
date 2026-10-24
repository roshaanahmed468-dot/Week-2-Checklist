
import requests

# API endpoints to test
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]

# Send GET requests
for url in urls:
    print("=" * 60)
    print("Endpoint:", url)
    print("HTTP Method: GET")

    try:
        response = requests.get(url, timeout=10)

        print("Status Code:", response.status_code)
        print("Response Body:")

        try:
            print(response.json())
        except ValueError:
            print(response.text)

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)

print("=" * 60)
print("GET request testing completed.")
