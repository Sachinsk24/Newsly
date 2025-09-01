import os
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
from newspaper import Article

# Load environment variables
load_dotenv()

app = Flask(__name__)

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
if not NEWSAPI_KEY:
    raise ValueError("⚠️ NEWSAPI_KEY not found in .env file")

BASE_URL = "https://newsapi.org/v2/top-headlines"


def fetch_articles(page, page_size, category=None):
    """Fetch paginated articles from NewsAPI with optional category filtering."""
    params = {
        "country": "us",
        "apiKey": NEWSAPI_KEY,
        "pageSize": page_size,
        "page": page
    }
    if category:
        params["category"] = category

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()

    if data.get("status") != "ok":
        raise ValueError("❌ Error fetching articles")

    articles = []
    for art in data.get("articles", []):
        try:
            url = art.get("url", "")
            if not url:
                continue

            # Use newspaper3k for parsing
            article = Article(url)
            article.download()
            article.parse()

            articles.append({
                "title": art.get("title", "No title"),
                "content": (article.text[:200] + "...") if article.text else "No content available.",
                "image": art.get("urlToImage"),
                "source": url,
                "published_at": art.get("publishedAt", "")
            })

        except Exception as e:
            print(f"Skipping article due to error: {e}")
            continue

    total_results = min(data.get("totalResults", 0), 100)  # API caps at 100
    total_pages = (total_results // page_size) + (1 if total_results % page_size else 0)

    return articles, total_pages, total_results


@app.route("/")
def index():
    try:
        page = request.args.get("page", 1, type=int)
        page_size = 6  # Show 6 articles per page
        category = request.args.get("category", None)

        articles, total_pages, total_results = fetch_articles(page, page_size, category)

        return render_template(
            "index.html",
            articles=articles,
            page=page,
            total_pages=total_pages,
            category=category,
            total_results=total_results
        )

    except requests.exceptions.RequestException as e:
        return f"⚠️ Error fetching news: {e}"
    except Exception as e:
        return f"⚠️ Unexpected error: {e}"


if __name__ == "__main__":
    app.run(debug=True)
