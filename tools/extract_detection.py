# Holt die Erkennungsfunktionen unverändert aus src/index.html, damit sie in Node laufen.
import re, sys
s = open(sys.argv[1], encoding='utf-8').read()
js = s[s.index('<script>\n(function(){'):]
def fn(name):
    i = js.index('function ' + name + '(')
    j = js.index('{', i); d = 0
    for k in range(j, len(js)):
        if js[k] == '{': d += 1
        elif js[k] == '}':
            d -= 1
            if d == 0: return js[i:k+1]
def const(line_start):
    i = js.index(line_start); return js[i:js.index('\n', i)]
parts = [const('const CW='), const('const FPS='), 'const BRIDGE=1.0;', const('const ZONES='), const('const CORNERS='),
         'const clamp=(v,a,b)=>v<a?a:v>b?b:v;', const('const median='), const('const mean='),
         'function loadLearn(){return {};}', 'const dT=q=>Math.hypot(q.x-TX,q.y-TY);']
for n in ['cornerOf','grid','speeds','shotsFrom','findRallies','boxOf','findServes','calKey','endBias','deepAnalysis','shotSequence','computeExcl']:
    parts.append(fn(n))
parts.append('module.exports={deepAnalysis,computeExcl,FPS};')
open(sys.argv[2], 'w').write('\n'.join(parts))
print('ok')
