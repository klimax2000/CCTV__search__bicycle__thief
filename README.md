# Detection Logger

Dieses Skript dient der automatisierten Objekterkennung (Personen, Fahrräder, Autos) in einem Live-Kamerafeed und schreibt jede Erkennung sofort in eine CSV-Datei.

## Hintergrund & Motivation

Im April 2025 wurde mein Canyon-Mountainbike aus dem Fahrradkeller gestohlen. Ich durfte mit Erlaubnis der benachbarten Autovermietung für drei Stunden die CCTV-Aufnahmen eines möglichen Fluchtwegs einsehen – allerdings ohne eigene Software auf deren System zu installieren. Um die Wahrscheinlichkeit zu erhöhen, den Dieb zu erkennen, habe ich dieses Skript entwickelt.

## Funktionsweise

- 📷 **Kamera-Feed:** Das Skript verbindet sich mit dem Livestream eines Smartphones (per DroidCam-App). Die passende URL wird in der Variable `url` eingetragen.
- 🧠 **Objekterkennung:** Es werden `"bicycle"`, `"car"` und `"person"` automatisch erkannt.
- 📝 **Logging:** Jede Erkennung wird mit Zeitstempel und Koordinaten in `detections_log.csv` gespeichert.
- 🪟 **Live-Anzeige:** Das Videofenster zeigt alle Detektionen in Echtzeit. Mit **q** beenden.

## Beispielvideo

[![Video ansehen](https://img.youtube.com/vi/4smgL218ykA/0.jpg)](https://youtube.com/shorts/4smgL218ykA?feature=shared)

## YOLOv8 Modell-Datei nicht enthalten

Dieses Projekt nutzt das Modell **YOLOv8** von [Ultralytics](https://github.com/ultralytics/ultralytics) zur Objekterkennung.  
Die Modell-Datei `yolov8n.pt` ist aus **lizenzrechtlichen Gründen** nicht im Repository enthalten.

Bitte laden Sie das Modell oder eine aktuellere Version manuell von der offiziellen Ultralytics-Seite herunter und platzieren sie im Projektordner.

## Voraussetzungen

- Python 3.x
- Pakete: `opencv-python`, `pandas`, `ultralytics`

Installation mit:
```bash
pip install opencv-python pandas ultralytics
