import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi"


# ---------------- AI ANALYSIS (EXPLANATION ONLY) ----------------
def analyze_data(summary):

    prompt = f"""
Analyze this data quality summary:

{summary}

Explain clearly:

Data Issues:
- ...

Fix Suggestions:
- ...
"""

    try:
        res = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        response = res.json().get("response", "").strip()

        if len(response) < 10:
            return "AI could not generate explanation."

        return response

    except Exception as e:
        return f"LLM Error: {str(e)}"


# ---------------- AI CODE GENERATION ----------------
def generate_fix_code(summary):

    prompt = f"""
Generate PySpark code based on this data issue summary:

{summary}

Tasks:
- Remove null customer_id
- Remove negative amount
- Drop duplicate order_id

Return only PySpark code using df as dataframe.
"""

    try:
        res = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        code = res.json().get("response", "").strip()

        if len(code) < 10:
            return "# AI could not generate code"

        return code

    except Exception as e:
        return f"# LLM Error: {str(e)}"