# 🏠 House Price Prediction App

A machine learning web app built with **Streamlit** that predicts house prices based on features such as **house age, distance to MRT station, number of convenience stores, latitude, and longitude**.

🚀 **Live Demo**: [Streamlit Cloud App]([https://housepriceapp-b7bqjgcv3jqe4tpbab3f6t.streamlit.app/])

---

## 📌 Project Overview
This project demonstrates how to:
- Train a **Random Forest Regression** model on a housing dataset.
- Save and load the model using **Pickle**.
- Build an interactive **Streamlit app** for predictions.
- Deploy the app to **Streamlit Community Cloud**.

It is a complete end-to-end ML workflow: **data → model → deployment**.

---

## ⚙️ Features
- User-friendly web interface.
- Input fields:
  - House Age (years)
  - Distance to nearest MRT (meters)
  - Number of convenience stores nearby
  - Latitude & Longitude
- Real-time prediction of house price.
- Deployed and accessible via a public URL.

---

## 🛠️ Tech Stack
- **Python 3.9**
- **Pandas** – data manipulation
- **Scikit-learn** – machine learning (Random Forest Regressor)
- **Pickle** – model persistence
- **Streamlit** – app framework & deployment

## 📂 Project Structure

House_Price_App/
│
├── streamlit_app.py # Streamlit app code
├── random_forest.pkl # Trained ML model
├── requirements.txt # Dependencies
├── runtime.txt # Python version pin (for Streamlit Cloud)
└── README.md # Project documentation

## 📂 Project Structure
