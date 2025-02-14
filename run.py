import streamlit as st
import asyncio
from lib.llm import run_graph

st.title("Fantasy Football League Data Analysis")

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "Who has the most wins?",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        try:
            result = run_graph(text)
            st.info(result)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")