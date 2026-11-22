#!/usr/bin/env python3
"""Convert IEEE oui.csv (https://standards-oui.ieee.org/oui/oui.csv) to a compact oui.json.
Usage: python3 tools/make_oui.py oui.csv oui.json
Put oui.json at the ROOT of the GitHub repo; the app downloads it."""
import csv, json, sys, re
src, dst = sys.argv[1], sys.argv[2]
out = {}
with open(src, newline='', encoding='utf-8') as f:
    r = csv.reader(f); next(r, None)
    for row in r:
        if len(row) < 3: continue
        name = re.sub(r'\b(Co\.?,? ?Ltd\.?|Inc\.?|Corporation|Corp\.?|Technologies|Technology|GmbH|LLC)\b', '', row[2], flags=re.I).strip(' ,.')
        out[row[1].upper()] = name[:28]
json.dump(out, open(dst, 'w'), separators=(',', ':'), ensure_ascii=False)
print(len(out), 'vendors')
