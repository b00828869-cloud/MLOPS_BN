from fastapi import FastAPI
from schemas import ApartmentIn, PredictionOut
from model import predict_price, MODEL_VERSION

app = FastAPI(title="Apartment Valuation API")

@app.get("/")
def root():
    return {"status": "running", "model_version": MODEL_VERSION}

@app.post("/predict", response_model=PredictionOut)
def predict(apartment: ApartmentIn):
    price = predict_price(apartment)
    return PredictionOut(
        estimated_price=price,
        model_version=MODEL_VERSION
    )
