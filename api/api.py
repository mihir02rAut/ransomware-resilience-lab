from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/status")
def get_status():
    return {
        "status": "OK",
        "timestamp": time.time()
    }
