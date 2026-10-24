
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def get_post(post_id):
    """Retrieve and display a post using its ID."""

    url = f"{BASE_URL}/{post_id}"

    try:
        response = requests.get(url, timeout=10)

        print("\nHTTP Status Code:", response.status_code)

        if response.status_code == 200:
            post = response.json()

            print("\n--- Post Details ---")
            print("Post ID:", post["id"])
            print("User ID:", post["userId"])
            print("Title:", post["title"])
            print("Body:", post["body"])

        elif response.status_code == 401:
            print("Authentication Error: Access is unauthorized.")

        elif response.status_code == 404:
            print("Not Found: The requested post does not exist.")

        elif response.status_code == 429:
            print("Rate Limit Error: Too many requests.")
            print("Wait before sending another request.")

        elif response.status_code >= 500:
            print("Server Error: The API server encountered a problem.")

        else:
            print("API Error:", response.status_code)
            print(response.text)

    except requests.exceptions.Timeout:
        print("Timeout Error: The API took too long to respond.")

    except requests.exceptions.ConnectionError:
        print("Network Error: Could not connect to the API.")

    except requests.exceptions.RequestException as error:
        print("Request Error:", error)


def main():
    print("=== Complete API Client ===")
    print("API:", BASE_URL)

    try:
        post_id = int(input("Enter post ID: "))

        if post_id < 1:
            print("Please enter a post ID between 1 and 100.")
            return

        get_post(post_id)

    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
