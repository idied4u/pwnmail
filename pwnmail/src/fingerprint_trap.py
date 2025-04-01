# Pwnmail Fingerprint Surveillance Trap
# Tracks and alerts if a public key fingerprint changes (MITM detection)

import os
import json
from core import import_public_key

DB_PATH = os.path.expanduser("~/.pwnmail_trusted_keys.json")

def load_fingerprint_db():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r") as f:
            return json.load(f)
    return {}

def save_fingerprint_db(db):
    with open(DB_PATH, "w") as f:
        json.dump(db, f, indent=2)

def trap_key_change(key_data):
    result = import_public_key(key_data)
    new_fingerprints = result.fingerprints
    db = load_fingerprint_db()
    alerts = []

    for fp in new_fingerprints:
        if fp in db:
            if db[fp] != key_data:
                alerts.append(fp)
                print(f"⚠️ ALERT: Fingerprint {fp} has changed! Possible MITM attempt.")
        else:
            print(f"✅ New key added: {fp}")
            db[fp] = key_data

    save_fingerprint_db(db)
    return alerts

# Example usage
if __name__ == "__main__":
    print("Paste your armored public key (end with CTRL+D):")
    key_data = ""
    try:
        while True:
            line = input()
            key_data += line + "\n"
    except EOFError:
        pass

    trap_key_change(key_data)
