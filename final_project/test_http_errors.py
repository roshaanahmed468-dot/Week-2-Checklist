
from unittest.mock import Mock, patch
from src.api_client import get_post


def test_http_error(status_code):
    fake_response = Mock()
    fake_response.status_code = status_code
    fake_response.text = "Simulated API error"

    with patch(
        "src.api_client.requests.get",
        return_value=fake_response
    ):
        print(f"\n--- Testing HTTP {status_code} ---")
        get_post(1)


for code in [401, 429, 500]:
    test_http_error(code)
