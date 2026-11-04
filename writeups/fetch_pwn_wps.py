import json, base64, urllib.request, urllib.parse, os, time

REPO = 'ThanatosXingYu/qwb2026s10_writeups'
BASE = f'https://api.github.com/repos/{REPO}/contents/'
OUT = r'D:\COMPETITIOM\QWB\_archive\qwb_wp\pwn'
os.makedirs(OUT, exist_ok=True)

paths = [
    'PWN/PWN1_babel/PWN1_babel_WriteUp.md',
    'PWN/PWN3_babysilent/PWN3_babysilent_WriteUp.md',
    'PWN/PWN6_bad_puppet/PWN6_bad_puppet_WriteUp.md',
    'PWN/PWN8_drywell/PWN8_drywell_WriteUp.md',
    'PWN/PWN9_easytl/PWN9_easytl_WriteUp.md',
    'PWN/PWN10_HESEUS/PWN10_HESEUS_WriteUp.md',
    'PWN/PWN11_oldsvr/PWN11_oldsvr_WriteUp.md',
    'PWN/PWN12_ez_qemu/PWN12_ez_qemu_WriteUp.md',
    'PWN/PWN14_hexachord/PWN14_hexachord_WriteUp.md',
    'PWN/PWN15_What The Fox!/PWN15_What The Fox!_WriteUp.md',
    'PWN/PWN16_shadowledger/PWN16_shadowledger_WriteUp.md',
    'PWN/PWN17_Ironclad/PWN17_Ironclad_WriteUp.md',
]
for p in paths:
    name = p.split('/')[1] + '.md'
    dst = os.path.join(OUT, name)
    if os.path.exists(dst):
        print('SKIP', name); continue
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(BASE + urllib.parse.quote(p), headers={'User-Agent': 'x'}), timeout=60))
        b = base64.b64decode(d['content'])
        open(dst, 'wb').write(b)
        print('OK', name, len(b))
        time.sleep(0.4)
    except Exception as e:
        print('ERR', name, type(e).__name__, str(e)[:120])
