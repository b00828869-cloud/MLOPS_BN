from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Apartment(BaseModel):
    surface: float
    rooms: int

def mock_model(surface: float, rooms: int) -> float:
    return 50000 + surface * 4000 + rooms * 20000


@app.get("/")
def root():
    return {"message": "Apartment price API is running"}


@app.post("/predict")
def predict(apartment: Apartment):
    price = mock_model(apartment.surface, apartment.rooms)
    return {
        "estimated_price": price,
        "currency": "EUR"
    }
