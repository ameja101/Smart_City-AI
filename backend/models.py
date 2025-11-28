from sqlalchemy import Column, Integer, String, Float
from database import Base

class VehiclePing(Base):
    __tablename__ = "vehicle_pings"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    timestamp = Column(String)

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    location = Column(String)
    status = Column(String)
    timestamp = Column(String)

from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from database import Base

class VehiclePing(Base):
    __tablename__ = "vehicle_pings"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String, index=True)
    lat = Column(Float)
    lon = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
