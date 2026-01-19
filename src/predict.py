import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models/churn_model.joblib")
FEATURE_PATH = os.path.join(BASE_DIR, "models/feature_names.joblib")

# Load trained model and feature names
model = joblib.load(MODEL_PATH)
feature_names = joblib.load(FEATURE_PATH)

def predict_churn(input_dict):
    # Create dataframe
    df = pd.DataFrame([input_dict])

    # Ensure all features exist
    for col in feature_names:
        if col not in df.columns:
            df[col] = 0  # default value if missing

    df = df[feature_names]

    # Predict
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return prediction, probability
