import json
import os
import requests
from dotenv import load_dotenv
from token import STRING

load_dotenv()

CLIENT_ID = os.getenv("API_CLIENT_ID")
CLIENT_SECRET = os.getenv("API_CLIENT_SECRET")
AUTH_URL = os.getenv("AUTH_URL")
print("AUTH_URL:", AUTH_URL)
API_URL = os.getenv("API_URL")

def get_properties():
    response = requests.get(API_URL)
    return response.json()


def get_token():
    payload = {
        "username": CLIENT_ID,
        "password": CLIENT_SECRET
    }
    print("\n===== AUTH PAYLOAD =====")
    print(payload)
    response = requests.post(
        AUTH_URL,
        json=payload
    )
    print("\n===== AUTH STATUS =====")
    print(response.status_code)
    print("\n===== AUTH RESPONSE =====")
    print(response.text)
    response.raise_for_status()
    data = response.json()
    return data["token"]


def add_property():
    # Leer JSON
    with open("data/property_test.json", "r", encoding="utf-8") as file:
        property_data = json.load(file)

    # Show payload
    print("\n===== PAYLOAD =====")
    print(json.dumps(property_data, indent=2, ensure_ascii=False))

    # Get Token
    token = get_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    # POST request
    response = requests.post(
        API_URL,
        json=property_data,
        headers=headers
    )

    print("\n===== STATUS =====")
    print(response.status_code)
    print("\n===== RESPONSE =====")
    print(response.text)
    response.raise_for_status()

    return response.json()
