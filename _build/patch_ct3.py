fp = r'D:\KU-Assignment\IVF\review2\AIR_Review_Package\github\_build\build_site.py'
src = open(fp,encoding='utf-8').read()
start = src.index('def clean_tex(t):')
end = src.index('CITE_RE =')
B = chr(92)
BS = B*2  # double-backslash for regex literal backslash
BL = B + '{'   # regex literal {
BR = B + '}'   # regex literal }
lines = []
lines.append('def clean_tex(t):')
lines.append("    t = re.sub(r'(?<!" + B + ")%.*', '', t)")
lines.append('    for _ in range(8):')
lines.append('        depth=0; cut=-1')
lines.append("        for m in re.finditer(r'" + B + "(begin" + B + "{|end" + B + "{[^}]*" + B + "}|begingroup|endgroup)', t):")
lines.append('            tok=m.group(1)')
lines.append("            if tok.startswith('begin'): depth+=1")
lines.append('            else:')
lines.append('                depth-=1')
lines.append('                if depth<0: cut=m.end(); break')
lines.append('        if cut<0: break')
lines.append('        t=t[cut:]')
for env in ['longtable','sidewaystable','tabularx','tabular','figure','minipage','table','equation','align','sidewaysfigure']:
    lines.append("    t = re.sub(r'" + B + "begin" + B + "{?" + env + "*?" + B + "}(?:[^}]*" + B + "})?[" + B + "s" + B + "S]*?" + B + "end" + B + "{?" + env + "*?" + B + "}', ' ', t)")
lines.append("    t = re.sub(r'" + B + "begingroup[" + B + "s" + B + "S]*?" + B + "endgroup', ' ', t)")
lines.append("    t = re.sub(r'" + B + "bgroup[" + B + "s" + B + "S]*?" + B + "egroup', ' ', t)")
lines.append("    t = re.sub(r'" + B + "(?:setlength|renewcommand|setcounter|addtocounter|newcommand|providecommand|def|let)" + B + "{[^}]*" + B + "}" + B + "{[^}]*" + B + "}', ' ', t)")
lines.append("    t = re.sub(r'" + B + "(?:setlength|renewcommand|setcounter)" + B + "{[^}]*" + B + "}', ' ', t)")
lines.append("    t = re.sub(r'" + B + "cite[tp]?(?:" + B + "[[^" + B + "]]" + B + "])*" + B + "{([^}]*)" + B + "}', r'[@" + B + "1]', t)")
lines.append("    t = re.sub(r'" + B + "(?:label|ref|eqref|autoref|pageref)" + B + "{[^}]*" + B + "}', '', t)")
lines.append("    t = re.sub(r'" + B + "(?:textbf|textit|emph|texttt|textsc|underline)" + B + "{([^}]*)" + B + "}', r'" + B + "1', t)")
lines.append("    t = re.sub(r'" + B + "(sub)*section*?" + B + "{[^}]*" + B + "}', '', t)")
lines.append("    t = re.sub(r'" + B + "(?:begin|end)" + B + "{[^}]*" + B + "}', ' ', t)")
lines.append("    t = re.sub(r'" + B + "[a-zA-Z]+" + B + "*?(?:" + B + "[[^" + B + "]]" + B + "])?', ' ', t)")
lines.append("    t = t.replace('~',' ').replace('" + B + "%','%').replace('" + B + "&','&').replace('" + B + "_','_').replace('" + B + "$','$')")
lines.append("    t = re.sub(r'[{}]', '', t)")
lines.append("    t = re.sub(r'" + B + "s+', ' ', t).strip()")
lines.append('    return t')
lines.append('')
newf = chr(10).join(lines)
# now convert single \  to \\  in the regex portions (i.e. every B inside r'...' becomes \\)
# Actually: in the emitted source, B produced '\' which in r'...' is literal backslash. But for matching \begin we need \\begin.
# Simpler: rebuild with BB = B+B for every regex backslash
lines2=[]
lines2.append('def clean_tex(t):')
lines2.append("    t = re.sub(r'(?<!" + B + ")%.*', '', t)")
lines2.append('    for _ in range(8):')
lines2.append('        depth=0; cut=-1')
lines2.append("        for m in re.finditer(r'" + B + "(begin" + B + "{|end" + B + "{[^}]*" + B + "}|begingroup|endgroup)', t):")
lines2.append('            tok=m.group(1)')
lines2.append("            if tok.startswith('begin'): depth+=1")
lines2.append('            else:')
lines2.append('                depth-=1')
lines2.append('                if depth<0: cut=m.end(); break')
lines2.append('        if cut<0: break')
lines2.append('        t=t[cut:]')
for env in ['longtable','sidewaystable','tabularx','tabular','figure','minipage','table','equation','align','sidewaysfigure']:
    lines2.append("    t = re.sub(r'" + B + "begin" + B + "{?" + env + "*?" + B + "}(?:[^}]*" + B + "})?[" + B + "s" + B + "S]*?" + B + "end" + B + "{?" + env + "*?" + B + "}', ' ', t)")
