
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
model = pipeline("sentiment-analysis")

class RequestBody(BaseModel):
    text: str

@app.post("/predict")
async def predict(request: RequestBody):
    result = model(request.text)
    return result
