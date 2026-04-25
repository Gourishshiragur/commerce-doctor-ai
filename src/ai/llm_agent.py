import requests

def analyze_data(data_sample):

    prompt = f"""
    You are a data quality expert.

    Given this ecommerce data:
    {data_sample}

    Find:
    1. Data Issues
    2. Fix Suggestions

    Give answer in bullet points.
    """

    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi",
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )

        data = res.json()
        response = data.get("response", "").strip()

        if not response:
            return "No meaningful response from AI"

        return response

    except Exception as e:
        return f"LLM Error: {str(e)}"