"""
ocr_module.py
Path 1: Optical Character Recognition using pytesseract.
Project 4: Image & Text Recognition — DecodeLabs AI Internship
"""

import os
import platform
import pytesseract
from preprocess import (
    load_image, to_grayscale, apply_gaussian_blur,
    apply_adaptive_threshold
)
from colors import (
    Colors, ok, info, warn, success, heading, divider
)

# =========================================================
# WINDOWS USERS: Set the Tesseract path directly
# If your Tesseract is in a different folder, change this path.
# =========================================================
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def run_ocr(image_path, output_txt="output/ocr_result.txt"):
    """
    OCR pipeline:
    1. Load image
    2. Grayscale
    3. Gaussian Blur
    4. Adaptive Threshold
    5. Tesseract OCR (PSM 4 for best results)
    6. Confidence check (80% gate)
    """
    print()
    print(divider('='))
    print(heading("  PATH 1: OPTICAL CHARACTER RECOGNITION (OCR)"))
    print(divider('='))

    # --- Pre-processing ---
    image = load_image(image_path)
    gray = to_grayscale(image)
    blurred = apply_gaussian_blur(gray)
    threshold = apply_adaptive_threshold(blurred)

    # --- OCR ---
    # PSM 4 = Single column of text of variable sizes (best for Notepad images)
    config = '--psm 4'
    text = pytesseract.image_to_string(threshold, config=config)

    print()
    print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}--- Recognized Text ---{Colors.RESET}")
    if text.strip():
        print(f"{Colors.WHITE}{text.strip()}{Colors.RESET}")
    else:
        print(warn("No text found"))
    print(divider('-'))

    # --- Confidence Check (80% rule) ---
    data = pytesseract.image_to_data(threshold, output_type=pytesseract.Output.DICT)
    confidences = [int(c) for c in data['conf'] if c != '-1']

    avg_conf = 0.0
    if confidences:
        avg_conf = sum(confidences) / len(confidences)

        # Color based on confidence
        if avg_conf >= 80:
            conf_color = Colors.BRIGHT_GREEN
        elif avg_conf >= 60:
            conf_color = Colors.BRIGHT_YELLOW
        else:
            conf_color = Colors.BRIGHT_RED

        print(info(f"Average Confidence: {conf_color}{Colors.BOLD}{avg_conf:.2f}%{Colors.RESET}"))

        if avg_conf >= 80:
            print(success("Confidence >= 80% threshold"))
        else:
            print(warn("Confidence below 80% — please check image quality"))
    else:
        print(warn("No confidence data found"))

    # --- Save output ---
    os.makedirs(os.path.dirname(output_txt), exist_ok=True)
    with open(output_txt, 'w', encoding='utf-8') as f:
        f.write(text)
    print(ok(f"Text saved: {output_txt}"))

    return text, avg_conf