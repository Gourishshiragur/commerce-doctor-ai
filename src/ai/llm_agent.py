import requests

# ---------------- AI ANALYSIS ----------------
def analyze_data(data_sample):

    prompt = f"""
You are a senior data engineer.

Here is a sample of an ecommerce dataset:
{data_sample}

STRICT CHECK RULES:
1. If any order_id appears more than once → mark as DUPLICATE
2. If any customer_id is null → mark as MISSING
3. If any amount is less than 0 → mark as INVALID

IMPORTANT:
- Do NOT assume data is clean
- Only use the given sample
- Be precise

OUTPUT FORMAT:

Data Issues:
- ...

Fix Suggestions:
- ...
"""

    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        response = res.json().get("response", "").strip()

        if len(response) < 15:
            return "AI could not detect issues properly. Try with more data."

        return response

    except Exception as e:
        return f"LLM Error: {str(e)}"


# ---------------- AI CODE GENERATION ----------------
def generate_fix_code(data_sample):

    prompt = f"""
You are a senior PySpark engineer.

Dataset sample:
{data_sample}

Write PySpark code to:
- Remove rows where customer_id is null
- Remove rows where amount < 0
- Remove duplicate order_id

IMPORTANT:
- Use PySpark DataFrame syntax
- Assume dataframe name is df
- Do NOT add explanations

Return only clean PySpark code.
"""

    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        code = res.json().get("response", "").strip()

        if len(code) < 15:
            return "# AI could not generate valid code"

        return code

    except Exception as e:
        return f"# LLM Error: {str(e)}"