lines2.append("    t = re.sub(r'" + B + "begingroup[" + B + "s" + B + "S]*?" + B + "endgroup', ' ', t)")
lines2.append("    t = re.sub(r'" + B + "bgroup[" + B + "s" + B + "S]*?" + B + "egroup', ' ', t)")
lines2.append("    t = re.sub(r'" + B + "(?:setlength|renewcommand|setcounter|addtocounter|newcommand|providecommand|def|let)" + B + "{[^}]*" + B + "}" + B + "{[^}]*" + B + "}', ' ', t)")
lines2.append("    t = re.sub(r'" + B + "(?:setlength|renewcommand|setcounter)" + B + "{[^}]*" + B + "}', ' ', t)")
lines2.append("    t = re.sub(r'" + B + "cite[tp]?(?:" + B + "[[^" + B + "]]" + B + "])*" + B + "{([^}]*)" + B + "}', r'[@" + B + "1]', t)")
lines2.append("    t = re.sub(r'" + B + "(?:label|ref|eqref|autoref|pageref)" + B + "{[^}]*" + B + "}', '', t)")
lines2.append("    t = re.sub(r'" + B + "(?:textbf|textit|emph|texttt|textsc|underline)" + B + "{([^}]*)" + B + "}', r'" + B + "1', t)")
lines2.append("    t = re.sub(r'" + B + "(sub)*section*?" + B + "{[^}]*" + B + "}', '', t)")
lines2.append("    t = re.sub(r'" + B + "(?:begin|end)" + B + "{[^}]*" + B + "}', ' ', t)")
lines2.append("    t = re.sub(r'" + B + "[a-zA-Z]+" + B + "*?(?:" + B + "[[^" + B + "]]" + B + "])?', ' ', t)")
lines2.append("    t = t.replace('~',' ').replace('" + B + "%','%').replace('" + B + "&','&').replace('" + B + "_','_').replace('" + B + "$','$')")
lines2.append("    t = re.sub(r'[{}]', '', t)")
lines2.append("    t = re.sub(r'" + B + "s+', ' ', t).strip()")
lines2.append('    return t')
lines2.append('')
# emit, doubling every single backslash inside the regex parts
out=[]
for ln in lines2:
    # every '\' that is inside an r'...' pattern needs to be '\\' in source
    # the generated ln has B where we want literal backslash -> emit B+B in source for regex backslash, B for { }
    # simplest: in regex contexts we wrote B for 'literal backslash' and B+'{' for literal brace. So emit B -> B+B, but B+'{' should stay B+'{'
    res=''
    i=0
    while i<len(ln):
        if ln[i]==B and i+1<len(ln) and ln[i+1] in '[]{}()^*+?|swdsSWBb': res+=B+B; i+=1
        elif ln[i]==B and i+1<len(ln) and ln[i+1] in '{},': res+=B; i+=1
        elif ln[i]==B and i+1<len(ln) and ln[i+1]==B: res+=B+B; i+=2
        else: res+=ln[i]; i+=1
    out.append(res)
newf = chr(10).join(out)
open(fp,'w',encoding='utf-8').write(src[:start]+newf+src[end:])
print('rewrote, sample:', out[10] if len(out)>10 else out[-1])
