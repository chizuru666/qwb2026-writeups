import json, base64, urllib.request, urllib.parse, os, time

REPO = 'ThanatosXingYu/qwb2026s10_writeups'
BASE = f'https://api.github.com/repos/{REPO}/contents/'
OUT = r'D:\COMPETITIOM\QWB\_archive\qwb_wp\all'
os.makedirs(OUT, exist_ok=True)

paths = [
    'Web/Web1_BlindReview/Web1_BlindReview_WriteUp.md',
    'Web/Web3_ezphp/Web3_ezphp_WriteUp.md',
    'Web/Web4_ezstar/Web4_ezstar_WriteUp.md',
    'Web/Web6_Crack a Little Smile/Web6_Crack a Little Smile_WriteUp.md',
    'Web/Web7_fault_web_and_fault_hash/Web7_fault_web_and_fault_hash_WriteUp.md',
    'Web/Web9_vaultlink_revenge/Web9_vaultlink_revenge_WriteUp.md',
    'Reverse/Reverse1_ELFStudy/Reverse1_ELFStudy_WriteUp.md',
    'Reverse/Reverse2_firmware/Reverse2_firmware_WriteUp.md',
    'Reverse/Reverse3_license/Reverse3_license_WriteUp.md',
    'Misc/Misc1_宇宙微波背景辐射/Misc1_宇宙微波背景辐射_WriteUp.md',
    'Misc/Misc2_0perator/Misc2_0perator_WriteUp.md',
    'Misc/Misc3_NeuronShuffle/Misc3_NeuronShuffle_WriteUp.md',
    'Misc/Misc4_谍影重重7/Misc4_谍影重重7_WriteUp.md',
    'Misc/Misc6_问卷调查/Misc6_问卷调查_WriteUp.md',
    'Crypto/Crypto1_frozen/Crypto1_frozen_WriteUp.md',
    'Crypto/Crypto2_vmshare/Crypto2_vmshare_WriteUp.md',
    'Crypto/Crypto3_hoRRibleRing/Crypto3_hoRRibleRing_WriteUp.md',
    'Crypto/Crypto4_zkRSA/Crypto4_zkRSA_WriteUp.md',
    'Crypto/Crypto6_crp-11741/Crypto6_crp-11741_WriteUp.md',
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
        time.sleep(0.5)
    except Exception as e:
        print('ERR', name, type(e).__name__, str(e)[:100])
