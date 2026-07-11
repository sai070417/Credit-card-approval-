# ============================================
# Credit Card Approval Prediction
# Importing Required Libraries
# ============================================

# Data Manipulation
import pandas as pd
import numpy as np

# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer

# Classification Models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Model Evaluation
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# Save and Load Model
import joblib

# Ignore Warnings
import warnings
warnings.filterwarnings("ignore")

print("All required libraries imported successfully!")
# Importing the Libraries

Importing the required Python libraries is the first step in the Credit Card Approval Prediction project. These libraries provide functions for data loading, preprocessing, visualization, machine learning model training, evaluation, and model saving.

## Libraries Used
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

These libraries help perform the complete machine learning workflow efficiently.
