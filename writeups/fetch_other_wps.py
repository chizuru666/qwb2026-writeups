import json, base64, urllib.request, urllib.parse, os, sys

REPO = 'ThanatosXingYu/qwb2026s10_writeups'
BASE = f'https://api.github.com/repos/{REPO}/contents/'
OUT = r'D:\COMPETITIOM\QWB\_archive\qwb_wp\other'
os.makedirs(OUT, exist_ok=True)

files = [
    ('PWN/PWN13_CanonicoPWN/PWN13_CanonicoPWN_WriteUp.md', 'CanonicoPWN_WP.md'),
    ('Misc/Misc5_Dreambound/Misc5_Dreambound_WriteUp.md', 'Dreambound_WP.md'),
    ('PWN/PWN7_Blackout/PWN7_Blackout_WriteUp.md', 'Blackout_WP.md'),
    ('PWN/PWN2_babyark/PWN2_babyark_WriteUp.md', 'babyark_WP.md'),
]
for path, name in files:
    try:
        url = BASE + urllib.parse.quote(path)
        req = urllib.request.Request(url, headers={'User-Agent': 'x'})
        d = json.load(urllib.request.urlopen(req, timeout=60))
        b = base64.b64decode(d['content'])
        open(os.path.join(OUT, name), 'wb').write(b)
        print('OK', name, len(b))
    except Exception as e:
        print('ERR', name, type(e).__name__, e)
