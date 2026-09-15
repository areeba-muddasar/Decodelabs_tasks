# 🤖 DecodeLabs AI Internship Projects

This repository contains the projects completed during my **Artificial Intelligence Internship at DecodeLabs **.

The projects demonstrate practical implementation of **Python programming, rule-based AI, supervised machine learning, data processing, recommendation systems, and model evaluation**.

---

## 📌 Projects

### Project 1 — Rule-Based AI Chatbot

A Python-based conversational chatbot that uses predefined rules and a dictionary-based knowledge base to respond to user queries.

#### Key Features

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

#### Files

```text
Project1_Rule_Based_Chatbot/
│
├── chatbot.py
├── colors.py
├── knowledge_base.py
└── .gitignore
```

#### Technologies

* Python
* Regular Expressions
* Dictionaries
* Functions
* Conditional Logic
* Git & GitHub

---

### Project 2 — Data Classification Using Machine Learning

A supervised machine learning project using the **Iris Dataset** to classify flowers into three different species based on their measurements.

The project demonstrates a complete basic machine learning workflow, including data preparation, feature scaling, model training, prediction, and evaluation.

#### Key Features

* Iris Dataset with 150 samples
* Three target classes
* Four input features
* Data preprocessing
* Feature scaling using `StandardScaler`
* 80/20 train-test split
* K-Nearest Neighbors (KNN) classifier
* K = 5
* Confusion Matrix
* Precision, Recall, and F1 Score
* Model evaluation

#### File

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
Decodelabs_tasks/
│
├── Project1_Rule_Based_Chatbot/
│   ├── chatbot.py
│   ├── colors.py
│   ├── knowledge_base.py
│   └── .gitignore
│
├── Project2_Data_Classification.ipynb
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
```

---

## 🚀 How to Run

### Project 1 — Rule-Based AI Chatbot

Navigate to the Project 1 directory:

```bash
cd Project1_Rule_Based_Chatbot
```

Run the chatbot:

```bash
python chatbot.py
```

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

---

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

Artificial Intelligence Graduate
FAST-NUCES

GitHub: [@areeba-muddasar](https://github.com/areeba-muddasar)

---

## 🙏 Acknowledgement

I would like to thank **DecodeLabs** for providing the opportunity to work on practical Artificial Intelligence projects and gain hands-on experience during the **AI Internship**.
