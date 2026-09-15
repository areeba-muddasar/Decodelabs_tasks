# 🤖 DecodeLabs AI Internship Projects

<<<<<<< HEAD
Welcome to my Artificial Intelligence Internship Projects repository, developed during my AI Internship at DecodeLabs — Batch 2026.

This repository contains three practical projects covering rule-based AI, supervised machine learning, and content-based recommendation systems.
=======
This repository contains the projects completed during my **Artificial Intelligence Internship at DecodeLabs **.

The projects demonstrate practical implementation of **Python programming, rule-based AI, supervised machine learning, data processing, recommendation systems, and model evaluation**.

>>>>>>> 506cb237461f31959aab18e152d297c48acd3144

Each project demonstrates a different aspect of Artificial Intelligence and Machine Learning, from building a conversational chatbot to developing a machine learning classifier and an AI-powered career recommendation system.

# 📌 Projects Overview
#	Project	Main Concepts	Technologies
1	🤖 Rule-Based AI Chatbot	Rule-Based AI, Knowledge Base, Input Processing	Python
2	🌸 Iris Data Classification	Supervised ML, KNN, Data Preprocessing	Python, Scikit-learn
3	🎯 AI Tech Stack Recommender	TF-IDF, Cosine Similarity, Content-Based Filtering	Python, Streamlit, Scikit-learn
🤖 Project 1 — Rule-Based AI Chatbot

A Python-based conversational chatbot that responds to user queries using predefined rules and a dictionary-based knowledge base.

Highlights
Interactive command-line chatbot
Greeting and help commands
AI, Machine Learning, Deep Learning, Python, and Data Science topics
Input sanitization
Name detection and memory
Conversation history
Session statistics
Time and date commands
Multiple variations for similar intents
Fallback responses
Colored terminal interface

📂 Project Folder: Project1_Rule_Based_Chatbot

<<<<<<< HEAD
📖 Documentation: See the project's README.md
=======
* Interactive command-line conversation
* Greeting and help commands
* AI, Machine Learning, Deep Learning, Python, and Data Science topics
* Predefined knowledge base
* Input sanitization and processing
* Name detection and memory
* Conversation history tracking
* Session statistics
* Time and date commands
* Fallback responses for unknown questions
* Exit and goodbye commands
* Colored terminal interface
>>>>>>> 506cb237461f31959aab18e152d297c48acd3144

🌸 Project 2 — Iris Data Classification

A supervised machine learning project using the Iris Dataset to classify flowers into three species using the K-Nearest Neighbors (KNN) algorithm.

Highlights
150 Iris samples
Three target classes
Four input features
Data preprocessing
80/20 train-test split
Feature scaling using StandardScaler
KNN classifier with K = 5
Confusion Matrix
Precision, Recall, and F1 Score
Data visualization

📂 Project Folder: Project2_Data_Classification

📖 Documentation: See the project's README.md

<<<<<<< HEAD
🎯 Project 3 — AI Tech Stack Recommender
=======
### Project 2 — Data Classification Using Machine Learning
>>>>>>> 506cb237461f31959aab18e152d297c48acd3144

A Content-Based Recommendation System that analyzes a user's skills and recommends relevant technology career roles using TF-IDF Vectorization and Cosine Similarity.

<<<<<<< HEAD
The project is presented through an interactive Streamlit web application.
=======
The project demonstrates a complete basic machine learning workflow, including data preparation, feature scaling, model training, prediction, and evaluation.
>>>>>>> 506cb237461f31959aab18e152d297c48acd3144

Highlights
Content-Based Filtering
TF-IDF Vectorization
Cosine Similarity
Similarity-score ranking
Top-N recommendations
Skill Gap Analysis
Job Directory
Search & Filter
Job comparison
Analytics dashboard
Plotly visualizations
Cold Start handling
CSV export
Custom CSS styling
50+ technology-oriented job roles

📂 Project Folder: Project3_AI-Recommendation-Project

📖 Documentation: See the project's README.md

<<<<<<< HEAD
🛠️ Technologies Used
Programming
Python 3.x
Data Science & Machine Learning
Pandas
NumPy
Scikit-learn
K-Nearest Neighbors
StandardScaler
Recommendation Systems
TF-IDF
Cosine Similarity
Content-Based Filtering
Visualization
Matplotlib
Seaborn
Plotly
Application Development
Streamlit
Development & Version Control
Jupyter Notebook
Google Colab
VS Code
Git
GitHub
📂 Repository Structure
=======
```text
Project2_Data_Classification.ipynb
```

#### Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook / Google Colab

---

### Project 3 — AI Recommendation Logic: Tech Stack Recommender

A **Content-Based Recommendation System** that maps a user's skills to the most relevant tech career paths using **TF-IDF Vectorization** and **Cosine Similarity**.

The project implements a complete recommendation pipeline, from user input processing and similarity scoring to ranked Top-N recommendations. The system is presented through an interactive **Streamlit web application**.

#### Key Features

* Content-Based Filtering
* TF-IDF (Term Frequency–Inverse Document Frequency) Vectorization
* Cosine Similarity for recommendation ranking
* Recommendation pipeline:

  * Ingestion
  * Scoring
  * Sorting
  * Filtering
* Interactive Streamlit web application
* Recommendations dashboard
* Job Directory
* Search & Filter functionality
* Analytics dashboard
* Job comparison
* Dataset information
* Customizable Top-N recommendations
* Skill Gap Analysis
* Match-score visualizations using Plotly
* Cold Start handling with trending recommendations
* CSV export of recommendations
* Custom CSS styling
* Dataset containing 50+ job roles and required skills

