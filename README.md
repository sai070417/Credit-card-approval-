
Credit Card Approval Prediction Using Machine Learning

Project Overview

The Credit Card Approval Prediction project is a Machine Learning-based application developed to predict credit card approval based on applicant information and credit history.

Credit card approval is an important process for financial institutions and banks. Traditionally, applications are evaluated manually by considering various factors such as applicant income, employment status, family information, property ownership, previous credit records, and other financial details.

The main objective of this project is to use Machine Learning algorithms to analyze applicant and credit data and build a predictive model that can assist in determining credit card approval.

The project includes the complete Machine Learning workflow, starting from downloading and understanding the dataset to data preprocessing, exploratory data analysis, model training, model evaluation, and deployment of the final model using a Flask web application.


---

Project Objectives

The major objectives of this project are:

To collect and analyze credit card applicant data.

To understand the structure and characteristics of the dataset.

To perform Exploratory Data Analysis (EDA).

To identify and handle missing values.

To remove duplicate records.

To clean and preprocess the dataset.

To perform feature engineering.

To convert categorical features into numerical values.

To merge application and credit history datasets.

To split the processed data into training and testing datasets.

To train multiple Machine Learning classification models.

To evaluate and compare the performance of different models.

To select and save the best-performing Machine Learning model.

To create a user-friendly web application using Flask.

To allow users to enter applicant information and receive a credit card approval prediction.



---

Dataset Description

The project uses the Credit Card Approval Prediction Dataset.

The dataset contains two CSV files:

1. application_record.csv

This dataset contains information about credit card applicants.

Some of the important features include:

Applicant ID

Gender

Car ownership

Property ownership

Number of children

Annual income

Income type

Education level

Family status

Housing type

Date of birth

Employment information

Mobile phone availability

Work phone availability

Phone availability

Email availability

Occupation type

Number of family members


2. credit_record.csv

This dataset contains the previous credit history of applicants.

Some important features include:

Applicant ID

Month balance

Credit status


The two datasets are processed and merged using the common applicant ID column.


---

Project Workflow

The complete project is divided into five major Epics.

Epic 1: Dataset Collection

The first stage of the project involves obtaining the required Credit Card Approval Prediction dataset.

The dataset is downloaded and extracted into the Google Colab environment.

After extraction, the following two files are used:

application_record.csv

credit_record.csv


These datasets are then loaded into the project for further analysis and processing.


---

Epic 2: Exploratory Data Analysis

The second stage of the project focuses on understanding and analyzing the dataset.

Importing Libraries

The required Python libraries are imported, including:

Pandas

NumPy

Matplotlib

Scikit-learn


Reading the Dataset

The application_record.csv and credit_record.csv files are loaded using the Pandas library.

The shape and first few records of both datasets are displayed to understand their structure.

Univariate Analysis

Univariate analysis is performed to analyze individual variables in the dataset.

For example, the distribution of applicants based on their occupation type is analyzed using value counts and graphical visualization.

Multivariate Analysis

Multivariate analysis is performed to understand the relationships between multiple numerical variables.

A correlation matrix and heatmap are generated to analyze relationships among different features.

Descriptive Analysis

Descriptive statistics are calculated to understand important statistical information about numerical features.

This includes values such as:

Count

Mean

Standard deviation

Minimum value

Maximum value

Percentiles



---

Epic 3: Data Preprocessing

Data preprocessing is one of the most important stages of the Machine Learning project.

The raw dataset must be cleaned and transformed before it can be used to train Machine Learning models.

Removing Duplicate Records

Duplicate applicant records are identified and removed using the applicant ID.

This helps prevent duplicate information from affecting model training.

Handling Missing Values

The dataset is checked for missing values.

Missing occupation information is handled by replacing empty values with an appropriate value.

Data Cleaning

The birth and employment information is converted into a more understandable format.

Negative day values are processed and transformed into useful features.

Feature Engineering

New features are created from existing dataset columns.

Some of the newly created features include:

Applicant Age

Years of Employment

Total Family Information


Feature engineering helps improve the usefulness of the data for Machine Learning algorithms.

Creating the Target Variable

The credit status information is processed to create a target variable.

This target variable is used by Machine Learning models to perform classification.

Merging the Datasets

The application dataset and credit history dataset are merged using the common applicant ID.

The merged dataset is then used for further preprocessing and model development.

Handling Categorical Values

Machine Learning models require numerical input.

Therefore, categorical columns such as gender, income type, education level, family status, occupation type, and housing type are converted into numerical values using encoding techniques.

Splitting the Dataset

The processed dataset is separated into:

Independent variables (X)

Target variable (y)


The data is then divided into:

Training Dataset

Testing Dataset


The training data is used to train Machine Learning models, while the testing data is used to evaluate model performance.


---

Epic 4: Machine Learning Model Building

Three different Machine Learning classification algorithms are implemented in this project.

