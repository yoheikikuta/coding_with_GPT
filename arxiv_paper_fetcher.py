from datetime import datetime
import argparse
import feedparser
import urllib.parse


def search_arxiv(query, max_results=10):
    encoded_query = urllib.parse.quote(query)
    url = f'http://export.arxiv.org/api/query?search_query={encoded_query}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}'

    response = feedparser.parse(url)

    return response.entries


def print_paper_info(paper, idx):
    print(f"{idx}. {paper.title}")
    print(f"著者: {', '.join(author.name for author in paper.authors)}")
    print(f"arXiv ID: {paper.id}")
    print(f"要約: {paper.summary[:200]}...")  # 要約の最初の200文字を表示
    print(f"公開日: {paper.published}")
    print(f"更新日: {paper.updated}\n")


def main(args):
    query = f"cat:{args.category}"
    
    if args.start_year and args.end_year:
        query += f" AND submittedDate:[{args.start_year}0101 TO {args.end_year}1231]"
    else:
        query += f" AND submittedDate:[{datetime.now().year}0101 TO {datetime.now().year}1231]"
        
    if args.keyword:
        query += f' AND (ti:"{args.keyword}" OR abs:"{args.keyword}")'

    papers = search_arxiv(query, args.num_results)

    for idx, paper in enumerate(papers, start=1):
        print_paper_info(paper, idx)


def get_args():
    parser = argparse.ArgumentParser(description="Fetch arXiv papers with specified category and keyword in title or abstract.")
    parser.add_argument("-c", "--category", required=True, help="Category to fetch papers from")
    parser.add_argument("-n", "--num_results", type=int, default=10, help="Number of papers to fetch")
    parser.add_argument("-s", "--start_year", type=int, help="Start year for submitted date range")
    parser.add_argument("-e", "--end_year", type=int, help="End year for submitted date range")
    parser.add_argument("-k", "--keyword", help="Keyword to search in title or abstract")
    return parser.parse_args()


if __name__ == "__main__":
    # args = get_args()
    # main(args)
    main(query, num_results, start_year, end_year, keyword)
