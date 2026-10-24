
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

print("HTTP Method: DELETE")
print("Endpoint:", url)

try:
    response = requests.delete(url, timeout=10)

    print("Status Code:", response.status_code)
    print("Response:")

    if response.status_code == 200:
        print("Post deleted successfully.")
        print("Response Body:", response.text)
    elif response.status_code == 204:
        print("Post deleted successfully. No response body.")
    else:
        print("Request was not successful.")

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
