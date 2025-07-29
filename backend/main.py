from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import uvicorn

# Load the saved model
model = joblib.load("model/random_forest_model.pkl")


# Define the input data schema
class DiabetesInput(BaseModel):
    pregnancies: int
    glucose: float
    blood_pressure: float
    skin_thickness: float
    insulin: float
    bmi: float
    diabetes_pedigree_function: float
    age: int


# Create FastAPI app instance
app = FastAPI(
    title="Diabetes Detection API",
    description="Predict whether a patient is diabetic or not based on health data",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Diabetes Detection API"}


@app.post("/predict")
def predict_diabetes(data: DiabetesInput):
    # Convert input data to numpy array
    input_data = np.array([
        [
            data.pregnancies,
            data.glucose,
            data.blood_pressure,
            data.skin_thickness,
            data.insulin,
            data.bmi,
            data.diabetes_pedigree_function,
            data.age
        ]
    ])

    # Make prediction
    prediction = model.predict(input_data)[0]
    result = "Diabetic" if prediction == 1 else "Non-Diabetic"

    return {"prediction": result}


# ---- Entry Point ----
def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
