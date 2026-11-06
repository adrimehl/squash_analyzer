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

Stand 6.11.2026, zwei geprüfte Videos (Video 1: 4:40 min, 16 Ballwechsel; Video 2: 6:05 min, 20 Ballwechsel):

| | Video 1 vorher | Video 1 jetzt | Video 2 vorher | Video 2 jetzt |
|---|---|---|---|---|
| gefunden | 12/16 | 15/16 | 18/20 | 19/20 |
| falsch, nicht markiert | 2 | 0 | 1 | 0 |
| falsch, als ? markiert | – | 3 | – | 1 |

Der jeweils fehlende ist gefunden, aber stark verkürzt (Beginn bzw. Ende), und zählt darum nicht als Treffer.
Lehre aus Video 2: Die Aufschlag-Regel (zweimal dasselbe Feld) darf nicht löschen, nur markieren:
nach einem Let oder im lockeren Spiel sind beide Aufschläge echt.
