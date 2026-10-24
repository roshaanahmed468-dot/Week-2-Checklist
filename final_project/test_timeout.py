
import requests
from unittest.mock import patch


def test_timeout():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    with patch(
        "requests.get",
        side_effect=requests.exceptions.Timeout
    ):
        try:
            response = requests.get(url, timeout=10)
            print("Status Code:", response.status_code)

        except requests.exceptions.Timeout:
            print("Timeout Error: The API took too long to respond.")


test_timeout()
