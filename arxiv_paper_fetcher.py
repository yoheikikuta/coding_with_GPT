from datetime import datetime
import argparse
import feedparser
import urllib.parse


def search_arxiv(query, max_results=10):
    encoded_query = urllib.parse.quote(query)
    base_url = 'http://export.arxiv.org/api/query?'
    search_query = f'search_query={encoded_query}'
    max_results = f'max_results={max_results}'
    url = f'{base_url}{search_query}&{max_results}'

    response = feedparser.parse(url)

    return response.entries

def main(query, max_results=10, start_year=None, end_year=None, keyword=None):
    if start_year and end_year:
        query += f" AND submittedDate:[{start_year}0101 TO {end_year}1231]"
    else:
        query += f" AND submittedDate:[{datetime.now().year}0101 TO {datetime.now().year}1231]"
        
    if keyword:
        query += f' AND (ti:"{keyword}" OR abs:"{keyword}")'

    max_results = 10  # 取得したい最大結果数
    papers = search_arxiv(query, max_results)

    for idx, paper in enumerate(papers, start=1):
        print(f"{idx}. {paper.title}")
        print(f"著者: {', '.join(author.name for author in paper.authors)}")
        print(f"arXiv ID: {paper.id}")
        print(f"要約: {paper.summary[:200]}...")  # 要約の最初の200文字を表示
        print(f"公開日: {paper.published}")
        print(f"更新日: {paper.updated}\n")

def get_args():
    parser = argparse.ArgumentParser(description="Fetch arXiv papers with specified category and keyword in title or abstract.")
    parser.add_argument("-c", "--category", required=True, help="Category to fetch papers from")
    parser.add_argument("-n", "--num_results", type=int, default=10, help="Number of papers to fetch")
    parser.add_argument("-s", "--start_year", type=int, help="Start year for submitted date range")
    parser.add_argument("-e", "--end_year", type=int, help="End year for submitted date range")
    parser.add_argument("-k", "--keyword", help="Keyword to search in title or abstract")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    query = f"cat:{args.category}"
    main(query, args.num_results, args.start_year, args.end_year, args.keyword)
