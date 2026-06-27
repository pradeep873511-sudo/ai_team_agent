import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def qa_test(app_name, code):
    prompt = f"""
You are a QA Agent. You receive code written by a Developer and review it for bugs and generate tests.

App Name: {app_name}
Code:
{code}

Respond with:
1. Bugs Found - list any bugs or issues in the code
2. Edge Cases - list edge cases that are not handled
3. Test Cases - write minimum 5 test cases to test the app
4. Final Verdict - pass or fail

Be specific and practical. No fluff.
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )
    return response.choices[0].message.content