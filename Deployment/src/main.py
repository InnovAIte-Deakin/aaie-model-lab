from typing import Union
from dotenv import load_dotenv
from fastapi import FastAPI
from google import genai
import os

load_dotenv()
model_id = os.getenv("GOOGLE_MODEL_ID")
api_key = os.getenv("GOOGLE_API_KEY")

app = FastAPI()
client = genai.Client(api_key=api_key)


def generate_response(prompt: str) -> str:
    response = client.models.generate_content(
        model=model_id, contents=prompt
    )
    return response.text

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/joke/{topic}")
def read_joke(topic: str):
    prompt = f"Tell me a joke about {topic}."
    return {"joke": generate_response(prompt)}