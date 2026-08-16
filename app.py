import streamlit as st

from llm import generate_flowchart
from prompts import build_prompt

from streamlit_mermaid import st_mermaid

st.title("AI Flowchart Maker")

user_input = st.text_area(
    "Describe your flowchart"
)

if st.button("Generate"):

    prompt = build_prompt(user_input)

    mermaid_code = generate_flowchart(prompt)

    st.subheader("Generated Mermaid")

    st.code(mermaid_code)

    st.subheader("Flowchart")

    st_mermaid(mermaid_code)