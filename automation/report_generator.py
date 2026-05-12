from pathlib import Path
import json

RESULTS_FILE = Path(__file__).parent / "results.jsonl"


def summarise_results():
    if not RESULTS_FILE.exists():
        print("No results.jsonl file found. Run smoke_test.py first.")
        return

    lines = [json.loads(line) for line in RESULTS_FILE.read_text(encoding="utf-8").splitlines() if line.strip()]
    total = len(lines)
    successes = sum(1 for line in lines if line.get("success"))
    failures = total - successes
    latencies = [line["latency_seconds"] for line in lines if isinstance(line.get("latency_seconds"), (int, float))]
    average_latency = round(sum(latencies) / len(latencies), 4) if latencies else None

    print("=== Smoke Test Summary ===")
    print(f"Total tests: {total}")
    print(f"Successful: {successes}")
    print(f"Failed: {failures}")
    print(f"Average latency: {average_latency}")


if __name__ == "__main__":
    summarise_results()
