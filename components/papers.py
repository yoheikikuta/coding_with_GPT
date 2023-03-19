import streamlit as st
from datetime import datetime
from utils.translation import translate_text


def display_papers(papers, api_key):
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
