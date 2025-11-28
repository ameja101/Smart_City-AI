from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Incident
from schemas import IncidentCreate

router = APIRouter(prefix="/incidents", tags=["Incidents"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def report_incident(data: IncidentCreate, db: Session = Depends(get_db)):
    incident = Incident(**data.dict())
    db.add(incident)
    db.commit()
    return {"status": "incident logged"}

@router.get("/")
def list_incidents(db: Session = Depends(get_db)):
    return db.query(Incident).order_by(Incident.id.desc()).all()
