from fastapi import FastAPI
from services.properties import get_properties

app = FastAPI()


@app.get("/")
def home():
    return {"message": "FastAPI running!"}


@app.get("/propiedades")
def properties():
    return get_properties()