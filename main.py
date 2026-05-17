from contextlib import asynccontextmanager

from fastapi import FastAPI
from services.properties import get_properties, add_property

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting app...")
    result = add_property()
    print("Property created:")
    print(result)
    yield
    print("Shutting down...")
app = FastAPI(lifespan=lifespan)

def home():
    return {"message": "FastAPI running!"}


@app.get("/properties")
def properties():
    return get_properties()

@app.post("/properties")
def create_property():
    return add_property()