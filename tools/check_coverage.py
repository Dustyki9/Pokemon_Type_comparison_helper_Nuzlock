import json
import os

ROOT = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(ROOT, 'pokemon_data.txt')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

keys = set()
for k in data.keys():
    try:
        keys.add(int(k))
    except:
        pass

min_id = 1
max_id = 721
missing = [i for i in range(min_id, max_id+1) if i not in keys]
extra = sorted([k for k in keys if k < min_id or k > max_id])

def name_for(i):
    return data.get(str(i), {}).get('name') if str(i) in data else None

print('Total keys found:', len(keys))
print('Expected range: {}-{}'.format(min_id, max_id))
print('Missing count:', len(missing))
if missing:
    print('Missing IDs:', missing)
    for i in missing[:50]:
        print(i, '->', name_for(i))
else:
    print('No missing IDs in the range.')

if extra:
    print('Extra IDs outside range:', extra)

# Quick sanity sample: show first and last 5 entries
first5 = sorted(keys)[:5]
last5 = sorted(keys)[-5:]
print('\nSample first 5:')
for i in first5:
    print(i, name_for(i))
print('\nSample last 5:')
for i in last5:
    print(i, name_for(i))

