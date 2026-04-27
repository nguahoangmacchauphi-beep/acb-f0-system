import json
import os
from datetime import datetime

HISTORY_FILE = "history_log.json"


def save_history(record):
    if not isinstance(record, dict):
        raise ValueError("History record must be dict")

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "data": record
    }

    # load existing
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            try:
                logs = json.load(f)
            except:
                logs = []
    else:
        logs = []

    logs.append(entry)

    # append back
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)

    return True