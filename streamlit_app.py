import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

@st.cache_resource
def load_model():
    with open("random_forest.pkl", "rb") as f:
        obj = pickle.load(f)

    # If pickle contains a dict, extract model
    if isinstance(obj, dict):
        if "model" in obj:
            return obj["model"]
        else:
            st.error(f"Pickle contains a dict with keys: {list(obj.keys())}")
            return None
    return obj

model = load_model()

st.title("🏠 House Price Predictor")
st.write("Enter property details and get a predicted price.")

with st.form("price_form"):
    age = st.number_input("House Age (years)", min_value=0, max_value=120, value=10, step=1)
    distance_MRT = st.number_input("Distance to nearest MRT (meters)", min_value=0.0, max_value=20000.0, value=500.0, step=50.0)
    convenience_stores = st.number_input("Convenience stores (count)", min_value=0, max_value=50, value=5, step=1)
    latitude = st.number_input("Latitude (°)", min_value=-90.0, max_value=90.0, value=25.0, step=0.0001, format="%.6f")
    longitude = st.number_input("Longitude (°)", min_value=-180.0, max_value=180.0, value=121.0, step=0.0001, format="%.6f")
    submitted = st.form_submit_button("Predict")

if submitted:
    # ⚠️ Feature names MUST match training columns
    X = pd.DataFrame([{
        "age": age,
        "distance_MRT": distance_MRT,
        "convenience_stores": convenience_stores,
        "latitude": latitude,
        "longitude": longitude
    }])

    try:
        y_pred = model.predict(X)[0]
        st.success(f"Estimated price: **€{y_pred:,.0f}**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        st.info("Check that feature names and types match exactly what the model was trained on.")
