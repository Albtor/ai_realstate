from fastapi import FastAPI
from services.properties import get_properties, add_property

app = FastAPI()
@app.get("/")
def home():
    return {"message": "FastAPI running!"}


@app.get("/properties")
def properties():
    return get_properties()

@app.post("/properties")
def create_property():
    return add_property()