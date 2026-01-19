import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data/raw/Telco-Customer-Churn.csv")
PROCESSED_PATH = os.path.join(BASE_DIR, "data/processed/churn_processed.csv")

# Load data
df = pd.read_csv(DATA_PATH)

# Drop customerID as it is not useful
if 'customerID' in df.columns:
    df.drop('customerID', axis=1, inplace=True)

# Convert 'TotalCharges' to numeric, coerce errors (empty strings → NaN)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

# Encode categorical columns
cat_cols = df.select_dtypes(include='object').columns
le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# Save processed data
os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
df.to_csv(PROCESSED_PATH, index=False)
print("✅ Preprocessing complete. Processed data saved to:", PROCESSED_PATH)
