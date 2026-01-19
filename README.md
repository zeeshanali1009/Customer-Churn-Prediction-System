# 📉 Customer Churn Prediction System

*(End-to-End Machine Learning Project)*

---

## 🎯 Client Problem Statement (Real-World Scenario)

**Client says:**

> “We are a telecom company. Customers are leaving our service.
> We want an ML system that predicts whether a customer will churn or not, so we can take action before losing them.”

**Business Goal:**
Build a machine learning solution that can **predict customer churn in advance**, enabling proactive retention strategies and reducing revenue loss.

---

## 📌 Project Overview

The **Customer Churn Prediction System** is an end-to-end machine learning application designed to predict whether a customer is likely to **churn (leave)** or **remain loyal** to a telecom service.

By analyzing customer demographics, service usage, contract details, and billing information, the system helps businesses:

* Identify high-risk customers
* Take preventive retention actions
* Improve customer lifetime value (CLV)
* Reduce operational and marketing costs

The project simulates a **real enterprise use-case** and covers the full ML lifecycle — from data preprocessing to deployment via a web application.

---

## 📊 Dataset Description

**Dataset:** Telco Customer Churn Dataset
**Source:** Publicly available (e.g., Kaggle) / Enterprise-style telecom data

### Key Feature Groups

**Customer Demographics**

* Gender
* SeniorCitizen
* Partner
* Dependents

**Account & Contract Information**

* Tenure
* Contract type
* PaperlessBilling
* PaymentMethod

**Subscribed Services**

* PhoneService
* InternetService
* OnlineSecurity
* StreamingTV
* TechSupport, etc.

**Financial Information**

* MonthlyCharges
* TotalCharges

**Target Variable**

* `Churn` (Yes / No)

**Dataset Size**

* ~7,043 customer records (after preprocessing)

---

## 🧠 Approach & Methodology

### 1️⃣ Exploratory Data Analysis (EDA)

* Analyzed feature distributions and churn patterns
* Identified missing values and data inconsistencies
* Studied churn behavior across different customer segments
* Checked class imbalance in the target variable

### 2️⃣ Data Preprocessing

* Handled missing values in `TotalCharges`
* Encoded categorical variables using:

  * Label Encoding
  * One-Hot Encoding
* Scaled numerical features where required
* Ensured consistent feature alignment for training and inference

### 3️⃣ Model Training

* Split dataset into **80% training** and **20% testing**
* Trained a **Random Forest Classifier** due to:

  * Robust performance
  * Ability to handle mixed feature types
  * Resistance to overfitting
* Evaluated model using:

  * Accuracy
  * Precision
  * Recall
  * F1-Score
  * ROC-AUC

### 4️⃣ Model Persistence

* Saved trained model and preprocessing objects using `joblib`
* Ensured reproducibility and reuse without retraining

### 5️⃣ Deployment

* Built an interactive **Streamlit web application**
* Users can input customer details
* App predicts:

  * Churn probability
  * Final churn decision (Yes / No)

---

## 📈 Key Results

* ✔ Model achieved **~82% accuracy** on test data
* ✔ Provides churn probability for better business interpretation
* ✔ Handles diverse customer profiles effectively
* ✔ Produces real-time predictions via web interface

---

## 🛠️ Tech Stack

**Programming Language**

* Python

**Libraries**

* NumPy
* Pandas
* Scikit-Learn
* Joblib
* Streamlit

**Tools & Platforms**

* Jupyter Notebook
* VS Code
* Docker
* GitHub Actions (CI)
* Streamlit Cloud

---

## 💼 Real-World Business Use Cases

* Telecom companies
* Subscription-based businesses
* SaaS platforms
* Customer retention and loyalty teams
* CRM and marketing analytics systems

---

## 🌟 Why This Project Matters (Freelance Perspective)

This project demonstrates:

* ✔ End-to-end ML pipeline development
* ✔ Real business problem solving
* ✔ Classification modeling expertise
* ✔ Deployment and production readiness
* ✔ CI/CD and Dockerization skills

**Perfect proof for freelance clients:**

> “I can build, train, deploy, and automate ML solutions for real businesses.”

---

## ✅ Project Status

* ✔ Model Trained
* ✔ Tested
* ✔ Dockerized
* ✔ CI Pipeline Added
* ✔ Deployed

## 🌐 Live Demo

🚀 **Deployed Streamlit App:**
👉 [https://customer-churn-prediction-system-oqrbwjvnxmir6ufpdlvc9c.streamlit.app/](https://customer-churn-prediction-system-oqrbwjvnxmir6ufpdlvc9c.streamlit.app/)


