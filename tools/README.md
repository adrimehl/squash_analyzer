# Messwerkzeuge für die Ballwechsel-Erkennung

Misst die automatische Erkennung gegen von Hand geprüfte Ballwechsel, ohne Video.

1. In der App ein Video analysieren, alle Ballwechsel prüfen und korrigieren, Häkchen
   „alle geprüft“ setzen und „Analyse-Daten exportieren“ (JSON).
2. Erkennungsfunktionen unverändert aus der App holen und messen:

```bash
python tools/extract_detection.py src/index.html /tmp/detection.js
node tools/evaluate_rallies.js /tmp/detection.js <export>.json -v
```

Ausgabe: gefundene, fehlende und falsche Ballwechsel sowie die Abweichung von Beginn und Ende.
Die Export-Dateien enthalten persönliche Daten (Namen, Spielverlauf) und gehören nicht ins Repository.

Stand nach der Verbesserung vom 6.11.2026 (ein geprüftes Video, 4:40 min, 16 Ballwechsel):
vorher 12/16 gefunden, 2 falsch; nachher alle 16 gefunden (einer zu kurz), 0 falsch.
Enden im Median 2,2 s zu spät; die App gleicht das über das Lernen aus Korrekturen aus.