Logistic Regression

Logistic Regression is a supervised Machine Learning classification algorithm.

The Logistic Regression model is trained using the training dataset and tested using the testing dataset.

The model's performance is evaluated using accuracy and classification metrics.

Random Forest Classifier

Random Forest is an ensemble Machine Learning algorithm that combines multiple Decision Trees.

The Random Forest model is trained using the processed training dataset.

Predictions are generated using the testing dataset, and the model performance is evaluated.

Decision Tree Classifier

The Decision Tree algorithm performs classification by creating a tree-like decision structure based on dataset features.

The model is trained and evaluated using the same training and testing datasets.

Model Comparison

The performance of all three models is compared.

The implemented models are:

Logistic Regression

Random Forest Classifier

Decision Tree Classifier


The model with the best performance is selected as the final Machine Learning model.

Saving the Model

The best-performing model is saved using Python's Pickle library.

The model is saved as:

model.pkl

The model feature columns are also saved as:

model_columns.pkl

These files are later used by the Flask web application to make predictions.


---

Epic 5: Model Deployment Using Flask

The final stage of the project involves integrating the trained Machine Learning model with a web application.

The web application is developed using the Flask framework.

HTML Pages

Three HTML pages are created:

home.html

The home page displays the project title and provides an option to start the prediction process.

index.html

The prediction page contains an HTML form.

Users can enter applicant details such as:

Gender

Car ownership

Property ownership

Number of children

Annual income

Age

Years of employment

Number of family members


The entered information is sent to the Flask application for prediction.

result.html

The result page displays the final prediction generated by the Machine Learning model.

The application displays whether the credit card application is predicted to be approved or not approved.

Flask Application

The app.py file acts as the backend of the web application.

The Flask application:

Loads the trained Machine Learning model.

Loads the model feature columns.

Receives user information from the HTML form.

Converts the entered data into the required model input format.

Performs the prediction.

Sends the prediction result to the result page.


Running the Application

The Flask application is executed in Google Colab.

Ngrok is used to create a public URL that allows the Flask web application to be accessed through a web browser.


---

Technologies Used

The following technologies and tools were used to develop this project:

Python

Google Colab

Pandas

NumPy

Matplotlib

Scikit-learn

Machine Learning

Logistic Regression

Random Forest Classifier

Decision Tree Classifier

Flask

HTML

Pickle

Pyngrok

Git

GitHub



---

Project Structure

Credit-Card-Approval-Prediction/
│
├── Credit_Card_Approval_Prediction.ipynb
│
├── app.py
│
├── model.pkl
│
├── model_columns.pkl
│
├── templates/
│   ├── home.html
│   ├── index.html
│   └── result.html
│
└── README.md


---

Machine Learning Algorithms Used

The project implements and compares three Machine Learning classification algorithms:

1. Logistic Regression

A classification algorithm used to predict binary outcomes based on input features.

2. Random Forest Classifier

An ensemble learning algorithm that uses multiple Decision Trees to generate predictions.

3. Decision Tree Classifier

A supervised Machine Learning algorithm that performs classification using a tree-based decision structure.


---

Model Evaluation

The Machine Learning models are evaluated using:

Accuracy Score

Classification Report

Model Performance Comparison


After evaluating all the trained models, the best-performing model is selected and saved for deployment.


---

Web Application Features

The developed web application provides the following features:

Simple and user-friendly interface.

Applicant information input form.

Integration with the trained Machine Learning model.

Real-time prediction.

Credit card approval prediction result.

Flask-based backend.

Public application access using Ngrok.



---

How to Run the Project

To run the project:

1. Open the Jupyter Notebook or Google Colab notebook.


2. Install all required Python libraries.


3. Download and load the datasets.


4. Run the Exploratory Data Analysis cells.


5. Run the data preprocessing cells.


6. Train the Machine Learning models.


7. Compare the model performances.


8. Save the best-performing model.


9. Create the Flask application and HTML templates.


10. Add the Ngrok authentication token.


11. Start the Flask server.


12. Generate the public Ngrok URL.


13. Open the generated URL in a browser.


14. Enter applicant information.


15. Click the prediction button to view the result.




---

Conclusion

The Credit Card Approval Prediction Using Machine Learning project demonstrates the complete development process of a Machine Learning application.

The project starts with dataset collection and continues through Exploratory Data Analysis, data preprocessing, feature engineering, categorical data encoding, model training, model evaluation, and model deployment.

Three Machine Learning classification algorithms—Logistic Regression, Random Forest, and Decision Tree—are trained and compared.

The best-performing model is saved and integrated with a Flask web application. The final application provides a simple interface where users can enter applicant information and obtain a credit card approval prediction.

This project demonstrates the practical implementation of Machine Learning concepts and shows how a trained Machine Learning model can be integrated into a web application to create a complete end-to-end Machine Learning project.# Credit-card-approval-
