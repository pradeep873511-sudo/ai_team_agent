import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_requirements(app_name, requirements):
    prompt = f"""
You are a Product Manager AI agent. Your job is to take a user's app idea and break it down into clear, structured development tasks.

App Name: {app_name}
Requirements: {requirements}

Respond with:
1. Project Overview - one paragraph summary
2. Core Features - list each feature clearly
3. Development Tasks - numbered list of tasks for the developer to implement
4. Tech Stack Suggestion - what technologies to use

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

if __name__ == "__main__":
    app_name = input("App name: ")
    requirements = input("Requirements: ")
    
    result = analyze_requirements(app_name, requirements)
    print("\n=== REQUIREMENTS AGENT OUTPUT ===")
    print(result)