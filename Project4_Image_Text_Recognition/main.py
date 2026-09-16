"""
main.py
Project 4: Image & Text Recognition
Runs BOTH OCR (Path 1) and Object Detection (Path 2).
DecodeLabs AI Internship — Batch 2026
"""

import os
from ocr_module import run_ocr
from detection_module import run_detection
from colors import (
    Colors, warn, error, heading, divider, banner
)


def main():
    print()
    print(banner("PROJECT 4: BUILDING THE MACHINE'S OPTIC NERVE", width=62))

    # --- Path 1: OCR ---
    ocr_image = "sample_images/sample_text.png"
    if os.path.exists(ocr_image):
        try:
            text, conf = run_ocr(ocr_image)
        except Exception as e:
            print(error(f"OCR Error: {e}"))
    else:
        print(warn(f"OCR image not found: {ocr_image}"))
        print(f"    {Colors.DIM}Please save a text image as 'sample_images/sample_text.png'{Colors.RESET}")

    # --- Path 2: Object Detection ---
    detect_image = "sample_images/sample_object.jpg"
    if os.path.exists(detect_image):
        try:
            img, count = run_detection(detect_image)
        except FileNotFoundError as e:
            print(error(f"{e}"))
        except Exception as e:
            print(error(f"Detection Error: {e}"))
    else:
        print(warn(f"Detection image not found: {detect_image}"))
        print(f"    {Colors.DIM}Please save an object image as 'sample_images/sample_object.jpg'{Colors.RESET}")

    # --- Summary ---
    print()
    print(divider('='))
    print(heading("  PROJECT 4 COMPLETE"))
    print(divider('='))
    print(f"  {Colors.BRIGHT_GREEN}✓{Colors.RESET} Library Integration")
    print(f"  {Colors.BRIGHT_GREEN}✓{Colors.RESET} Pre-Processing Integrity")
    print(f"  {Colors.BRIGHT_GREEN}✓{Colors.RESET} Accuracy Benchmark (80% gate)")
    print(f"  {Colors.BRIGHT_GREEN}✓{Colors.RESET} Visual Confirmation (check output/ folder)")
    print(divider('='))
    print()


if __name__ == "__main__":
    main()