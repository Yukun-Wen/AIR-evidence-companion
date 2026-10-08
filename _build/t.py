
import re
B = chr(92)
env_txt = B + 'begin{longtable}{X}'
for pat in [B*2+'begin'+B*2+'{([^}]*)'+B*2+'}', B+'begin'+B*2+'{([^}]*)'+B*2+'}', B*2+'begin'+B+'{([^}]*)'+B+'}']:
    m = re.search(pat, env_txt)
    print(repr(pat), '->', m.group(1) if m else None)
