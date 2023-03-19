import streamlit as st
from arxiv_paper_fetcher import search_arxiv
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


def build_query(category, start_year, end_year, keyword):
    query = f"cat:{category}"

    if start_year and end_year:
        query += f" AND submittedDate:[{start_year}0101 TO {end_year}1231]"

    if keyword and keyword.strip():
        query += f' AND (ti:"{keyword}" OR abs:"{keyword}")'
    
    return query


def display_papers(papers):
    for idx, paper in enumerate(papers, start=1):
        with st.container():
            st.markdown(f"**{idx}. {paper.title}**")
            st.markdown(f"著者: {', '.join(author.name for author in paper.authors)}")
            st.markdown(f"arXiv ID: {paper.id}")
            st.markdown(f"要約: {paper.summary[:200]}...")
            st.markdown(f"公開日: {paper.published}")
            st.markdown(f"更新日: {paper.updated}\n")
            st.markdown("---")


def app():
    st.title("arXiv Paper Fetcher")

    category, num_results, start_year, end_year, keyword = get_inputs()
    
    if st.button("Fetch Papers"):
        query = build_query(category, start_year, end_year, keyword)
        papers = search_arxiv(query, int(num_results))
        display_papers(papers)


if __name__ == "__main__":
    app()
