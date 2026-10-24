
import requests

base_url = "https://jsonplaceholder.typicode.com"

# Test 1: HTTP 200
print("TEST 1: GET existing post")
try:
    response = requests.get(
        base_url + "/posts/1",
        timeout=10
    )
    print("Method: GET")
    print("Status Code:", response.status_code)
    print("Meaning: Successful request")
except requests.exceptions.RequestException as error:
    print("Request failed:", error)

print("-" * 50)

# Test 2: HTTP 201
print("TEST 2: POST a new post")
data = {
    "title": "My API Lab",
    "body": "Testing status code 201",
    "userId": 1
}

try:
    response = requests.post(
        base_url + "/posts",
        json=data,
        timeout=10
    )
    print("Method: POST")
    print("Status Code:", response.status_code)
    print("Meaning: Resource created")
    print("Response:", response.json())
except requests.exceptions.RequestException as error:
    print("Request failed:", error)

print("-" * 50)

# Test 3: HTTP 404
print("TEST 3: GET a non-existing post")
try:
    response = requests.get(
        base_url + "/posts/9999",
        timeout=10
    )
    print("Method: GET")
    print("Status Code:", response.status_code)

    if response.status_code == 404:
        print("Meaning: Resource not found")
    else:
        print("Unexpected result; check the returned status.")

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
