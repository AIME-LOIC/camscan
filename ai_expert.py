import google.generativeai as genai

# Setup your API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

def get_code_fix(raw_code):
    prompt = f"""
    The following code was scanned from paper. It may have OCR typos.
    1. Clean up the typos.
    2. Identify the bugs.
    3. Provide the corrected code.
    
    CODE:
    {raw_code}
    """
    response = model.generate_content(prompt)
    return response.text
