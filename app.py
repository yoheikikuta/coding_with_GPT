import streamlit as st
from arxiv_paper_fetcher import search_arxiv
from components.inputs import get_inputs
from components.papers import display_papers
from utils.arxiv_query import build_query
from utils.translation import translate_text, load_api_key

def app():
    st.title("arXiv Paper Fetcher")

    category, num_results, start_year, end_year, keyword = get_inputs()
    api_key = load_api_key()
    
    if st.button("Fetch Papers"):
        query = build_query(category, start_year, end_year, keyword)
        papers = search_arxiv(query, int(num_results))
        display_papers(papers, api_key)

if __name__ == "__main__":
    app()
