# 🌸 Iris Flower Classification Using Machine Learning

A supervised machine learning project developed as part of the **DecodeLabs Artificial Intelligence Internship — Batch 2026**.

The project uses the classic **Iris Dataset** and a **K-Nearest Neighbors (KNN)** classifier to predict the species of an iris flower based on its physical measurements.

---

## 📌 Project Overview

The objective of this project is to implement a complete basic machine learning classification workflow.

The model learns from measurements of iris flowers and classifies them into one of three species:

- Iris Setosa
- Iris Versicolor
- Iris Virginica

The workflow includes data preprocessing, feature scaling, train-test splitting, model training, prediction, and evaluation.

---

## 📊 Dataset

The project uses the **Iris Dataset**, containing:

| Attribute | Details |
|---|---|
| Total Samples | 150 |
| Number of Classes | 3 |
| Input Features | 4 |
| Classification Type | Multi-class |
| Algorithm | K-Nearest Neighbors |

### Input Features

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

### Target Classes

- Setosa
- Versicolor
- Virginica

---

## 🔄 Machine Learning Workflow

```text
Iris Dataset
     │
     ▼
Data Preparation
     │
     ▼
Feature Selection
     │
     ▼
Train-Test Split
     │
     ▼
Feature Scaling
(StandardScaler)
     │
     ▼
KNN Model Training
     │
     ▼
Predictions
     │
     ▼
Model Evaluation
```

---

## ✨ Key Features

- Iris dataset exploration
- Data preprocessing
- Feature and target separation
- 80/20 train-test split
- Feature scaling using `StandardScaler`
- K-Nearest Neighbors classification
- K = 5
- Model prediction
- Confusion Matrix
- Precision
- Recall
- F1 Score
- Classification performance analysis
- Data visualization

---

## 🗂️ Project Structure

```text
Project2_Data_Classification/
│
├── Project2_Data_Classification.ipynb
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook
- Google Colab

---

## ⚙️ How to Run

### Option 1 — Google Colab

Open:

```text
Project2_Data_Classification.ipynb
```

in Google Colab and run the notebook cells sequentially.

### Option 2 — Jupyter Notebook

Install the required libraries:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Then open:

```text
Project2_Data_Classification.ipynb
```

Run the cells sequentially to reproduce the analysis and model evaluation.

---

## 📈 Model Evaluation

The model is evaluated using:

### Confusion Matrix

Used to visualize correct and incorrect predictions across the three iris classes.

### Precision

Measures how many predicted instances of a class are actually correct.

### Recall

Measures how many actual instances of a class are correctly identified.

### F1 Score

Provides a combined measure of precision and recall.

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Understanding supervised machine learning
- Working with structured datasets
- Data preprocessing
- Feature scaling
- Train-test splitting
- KNN classification
- Model prediction
- Confusion matrix analysis
- Classification metrics
- Data visualization
- Using Scikit-learn for machine learning workflows
- Working with Jupyter Notebook and Google Colab

---

## 👩‍💻 Author

**Areeba Muddasar**  
Artificial Intelligence Graduate — FAST-NUCES

---

## 🏢 Internship

**DecodeLabs — Artificial Intelligence Internship**  
**Batch 2026**

---

⭐ Developed as part of my practical AI internship project work at DecodeLabs.