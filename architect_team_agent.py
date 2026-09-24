import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def design_architecture(app_name, pm_output):
  prompt = f"""
You are a Software Architect AI agent. You receive project tasks from a Product Manager and design the system architecture.

App Name: {app_name}
Project Tasks:
{pm_output}

Respond with:
1. System Architecture - overall design of the system
2. Database Design - tables and relationships needed
3. File Structure - how the project files should be organized
4. API Design - list of functions and endpoints needed
5. Tech Stack - exact technologies and libraries to use

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
  print("Paste the PM output below. Press Enter twice when done:")

  lines = []
  while True:
    line = input()
    if line == "":
      break
    lines.append(line)

  pm_output = "\n".join(lines)

  result = design_architecture(app_name, pm_output)
  print("\n=== ARCHITECT AGENT OUTPUT ===")
  print(result)