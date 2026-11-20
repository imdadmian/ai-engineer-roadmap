
# Day 05: Machine Learning Classification
# Project: Equipment Failure Prediction

from xml.parsers.expat import model

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


print("Day 05 - Machine Learning Classification")
print("Required libraries imported successfully!")

# Step 2: Create manufacturing sensor dataset

data = {
    "Temperature": [72, 95, 81, 102, 76, 88, 69, 97],
    "Vibration": [2.1, 6.8, 3.5, 7.4, 2.8, 5.2, 1.9, 6.5],
    "RPM": [1450, 1520, 1480, 1550, 1460, 1510, 1440, 1530],
    "Pressure": [5.2, 6.1, 5.5, 6.5, 5.3, 5.9, 5.1, 6.2],
    "Failure": [0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

print("\n===== MANUFACTURING SENSOR DATASET =====")
print(df)

# Separate input features and target variable
X = df[["Temperature", "Vibration", "RPM", "Pressure"]]
y = df["Failure"]

print("\nFeatures shape:", X.shape)
print("Target shape:", y.shape)
# Step 3: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42,stratify=y)
print("\n===== TRAINING AND TESTING DATA =====")
print("Training features:", X_train.shape)
print("Testing features:", X_test.shape)

print("\nTraining class distribution:")
print(y_train.value_counts().sort_index())

print("\nTesting class distribution:")
print(y_test.value_counts().sort_index())
# Step 4: Create and train Logistic Regression model
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(random_state=42))
])
model.fit(X_train, y_train)
print("\nModel training completed successfully!")
# Step 5: Predict equipment failures
# Predict using testing data
y_pred = model.predict(X_test)
# Predict probability of failure
y_probability = model.predict_proba(X_test)
print("\n===== EQUIPMENT FAILURE PREDICTIONS =====")

print("Actual values:", y_test.values)
print("Predicted values:", y_pred)

print("\nFailure probabilities:")
print(y_probability[:, 1])

# Step 6: Evaluate classification model

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)

print("\n===== MODEL EVALUATION =====")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

print("\nConfusion Matrix:")
print(cm)
