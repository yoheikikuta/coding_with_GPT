import json
import streamlit as st
from arxiv_paper_fetcher import search_arxiv
from datetime import datetime
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

import httplib2
from google_auth_httplib2 import AuthorizedHttp
from googleapiclient.discovery import build

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"


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

def translate_text(text, api_key, target_language="ja"):
    service = build("translate", "v2", developerKey=api_key)
    result = service.translations().list(source="en", target=target_language, q=text).execute()
    return result["translations"][0]["translatedText"]

def display_papers(papers):
    for idx, paper in enumerate(papers, start=1):
        with st.container():
            st.markdown(f"**{idx}. {paper.title}**")
            st.markdown(f"著者: {', '.join(author.name for author in paper.authors)}")
            st.markdown(f"arXiv ID: {paper.id}")
            st.markdown(f"要約: {paper.summary}")

            # 日本語訳を表示する
            translated_summary = translate_text(paper.summary, api_key=api_key)
            st.markdown(f"要約 (日本語): {translated_summary}")

            published_date = datetime.strptime(paper.published, "%Y-%m-%dT%H:%M:%SZ").date()
            st.markdown(f"公開日: {published_date}")
            
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
