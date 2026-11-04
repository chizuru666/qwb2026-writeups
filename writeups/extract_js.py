import re
src = open(r'D:\COMPETITIOM\QWB\_archive\qwb_wp\Babyv8_exp.py', encoding='utf-8').read()
m = re.search(r"EXPLOIT_JS = r'''(.*?)'''\.strip\(\)", src, re.S)
js = m.group(1).strip()
open(r'D:\COMPETITIOM\QWB\_archive\qwb_wp\Babyv8_exploit.js', 'w', encoding='utf-8').write(js + '\n')
print('bytes', len(js))
