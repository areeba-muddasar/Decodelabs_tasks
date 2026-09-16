# Project 4: Image & Text Recognition

A Python-based computer vision project implementing **OCR (Optical Character Recognition)** and **Object Detection** as part of the **DecodeLabs Artificial Intelligence Internship**.

---

## 🎯 Goal

Build a Python application capable of processing visual data, extracting text from images, and detecting objects using computer vision and deep learning techniques.

---

## ✨ Features

- **OCR** using Tesseract
- **Object Detection** using YOLOv8
- Image preprocessing
- Grayscale conversion
- Gaussian Blur
- Adaptive Thresholding
- Confidence scoring with an 80% threshold
- Colored terminal output using ANSI colors
- Bounding boxes with object labels
- OCR results saved to a text file
- Detection results saved as an annotated image
- Automatic YOLOv8 model download on first run

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.x | Core programming language |
| OpenCV (`cv2`) | Image processing and computer vision |
| pytesseract | Python wrapper for Tesseract OCR |
| Tesseract OCR | Text recognition |
| YOLOv8 | Object detection |
| Ultralytics | YOLOv8 implementation |
| NumPy | Numerical and matrix operations |
| ANSI Colors | Terminal output formatting |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/areeba-muddasar/Decodelabs_tasks.git
cd Decodelabs_tasks/Project4_Image_Text_Recognition
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Tesseract OCR

#### Windows

Install Tesseract OCR and make sure it is available at:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

If required, configure the path in `ocr_module.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

#### macOS

```bash
brew install tesseract
```

#### Linux

```bash
sudo apt install tesseract-ocr
```

---

## ▶️ How to Run

Run the main application:

```bash
python main.py
```

On the first run, the YOLOv8 model may be downloaded automatically.

---

## 📂 Project Structure

```text
Project4_Image_Text_Recognition/
│
├── main.py
├── ocr_module.py
├── detection_module.py
├── preprocess.py
├── colors.py
├── requirements.txt
├── README.md
│
├── sample_images/
│   ├── sample_text.png
│   └── sample_object.jpg
│
└── output/
    ├── ocr_result.txt
    └── detection_result.jpg
```

### File Description

| File / Folder | Description |
|---|---|
| `main.py` | Main entry point for the project |
| `ocr_module.py` | Handles OCR processing |
| `detection_module.py` | Handles YOLOv8 object detection |
| `preprocess.py` | Performs image preprocessing |
| `colors.py` | Handles terminal color formatting |
| `requirements.txt` | Contains project dependencies |
| `sample_images/` | Contains input images |
| `output/` | Stores generated results |
| `README.md` | Project documentation |

---

## 🔍 How It Works

### Path 1: Optical Character Recognition (OCR)

The OCR pipeline processes the image through several stages:

```text
Input Image
     ↓
Grayscale Conversion
     ↓
Gaussian Blur
     ↓
Adaptive Threshold
     ↓
Tesseract OCR
     ↓
Confidence Check
     ↓
Extracted Text
```

### OCR Processing

1. The image is loaded using OpenCV.
2. It is converted to grayscale.
3. Gaussian Blur is applied to reduce noise.
4. Adaptive Thresholding improves text visibility.
5. Tesseract extracts text from the processed image.
6. Recognition confidence is evaluated.
7. The extracted text is saved to `output/ocr_result.txt`.

---

### Path 2: Object Detection

The object detection pipeline uses YOLOv8:

```text
Input Image
     ↓
YOLOv8 Model
     ↓
Object Detection
     ↓
Confidence Filtering
     ↓
Bounding Boxes
     ↓
