import cv2
import numpy as np
from ultralytics import YOLO
from sort import Sort

# Load YOLO model
model = YOLO("yolov8n.pt")

# Initialize tracker
tracker = Sort()

# Webcam input
cap = cv2.VideoCapture(0)  # 0 = webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO detection
    results = model(frame, stream=True)
    detections = []

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])

            if conf > 0.5:
                detections.append([x1, y1, x2, y2])

    # Convert to numpy
    detections = np.array(detections)

    # Apply tracking
    tracked_objects = tracker.update(detections)

    # Draw boxes
    for obj in tracked_objects:
        x1, y1, x2, y2, track_id = obj
        cv2.rectangle(frame, (int(x1), int(y1)),
                              (int(x2), int(y2)),
                              (0, 255, 0), 2)
        cv2.putText(frame, f"ID: {track_id}",
                    (int(x1), int(y1)-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (0, 255, 0), 2)

    cv2.imshow("Object Detection & Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
