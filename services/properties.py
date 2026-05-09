from token import STRING

import requests
import os
import requests
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv("API_CLIENT_ID")
CLIENT_SECRET = os.getenv("API_CLIENT_SECRET")
AUTH_URL = os.getenv("AUTH_URL")
API_URL = os.getenv("API_URL")

def get_properties():
    response = requests.get(API_URL)

    return response.json()


def getToken():
    auth_payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    auth_response = requests.post(
        AUTH_URL,
        json=auth_payload
    )

    auth_response.raise_for_status()
    token = auth_response.json()["access_token"]
    print("Token generated : " + token)

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}