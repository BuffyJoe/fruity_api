from pydantic import BaseModel
import datetime as _dt
from typing import List

class _fruit(BaseModel):
    name = str
    

class Siting(BaseModel):
    id = int
    fruit_id = int
    condition: str
    latitude : float
    longitude: float
    class Config:
        orm_mode = True

class create_siting(BaseModel):
    condition: str
    latitude : float
    longitude: float

class create_fruit(BaseModel):
    name: str

class Fruit(BaseModel):
    name: str
    id : int
    siting : List[Siting] = []

    class Config:
        orm_mode = True


    