
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=10)

    # Check whether the API returned an HTTP error
    response.raise_for_status()

    print("Request successful.")
    print("Status Code:", response.status_code)
    print("Post Title:", response.json()["title"])

except requests.exceptions.Timeout:
    print("Timeout Error: The server took too long to respond.")

except requests.exceptions.HTTPError as error:
    print("API Error:", error)

except requests.exceptions.ConnectionError:
    print("Network Error: Could not connect to the server.")

except requests.exceptions.RequestException as error:
    print("Request Failure:", error)
