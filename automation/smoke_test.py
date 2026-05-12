import json
import time
from pathlib import Path

import requests

URL = "http://127.0.0.1:8000/status"
ITERATIONS = 10
TIMEOUT_SECONDS = 2
OUTPUT_FILE = Path(__file__).parent / "results.jsonl"
HTML_REPORT = Path(__file__).parent / "report.html"


def run_smoke_test():
    results = []
    for i in range(ITERATIONS):
        start = time.time()
        try:
            response = requests.get(URL, timeout=TIMEOUT_SECONDS)
            latency = round(time.time() - start, 4)
            result = {
                "test_number": i + 1,
                "status_code": response.status_code,
                "latency_seconds": latency,
                "success": response.status_code == 200,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            }
        except Exception as exc:
            result = {
                "test_number": i + 1,
                "status_code": "ERROR",
                "latency_seconds": None,
                "success": False,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "error": str(exc),
            }
        results.append(result)
        time.sleep(1)
    return results


def write_jsonl(results):
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        for entry in results:
            f.write(json.dumps(entry) + "\n")


def write_html(results):
    rows = []
    for entry in results:
        rows.append(
            f"<tr><td>{entry['test_number']}</td><td>{entry['status_code']}</td>"
            f"<td>{entry['latency_seconds']}</td><td>{entry['success']}</td>"
            f"<td>{entry['timestamp']}</td></tr>"
        )

    html = f"""
    <!DOCTYPE html>
    <html lang=\"en\">
    <head>
      <meta charset=\"UTF-8\">
      <title>Smoke Test Report</title>
      <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ccc; padding: 10px; text-align: left; }}
        th {{ background: #f4f4f4; }}
      </style>
    </head>
    <body>
      <h1>API Smoke Test Report</h1>
      <p>Target: {URL}</p>
      <table>
        <thead>
          <tr><th>Test</th><th>Status</th><th>Latency (s)</th><th>Success</th><th>Timestamp</th></tr>
        </thead>
        <tbody>
          {''.join(rows)}
        </tbody>
      </table>
    </body>
    </html>
    """
    HTML_REPORT.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    results = run_smoke_test()
    write_jsonl(results)
    write_html(results)
    print(f"Smoke test completed. Results saved to {OUTPUT_FILE} and {HTML_REPORT}")
