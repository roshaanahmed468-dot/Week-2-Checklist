
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read API key from environment
api_key = os.getenv("API_KEY")

if api_key:
    print("API_KEY loaded successfully.")
    print("API_KEY is configured:", True)
else:
    print("API_KEY was not found.")
