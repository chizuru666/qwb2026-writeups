import json, base64, urllib.request, urllib.parse, os

REPO = 'ThanatosXingYu/qwb2026s10_writeups'
BASE = f'https://api.github.com/repos/{REPO}/contents/'
OUT = r'D:\COMPETITIOM\QWB\_archive\qwb_wp\timu'
os.makedirs(OUT, exist_ok=True)

paths = [
    'PWN/PWN5_Babyv8/题目.md',
    'PWN/PWN13_CanonicoPWN/题目.md',
    'PWN/PWN7_Blackout/题目.md',
    'PWN/PWN2_babyark/题目.md',
    'PWN/PWN4_babystar/题目.md',
    'Misc/Misc5_Dreambound/题目.md',
    'Web/Web8_vaultlink/题目.md',
    'Crypto/Crypto5_crp-12025/题目.md',
]
for p in paths:
    try:
        url = BASE + urllib.parse.quote(p)
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'x'}), timeout=60))
        b = base64.b64decode(d['content'])
        name = p.split('/')[1] + '.md'
        open(os.path.join(OUT, name), 'wb').write(b)
        print('OK', name, len(b))
    except Exception as e:
        print('ERR', p, type(e).__name__, e)
