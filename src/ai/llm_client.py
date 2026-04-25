import requests

def call_llm(prompt):
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        return res.json()["response"]
    except Exception as e:
        return f"LLM Error: {str(e)}"