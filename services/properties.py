import requests

API_URL = "https://mi-api-realstate.onrender.com"
# API_URL_LOCAL = "https://localhost:3000"


def get_properties():
    response = requests.get(API_URL)

    return response.json()