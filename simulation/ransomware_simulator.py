import os
import time
from pathlib import Path

TARGET_DIR = Path(__file__).parent / "test_data"
TARGET_DIR.mkdir(exist_ok=True)

print("Starting safe ransomware-style simulation...")

for i in range(20):
    file_path = TARGET_DIR / f"file_{i}.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Simulated encrypted content placeholder\n")
        f.write(f"Iteration: {i}\n")
        f.write(f"Timestamp: {time.time()}\n")
    time.sleep(0.5)

print("Simulation completed. Review file activity in your monitored folder / SIEM.")
