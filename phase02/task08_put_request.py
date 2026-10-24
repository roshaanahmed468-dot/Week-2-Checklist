
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

# Updated post data
data = {
    "id": 1,
    "title": "Updated API Lab",
    "body": "Testing PUT request to update a post",
    "userId": 1
}

print("HTTP Method: PUT")
print("Endpoint:", url)
print("Request Body:", data)

try:
    response = requests.put(url, json=data, timeout=10)

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
