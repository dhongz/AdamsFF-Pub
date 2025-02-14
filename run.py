import streamlit as st
import asyncio
from lib.llm import run_graph

# Configure the page
st.set_page_config(
    page_title="Fantasy Football Analysis",
    page_icon="��",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS with more sophisticated styling
st.markdown("""
    <style>
    .stTitle {
        font-size: 42px;
        padding-bottom: 20px;
        color: #1f4037;
        text-align: center;
    }
    .stForm {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stTextArea {
        border: 2px solid #1f4037;
        border-radius: 5px;
    }
    .stButton button {
        background-color: #1f4037;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 2rem;
        transition: all 0.3s;
    }
    .stButton button:hover {
        background-color: #2d5a4e;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .example-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Header section
st.title("🏈 Adams Fantasy Football League")
st.markdown("---")

# Create columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    with st.form("query_form", clear_on_submit=False):
        text = st.text_area(
            "",
            placeholder="Example: Who has the most wins this season?",
            height=100,
            key="query_input"
        )
        
        col_btn1, col_btn2 = st.columns([1, 4])
        with col_btn1:
            submitted = st.form_submit_button("Ask")
        with col_btn2:
            if submitted and text:
                with st.spinner("Processing your request..."):
                    try:
                        result = run_graph(text)
                        st.markdown("### Results")
                        st.info(result)
                    except Exception as e:
                        st.error(f"❌ An error occurred: {str(e)}")
            elif submitted and not text:
                st.warning("⚠️ Please enter a question to analyze")

with col2:
    st.markdown('<div class="example-card">', unsafe_allow_html=True)
    st.markdown("### 💡 Example Questions")
    examples = [
        "Who has the most wins?",
        "What's the highest scoring team?",
        "Give me an extensive storyline on the history of our league. Talk about interesting team timelines focusing on team points scores, margins of victory and playoff success. Don't forget to mention the lows as well."
        "Which team scores the most points on average?",
        "What's the average points per game across all teams?"
    ]
    
    for example in examples:
        st.markdown(f"- {example}")
    st.markdown("</div>", unsafe_allow_html=True)
