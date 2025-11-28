from fastapi import FastAPI
from routers.vehicle import router as vehicle_router
from routers.incidents import router as incident_router

app = FastAPI(title="Smart City Backend")

app.include_router(vehicle_router)
app.include_router(incident_router)
