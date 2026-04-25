import requests

# ---------------- AI ANALYSIS ----------------
def analyze_data(data_sample):

    prompt = f"""
    You are a senior data engineer.

    Analyze this ecommerce dataset:
    {data_sample}

    Identify clearly:
    - Null values
    - Duplicate records
    - Negative or invalid values

    Then suggest fixes.

    Return answer in bullet points.
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

        response = res.json().get("response", "").strip()

        if len(response) < 10:
            return "AI could not generate meaningful output. Try again."

        return response

    except Exception as e:
        return f"LLM Error: {str(e)}"


# ---------------- AI CODE GENERATION ----------------
def generate_fix_code(data_sample):

    prompt = f"""
    You are a PySpark expert.

    Given this dataset:
    {data_sample}

    Write PySpark code to:
    - Remove null customer_id
    - Remove negative amount
    - Drop duplicate order_id

    Return only valid PySpark code.
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

        if len(code) < 10:
            return "# AI could not generate code"

        return code

    except Exception as e:
        return f"# LLM Error: {str(e)}"