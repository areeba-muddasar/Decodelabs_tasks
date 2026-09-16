# 🖼️ Image & Text Recognition

A Python-based **Computer Vision project** developed as part of the **DecodeLabs Artificial Intelligence Internship**.

This project combines **Optical Character Recognition (OCR)** and **Object Detection** to extract text from images and identify objects using image processing techniques and a pretrained **YOLOv8n model**.

---

## 📌 Project Overview

The goal of this project is to build a basic image recognition system capable of performing two main tasks:

1. **Text Recognition** — Extract text from images using OCR.
2. **Object Detection** — Detect and identify objects in images using YOLOv8.

The OCR pipeline uses image preprocessing techniques to improve text extraction, while the object detection pipeline uses the pretrained `yolov8n.pt` model to detect objects and display their bounding boxes with confidence scores.

---

## ✨ Key Features

### 📝 Optical Character Recognition

- Extracts text from images
- Grayscale image conversion
- Gaussian blur
- Adaptive thresholding
- Tesseract OCR integration
- OCR confidence calculation
- Confidence threshold validation
- Saves extracted text to a file

### 🎯 Object Detection

- YOLOv8 object detection
- Uses pretrained `yolov8n.pt` model
- Detects multiple objects in an image
- Confidence-based filtering
- Bounding box visualization
- Object labels and confidence scores
- Saves annotated detection results

### ⚙️ General Features

- Modular Python project structure
- Separate OCR and detection modules
- Image preprocessing module
- Colored terminal output
- Error handling
- Organized output files
- Sample images for testing

---

## 🗂️ Project Structure

```text
Project4_Image_Text_Recognition/
│
├── main.py
├── ocr_module.py
├── detection_module.py
├── preprocess.py
├── colors.py
├── yolov8n.pt
├── requirements.txt
├── Project 4 README.md
│
├── sample_images/
│   ├── sample_text.png
│   └── sample_object.jpg
│
└── output/
    ├── ocr_result.txt
    └── detection_result.jpg
```

---

## 📄 File Description

| File / Folder | Description |
|---|---|
| `main.py` | Main application that runs the OCR and object detection pipelines |
| `ocr_module.py` | Handles text extraction using Tesseract OCR |
| `detection_module.py` | Performs object detection using YOLOv8 |
| `preprocess.py` | Contains image preprocessing functions |
| `colors.py` | Provides terminal color formatting |
| `yolov8n.pt` | Pretrained YOLOv8n model weights |
| `requirements.txt` | Contains required Python dependencies |
| `Project 4 README.md` | Project documentation |
| `sample_images/` | Contains sample images used for testing |
| `output/` | Stores OCR text and object detection results |

---

## 🛠️ Technologies Used

- **Python 3.x**
- **OpenCV**
- **Tesseract OCR**
- **Ultralytics YOLOv8**
- **YOLOv8n**
- **PyTorch**
- **NumPy**
- **Pillow**
- **Image Processing**
- **Object Detection**
- **Optical Character Recognition**
- **Git & GitHub**

---

## 🔄 How It Works

### 📝 OCR Pipeline

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
     ↓
Save Result
```

### 🎯 Object Detection Pipeline

```text
Input Image
     ↓
YOLOv8n Model
     ↓
Object Detection
     ↓
Confidence Filtering
     ↓
Bounding Boxes
     ↓
Annotated Output Image
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/areeba-muddasar/Decodelabs_tasks.git
```

### 2. Navigate to Project 4

```bash
cd Decodelabs_tasks/Project4_Image_Text_Recognition
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔤 Tesseract OCR Setup

This project requires **Tesseract OCR** to perform text recognition.

After installing Tesseract, make sure its executable is correctly configured on your system.

If required, the Tesseract path can be specified in the Python OCR module.

Example:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## ▶️ How to Run

After activating the virtual environment and installing the dependencies:

```bash
python main.py
```

The program processes the sample images and generates OCR and object detection results.

---

## 🖼️ Sample Images

### OCR Sample

The OCR pipeline can process an image containing readable text such as:

```text
MACHINE LEARNING IS A BRANCH OF AI
DEEP LEARNING USES NEURAL NETWORKS
PYTHON IS A POPULAR PROGRAMMING LANGUAGE
```

### Object Detection Sample

The object detection pipeline can process an image containing common objects such as:

- Person
- Car
- Dog
- Bicycle
- Other supported YOLO classes

---

## 📊 Confidence Threshold

The project uses an **80% confidence threshold** for validating OCR and object detection results.

### Example OCR Output

```text
[INFO] Average Confidence: 87.45%
[PASS] Confidence >= 80% threshold
[OK] Text saved: output/ocr_result.txt
```

### Example Object Detection Output

```text
[DETECTED] person: 91.9%
[DETECTED] car: 89.8%
[DETECTED] dog: 88.7%

[PASS] Total 3 object(s) detected above 80%
[OK] Output saved: output/detection_result.jpg
```

---

## 🖥️ Full Terminal Output

```text
============================================================
       PROJECT 4: IMAGE & TEXT RECOGNITION
       DecodeLabs - Batch 2026
============================================================

[INFO] Loading sample image...
[INFO] Starting image preprocessing...

[OCR] Extracting text...

------------------------------------------------------------
OCR RESULT
------------------------------------------------------------

MACHINE LEARNING IS A BRANCH OF AI
DEEP LEARNING USES NEURAL NETWORKS
PYTHON IS A POPULAR PROGRAMMING LANGUAGE

------------------------------------------------------------
[INFO] Average Confidence: 87.45%
[PASS] Confidence >= 80% threshold
[OK] Text saved: output/ocr_result.txt

============================================================
OBJECT DETECTION
============================================================

[INFO] Loading YOLOv8n model...
[INFO] Model: yolov8n.pt

[DETECTED] person: 91.9%
[DETECTED] car: 89.8%
[DETECTED] dog: 88.7%

[PASS] Total 3 object(s) detected above 80%
[OK] Output saved: output/detection_result.jpg

============================================================
PROCESSING COMPLETED SUCCESSFULLY
============================================================
```

---

## 📁 Output Files

### OCR Result

The extracted text is saved in:

```text
output/ocr_result.txt
```

### Object Detection Result

The annotated image with bounding boxes is saved in:

```text
output/detection_result.jpg
```

---

## ✅ Project Validation

| Component | Status |
|---|---|
| Image Loading | ✅ Completed |
| Image Preprocessing | ✅ Completed |
| OCR Text Extraction | ✅ Completed |
| OCR Confidence Check | ✅ Completed |
| YOLOv8 Model Loading | ✅ Completed |
| Object Detection | ✅ Completed |
| Confidence Filtering | ✅ Completed |
| Bounding Box Visualization | ✅ Completed |
| Output File Generation | ✅ Completed |

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Computer vision fundamentals
- Image preprocessing
- Grayscale conversion
- Gaussian blurring
- Adaptive thresholding
- Optical Character Recognition
- Tesseract OCR
- OCR confidence evaluation
- Object detection
- YOLOv8
- Using pretrained deep learning models
- Confidence-based filtering
- Bounding box visualization
- Modular Python programming
- File and output management
- Git and GitHub

---

## 🚀 Future Scope

The project can be further extended with:

- Real-time webcam object detection
- Video-based object detection
- Advanced OCR preprocessing
- Handwritten text recognition
- Multiple language OCR support
- Custom YOLO model training
- Web-based interface using Streamlit
- Real-time text and object recognition
