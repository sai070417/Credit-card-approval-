# Entity Relationship Diagram (ER Diagram)

## Description

The Entity Relationship (ER) Diagram represents the database structure of the Credit Card Approval Prediction System. It illustrates how different entities interact to store applicant information, credit history, machine learning model details, and approval prediction results.

## Entities

### 1. Users
Stores user account information.
- UserID (Primary Key)
- Name
- Email
- Password
- Role

### 2. Applicant_Details
Stores applicant personal and financial information.
- ApplicantID (Primary Key)
- UserID (Foreign Key)
- IncomeType
- EducationType
- FamilyStatus
- HousingType
- EmploymentDays

### 3. Credit_History
Stores applicant credit information.
- HistoryID (Primary Key)
- ApplicantID (Foreign Key)
- PaymentMonths
- OverdueStatus

### 4. ML_Model
Stores machine learning model information.
- ModelID (Primary Key)
- ModelName
- Algorithm
- Accuracy

### 5. Approval_Prediction
Stores prediction results.
- PredictionID (Primary Key)
- ApplicantID (Foreign Key)
- ModelID (Foreign Key)
- ApprovalResult
- RiskCategory

## Relationships

- One User can manage multiple Applicant Details.
- One Applicant can have multiple Credit History records.
- One Applicant receives one Approval Prediction.
- One ML Model predicts multiple applicants.
- Credit History is used to generate the Approval Prediction.

## Cardinality

- Users → Applicant_Details : One-to-Many
- Applicant_Details → Credit_History : One-to-Many
- Applicant_Details → Approval_Prediction : One-to-One
- ML_Model → Approval_Prediction : One-to-Many