#### Files

```text
Project3_AI-Recommendation-Project/
│
├── .streamlit/
│   └── config.toml
├── assets/
│   └── styles.css
├── output/
├── raw_skills.csv
├── app.py
├── recommender.py
├── requirements.txt
└── README.md
```

#### Technologies

* Python
* Streamlit
* Pandas
* Scikit-learn
* Plotly
* TF-IDF
* Cosine Similarity
* Content-Based Filtering

#### How to Run

Navigate to the Project 3 directory:

```bash
cd Project3_AI-Recommendation-Project
```

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

The recommendation logic can also be executed through the command line:

```bash
python recommender.py
```

---

## 🛠️ Technologies Used

| Category         | Technologies                            |
| ---------------- | --------------------------------------- |
| Programming      | Python 3.x                              |
| Data Handling    | Pandas, NumPy                           |
| Machine Learning | Scikit-learn                            |
| Visualization    | Matplotlib, Seaborn, Plotly             |
| Web Framework    | Streamlit                               |
| Recommendation   | TF-IDF, Cosine Similarity               |
| Development      | VS Code, Jupyter Notebook, Google Colab |
| Version Control  | Git, GitHub                             |

---

## 📂 Repository Structure

```text
>>>>>>> 506cb237461f31959aab18e152d297c48acd3144
Decodelabs_tasks/
│
├── Project1_Rule_Based_Chatbot/
│   ├── chatbot.py
│   ├── colors.py
│   ├── knowledge_base.py
│   ├── .gitignore
│   └── README.md
│
├── Project2_Data_Classification/
│   ├── Project2_Data_Classification.ipynb
│   └── README.md
│
├── Project3_AI-Recommendation-Project/
│   ├── .streamlit/
│   │   └── config.toml
│   ├── assets/
│   │   └── styles.css
│   ├── output/
│   ├── raw_skills.csv
│   ├── app.py
│   ├── recommender.py
│   ├── requirements.txt
│   └── README.md
│
├── Project3_AI-Recommendation-Project/
│   ├── .streamlit/
│   │   └── config.toml
│   ├── assets/
│   │   └── styles.css
│   ├── output/
│   ├── raw_skills.csv
│   ├── app.py
│   ├── recommender.py
│   ├── requirements.txt
│   └── README.md
│
└── README.md
🎯 Learning Outcomes

These projects provided hands-on experience with:

Python programming
Problem solving and logical thinking
Rule-based AI systems
Knowledge-base design
User input processing
Supervised machine learning
Data preprocessing
Feature scaling
Classification algorithms
Model evaluation
Confusion matrices and evaluation metrics
Recommendation systems
TF-IDF Vectorization
Cosine Similarity
Content-Based Filtering
Similarity-based ranking
Streamlit application development
Interactive data visualization
Git and GitHub
🚀 Project Navigation

Explore each project:

<<<<<<< HEAD
🤖 Project 1 — Rule-Based AI Chatbot
=======
Navigate to the Project 1 directory:
>>>>>>> 506cb237461f31959aab18e152d297c48acd3144

A rule-based conversational AI system built with Python.

🌸 Project 2 — Iris Data Classification

A supervised machine learning classification project using KNN.

<<<<<<< HEAD
🎯 Project 3 — AI Tech Stack Recommender

A content-based career recommendation system using TF-IDF and Cosine Similarity.
=======
---

### Project 2 — Data Classification

Open:

```text
Project2_Data_Classification.ipynb
```

Run the notebook using **Jupyter Notebook** or **Google Colab**.

---

### Project 3 — Tech Stack Recommender

Navigate to the Project 3 directory:

```bash
cd Project3_AI-Recommendation-Project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

Alternatively, run the recommendation system through the CLI:

```bash
python recommender.py
```
>>>>>>> 506cb237461f31959aab18e152d297c48acd3144

👩‍💻 Author

<<<<<<< HEAD
Areeba Muddasar
=======
## 🎯 Learning Outcomes

Through these projects, I gained practical experience in:

* Python programming and problem solving
* Rule-based conversational systems
* Input processing and validation
* Knowledge-base design
* Supervised machine learning
* Data preprocessing
* Feature scaling
* Model training and evaluation
* Classification algorithms
* Confusion matrix and evaluation metrics
* Content-Based Recommendation Systems
* TF-IDF Vectorization
* Cosine Similarity
* Recommendation Pipeline Design
* Streamlit Web Application Development
* Interactive Data Visualization
* Git and GitHub workflow

---

## 👩‍💻 Author

**Areeba Muddasar**
>>>>>>> 506cb237461f31959aab18e152d297c48acd3144

Artificial Intelligence Graduate
FAST-NUCES

GitHub: @areeba-muddasar

🙏 Acknowledgement

I would like to thank DecodeLabs for providing the opportunity to work on practical Artificial Intelligence projects and gain hands-on experience during the AI Internship — Batch 2026.

<<<<<<< HEAD
⭐ DecodeLabs AI Internship — Batch 2026
=======
I would like to thank **DecodeLabs** for providing the opportunity to work on practical Artificial Intelligence projects and gain hands-on experience during the **AI Internship**.
>>>>>>> 506cb237461f31959aab18e152d297c48acd3144
