import streamlit as st
from pm_team_agent import manage_project
from architect_team_agent import design_architecture
from requirements_team_agent import analyze_requirements
from developer_team_agent import develop_code
from codereviewer_team_agent import review_code
from qa_team_agent import qa_test

st.set_page_config(page_title="AI Team Agent", layout="wide")

st.title("AI Team Agent")
st.write("Describe your app and our AI team will build it for you.")

app_name = st.text_input("App Name")
requirements = st.text_area("Requirements", height=150)

if st.button("Build My App"):
    if not app_name or not requirements:
        st.error("Please enter both app name and requirements.")
    else:
        with st.spinner("PM Agent is planning..."):
            pm_output = manage_project(app_name, requirements)
        st.subheader("PM Agent Output")
        st.write(pm_output)

        with st.spinner("Architect Agent is designing..."):
            architect_output = design_architecture(app_name, pm_output)
        st.subheader("Architect Agent Output")
        st.write(architect_output)

        with st.spinner("Requirements Agent is analyzing..."):
            requirements_output = analyze_requirements(app_name, requirements)
        st.subheader("Requirements Agent Output")
        st.write(requirements_output)

        with st.spinner("Developer Agent is writing code..."):
            code_output = develop_code(app_name, pm_output, architect_output, requirements_output)
        st.subheader("Developer Agent Output")
        st.code(code_output, language="python")

        with st.spinner("Code Reviewer Agent is reviewing..."):
            review_output = review_code(app_name, code_output)
        st.subheader("Code Reviewer Output")
        st.write(review_output)

        with st.spinner("QA Agent is testing..."):
            qa_output = qa_test(app_name, code_output)
        st.subheader("QA Agent Output")
        st.write(qa_output)

        filename = app_name.replace(" ", "_").lower() + ".py"
        st.download_button(
            label="Download Code",
            data=code_output,
            file_name=filename,
            mime="text/plain"
        )