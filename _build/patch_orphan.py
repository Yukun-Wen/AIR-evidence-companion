# -*- coding: utf-8 -*-
import re
fp = r'D:\KU-Assignment\IVF\review2\AIR_Review_Package\github\_build\build_site.py'
t = open(fp, encoding='utf-8').read()
start = t.index('    # drop everything before the last orphan')
end   = t.index('    # drop float/table environments entirely')
newb = '''    # cut the window at any orphan end{...}/endgroup (env opened before the window)
    for _ in range(8):
        depth=0; cut=-1
        for m in re.finditer(r'\\(begin\{|end\{[^}]*\}|begingroup|endgroup)', t):
            tok=m.group(1)
            if tok.startswith('begin'): depth+=1
            else:
                depth-=1
                if depth<0: cut=m.end(); break
        if cut<0: break
        t=t[cut:]
'''
open(fp,'w',encoding='utf-8').write(t[:start]+newb+t[end:])
print('patched')
