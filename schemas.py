from pydantic import BaseModel, Field

class ApartmentIn(BaseModel):
    surface: float = Field(..., gt=0)
    rooms: int = Field(..., ge=0)

class PredictionOut(BaseModel):
    estimated_price: float
    currency: str = "EUR"
    model_version: str
