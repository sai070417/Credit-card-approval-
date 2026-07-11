# ============================================
# Credit Card Approval Prediction
# Feature Engineering
# ============================================

import pandas as pd

# Load datasets
application = pd.read_csv("data/application_record_final.csv")
credit = pd.read_csv("data/credit_record.csv")

# Convert credit status into binary target
# Good Credit (Approved = 1), Bad Credit (Rejected = 0)
credit["TARGET"] = credit["STATUS"].apply(
    lambda x: 1 if x in ["C", "X", "0"] else 0
)

# Aggregate target by applicant ID
credit_target = credit.groupby("ID")["TARGET"].max().reset_index()

# Merge application and credit datasets
final_df = application.merge(credit_target, on="ID", how="inner")

# Create Age in Years
if "DAYS_BIRTH" in final_df.columns:
    final_df["AGE_YEARS"] = (final_df["DAYS_BIRTH"] / 365).astype(int)

# Create Employment Years
if "DAYS_EMPLOYED" in final_df.columns:
    final_df["EMPLOYMENT_YEARS"] = (final_df["DAYS_EMPLOYED"] / 365).astype(int)

# Income per Family Member
if "AMT_INCOME_TOTAL" in final_df.columns and "CNT_FAM_MEMBERS" in final_df.columns:
    final_df["INCOME_PER_MEMBER"] = (
        final_df["AMT_INCOME_TOTAL"] / final_df["CNT_FAM_MEMBERS"]
    )

# Save final engineered dataset
final_df.to_csv("data/final_dataset.csv", index=False)

print("Feature engineering completed successfully!")
print(final_df.head())
