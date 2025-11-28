from fastapi import FastAPI
from routers import vehicle, incidents

app = FastAPI(
    title="Smart City API – Enugu",
    version="1.0.0",
)

app.include_router(vehicle.router)
app.include_router(incidents.router)

@app.get("/")
def home():
    return {"message": "Smart City API running successfully"}
