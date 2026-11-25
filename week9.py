import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
dataframe = pd.read_csv(r'C:\Users\c7741668\OneDrive - Leeds Beckett University\PDS\PYCharm\diabetes(1).csv')
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y,
test_size=test_size, random_state=seed)
# Fit the model on training set
model = LogisticRegression(solver='lbfgs', max_iter=1000
)
model.fit(X_train, Y_train)

# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)

import pickle
import numpy as np

# 1. Load the serialized model as a black-box component
filename = 'finalized_model.sav'
with open(filename, 'rb') as file:
    black_box_model = pickle.load(file)

def run_diabetes_screening_app():
    print("------------------------------------------")
    print("   PATIENT DIABETES RISK SCREENING APP    ")
    print("------------------------------------------")
    print("Enter the patient's clinical metrics:\n")

    # 2. Collect inputs matching the 8 features expected by the model
    pregnancies = float(input("1. Number of Pregnancies: "))
    glucose = float(input("2. Plasma Glucose Concentration: "))
    blood_pressure = float(input("3. Diastolic Blood Pressure (mm Hg): "))
    skin_thickness = float(input("4. Triceps Skin Fold Thickness (mm): "))
    insulin = float(input("5. 2-Hour Serum Insulin (mu U/ml): "))
    bmi = float(input("6. Body Mass Index (BMI): "))
    dpf = float(input("7. Diabetes Pedigree Function: "))
    age = float(input("8. Age (years): "))

    # Format input into a 2D array (1 patient, 8 features)
    patient_data = np.array([[
        pregnancies, glucose, blood_pressure, skin_thickness,
        insulin, bmi, dpf, age
    ]])

    # 3. Pass data into the black box for prediction & probability
    prediction = black_box_model.predict(patient_data)[0]
    probability = black_box_model.predict_proba(patient_data)[0][1] * 100

    # 4. Present user-friendly results
    print("\n--- SCREENING RESULT ---")
    if prediction == 1:
        print(f"Status: HIGH RISK (Positive)")
        print(f"Estimated Probability: {probability:.1f}%")
        print("Action: Refer patient for confirmatory clinical testing.")
    else:
        print(f"Status: LOW RISK (Negative)")
        print(f"Estimated Probability: {probability:.1f}%")
        print("Action: Routine follow-up recommended.")

if __name__ == "__main__":
    run_diabetes_screening_app()
