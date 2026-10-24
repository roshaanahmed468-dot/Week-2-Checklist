
import requests

# API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    # Send GET request
    response = requests.get(url, timeout=10)

    # Check status code
    print("Status:", response.status_code)

    if response.status_code == 200:
        # Convert JSON response into Python dictionary
        post = response.json()

        # Print selected fields
        print("Post ID:", post["id"])
        print("Title:", post["title"])
        print("Body:", post["body"])
    else:
        print("Request failed.")

except requests.exceptions.RequestException as error:
    print("API request error:", error)
