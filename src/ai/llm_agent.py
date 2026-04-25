import requests

# ---------------- AI ANALYSIS ----------------
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


# ---------------- AI CODE GENERATION ----------------
def generate_fix_code(data_sample):

    prompt = f"""
    You are a senior data engineer.

    Given this dataset:
    {data_sample}

    Generate PySpark code to fix:
    - null values in customer_id
    - negative values in amount
    - duplicate order_id

    Only return PySpark code. No explanation.
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
        code = data.get("response", "").strip()

        if not code:
            return "# No code generated"

        return code

    except Exception as e:
        return f"# LLM Error: {str(e)}"