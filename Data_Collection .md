# Epic 1: Data Collection

## Story 1: Download the Dataset

### Description

The first step of the Credit Card Approval Prediction project is to collect a reliable dataset for training and testing the machine learning model. The dataset contains applicant information such as demographic details, financial status, employment information, credit history, and the final approval status.

The dataset is obtained from Kaggle, which provides high-quality datasets for machine learning and data science projects.

### Dataset Source

**Kaggle – Credit Card Approval Prediction Dataset**

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

### Dataset Information

The dataset contains multiple attributes, including:

- Gender
- Age
- Income Type
- Education Level
- Family Status
- Housing Type
- Employment Days
- Credit History
- Number of Family Members
- Annual Income
- Loan Amount
- Target Variable (Approved / Rejected)

### Steps Performed

1. Visit the Kaggle website.
2. Search for the Credit Card Approval dataset.
3. Download the dataset in CSV format.
4. Store the dataset inside the project's **data/** folder.
5. Verify that the dataset has been downloaded successfully.

### Folder Structure

```
Credit-Card-Approval-Prediction/
│── data/
│   ├── application_record.csv
│   ├── credit_record.csv
│── notebooks/
│── app.py
│── train_model.py
│── README.md
```

### Outcome

The dataset is successfully downloaded and stored for further preprocessing, visualization, feature engineering, and machine learning model development.
