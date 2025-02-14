from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()

class Config:
    ESPN_S2 = st.secrets['ESPN_S2']
    LEAGUE_ID = st.secrets['LEAGUE_ID']
    SWID = st.secrets['SWID']
    LANGCHAIN_API_KEY = st.secrets['LANGCHAIN_API_KEY']
    LANGCHAIN_URL = st.secrets['LANGCHAIN_URL']

config = Config()