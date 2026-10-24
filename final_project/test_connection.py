
import requests
from unittest.mock import patch


def test_connection_error():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    with patch(
        "requests.get",
        side_effect=requests.exceptions.ConnectionError
    ):
        try:
            response = requests.get(url, timeout=10)
            print("Status Code:", response.status_code)

        except requests.exceptions.ConnectionError:
            print("Network Error: Could not connect to the API.")


test_connection_error()
