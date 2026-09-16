"""
preprocess.py
Common image pre-processing functions for OCR and Object Detection.
Project 4: Image & Text Recognition — DecodeLabs AI Internship
"""

import cv2
from colors import ok


def load_image(path):
    """Load image and handle errors."""
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {path}")
    print(ok(f"Image loaded: {path} | Shape: {image.shape}"))
    return image


def to_grayscale(image):
    """Step 1: Convert RGB to grayscale."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(ok("Step 1: Grayscale conversion complete"))
    return gray


def apply_gaussian_blur(gray, kernel=(5, 5)):
    """Step 2: Apply Gaussian Blur to remove noise."""
    blurred = cv2.GaussianBlur(gray, kernel, 0)
    print(ok(f"Step 2: Gaussian Blur applied (kernel={kernel})"))
    return blurred


def apply_adaptive_threshold(blurred):
    """Step 3: Apply Adaptive Threshold (binary decision)."""
    threshold = cv2.adaptiveThreshold(
        blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 25, 10
    )
    print(ok("Step 3: Adaptive Threshold applied"))
    return threshold


def save_image(image, path):
    """Save result image."""
    cv2.imwrite(path, image)
    print(ok(f"Output saved: {path}"))