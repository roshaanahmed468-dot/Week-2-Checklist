
import requests

url = "https://jsonplaceholder.typicode.com/posts/9999"

try:
    response = requests.get(url, timeout=10)
    print("Status Code:", response.status_code)

    if response.status_code == 404:
        print("Request failed.")
        print("Resource not found.")
    elif response.status_code == 200:
        print("Request successful.")
    else:
        print("Unexpected status code:", response.status_code)

except requests.exceptions.RequestException as error:
    print("API request error:", error)
