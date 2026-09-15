# 🎯 AI Tech Stack Recommender

A **Content-Based Recommendation System** developed as part of the **DecodeLabs Artificial Intelligence Internship — Batch 2026**.

The system analyzes a user's skills and recommends the most relevant **technology-focused career roles** using **TF-IDF Vectorization** and **Cosine Similarity**.

The project includes an interactive **Streamlit web application** for exploring recommendations, comparing roles, analyzing skill gaps, and viewing dataset insights.

---

## 📌 Project Overview

The objective of this project is to build an intelligent recommendation system that connects a user's existing technical skills with suitable career roles.

Instead of relying on user-to-user behavior or collaborative filtering, the system compares the user's skills with the required skills for available job roles.

The recommendation process follows:

```text
User Skills
     │
     ▼
Text Processing
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Cosine Similarity
     │
     ▼
Similarity Scores
     │
     ▼
Sort by Score
     │
     ▼
Filter Top-N
     │
     ▼
Job Recommendations
```

---

## ✨ Key Features

### 🎯 Recommendation Engine

- Content-Based Filtering
- TF-IDF Vectorization
- Cosine Similarity
- Similarity score calculation
- Ranked Top-N recommendations
- Customizable number of recommendations

### 📊 Analytics & Visualization

- Match-score visualizations
- Interactive Plotly charts
- Recommendation analytics
- Dataset statistics

### 🔍 Search & Exploration

- Job Directory
- Search functionality
- Job filtering
- Job comparison
- Required skill exploration

### 🧠 Skill Analysis

- User skill matching
- Skill Gap Analysis
- Identification of missing skills
- Career-role relevance analysis

### 🛡️ Additional Features

- Cold Start handling
- Trending-role fallback recommendations
- CSV export
- Custom CSS styling
- Interactive Streamlit interface

---

## 🖥️ Application Sections

The Streamlit application provides multiple sections for exploring the recommendation system:

| Section | Purpose |
|---|---|
| 🎯 Recommendations | Displays personalized job recommendations |
| 📋 Job Directory | Browse available technology roles |
| 🔍 Search & Filter | Search and filter job roles |
| 📊 Analytics | Explore recommendation and dataset insights |
| ⚖️ Compare Jobs | Compare different career roles |
| 📊 Dataset Info | View dataset information and statistics |

---

## 📂 Dataset

The system uses a dataset containing **50+ technology-oriented job roles** and their required skills.

The user's skills are compared against the skill requirements of each role to calculate a similarity score.

Higher similarity scores indicate stronger alignment between the user's skills and the selected career role.

---

## 🧮 Recommendation Method

### TF-IDF

**Term Frequency–Inverse Document Frequency (TF-IDF)** converts skill text into numerical vectors.

This allows the system to represent the skills associated with both users and job roles mathematically.

### Cosine Similarity

Cosine Similarity measures the similarity between the user's skill vector and each job-role vector.

The resulting score is used to rank the available roles.

---

## 🔄 Recommendation Pipeline

The core recommendation process consists of four major stages:

### 1. Ingestion

Load the job-role dataset and user skill input.

### 2. Scoring

Convert skill text into TF-IDF vectors and calculate cosine similarity.

### 3. Sorting

Sort job roles by similarity score in descending order.

### 4. Filtering

Select the requested number of highest-ranked recommendations.

---

## 🗂️ Project Structure

```text
Project3_AI-Recommendation-Project/
│
├── .streamlit/
│   └── config.toml
│
├── assets/
│   └── styles.css
│
├── output/
│
├── raw_skills.csv
├── app.py
├── recommender.py
├── requirements.txt
└── README.md
```

### File Description

| File / Folder | Description |
|---|---|
| `app.py` | Streamlit web application |
| `recommender.py` | Recommendation system logic |
| `raw_skills.csv` | Job roles and required skills dataset |
| `assets/styles.css` | Custom application styling |
| `.streamlit/config.toml` | Streamlit configuration |
| `output/` | Generated output files |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## 🛠️ Technologies Used

- Python 3.x
- Streamlit
- Pandas
- Scikit-learn
- Plotly
- TF-IDF
- Cosine Similarity
- Content-Based Filtering
- CSS
- Git & GitHub

---

## ⚙️ Installation & Setup

### 1. Navigate to the Project Directory

```bash
cd Project3_AI-Recommendation-Project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 💻 CLI Version

The recommendation logic can also be executed directly through the command line:

```bash
python recommender.py
```

---

## 📤 Export Recommendations

The application provides an option to export recommendation results as a **CSV file**, making it easy to save and further analyze the generated recommendations.

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Building recommendation systems
- Content-Based Filtering
- TF-IDF Vectorization
- Cosine Similarity
- Similarity-score ranking
- Top-N recommendation logic
- Data processing with Pandas
- Building interactive Streamlit applications
- Interactive visualization with Plotly
- Skill Gap Analysis
- Handling cold-start scenarios
- Designing recommendation pipelines
- Creating user-friendly data applications
- Managing Python dependencies
- Git and GitHub workflow

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