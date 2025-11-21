import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

print("Loading dataset...")

# ⬇⬇ CHANGE THIS PATH BASED ON YOUR FILE NAME ⬇⬇
df = pd.read_csv(r"F:\Digizura\Python1\Used_Car_Price_Prediction.csv")

print("Dataset loaded successfully!\n")

print("Columns in dataset:")
print(df.columns)

# -----------------------------
# 1. CLEAN DATA
# -----------------------------
print("\nCleaning data...")

# Remove rows with missing values
df = df.dropna()

# Convert numeric columns
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="ignore")

# Select only numeric columns because Linear Regression cannot use strings
numeric_df = df.select_dtypes(include=['int64', 'float64'])

print("\nNumeric Columns:")
print(numeric_df.columns)

# Ensure target column exists
target_column = "sale_price"
  # change if different

if target_column not in numeric_df.columns:
    raise Exception(f"'{target_column}' column not found. Check column names!")

# -----------------------------
# 2. SPLIT FEATURES + TARGET
# -----------------------------
X = numeric_df.drop(columns=[target_column])
y = numeric_df[target_column]

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 3. TRAIN MODEL
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# 4. EVALUATE MODEL
# -----------------------------
y_pred = model.predict(X_test)
accuracy = r2_score(y_test, y_pred)

print(f"\nModel Accuracy (R² Score): {accuracy}")

# -----------------------------
# 5. PREDICT NEW VALUES
# -----------------------------
print("\nEnter values to predict car price:")
input_data = {}

for col in X.columns:
    value = float(input(f"{col}: "))
    input_data[col] = value

input_df = pd.DataFrame([input_data])
prediction = model.predict(input_df)[0]

print(f"\nPredicted Selling Price: ₹ {prediction:.2f}")
