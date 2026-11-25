# ModemYar

مخزن پروفایل مودم‌ها برای برنامهٔ مودم یار · Modem profiles for the Router Yar app.

برنامه فایل `profiles/index.json` و همهٔ فایل‌های فهرست‌شده در آن را دانلود می‌کند.
فرمت: `{ "profiles": ["realtek-boa.json"] }` — نام فایل‌ها فقط حروف انگلیسی، عدد، `.`، `_` و `-` و پسوند `.json`.
`profiles/example.json` فقط نمونه است و در فهرست نیست. راهنمای نوشتن پروفایل: `PROFILES.md`.

## oui.json (optional)
Vendor names for device types. Generate with `python3 tools/make_oui.py oui.csv oui.json` and put it at the repo root.
