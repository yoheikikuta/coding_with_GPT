# arXiv Paper Fetcher
arXiv Paper Fetcherは、arXivから論文を検索し、その要約を日本語に翻訳して表示するStreamlitアプリケーションです。カテゴリ、日付範囲、キーワードを指定して論文を検索できます。

## 主な機能
arXivのカテゴリを選択して論文を検索
日付範囲を指定して論文を検索
キーワードを指定して論文のタイトルと要約で検索
検索結果の論文の要約を日本語に翻訳
インストール
このリポジトリをクローンし、必要なPythonパッケージをインストールします。

```bash
git clone https://github.com/yourusername/arxiv-paper-fetcher.git
cd arxiv-paper-fetcher
pip install -r requirements.txt
```

## 環境変数の設定
Google Cloud Translation APIを使用するために、環境変数にAPIキーを設定する必要があります。.envファイルを作成し、次のようにAPIキーを追加します。

```makefile
API_KEY=your_api_key_here
```

## アプリケーションの実行
Streamlitアプリケーションをローカルで実行します。

```bash
streamlit run main.py
```
ブラウザで表示されるURLにアクセスしてアプリケーションを使用します。

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。詳細については、LICENSEファイルを参照してください。
