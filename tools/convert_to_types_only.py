import json
import os
import shutil
import datetime

ROOT = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(ROOT, "pokemon_data.txt")


def backup(path):
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    bak = f"{path}.{ts}.bak"
    shutil.copy2(path, bak)
    return bak


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)


def convert():
    if not os.path.exists(DATA_PATH):
        print('No data file at', DATA_PATH)
        return
    bak = backup(DATA_PATH)
    print('Backup created:', bak)
    data = load_json(DATA_PATH)
    minimal = {}
    for k, v in data.items():
        # preserve name and Type only
        name = v.get('name') or v.get('Name') or ''
        types = v.get('Type') or v.get('type') or []
        if isinstance(types, str):
            types = [t.strip() for t in types.split(',') if t.strip()]
        types = [t.title() for t in types if t]
        minimal[k] = {'name': name, 'Type': types}
    write_json(DATA_PATH, minimal)
    print('Wrote minimal types-only data to', DATA_PATH)


if __name__ == '__main__':
    convert()

