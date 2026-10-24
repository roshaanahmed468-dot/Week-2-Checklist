
def handle_status_code(status_code):
    if 200 <= status_code < 300:
        print("Success: Request completed successfully.")

    elif status_code == 400:
        print("Bad Request: The request is invalid.")

    elif status_code == 401:
        print("Unauthorized: Authentication is required or invalid.")

    elif status_code == 404:
        print("Not Found: The requested resource does not exist.")

    elif status_code == 429:
        print("Too Many Requests: Rate limit exceeded.")

    elif status_code == 500:
        print("Internal Server Error: The server encountered a problem.")

    else:
        print("Unexpected status code:", status_code)


# Test the different HTTP status codes
status_codes = [200, 400, 401, 404, 429, 500]

for code in status_codes:
    print("\nStatus Code:", code)
    handle_status_code(code)
