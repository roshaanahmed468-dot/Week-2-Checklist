
import requests

base_url = "https://jsonplaceholder.typicode.com/posts"

# Retrieve posts 1, 2, and 3 using a loop
for post_id in range(1, 4):
    url = base_url + "/" + str(post_id)

    try:
        response = requests.get(url, timeout=10)

        print("Status:", response.status_code)

        if response.status_code == 200:
            post = response.json()
            print("Post", post_id, ":", post["title"])
        else:
            print("Could not retrieve post", post_id)

    except requests.exceptions.RequestException as error:
        print("Request error for post", post_id, ":", error)

    print("------------------------------")
