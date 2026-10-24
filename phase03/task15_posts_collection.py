
import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    # Send GET request to retrieve all posts
    response = requests.get(url, timeout=10)

    print("Status:", response.status_code)

    if response.status_code == 200:
        # Convert JSON response into a Python list
        posts = response.json()

        # Count the total posts
        print("Total Posts:", len(posts))

        # Display the first five post titles
        print("\nFirst Five Post Titles:")

        for post in posts[:5]:
            print(post["title"])

    else:
        print("Failed to retrieve posts.")

except requests.exceptions.RequestException as error:
    print("API request error:", error)
