import requests
import json

url = "http://127.0.0.1:11434/api/generate"
data = {
    "model": "llama3.2",
    "prompt": "Qué es un zx spectrum?",
    "max_tokens": 100
}


headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()

    respuesta=""

    lines=response.text.splitlines()

    for linea in range(len(lines)):
     data=json.loads(lines[linea])
     respuesta+=data["response"]
     print(data["response"],end="")
     
    #print(respuesta)
     
except requests.exceptions.RequestException as e:
    print(f"Error al realizar la solicitud: {e}")
