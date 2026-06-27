import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def develop_code(app_name, pm_output, architect_output, requirements_output):
    prompt = f"""
You are a Developer AI agent. You receive structured requirements from a Product Manager and write clean, working Python code.

App Name: {app_name}
Project plan:
{pm_output}

system architecture:
{architect_output}

Requirements:
{requirements_output}

Write the complete Python code to implement this app. Include:
- All imports
- Clear comments
- Working functions
- A main block to run it

Write only code. No explanations outside of comments.
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    app_name = input("App name: ")
    print("Paste the requirements output below. Press Enter twice when done:")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    requirements_output = "\n".join(lines)
    
    result = develop_code(app_name, requirements_output)
    print("\n=== DEVELOPER AGENT OUTPUT ===")
    print(result)