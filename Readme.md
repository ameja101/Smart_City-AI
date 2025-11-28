# Enugu AI Smart City Infrastructure


This project implements:
- Real‑time **incident detection** using YOLOv8
- **Bus arrival prediction (ETA)** using GPS pings
- **Streamlit Dashboard** for city operators
- **Mobile App (Expo/React Native)** for the public
- **Edge deployment** on Raspberry Pi / Jetson for low‑latency infeigirence


---
## Features
- Detect congestion, stopped vehicles, collisions.
- Predict time‑to‑arrival (ETA) for buses.
- View everything on a live map dashboard.
- Citizens can submit incident reports.


---
## Installation
Install dependencies:
pip install -r requirements.txt
## Run the Bus GPS Ingestion Server
python ingest.py
Use gps_simulator.py for testing.
---
## Start the Dashboard
streamlit run streamlit_app.py


---
## Train Incident Detection Model
from ultralytics import YOLO model = YOLO('yolov8n.pt') model.train(data='models/data.yaml', epochs=50)
---
## Export Model for Raspberry Pi
model.export(format='onnx')
And run with `run_onnx.py`.


---
## Mobile App
cd mobile_app expo start
---
## Data Sources
- OpenStreetMap (bus stops, geometry)
- Enugu CCTV & traffic datasets
- YouTube driving footage for initial training
