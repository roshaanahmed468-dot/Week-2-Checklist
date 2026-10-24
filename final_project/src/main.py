"""Final project demo: connects to JSONPlaceholder, processes JSON, handles errors.

Run from the final_project folder:  python src/main.py
"""
from api_client import create_post, delete_post, get_post, list_posts, update_post


def show(label, ok, result):
    if ok:
        print(f"[OK]    {label}")
    else:
        print(f"[ERROR] {label}: {result}")
    return ok


def main():
    print("=== 1. GET a single post ===")
    ok, post = get_post(1)
    if show("GET /posts/1", ok, post):
        print(f"  id={post['id']}  userId={post['userId']}")
        print(f"  title: {post['title']}")

    print("\n=== 2. GET a collection and process it ===")
    ok, posts = list_posts()
    if show("GET /posts", ok, posts):
        print(f"  Number of posts: {len(posts)}")
        print("  First five titles:")
        for p in posts[:5]:
            print(f"   - {p['title']}")

    print("\n=== 3. Resource not found (404) ===")
    show("GET /posts/9999", *get_post(9999))

    print("\n=== 4. POST (create) ===")
    ok, created = create_post("My API Lab", "Testing POST request", 1)
    if show("POST /posts", ok, created):
        print(f"  Created id={created['id']}")

    print("\n=== 5. PUT (update) ===")
    show("PUT /posts/1", *update_post(1, "Updated title", "Updated body", 1))

    print("\n=== 6. DELETE ===")
    show("DELETE /posts/1", *delete_post(1))


if __name__ == "__main__":
    main()
