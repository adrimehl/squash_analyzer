# Hinweise für Claude

## Bei jeder Änderung: GitHub UND Artefakt aktualisieren

Der Nutzer will Änderungen sofort sehen, ohne etwas herunterzuladen. Deshalb nach jeder Änderung:

1. `src/index.html` (bzw. das Modell in `src/`) ändern.
2. `python build.py` ausführen (erzeugt `squash-analyzer.html`, die Einzeldatei).
3. Committen und pushen.
4. Das claude.ai-Artefakt „SquashAnalyzerPro“ aktualisieren:
   https://claude.ai/artifact/XkLYX28RKxir6fNKUNuKeH
   - `src/index.html` in den Scratchpad kopieren und mit `url` auf dieses Artefakt veröffentlichen.
   - Das Modell (`movenet-multipose.json`, `movenet-multipose-weights.wasm`) liegt dort bereits als Datei
     neben der Seite; nur bei Modelländerungen über `files` mitschicken.
   - In einer neuen Sitzung das Artefakt vorher mit `action: "read"` lesen (sonst wird die Veröffentlichung abgelehnt).

## Sonstiges
- Sprache der App und der Antworten: Deutsch, Schweizer Rechtschreibung (kein ß).
- Keine Videos oder Berichte ins Repository (siehe `.gitignore`).
