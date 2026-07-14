
from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained model and feature columns
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

with open("model_columns.pkl", "rb") as file:
    model_columns = pickle.load(file)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict")
def predict_page():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    # Create empty input with exactly the same columns used during training
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=model_columns
    )

    # Get values from HTML form
    gender = request.form["gender"]
    car = request.form["car"]
    property_value = request.form["property"]

    children = float(request.form["children"])
    income = float(request.form["income"])
    age = float(request.form["age"])
    employment = float(request.form["employment"])
    family = float(request.form["family"])

    # Set numerical values only if the columns exist
    values = {
        "CNT_CHILDREN": children,
        "AMT_INCOME_TOTAL": income,
        "AGE": age,
        "YEARS_EMPLOYED": employment,
        "CNT_FAM_MEMBERS": family,
        "TOTAL_FAMILY": children + family
    }

    for column, value in values.items():
        if column in input_data.columns:
            input_data.loc[0, column] = value

    # Set categorical one-hot encoded values
    categorical_values = [
        "CODE_GENDER_" + gender,
        "FLAG_OWN_CAR_" + car,
        "FLAG_OWN_REALTY_" + property_value
    ]

    for column in categorical_values:
        if column in input_data.columns:
            input_data.loc[0, column] = 1

    # Make prediction
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        result = "Credit Card Application Approved"
    else:
        result = "Credit Card Application Not Approved"

    return render_template(
        "result.html",
        prediction_text=result
    )


if __name__ == "__main__":
    app.run()
