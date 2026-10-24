
import requests

url = "https://jsonplaceholder.typicode.com/posts"

# Data to send to the API
data = {
    "title": "My API Lab",
    "body": "Testing POST request",
    "userId": 1
}

print("HTTP Method: POST")
print("Endpoint:", url)
print("Request Body:", data)

try:
    response = requests.post(url, json=data, timeout=10)

    print("Status Code:", response.status_code)
    print("Response Body:")

    try:
        print(response.json())
    except ValueError:
        print(response.text)

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
