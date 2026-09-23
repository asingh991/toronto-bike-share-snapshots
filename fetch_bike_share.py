import requests
import json
from datetime import datetime, timezone
import os

URL = "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/2b44db0d-eea9-442d-b038-79335368ad5a/resource/5c1c2c06-d27f-47b7-ae82-926a6d23d76f/download/bike-share-json.json"

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