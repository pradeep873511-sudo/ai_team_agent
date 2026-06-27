import os
from dotenv import load_dotenv
from pm_team_agent import manage_project
from architect_team_agent import design_architecture
from requirements_team_agent import analyze_requirements
from developer_team_agent import develop_code
from codereviewer_team_agent import review_code
from qa_team_agent import qa_test

load_dotenv()

def main():
    print("=== AI TEAM AGENT ===")
    print("Tell us about your app and we will build it for you.")
    print("")
    
    app_name = input("App name: ")
    requirements = input("Requirements: ")
    
    print("\nPM Agent is planning...")
    pm_output = manage_project(app_name, requirements)
    print("\n=== PM AGENT OUTPUT ===")
    print(pm_output)
    
    print("\nArchitect Agent is designing...")
    architect_output = design_architecture(app_name, pm_output)
    print("\n=== ARCHITECT AGENT OUTPUT ===")
    print(architect_output)
    
    print("\nRequirements Agent is analyzing...")
    requirements_output = analyze_requirements(app_name, requirements)
    print("\n=== REQUIREMENTS AGENT OUTPUT ===")
    print(requirements_output)
    
    print("\nDeveloper Agent is writing code...")
    code_output = develop_code(app_name, pm_output, architect_output, requirements_output)
    print("\n=== DEVELOPER AGENT OUTPUT ===")
    print(code_output)
    
    print("\nCode Reviewer Agent is reviewing...")
    review_output = review_code(app_name, code_output)
    print("\n=== CODE REVIEWER OUTPUT ===")
    print(review_output)
    
    print("\nQA Agent is testing...")
    qa_output = qa_test(app_name, code_output)
    print("\n=== QA AGENT OUTPUT ===")
    print(qa_output)
    
    filename = app_name.replace(" ", "_").lower() + ".py"
    with open(filename, "w") as f:
        f.write(code_output)
    
    print(f"\nCode saved to {filename}")

if __name__ == "__main__":
    main()