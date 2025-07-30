
# 🎓 Student Performance Prediction System

Welcome to the **Student Performance Prediction System**, a machine learning–based project that combines basic student record management with a predictive analytics pipeline. This system helps in identifying students who are likely to pass or fail based on their academic data.

---

## 📌 Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [How It Works](#how-it-works)
* [EDA & Model Tracking](#eda--model-tracking)
* [CI/CD & Versioning](#cicd--versioning)
* [Key Benefits](#key-benefits)
* [Getting Started](#getting-started)

---

## 📘 Project Overview

This project integrates a basic **Student Management System** with a **Machine Learning pipeline** to predict student performance using classification algorithms. It also demonstrates a complete **MLOps workflow** with CI/CD automation, experiment tracking, and model versioning.

The system is built using **Python**, **MLflow**, **DAGsHub**, and a **CI/CD pipeline** that includes **GitVersion** for version control.

---

## ✅ Features

* 📊 Perform exploratory data analysis (EDA)
* 🧠 Predict student performance (Pass/Fail) using ML models
* 📦 Track experiments and model versions using MLflow
* 🔄 Automate pipelines with GitVersion and CI/CD tools
* 📈 Visualize metrics and artifacts using DAGsHub

---

## 🧑‍💻 Tech Stack

| Component               | Tool/Library                                 |
| ----------------------- | -------------------------------------------- |
| Programming             | Python, Jupyter Notebook                     |
| Data Analysis           | Pandas, Matplotlib, Seaborn                  |
| ML Models               | Scikit-learn (Random Forest, SVM, KNN, etc.) |
| Experiment Tracking     | MLflow                                       |
| Data & Model Versioning | DAGsHub                                      |
| CI/CD                   | GitHub Actions / Jenkins                     |
| Version Control         | Git + GitVersion                             |

---

## ⚙️ How It Works

1. **Data Ingestion & Cleaning**
   Load and preprocess the student data.

2. **EDA (Exploratory Data Analysis)**
   Visualize distributions, correlation matrices, and feature relationships.

3. **Model Training**
   Train ML models to classify whether a student will pass or fail based on features.

4. **MLflow Logging**
   Track experiments (params, metrics, models) for easy comparison and reproducibility.

5. **Version Control with GitVersion**
   Auto-generate semantic versions on each commit to tag code and models.

6. **CI/CD Integration**
   Use GitHub Actions to automate testing, model training, and artifact storage.

7. **Prediction & Analysis**
   Predict new student outcomes using the best-trained model and update records accordingly.

---

## 📊 EDA & Model Tracking

* Conducted detailed EDA to understand feature relationships and class balance.

* Used **MLflow** for:

  * Logging hyperparameters, metrics (Accuracy, Recall, Precision)
  * Managing model artifacts and versions
  * Comparing experiments visually via MLflow UI

* Integrated with **DAGsHub** for:

  * Visual version tracking of datasets, code, and models
  * Real-time visualization of MLflow experiment results
  * Seamless collaboration and reproducibility

---

## 🔄 CI/CD & Versioning

* Implemented **CI/CD pipelines** to:

  * Automate ML model training and testing
  * Push changes to DAGsHub with traceable versions
  * Track builds with **GitVersion** to handle semantic versioning

This ensures clean, automated, and reproducible model development across all stages.

---

## 🚀 Key Benefits

* Early identification of students at risk of failing
* Real-time, reproducible experiment tracking with MLflow
* Collaborative version control using Git + DAGsHub
* Automated model lifecycle management via CI/CD pipeline

---

## 🧭 Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/Utkarshso/Student-Management-System.git
   cd Student-Management-System
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Launch the Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

4. To run ML pipeline and track experiments:

   * Run notebooks/scripts under `notebooks/` or `src/`
   * Check MLflow UI locally or connect to DAGsHub for remote tracking

