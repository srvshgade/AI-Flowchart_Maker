import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_flowchart(prompt):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    print(result)

    if "response" in result:
        mermaid_code = result["response"]

        mermaid_code = mermaid_code.replace("->>", "-->")

    return mermaid_code

    return "flowchart TD\nA[Error] --> B[No Response]"