# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import create_model

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("my_first_api")

# Create input/output pydantic models
input_model = create_model("my_first_api_input", **{'Text': 'i feel numb the end of the world as we know it and i feel numb a href http leslielandberg'})
output_model = create_model("my_first_api_output", prediction='sadness')


# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