Annotated Output Image
```

### Object Detection Processing

1. The input image is loaded.
2. YOLOv8 is loaded.
3. The model performs inference.
4. Detections are filtered using the confidence threshold.
5. Bounding boxes and labels are drawn.
6. The annotated image is saved to the `output/` folder.

---

## 📊 Confidence Threshold

The project uses an **80% confidence threshold** for filtering recognition and object detection results.

Results below the configured threshold are excluded from the displayed output.

---

## 🖥️ Sample Output

### OCR Result

**Input:** `sample_images/sample_text.png`

**Recognized Text:**

```text
MACHINE LEARNING IS A BRANCH OF AI
DEEP LEARNING USES NEURAL NETWORKS
PYTHON IS A POPULAR PROGRAMMING LANGUAGE
```

**Confidence:**

```text
[INFO] Average Confidence: 87.45%
[PASS] Confidence >= 80% threshold
[OK] Text saved: output/ocr_result.txt
```

---

### Object Detection Result

**Input:** `sample_images/sample_object.jpg`

**Detections:**

```text
[DETECTED] person: 91.9%
[DETECTED] car: 89.8%
[DETECTED] dog: 88.7%
[PASS] Total 3 object(s) detected above 80%
[OK] Output saved: output/detection_result.jpg
```

---

### Full Terminal Output

```text
##############################################################
          PROJECT 4: BUILDING THE MACHINE'S OPTIC NERVE
##############################################################
  DecodeLabs AI Internship — Batch 2026
##############################################################

=======================================================
  PATH 1: OPTICAL CHARACTER RECOGNITION (OCR)
=======================================================
[OK] Image loaded: sample_images/sample_text.png
[OK] Step 1: Grayscale conversion complete
[OK] Step 2: Gaussian Blur applied (kernel=(5, 5))
[OK] Step 3: Adaptive Threshold applied

--- Recognized Text ---
MACHINE LEARNING IS A BRANCH OF AI
DEEP LEARNING USES NEURAL NETWORKS
PYTHON IS A POPULAR PROGRAMMING LANGUAGE
-------------------------------------------------------
[INFO] Average Confidence: 87.45%
[PASS] Confidence >= 80% threshold
[OK] Text saved: output/ocr_result.txt

=======================================================
  PATH 2: OBJECT DETECTION (YOLOv8)
=======================================================
[OK] Image loaded: sample_images/sample_object.jpg
[OK] YOLOv8 model loading: yolov8n.pt
[OK] YOLOv8 model ready
[OK] Inference complete: 1 result(s)
  [DETECTED] person: 91.9%
  [DETECTED] car: 89.8%
  [DETECTED] dog: 88.7%
[PASS] Total 3 object(s) detected above 80%
[OK] Output saved: output/detection_result.jpg

=======================================================
  PROJECT 4 COMPLETE
=======================================================
  ✓ Library Integration
  ✓ Pre-Processing Integrity
  ✓ Accuracy Benchmark (80% gate)
  ✓ Visual Confirmation (check output/ folder)
=======================================================
```

---

## 📋 Project Validation

| # | Requirement | Status |
|---|---|---|
| 1 | Library Integration — Tesseract + YOLOv8 | ✅ |
| 2 | OCR Implementation | ✅ |
| 3 | Image Preprocessing | ✅ |
| 4 | Confidence Threshold | ✅ |
| 5 | Object Detection | ✅ |
| 6 | Visual Output | ✅ |
| 7 | OCR Result Saved | ✅ |
| 8 | Detection Result Saved | ✅ |

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Computer vision fundamentals
- Image preprocessing
- Optical Character Recognition
- Tesseract OCR integration
- Object detection using YOLOv8
- Pre-trained deep learning models
- Confidence thresholds
- Bounding box visualization
- Image input and output handling
- Python module organization
- Debugging computer vision applications

---

## 🔮 Future Scope

Possible future improvements include:

- Real-time video object detection
- Multi-language OCR support
- Custom YOLOv8 model training
- Real-time camera input
- Streamlit-based web interface
- Mobile or edge-device deployment
- Integration with robotics and automation

This project was developed for educational purposes as part of the **DecodeLabs AI Internship — Batch 2026**.
