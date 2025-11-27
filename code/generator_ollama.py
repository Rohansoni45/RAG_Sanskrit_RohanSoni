# generator_ollama.py

import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"   # Make sure you have pulled this using: ollama pull llama3

def generate_with_ollama(prompt, stream=False):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": stream
    }

    response = requests.post(OLLAMA_URL, json=payload)

    # If streaming=FALSE → the result is JSON with "response" key
    data = response.json()

    # Return whichever key exists: "response" or whole JSON
    return data.get("response", data)
