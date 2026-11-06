# -*- coding: utf-8 -*-
"""Baut squash-analyzer.html: die ganze App in EINER Datei.

src/index.html ist die Seite, wie sie auch als claude.ai-Artefakt läuft (dort liegen das
KI-Modell und seine Beschreibung als eigene Dateien daneben). Für die Einzeldatei werden
eingebettet:
  - TensorFlow.js (vendor/tf.min.js), damit nichts aus dem Internet nachgeladen werden muss
  - das MoveNet-MultiPose-Modell (src/movenet-multipose.json + -weights.wasm, Base64)
Ergebnis: ca. 15 MB, per Doppelklick im Browser zu öffnen.

Aufruf:  python build.py
"""
import base64
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'src')
OUT = os.path.join(HERE, 'squash-analyzer.html')


def read(*parts, mode='r'):
    with open(os.path.join(HERE, *parts), mode, **({} if 'b' in mode else {'encoding': 'utf-8'})) as f:
        return f.read()


def safe_js(code):
    # ein "</script" im Code würde das <script>-Element vorzeitig beenden
    return re.sub(r'</(script)', r'<\\/\1', code, flags=re.IGNORECASE)


def main():
    page = read('src', 'index.html')

    tf_tag = '<script src="https://cdnjs.cloudflare.com/ajax/libs/tensorflow/4.22.0/tf.min.js"></script>'
    if tf_tag not in page:
        raise SystemExit('TensorFlow.js-Einbindung in src/index.html nicht gefunden.')
    model = {
        'json': json.loads(read('src', 'movenet-multipose.json')),
        'weights': base64.b64encode(read('src', 'movenet-multipose-weights.wasm', mode='rb')).decode('ascii'),
    }
    embedded = ('<script>\n' + safe_js(read('vendor', 'tf.min.js')) + '\n</script>\n'
                '<script>window.__SQ_MODEL = ' + safe_js(json.dumps(model, separators=(',', ':'))) + ';</script>')
    page = page.replace(tf_tag, embedded, 1)

    html = ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            '<!-- Automatisch erzeugt aus src/index.html mit build.py - nicht von Hand ändern -->\n'
            # Grundeinstellungen, die claude.ai sonst um die Seite herum setzt
            '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
            'body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
            '</head>\n<body>\n' + page + '\n</body>\n</html>\n')
    with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write(html)
    print(f'{os.path.basename(OUT)}: {len(html.encode("utf-8")) / 1e6:.1f} MB')


if __name__ == '__main__':
    main()
