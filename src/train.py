import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_PATH = os.path.join(BASE_DIR, "data/processed/churn_processed.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models/churn_model.joblib")
FEATURE_PATH = os.path.join(BASE_DIR, "models/feature_names.joblib")

# Load processed data
df = pd.read_csv(PROCESSED_PATH)

# Features & target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and feature names
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
joblib.dump(model, MODEL_PATH)
joblib.dump(list(X.columns), FEATURE_PATH)

print("✅ Model trained and saved to:", MODEL_PATH)
print("✅ Feature names saved to:", FEATURE_PATH)
