import json
import os
import shutil
import datetime

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "pokemon_data.txt")

def normalize_type(s):
    if not isinstance(s, str):
        return s
    s = s.strip()
    # Keep acronyms/case like "Mr. Mime" untouched (only type strings are expected here)
    return s.title()

def dedupe_and_sort(lst):
    # preserve unique values, normalize, then sort for readability
    seen = []
    for item in lst:
        norm = normalize_type(item)
        if norm not in seen:
            seen.append(norm)
    return sorted(seen, key=lambda x: (x is None, x))

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def backup(path):
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    bak = f"{path}.{ts}.bak"
    shutil.copy2(path, bak)
    return bak

def clean(data):
    cleaned = {}
    # sort keys by numeric order
    for key in sorted(data.keys(), key=lambda k: int(k)):
        entry = data[key]
        # copy unchanged fields safely
        name = entry.get("name")
        strength = entry.get("Strength", []) or []
        types = entry.get("Type", []) or []
        weakness = entry.get("Weakness", []) or []

        # dedupe + normalize + sort
        strength_clean = dedupe_and_sort(strength)
        types_clean = dedupe_and_sort(types)
        weakness_clean = dedupe_and_sort(weakness)

        cleaned[key] = {
            "Strength": strength_clean,
            "Type": types_clean,
            "Weakness": weakness_clean,
            "name": name
        }
    return cleaned

def main():
    if not os.path.exists(DATA_PATH):
        print(f"Data file not found: {DATA_PATH}")
        return

    try:
        bak = backup(DATA_PATH)
        print(f"Backup created: {bak}")
    except Exception as e:
        print(f"Could not create backup: {e}")
        return

    try:
        data = load_json(DATA_PATH)
    except Exception as e:
        print(f"Failed to load JSON: {e}")
        return

    cleaned = clean(data)

    try:
        write_json(DATA_PATH, cleaned)
        print(f"Cleaned data written to {DATA_PATH}")
    except Exception as e:
        print(f"Failed to write cleaned file: {e}")
        # try to restore backup
        try:
            shutil.copy2(bak, DATA_PATH)
            print("Restored original from backup.")
        except Exception as re:
            print(f"Failed to restore backup: {re}")

if __name__ == "__main__":
    main()

