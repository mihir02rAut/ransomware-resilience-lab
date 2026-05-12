from fastapi import FastAPI
import time

app = FastAPI(
    title="Ransomware Resilience Lab API",
    description="Minimal service used to evaluate availability during simulated cyber disruption.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "project": "ransomware-resilience-lab",
        "message": "API is running",
    }


@app.get("/status")
def get_status():
    return {
        "status": "OK",
        "timestamp": time.time(),
        "service": "fastapi",
        "purpose": "availability-check",
    }
