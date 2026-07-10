# Project Flow

## Description

The Credit Card Approval Prediction project follows a structured machine learning workflow to determine whether a credit card application should be approved or rejected. The workflow includes data collection, exploratory data analysis, preprocessing, model training, evaluation, and deployment.

---

## Epic 1: Data Collection

### Story 1
Collect the credit card application dataset from a reliable source such as Kaggle or the UCI Machine Learning Repository.

### Story 2
Load the dataset using the Pandas library and verify its structure, size, and data types.

---

## Epic 2: Visualizing and Analysing the Data

### Story 1
Import the required Python libraries for data analysis and visualization.

### Story 2
Explore the dataset to understand its features, target variable, and distribution.

### Story 3
Perform univariate analysis using histograms and count plots.

### Story 4
Perform multivariate analysis using correlation heatmaps, pair plots, and box plots.

### Story 5
Summarize the important insights obtained from the exploratory data analysis.

---

## Epic 3: Data Pre-processing

### Story 1
Remove duplicate records from the dataset.

### Story 2
Handle missing values using suitable techniques.

### Story 3
Encode categorical variables into numerical values.

### Story 4
Scale numerical features using StandardScaler or MinMaxScaler.

### Story 5
Split the dataset into training and testing sets.

---

## Epic 4: Model Building

### Story 1
Train a Logistic Regression model.

### Story 2
Train a Decision Tree Classifier.

### Story 3
Train a Random Forest Classifier.

### Story 4
Compare model performance using Accuracy, Precision, Recall, F1-Score, and ROC-AUC, then select the best-performing model.

---

## Epic 5: Application Building

### Story 1
Design a simple and user-friendly web interface using Flask.

### Story 2
Integrate the trained machine learning model into the application.

### Story 3
Test the application using sample applicant data and verify the prediction results.

---

## Final Outcome

The completed system predicts whether a credit card application is approved or rejected based on applicant information. The trained model is deployed through a web application, allowing users to enter applicant details and receive instant approval predictions.
