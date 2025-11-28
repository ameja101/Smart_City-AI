from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import VehiclePing
from schemas import PingCreate

router = APIRouter(prefix="/vehicle", tags=["Vehicle"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/ping")
def add_ping(data: PingCreate, db: Session = Depends(get_db)):
    ping = VehiclePing(**data.dict())
    db.add(ping)
    db.commit()
    return {"status": "ok"}

@router.get("/latest")
def get_latest(db: Session = Depends(get_db)):
    rows = db.query(VehiclePing).order_by(VehiclePing.id.desc()).limit(50).all()
    return rows
