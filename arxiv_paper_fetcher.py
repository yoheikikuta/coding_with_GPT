import argparse
import feedparser

def search_arxiv(query, max_results=10):
    base_url = 'http://export.arxiv.org/api/query?'
    search_query = f'search_query={query}'
    max_results = f'max_results={max_results}'
    url = f'{base_url}{search_query}&{max_results}'

    response = feedparser.parse(url)

    return response.entries

def main(query, max_results):
    results = search_arxiv(query, max_results)
    query = "cat:hep-ph"  # 素粒子現象論に関連する論文を検索（例: "cat:hep-ph"）
    max_results = 10  # 取得したい最大結果数

    results = search_arxiv(query, max_results)

    for idx, paper in enumerate(results, start=1):
        print(f"{idx}. {paper.title}")
        print(f"著者: {', '.join(author.name for author in paper.authors)}")
        print(f"arXiv ID: {paper.id}")
        print(f"要約: {paper.summary[:200]}...")  # 要約の最初の200文字を表示
        print(f"公開日: {paper.published}")
        print(f"更新日: {paper.updated}\n")

def get_args():
    parser = argparse.ArgumentParser(description="arXiv論文情報取得")
    parser.add_argument(
        "-c",
        "--category",
        type=str,
        default="hep-ph",
        help="arXivのカテゴリ（デフォルト: hep-ph）"
    )
    parser.add_argument(
        "-n",
        "--num_results",
        type=int,
        default=10,
        help="取得する最大結果数（デフォルト: 10）"
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    query = f"cat:{args.category}"
    main(query, args.num_results)
