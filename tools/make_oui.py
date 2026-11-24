#!/usr/bin/env python3
"""Make a compact oui.json ({"AABBCC": "Vendor"}) from a vendor list.
Accepts: IEEE oui.csv, nmap-mac-prefixes ("AABBCC Vendor") or Wireshark manuf ("AA:BB:CC<TAB>Short<TAB>Long").
Usage: python3 tools/make_oui.py input oui.json"""
import csv, json, re, sys
src, dst = sys.argv[1], sys.argv[2]
SUF = re.compile(r'\b(Co\.?,? ?Ltd\.?|Inc\.?|Corporation|Corp\.?|Technologies|Technology|GmbH|LLC|Limited|Ltd\.?)\b', re.I)
def clean(n): return SUF.sub('', n).strip(' ,.')[:28]
out = {}
text = open(src, encoding='utf-8', errors='replace').read()
if text.lstrip().lower().startswith('registry'):
    r = csv.reader(text.splitlines()); next(r, None)
    for row in r:
        if len(row) >= 3 and re.fullmatch(r'[0-9A-Fa-f]{6}', row[1]): out[row[1].upper()] = clean(row[2])
else:
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'): continue
        m = re.match(r'^([0-9A-Fa-f]{6})\s+(.+)$', line)           # nmap
        if m: out[m.group(1).upper()] = clean(m.group(2)); continue
        m = re.match(r'^([0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2})\s+(\S+)(?:\s+(.*))?$', line)  # wireshark (24-bit only)
        if m: out[re.sub(r'[:-]', '', m.group(1)).upper()] = clean((m.group(3) or m.group(2)))
if len(out) < 1000: sys.exit('too few vendors: %d' % len(out))
json.dump(out, open(dst, 'w'), separators=(',', ':'), ensure_ascii=False)
print(len(out), 'vendors')
