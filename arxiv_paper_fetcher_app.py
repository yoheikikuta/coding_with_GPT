import streamlit as st
from arxiv_paper_fetcher import search_arxiv, get_args, main
from datetime import datetime


def app():
    st.title("arXiv Paper Fetcher")
    
    category = st.text_input("Category (e.g. hep-ph):")
    num_results = st.number_input("Number of papers to fetch", min_value=1, max_value=50, value=10, step=1)
    start_year = st.number_input("Start year for submitted date range", min_value=1900, max_value=datetime.now().year, value=1900, step=1)
    end_year = st.number_input("End year for submitted date range", min_value=1900, max_value=datetime.now().year, value=datetime.now().year, step=1)
    keyword = st.text_input("Keyword to search in title or abstract")
    
    if st.button("Fetch Papers"):
        query = f"cat:{category}"
        
        if start_year and end_year:
            query += f" AND submittedDate:[{start_year}0101 TO {end_year}1231]"
            
        if keyword and keyword.strip():
            query += f' AND (ti:"{keyword}" OR abs:"{keyword}")'

        papers = search_arxiv(query, num_results)

        for idx, paper in enumerate(papers, start=1):
            st.write(f"{idx}. {paper.title}")
            st.write(f"著者: {', '.join(author.name for author in paper.authors)}")
            st.write(f"arXiv ID: {paper.id}")
            st.write(f"要約: {paper.summary[:200]}...")
            st.write(f"公開日: {paper.published}")
            st.write(f"更新日: {paper.updated}\n")


if __name__ == "__main__":
    app()
