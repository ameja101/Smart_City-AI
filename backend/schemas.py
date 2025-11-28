from pydantic import BaseModel
from datetime import datetime

class IncidentCreate(BaseModel):
    title: str
    description: str
    lat: float
    lon: float

class IncidentResponse(BaseModel):
    id: int
    title: str
    description: str
    lat: float
    lon: float
    timestamp: datetime

    class Config:
        orm_mode = True

from pydantic import BaseModel
from datetime import datetime

class PingCreate(BaseModel):
    vehicle_id: str
    lat: float
    lon: float

class PingResponse(BaseModel):
    id: int
    vehicle_id: str
    lat: float
    lon: float
    timestamp: datetime   # <-- must match your DB column name

    class Config:
        orm_mode = True
