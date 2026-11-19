
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# Step 1: Create manufacturing sensor dataset
data = {
    "Temperature": [72, 95, 81, 102, 76, 88, 69, 97],
    "Vibration": [2.1, 6.8, 3.5, 7.4, 2.8, 5.2, 1.9, 6.5],
    "RPM": [1450, 1520, 1480, 1550, 1460, 1510, 1440, 1530],
    "Pressure": [5.2, 6.1, 5.5, 6.5, 5.3, 5.9, 5.1, 6.2],
    "Failure": [0, 1, 0, 1, 0, 1, 0, 1]
}

# Step 2: Convert dictionary into Pandas DataFrame
df = pd.DataFrame(data)

print("\n===== ORIGINAL DATASET =====")
print(df)

# Step 3: Separate features (X) and target (y)
X = df[["Temperature", "Vibration", "RPM", "Pressure"]]
y = df["Failure"]

# Step 4: Split data using stratified sampling
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Step 5: Display dataset dimensions
print("\n===== DATASET SHAPES =====")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# Step 6: Display training and testing features
print("\n===== TRAINING FEATURES =====")
print(X_train)

print("\n===== TESTING FEATURES =====")
print(X_test)

# Step 7: Display target variable
print("\n===== TARGET VARIABLE =====")
print(y)

# Step 8: Check data types
print("\n===== DATA TYPES =====")
print("Features type:", type(X))
print("Target type:", type(y))

# Step 9: Check class distribution
print("\n===== TRAINING TARGET DISTRIBUTION =====")
print(y_train.value_counts().sort_index())

print("\n===== TESTING TARGET DISTRIBUTION =====")
print(y_test.value_counts().sort_index())

# Step 10: Feature Scaling using StandardScaler

scaler = StandardScaler()

# Learn scaling parameters from training data only
X_train_scaled = scaler.fit_transform(X_train)

# Apply the same scaling to testing data
X_test_scaled = scaler.transform(X_test)

print("\n===== SCALED TRAINING FEATURES =====")
print(X_train_scaled)

print("\n===== SCALED TESTING FEATURES =====")
print(X_test_scaled)


# Step 11: Check for missing values

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== TOTAL MISSING VALUES =====")
print(df.isnull().sum().sum())


# Step 12: Simulate missing sensor readings

import numpy as np

df_missing = df.copy()

# Simulate missing readings
df_missing.loc[2, "Temperature"] = np.nan
df_missing.loc[5, "Vibration"] = np.nan

print("\n===== DATASET WITH MISSING VALUES =====")
print(df_missing)

print("\n===== MISSING VALUES PER COLUMN =====")
print(df_missing.isnull().sum())

# Step 13: Handle missing values using SimpleImputer

# Separate features and target from dataset with missing values
X_missing = df_missing[
    ["Temperature", "Vibration", "RPM", "Pressure"]
]
y_missing = df_missing["Failure"]

# Split before calculating replacement values
X_train_missing, X_test_missing, y_train_missing, y_test_missing = train_test_split(
    X_missing,
    y_missing,
    test_size=0.25,
    random_state=42,
    stratify=y_missing
)

# Create imputer
imputer = SimpleImputer(strategy="mean")

# Learn means from training data and replace missing values
X_train_imputed = imputer.fit_transform(X_train_missing)

# Apply the same means to testing data
X_test_imputed = imputer.transform(X_test_missing)

print("\n===== TRAINING DATA AFTER IMPUTATION =====")
print(pd.DataFrame(
    X_train_imputed,
    columns=X_missing.columns,
    index=X_train_missing.index
))

print("\n===== TESTING DATA AFTER IMPUTATION =====")
print(pd.DataFrame(
    X_test_imputed,
    columns=X_missing.columns,
    index=X_test_missing.index
))

print("\n===== TRAINING FEATURE MEANS =====")
print(pd.Series(imputer.statistics_, index=X_missing.columns))

# Step 14: Combine imputation and scaling into a pipeline

preprocessing_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

# Fit the pipeline on training data only
X_train_processed = preprocessing_pipeline.fit_transform(
    X_train_missing
)

# Apply the same transformations to testing data
X_test_processed = preprocessing_pipeline.transform(
    X_test_missing
)

# Convert processed arrays to DataFrames
train_processed_df = pd.DataFrame(
    X_train_processed,
    columns=X_missing.columns,
    index=X_train_missing.index
)

test_processed_df = pd.DataFrame(
    X_test_processed,
    columns=X_missing.columns,
    index=X_test_missing.index
)

print("\n===== FINAL PROCESSED TRAINING DATA =====")
print(train_processed_df.round(3))

print("\n===== FINAL PROCESSED TESTING DATA =====")
print(test_processed_df.round(3))

print("\n===== MISSING VALUES AFTER PREPROCESSING =====")
print("Training:", train_processed_df.isnull().sum().sum())
print("Testing:", test_processed_df.isnull().sum().sum())

