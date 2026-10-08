fp = r'D:\KU-Assignment\IVF\review2\AIR_Review_Package\github\_build\build_site.py'
src = open(fp,encoding='utf-8').read()
start = src.index('def clean_tex(t):')
end = src.index('CITE_RE =')
B = chr(92)
LBR = B + '{'   # regex literal {
RBR = B + '}'   # regex literal }
LB2 = B*2       # regex literal backslash
newf = '''def clean_tex(t):
    t = re.sub(r'(?<!''' + LB2 + ''')%.*', '', t)
    # drop everything before an orphan end{...}/endgroup (env opened before the window)
    for _ in range(8):
        depth=0; cut=-1
        for m in re.finditer(r'\(''' + '''begin''' + LBR + '''|end''' + LBR + '''[^}]*''' + RBR + '''|begingroup|endgroup)''', t):
            tok=m.group(1)
            if tok.startswith('begin'): depth+=1
            else:
                depth-=1
                if depth<0: cut=m.end(); break
        if cut<0: break
        t=t[cut:]
    # strip float/table environments (keep caption text)
    for env in ['longtable','sidewaystable','tabularx','tabular','figure','minipage','table','equation','align','sidewaysfigure']:
        t = re.sub(LB2+'begin'+LBR+env+RBR+'*?'+LBR+'begin'+LBR+env+'\\*?'+RBR+'['+B+'s'+B+'S]*?'+LB2+'end'+LBR+env+'\\*?'+RBR+'|'+LB2+'begin'+LBR+env+'\\*?'+RBR+'['+B+'s'+B+'S]*?'+LB2+'end'+LBR+env+'\\*?'+RBR, ' ', t)
    # strip grouping wrappers and layout commands
    t = re.sub(LB2+'begingroup['+B+'s'+B+'S]*?'+LB2+'endgroup', ' ', t)
    t = re.sub(LB2+'bgroup['+B+'s'+B+'S]*?'+LB2+'egroup', ' ', t)
    t = re.sub(LB2+'(?:setlength|renewcommand|setcounter|addtocounter|newcommand|providecommand|def|let)'+LBR+'[^}]*'+RBR+LBR+'{[^}]*'+RBR, ' ', t)
    t = re.sub(LB2+'(?:setlength|renewcommand|setcounter)'+LBR+'[^}]*'+RBR, ' ', t)
    t = re.sub(LB2+'cite[tp]?(?:\\[[^\\]]*\\])*'+LBR+'([^}]*)'+RBR, r'[@\1]', t)
    t = re.sub(LB2+'(?:label|ref|eqref|autoref|pageref)'+LBR+'[^}]*'+RBR, '', t)
    t = re.sub(LB2+'(?:textbf|textit|emph|texttt|textsc|underline)'+LBR+'([^}]*)'+RBR, r'\1', t)
    t = re.sub(LB2+'(sub)*section*?'+LBR+'[^}]*'+RBR, '', t)
    t = re.sub(LB2+'(?:begin|end)'+LBR+'[^}]*'+RBR, ' ', t)
    t = re.sub(LB2+'[a-zA-Z]+\\*?(?:\\[[^\\]]*\\])?', ' ', t)
    t = t.replace('~',' ').replace(LB2+'%','%').replace(LB2+'&','&').replace(LB2+'_','_').replace(LB2+'$','$')
    t = re.sub(r'[{}]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

'''
open(fp,'w',encoding='utf-8').write(src[:start]+newf+src[end:])
print('rewrote clean_tex')
