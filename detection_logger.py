import cv2
import time
import pandas as pd
import os

from ultralytics import YOLO

# SETTINGS
# droidcam for Phone 1: http://XXX.XXX.X.XXX:XXXX/video
# droidcam for Phone 2: http://XXX.XXX.X.XXX:YYYY/video
url = "http://XXX.XXX.X.XXX:XXXX/video"  # DroidCam IP!
output_csv = "detections_log.csv"

# Modell laden
model = YOLO("yolov8n.pt")

# allowed_classes = ["bicycle", "car", "truck", "person"]
allowed_classes = ["bicycle", "car", "person"]

# Videoquelle öffnen
cap = cv2.VideoCapture(url)

print("[INFO] Detection started... Press 'strg + c' to stop.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to grab frame.")
        break

    # Auflösung reduzieren
    frame = cv2.resize(frame, (640, 480))

    # Vorhersage
    results = model.predict(frame, verbose=False)

    for result in results:
        boxes = result.boxes.xyxy
        classes = result.boxes.cls

        for box, cls in zip(boxes, classes):
            class_name = model.names[int(cls)]
            if class_name not in allowed_classes:
                continue

            x1, y1, x2, y2 = map(int, box.tolist())
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            log_entry = [timestamp, class_name, x1, y1, x2, y2]
            print(f"[{timestamp}] Detected: {class_name} at [{x1}, {y1}, {x2}, {y2}]")

            # Append detection to CSV immediately
            df = pd.DataFrame(
                [log_entry], columns=["timestamp", "object", "x1", "y1", "x2", "y2"]
            )
            df.to_csv(
                output_csv, mode="a", header=not os.path.exists(output_csv), index=False
            )

            # Rechteck und Label zeichnen
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(
                frame,
                class_name,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 0, 0),
                2,
            )

    # Fenster anzeigen
    cv2.imshow("Detection", frame)

    # Exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print(f"[INFO] Detection finished. Logfile saved as {output_csv}")
