import json
import os
import shutil
import datetime
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(ROOT, "pokemon_data.txt")

API_BASE = "https://pokeapi.co/api/v2/pokemon/"


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


def fetch_pokemon(id_):
    url = API_BASE + str(id_)
    req = urllib.request.Request(url, headers={"User-Agent": "PokEpro Data Fetcher/1.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.load(resp)


def main():
    if not os.path.exists(DATA_PATH):
        print('Data file not found:', DATA_PATH)
        return

    bak = backup(DATA_PATH)
    print('Backup created:', bak)

    data = load_json(DATA_PATH)
    added = 0
    # Gen 7 National Dex range: 722..809 (includes Meltan/Melmetal at 808/809)
    for id_ in range(722, 810):
        key = str(id_)
        if key in data:
            continue
        try:
            pj = fetch_pokemon(id_)
        except Exception as e:
            print(f'Failed to fetch {id_}: {e}')
            time.sleep(1)
            continue
        types = [t['type']['name'].title() for t in sorted(pj.get('types', []), key=lambda x: x['slot'])]
        name = pj.get('name', '').replace('-', ' ').title()
        data[key] = {'name': name, 'Type': types}
        added += 1
        print(f'Added {id_}: {name} / {types}')
        time.sleep(0.2)

    if added:
        write_json(DATA_PATH, data)
        print(f'Wrote {added} new entries to {DATA_PATH}')
    else:
        print('No new entries were added.')

if __name__ == '__main__':
    main()

