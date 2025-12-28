from fastapi import FastAPI
from pydantic import BaseModel, Field
from .model import iris_model

app = FastAPI(
    title="Iris Classifier API",
    description="Simple ML inference service (Logistic Regression on Iris dataset)",
    version="1.0.0",
)


class IrisFeatures(BaseModel):
    sepal_length: float = Field(..., example=5.1)
    sepal_width: float = Field(..., example=3.5)
    petal_length: float = Field(..., example=1.4)
    petal_width: float = Field(..., example=0.2)


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Iris API is running"}


@app.post("/predict")
def predict_iris(features: IrisFeatures):
    input_list = [
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width,
    ]
    result = iris_model.predict(input_list)
    return {
        "input": input_list,
        "prediction": result["class_name"],
        "class_index": result["class_index"],
    }
