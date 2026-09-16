"""
detection_module.py
Path 2: Object Detection using YOLOv8 (ultralytics).
Project 4: Image & Text Recognition — DecodeLabs AI Internship

Uses YOLOv8 nano model — no manual model file download needed.
Library auto-downloads the model on first run.
"""

import os
import cv2
import numpy as np
from preprocess import load_image, save_image
from colors import ok, warn, detected, success, heading, divider

# YOLOv8 nano model (auto-downloaded on first run)
MODEL_NAME = "yolov8n.pt"

# Confidence threshold (Project 4 rule: 80%)
CONFIDENCE_THRESHOLD = 0.80


def load_model():
    """Load YOLOv8 nano model (auto-download)."""
    try:
        from ultralytics import YOLO
    except ImportError:
        raise ImportError(
            "ultralytics is not installed. Please run:\n"
            "  pip install ultralytics"
        )

    print(ok(f"YOLOv8 model loading: {MODEL_NAME}"))
    model = YOLO(MODEL_NAME)   # auto-downloads on first run (~6 MB)
    print(ok("YOLOv8 model ready"))
    return model


def run_detection(image_path, output_img="output/detection_result.jpg"):
    """
    Object Detection pipeline using YOLOv8.
    1. Load image
    2. Run YOLOv8 inference
    3. Filter by 80% confidence
    4. Draw bounding boxes
    5. Save output
    """
    print()
    print(divider('='))
    print(heading("  PATH 2: OBJECT DETECTION (YOLOv8)"))
    print(divider('='))

    image = load_image(image_path)
    model = load_model()

    # --- YOLOv8 inference ---
    results = model(image, verbose=False)
    print(ok(f"Inference complete: {len(results)} result(s)"))

    # --- Filter + Draw ---
    detected_count = 0
    for result in results:
        boxes = result.boxes
        if boxes is None:
            continue

        for box in boxes:
            confidence = float(box.conf[0])

            # 80% gate
            if confidence < CONFIDENCE_THRESHOLD:
                continue

            # Coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Class name
            cls_id = int(box.cls[0])
            class_name = model.names[cls_id]

            label = f"{class_name}: {confidence * 100:.1f}%"

            # Draw box
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Draw label background
            (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            cv2.rectangle(image, (x1, y1 - th - 10), (x1 + tw + 10, y1), (0, 255, 0), -1)

            # Draw text
            cv2.putText(image, label, (x1 + 5, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

            print(f"  {detected(label)}")
            detected_count += 1

    if detected_count == 0:
        print(warn("No objects detected above 80% confidence"))
    else:
        print(success(f"Total {detected_count} object(s) detected above 80%"))

    # --- Save ---
    os.makedirs(os.path.dirname(output_img), exist_ok=True)
    save_image(image, output_img)

    return image, detected_count