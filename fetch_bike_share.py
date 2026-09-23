import requests
import json
from datetime import datetime, timezone
import os

URL = "https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_status"

OUTPUT_DIR = "bike_share_snapshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_and_save():
    resp = requests.get(URL, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%Y-%m-%dT%H-%M-%S")
    filename = f"bike-share-{timestamp}.json"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"[{now.isoformat()}] Saved snapshot to {filepath}")

if __name__ == "__main__":
    fetch_and_save()
