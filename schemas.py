from pydantic import BaseModel

class Apartment(BaseModel):
    surface: float
    rooms: int
