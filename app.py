from fastapi import FastAPI
from schemas import Apartment
from model import mock_model

app = FastAPI()

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

