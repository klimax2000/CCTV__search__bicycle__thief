# Detection Logger

Dieses Skript dient der automatischen Objekterkennung (Personen, Fahrräder, Autos) in einem Live-Kamerafeed und schreibt jede Erkennung sofort in eine CSV-Datei.

## Hintergrund & Motivation

Im April 2025 wurde mein geliebtes Canyon Mountainbike aus dem Fahrradkeller gestohlen. Ich durfte mit Erlaubnis der benachbarten Autovermietung für 3 Stunden während der Geschäftszeiten die CCTV-Aufnahmen eines möglichen Fluchtwegs einsehen – allerdings ohne eigene Software auf deren System zu installieren. Um die Wahrscheinlichkeit zu erhöhen, den Dieb zu erkennen, habe ich dieses Skript gebaut: Es nutzt mein Handy (mit DroidCam-App) als Kamera, stimmt die FPS mit der CCTV-Wiedergabe ab und erkennt relevante Objekte automatisch.

## Funktionsweise

- **Kamera-Feed:** Das Skript verbindet sich mit dem Live-Stream eines Smartphones, auf dem die App **DroidCam** läuft. Die passende URL wird in der Variable `url` eingetragen.
- **Erkennung:** Es werden nur `"bicycle"`, `"car"` und `"person"` erkannt.
- **Logging:** Jede Erkennung wird sofort mit Zeitstempel und Koordinaten in `detections_log.csv` gespeichert (append, keine Überschreibung).
- **Anzeige:** Das Videofenster zeigt die Erkennungen live an. Mit **q** beenden.

## Beispiel-Video

[![Video ansehen](https://img.youtube.com/vi/4smgL218ykA/0.jpg)](https://youtube.com/shorts/4smgL218ykA?feature=shared)

Klicke auf das Bild, um das Referenzvideo auf YouTube zu öffnen.

## Constraints

- Keine Installation externer Software auf dem CCTV-System der Autovermietung.
- Analyse nur während der erlaubten Zeitfenster.
- Nutzung eines eigenen Handys als Kameraquelle.
- Maximale Geschwindigkeit und Synchronisation mit der CCTV-Wiedergabe.

## Voraussetzungen

- Python 3.x
- Pakete: `opencv-python`, `pandas`, `ultralytics`

Installiere die Pakete mit:
```bash
pip install opencv-python pandas ultralytics
