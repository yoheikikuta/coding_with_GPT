import streamlit as st
from datetime import datetime

def get_inputs():
    categories = [
        "hep-ph",
        "hep-th",
        "astro-ph",
        "cs.AI",
        "cs.CL",
        "math.ST",
        "q-bio",
        "quant-ph",
    ]
    
    category = st.selectbox("Category", categories)
    num_results = st.number_input("Number of papers to fetch", min_value=1, max_value=50, value=10, step=1)
    start_year = st.number_input("Start year for submitted date range", min_value=1900, max_value=datetime.now().year, value=1900, step=1)
    end_year = st.number_input("End year for submitted date range", min_value=1900, max_value=datetime.now().year, value=datetime.now().year, step=1)
    keyword = st.text_input("Keyword to search in title or abstract")
    return category, num_results, start_year, end_year, keyword
