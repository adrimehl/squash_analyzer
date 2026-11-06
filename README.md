# SquashAnalyzerPro

Videoanalyse für Squash: Video von hinten durch die Glaswand laden, Court markieren, Spieler antippen.
Die App misst Laufmeter, Positionen (Heatmaps, T-Kontrolle), Ballwechsel, Schläge und Ausfallschritte
und leitet Tipps daraus ab. **Alles läuft im Browser, das Video verlässt das Gerät nicht.**

## Benutzen

**`squash-analyzer.html`** herunterladen (auf GitHub: „Download raw file“) und per Doppelklick öffnen.
Die Datei enthält alles (App, KI-Modell, TensorFlow.js) und funktioniert auch ohne Internet.

Am besten in Chrome oder Edge am Computer: Die KI-Erkennung nutzt die Grafikkarte (WebGL) und ist dort
deutlich schneller als am Handy.

Nur in der claude.ai-Version verfügbar: „Tipps von Claude“ und der Coaching-Bericht von Claude
(sie nutzen die KI von claude.ai). Alles andere funktioniert in der Einzeldatei gleich.

## Wie es funktioniert

Kein Python, keine Installation: alles ist JavaScript im Browser.

| Teil | Technik |
|---|---|
| Spielererkennung | KI-Modell MoveNet MultiPose (Google), ausgeführt mit TensorFlow.js |
| Position auf dem Court | Homographie aus den vier markierten Court-Punkten |
| Ballgeräusche | Tonspur, Web Audio API (Bandpass 0,8–4 kHz, Knall-Erkennung) |
| Darstellung | Canvas und SVG |

## Aufbau

| Datei | Zweck |
|---|---|
| `src/index.html` | die App (so läuft sie auch als claude.ai-Artefakt) |
| `src/movenet-multipose.json`, `src/movenet-multipose-weights.wasm` | KI-Modell (Beschreibung und Gewichte, ca. 9,5 MB) |
| `vendor/tf.min.js` | TensorFlow.js 4.22.0 |
| `build.py` | baut `squash-analyzer.html` (alles in einer Datei): `python build.py` |
| `squash-analyzer.html` | erzeugte Einzeldatei, nicht von Hand ändern |

## Lizenzen

- MoveNet MultiPose: Google, Apache License 2.0
- TensorFlow.js: Google, Apache License 2.0 (Hinweis im Kopf von `vendor/tf.min.js`)
