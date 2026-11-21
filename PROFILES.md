# نوشتن پروفایل برای یک مدل مودم

هر پروفایل یک فایل JSON است که به برنامه می‌گوید با پنل وب آن مودم چطور حرف بزند. نمونه کامل: `docs/example-profile.json`
(با `tests/mock_modems.js` تست می‌شود). پروفایل را می‌توان در `assets/www/profiles.js` گذاشت یا از «تنظیمات ← پروفایل مودم‌ها» وارد کرد.

```jsonc
{
  "id": "my-modem", "name": "Brand Model",
  "detect": { "path": "/", "regex": "عبارتی که در صفحه ورود یا هدرهای این مودم هست" },   // تشخیص خودکار
  "login": {
    "type": "basic",                       // یا فرم/JSON با "request": {method, path, json|data|raw}
    "request": { "method": "POST", "path": "/api/login", "json": { "username": "{user}", "password": "{pass}" } },
    "password_transform": "plain|md5|sha1|sha256|base64",
    "success": { "status": 200, "json_path": "token", "store": "token", "body_contains": "", "body_not_contains": "", "regex": "" },
    "auth_header": { "Authorization": "Bearer {token}" },          // برای درخواست‌های بعدی
    "cookies": { "Authorization": "Basic {basic_b64}" }             // کوکی دستی (برخی پنل‌های قدیمی)
  },
  "info":    { "request": {...}, "format": "json|text", "map": { "model": "data.model", "uptime_s": {"regex": "up=(\\d+)"} }, "extras": {...} },
  "wifi":    { "request": {...}, "list": "data.networks", "map": { "id": "id", "ssid": "ssid", "enabled": "enabled", "band": "band" } },
  "wifi_set":{ "request": { "method": "POST", "path": "/wifi/{id}", "omit_empty": true, "json": { "ssid": "{ssid}", "enabled": "{enabled}", "password": "{password}" } } },
  "devices": { "request": {...}, "list": "data.hosts", "map": { "mac": "mac", "ip": "ip", "hostname": "name", "online": "online", "blocked": "blocked" } },
  "block":   { "request": { "method": "POST", "path": "/block", "json": { "mac": "{mac}", "blocked": "{blocked}" } } },
  "static_ip": {...}, "dns": {...}, "reboot": {...}, "logout": {...}
}
```
- متغیرهای قالب: `{user} {pass} {raw_pass} {basic_b64}` و برای هر عمل `{mac} {ip} {dns1} {dns2} {ssid} {enabled} {id} {blocked}`.
- پاسخ‌های متنی/HTML: `"format": "text"` و `"list_regex"` با گروه‌های نام‌دار JS مثل `(?<mac>..)`.
- هر بخشی که پروفایل نداشته باشد در برنامه غیرفعال و با پیام «پشتیبانی نمی‌شود» نمایش داده می‌شود.
- پنلی که رمز را در مرورگر با جاوااسکریپت رمزگذاری می‌کند (RSA/AES) با پروفایل ساده قابل پشتیبانی نیست و به کد اختصاصی نیاز دارد.
