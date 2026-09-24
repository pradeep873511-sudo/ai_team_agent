import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def manage_project(app_name, requirements):
  prompt = f"""
You are a Product Manager AI agent. Your job is to convert user requirements into clear, structured project tasks.

App Name: {app_name}
Requirements: {requirements}

Respond with:
1. Project Goals - what the app must achieve
2. User Stories - list each feature as a user story (As a user, I want to...)
3. Priority Tasks - ranked list of tasks from most to least important
4. Timeline Estimate - rough estimate to build each task
5. Risks - list any potential risks or challenges

Be specific and practical. No fluff.
"""
  response = client.chat.completions.create(
      model = "openai/gpt-oss-120b",
      messages=[{"role": "user", "content": prompt}],
      max_tokens=1000,
  )
  return response.choices[0].message.content


if __name__ == "__main__":
  app_name = input("App name: ")
  requirements = input("Requirements: ")

  result = manage_project(app_name, requirements)
  print("\n=== PM AGENT OUTPUT ===")
  print(result)