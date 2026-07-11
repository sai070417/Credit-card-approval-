# ============================================
# Credit Card Approval Prediction
# Decision Tree Model
# ============================================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Load Dataset
df = pd.read_csv("data/encoded_dataset.csv")

# Features and Target
X = df.drop("TARGET", axis=1)
y = df["TARGET"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Decision Tree Model
dt_model = DecisionTreeClassifier(
    criterion="gini",
    random_state=42
)

# Train Model
dt_model.fit(X_train, y_train)

# Make Predictions
y_pred = dt_model.predict(X_test)

# Evaluate Model
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# Save Model
joblib.dump(dt_model, "model/decision_tree.pkl")

print("\nDecision Tree Model Saved Successfully!")
