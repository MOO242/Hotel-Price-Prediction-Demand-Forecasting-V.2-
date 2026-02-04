# 🏨 Hotel Price Forecasting & Demand V2

**An End-to-End MLOps Pipeline for Predictive Hospitality Analytics

## 🎯 Overview

If V1 was about the *what* (predicting prices), **V2 is about the *how***. This version evolves from simple modeling into a production-grade system designed for scalability, reliability, and 90-day forecasting accuracy.

The core challenge addressed here is bridging the gap between a Jupyter Notebook and a deployed AWS environment, utilizing clean software architecture and robust data engineering.

---

## 🚀 Key Enhancements (V2 vs V1)

| Feature | V1 (Prototype) | V2 (Production) |
| --- | --- | --- |
| **Data Storage** | Local `.csv` files | Hybrid **SQL (Metadata)** & **MongoDB (NoSQL)** |
| **Architecture** | Monolithic script | **Modular Components** (Ingestion, Transformation, Trainer) |
| **Deployment** | Localhost | **AWS (EC2/EKS)** with CI/CD |
| **Observability** | Print statements | **Centralized Logging** & Custom Exception Handling |
| **Forecasting** | Static predictions | **90-Day Rolling Forecast** window |

---

## 🏗️ System Architecture

The pipeline is designed with a "Plug-and-Play" mindset. Each module is independent, allowing for easy updates to the model or data source without breaking the system.

1. **Data Ingestion:** Fetches raw data from SQL/MongoDB and triggers the pipeline.
2. **Data Transformation:** Handles feature engineering, scaling, and handling time-series seasonality.
3. **Model Trainer:** Evaluates multiple algorithms (XGBoost, Prophet, LSTM) and exports the best-performing model.
4. **Model Evaluation:** Uses MLflow/DVC (optional) to track metrics and versioning.
5. **Deployment:** Served via FastAPI and hosted on AWS.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.x
* **Database:** MongoDB (Booking logs), PostgreSQL (Room metadata)
* **Cloud:** AWS (S3 for artifacts, EC2 for hosting)
* **Orchestration:** Docker, GitHub Actions (CI/CD)
* **ML Frameworks:** Scikit-Learn, XGBoost, Statsmodels

---

## 📂 Project Structure

```text
├── src/
│   ├── components/        # Ingestion, Transformation, Model Trainer
│   ├── pipeline/          # Training & Prediction pipelines
│   ├── logger.py          # Centralized logging system
│   └── exception.py       # Custom error handling
├── notebooks/             # Exploratory Data Analysis (EDA)
├── artifacts/             # Stored models and preprocessors
├── app.py                 # FastAPI/Flask entry point
└── setup.py               # Metadata for package installation

```

---

## 🔧 Getting Started

1. **Clone the repo:**

```bash
git clone https://github.com/MOO242/Hotel-Price-Prediction-Demand-Forecasting-V.2.git

```

1. **Install Dependencies:**

```bash
pip install -r requirements.txt

```

1. **Run the Pipeline:**

```bash
python src/pipeline/train_pipeline.py

```

---
