import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def develop_code(
    app_name, pm_output="", architect_output="", requirements_output=""
):
  prompt = f"""
You are an expert Developer AI agent. Write a complete, functional, standard Python desktop application using Tkinter or pure Python code.

App Name: {app_name}

Requirements:
{requirements_output}

Project Plan:
{pm_output}

System Architecture:
{architect_output}

Instructions:
- Write ONLY clean, executable Python code.
- Include all necessary imports, functions, classes, and a main execution block.
- Do NOT include any introductory or concluding text, explanations, or refusal language.
- Start directly with the Python code imports.
"""
  response = client.chat.completions.create(
      model="openai/gpt-oss-120b",
      messages=[{"role": "user", "content": prompt}],
      max_tokens=2000,
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

  result = develop_code(app_name, requirements_output=requirements_output)
  print("\n=== DEVELOPER AGENT OUTPUT ===")
  print(result)