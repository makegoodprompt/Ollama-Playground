import json
import requests

url = "http://localhost:11434/api/chat"
model = "mistral"
role = "user"
content = "What is love?"

payload = {
    "model": model,
    "messages" : [
        {
            "role": role,
            "content" : content
        }]
}

response = requests.post(url, json=payload, stream = True)


if response.status_code == 200:
    print(f"Response from Ollama {model} model:")
    for line in response.iter_lines(decode_unicode=True):
        if line:
            try:
                json_data = json.loads(line)
                if "message" in json_data and "content" in json_data["message"]:
                    print(json_data["message"]["content"], end="")
            except json.JSONDecodeError:
                print(f"\nFailed to parse line: {line}")
    print()
else:
    print(f"Error: {response.status_code}")
    print(response.text)