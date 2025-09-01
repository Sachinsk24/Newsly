# News Article

A Flask-powered web app that delivers the latest headlines from [NewsAPI](https://newsapi.org) with clean article previews using `newspaper3k`.  
The project features category filtering, pagination, and responsive design for a smooth reading experience.

---

## 🚀 Features
- 🔍 **Category Filtering** – Browse General, Business, Technology, Sports, Health, Science, or Entertainment.
- 📄 **Article Summaries** – Extracted previews powered by `newspaper3k`.
- 🔄 **Pagination** – Easily navigate through pages of headlines.
- 🎨 **Responsive Design** – Clean Bootstrap interface for desktop and mobile.
- 🛡 **Error Handling** – Graceful fallback when an article is missing or blocked.

---

## 🛠 Installation & Setup

### **1. Clone the repository**
```bash
git clone https://github.com/YOUR-USERNAME/news-article.git
cd news-article

2. Create and activate a virtual environment

Windows (PowerShell):

py -m venv .venv
.venv\Scripts\Activate.ps1


macOS/Linux (bash/zsh):

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Add your NewsAPI key

Create a .env file in the project root with:

NEWSAPI_KEY=your_api_key_here

5. Run the application
python app.py


The app will start at:
http://127.0.0.1:5000

📦 Deployment with ngrok

To share your app quickly:

ngrok http 5000


Use the generated public URL to share the app.

📚 Technologies Used

Backend: Python, Flask, Requests, Newspaper3k

Frontend: Bootstrap, Font Awesome, Custom CSS

API: NewsAPI

🙌 Acknowledgements

NewsAPI
 for providing the news data.

Newspaper3k
 for article extraction.

Bootstrap
 for responsive UI components.
