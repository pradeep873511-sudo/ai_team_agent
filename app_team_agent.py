import os
from architect_team_agent import design_architecture
from codereviewer_team_agent import review_code
from developer_team_agent import develop_code
from pm_team_agent import manage_project
from qa_team_agent import qa_test
from requirements_team_agent import analyze_requirements
import streamlit as st

logo_exists = os.path.exists("agent_logo.png")

st.set_page_config(
    page_title="AI Team Agent",
    page_icon="agent_logo.png" if logo_exists else "🤖",
    layout="wide",
)

st.markdown(
    """
<style>
body { background-color: #0d0d0d; }
.agent-card {
    background-color: #1a1a1a;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    margin: 10px;
    border: 1px solid #2a2a2a;
}
.agent-icon { font-size: 40px; }
.agent-name { color: #ffffff; font-size: 16px; font-weight: bold; margin-top: 8px; }
.agent-desc { color: #888888; font-size: 13px; margin-top: 4px; }
.main-title { color: #ffffff; text-align: center; font-size: 36px; font-weight: bold; }
.sub-title { color: #888888; text-align: center; font-size: 16px; margin-bottom: 30px; }
</style>
""",
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
  if logo_exists:
    st.image("agent_logo.png", width=100)
  st.markdown(
      '<div class="main-title">AI Team Agent</div>', unsafe_allow_html=True
  )
  st.markdown(
      '<div class="sub-title">Your personal AI software company</div>',
      unsafe_allow_html=True,
  )

st.markdown("---")

c1, c2, c3, c4, c5, c6 = st.columns(6)

with c1:
  st.markdown(
      """<div class="agent-card">
        <div class="agent-icon">📋</div>
        <div class="agent-name">PM Agent</div>
        <div class="agent-desc">Plans the project</div>
    </div>""",
      unsafe_allow_html=True,
  )

with c2:
  st.markdown(
      """<div class="agent-card">
        <div class="agent-icon">🏗️</div>
        <div class="agent-name">Architect Agent</div>
        <div class="agent-desc">Designs the system</div>
    </div>""",
      unsafe_allow_html=True,
  )

with c3:
  st.markdown(
      """<div class="agent-card">
        <div class="agent-icon">📝</div>
        <div class="agent-name">Requirements Agent</div>
        <div class="agent-desc">Breaks down features</div>
    </div>""",
      unsafe_allow_html=True,
  )

with c4:
  st.markdown(
      """<div class="agent-card">
        <div class="agent-icon">💻</div>
        <div class="agent-name">Developer Agent</div>
        <div class="agent-desc">Writes the code</div>
    </div>""",
      unsafe_allow_html=True,
  )

with c5:
  st.markdown(
      """<div class="agent-card">
        <div class="agent-icon">🔍</div>
        <div class="agent-name">Reviewer Agent</div>
        <div class="agent-desc">Reviews code quality</div>
    </div>""",
      unsafe_allow_html=True,
  )

with c6:
  st.markdown(
      """<div class="agent-card">
        <div class="agent-icon">🧪</div>
        <div class="agent-name">QA Agent</div>
        <div class="agent-desc">Tests and finds bugs</div>
    </div>""",
      unsafe_allow_html=True,
  )

st.markdown("---")

st.markdown("### Tell us about your app")

app_name = st.text_input("App Name", placeholder="e.g. TaskMate")
requirements = st.text_area(
    "Requirements",
    height=150,
    placeholder="Describe what your app should do...",
)

if "results" not in st.session_state:
  st.session_state.results = None

if st.button("Build My App", use_container_width=True):
  if not app_name or not requirements:
    st.error("Please enter both app name and requirements.")
  else:
    results = {}
    with st.spinner("PM Agent is planning..."):
      results["pm"] = manage_project(app_name, requirements)

    with st.spinner("Architect Agent is designing..."):
      results["architect"] = design_architecture(app_name, results["pm"])

    with st.spinner("Requirements Agent is analyzing..."):
      results["requirements"] = analyze_requirements(app_name, requirements)

    with st.spinner("Developer Agent is writing code..."):
      results["code"] = develop_code(
          app_name,
          results["pm"],
          results["architect"],
          results["requirements"],
      )

    with st.spinner("Code Reviewer Agent is reviewing..."):
      results["review"] = review_code(app_name, results["code"])

    with st.spinner("QA Agent is testing..."):
      results["qa"] = qa_test(app_name, results["code"])

    st.session_state.results = results

if st.session_state.results:
  res = st.session_state.results

  st.subheader("PM Agent Output")
  st.write(res["pm"])

  st.subheader("Architect Agent Output")
  st.write(res["architect"])

  st.subheader("Requirements Agent Output")
  st.write(res["requirements"])

  st.subheader("Developer Agent Output")
  st.code(res["code"], language="python")

  st.subheader("Code Reviewer Output")
  st.write(res["review"])

  st.subheader("QA Agent Output")
  st.write(res["qa"])

  filename = (
      app_name.replace(" ", "_").lower() + ".py" if app_name else "generated_app.py"
  )
  st.download_button(
      label="Download Code",
      data=res["code"],
      file_name=filename,
      mime="text/plain",
  )