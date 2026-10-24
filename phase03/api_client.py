"""Phase 03 — JSON & Python API integration (Tasks 11–15).

Set API_BASE_URL to point at another server (used for offline testing); defaults to JSONPlaceholder.
"""
import os
import requests

BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")


# ---- Task 11: a JSON object as a Python dictionary ----
def task11_student_dict():
    student = {"name": "Ali", "marks": 85, "program": "BSCS"}
    print("Task 11 — Student record")
    print("Name:   ", student["name"])
    print("Marks:  ", student["marks"])
    print("Program:", student["program"])
    print()


# ---- Task 12: a JSON array as a list of dictionaries ----
def task12_student_list():
    students = [
        {"id": 1, "name": "Ali"},
        {"id": 2, "name": "Sara"},
        {"id": 3, "name": "Umar"},
    ]
    print("Task 12 — Loop through students")
    for student in students:
        print(f"ID: {student['id']}  Name: {student['name']}")
    print()


# ---- Tasks 13 & 14: GET a single post and loop over several ----
def get_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.get(url)
    print(f"Status: {response.status_code}")
    if response.status_code != 200:
        return None
    return response.json()


def task13_single_post():
    print("Task 13 — First API client")
    post = get_post(1)
    if post:
        print("Post ID:", post["id"])
        print("Title:  ", post["title"])
        print("Body:   ", post["body"])
    print()


def task14_multiple_posts():
    print("Task 14 — Multiple posts")
    for post_id in (1, 2, 3):
        post = get_post(post_id)
        if post:
            print(f"Post {post_id}: {post['title']}")
    print()


# ---- Task 15: retrieve and process a collection ----
def task15_collection():
    print("Task 15 — Collection")
    response = requests.get(f"{BASE_URL}/posts")
    response.raise_for_status()
    posts = response.json()
    print("Number of posts:", len(posts))
    print("First five titles:")
    for post in posts[:5]:
        print("-", post["title"])
    print()


if __name__ == "__main__":
    task11_student_dict()
    task12_student_list()
    task13_single_post()
    task14_multiple_posts()
    task15_collection()
