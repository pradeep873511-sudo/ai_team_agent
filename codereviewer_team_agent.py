import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def review_code(app_name, code):
  prompt = f"""
You are a Code Reviewer AI agent. You receive code written by a Developer agent and review it for quality.

App Name: {app_name}
Code:
{code}

Review the code and respond with:
1. Overall Quality - rate it out of 10
2. Issues Found - list any bugs, errors, or bad practices
3. Improvements - suggest specific improvements
4. Final Verdict - approve or needs revision

Be specific and practical. No fluff.
"""
  response = client.chat.completions.create(
      model = "openai/gpt-oss-120b",
      messages=[{"role": "user", "content": prompt}],
      max_tokens=2000,
  )
  return response.choices[0].message.content


if __name__ == "__main__":
  print("Paste the code to review. Press Enter twice when done:")

  lines = []
  while True:
    line = input()
    if line == "":
      break
    lines.append(line)

  code = "\n".join(lines)
  app_name = input("App name: ")

  result = review_code(app_name, code)
  print("\n=== CODE REVIEWER OUTPUT ===")
  print(result)