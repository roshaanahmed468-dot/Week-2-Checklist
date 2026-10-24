
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=10)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("Request successful.")
        print("Post Title:", response.json()["title"])
    else:
        print("Request failed.")
        print("Response:", response.status_code)

except requests.exceptions.Timeout:
    print("Error: Request timed out.")
