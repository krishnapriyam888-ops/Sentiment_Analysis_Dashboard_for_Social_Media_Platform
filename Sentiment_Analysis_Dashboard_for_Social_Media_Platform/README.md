# Sentiment Analysis Dashboard for Social Media Platform

A Flask-based college mini-project that demonstrates sentiment analysis on social-media-style posts. It includes a dashboard, interactive charts, a text analyzer, filters, CSV upload, CSV export, JSON API endpoints, sample data, and a viva/interview preparation guide.

## Features

- Responsive dashboard with total, positive, neutral, and negative post metrics.
- Doughnut chart for sentiment distribution and bar chart for platform coverage.
- Analyze a text snippet through the web interface or `/api/analyze`.
- Search/filter the post table by author/text, sentiment, and platform.
- Upload a CSV dataset with a required `text` column and optional `platform`, `author`, and `date` columns.
- Export analyzed posts to CSV.
- Sample dataset and REST-style JSON endpoints.
- Health endpoint at `/health`.
- No API key or paid service is required for the demo.

## Technology stack

- Python 3
- Flask
- HTML5, CSS3, JavaScript
- Chart.js (loaded from a CDN)
- CSV for dataset input/output

## Folder structure

```text
Sentiment_Analysis_Dashboard_for_Social_Media_Platform/
├── app.py
├── requirements.txt
├── README.md
├── sample_posts.csv
├── run_windows.bat
├── run_mac_linux.sh
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── docs/
│   └── VIVA_QUESTIONS_AND_ANSWERS.md
└── .venv/                 # create locally using the instructions below
```

## Setup on Windows

1. Install Python 3.10 or newer from https://www.python.org/downloads/ and enable **Add Python to PATH**.
2. Open Command Prompt in this project folder.
3. Create a virtual environment:

   ```bat
   py -m venv .venv
   ```

4. Activate it:

   ```bat
   .venv\\Scripts\\activate
   ```

5. Install dependencies:

   ```bat
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Start the server:

   ```bat
   python app.py
   ```

7. Open http://127.0.0.1:5000 in your browser.
8. Stop the server with `Ctrl+C`. Leave the environment with `deactivate`.

You can alternatively double-click `run_windows.bat`; it creates `.venv` if needed, installs requirements, and launches the app.

## Setup on macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

You can also run `bash run_mac_linux.sh`.

## CSV format

The uploaded CSV must include a `text` column. The other columns are optional.

```csv
platform,author,date,text
Instagram,@sample,2026-10-14,"I love this product. Great service!"
X,@sample2,2026-10-14,"The app is slow and confusing."
```

The demo's CSV upload is held in browser memory only; it is not stored in a database. Reloading restores the bundled sample dataset.

## API examples

### Analyze a post

```bash
curl -X POST http://127.0.0.1:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"The service was great and helpful\"}"
```

Example response:

```json
{
  "text": "The service was great and helpful",
  "sentiment": "Positive",
  "score": 1.0,
  "positive_hits": 2,
  "negative_hits": 0
}
```

### Get the sample dataset and statistics

```bash
curl http://127.0.0.1:5000/api/posts
```

### Health check

```bash
curl http://127.0.0.1:5000/health
```

## How the sentiment score works

This educational version uses a small transparent word lexicon. It counts positive and negative keywords and calculates:

`score = (positive_hits - negative_hits) / max(positive_hits + negative_hits, 1)`

- Score greater than 0: Positive
- Score less than 0: Negative
- No lexicon hits, or equal positive and negative hits: Neutral

The score ranges from -1 to +1. This is **not** a production-grade NLP model. It does not reliably handle negation ("not good"), sarcasm, emoji, slang, multilingual text, context, or domain-specific vocabulary. The score is a simple demo indicator, not a probability or confidence value.

## Academic integrity and responsible use

- Sample posts are illustrative and do not represent real users or real platform data.
- This project does not connect to Instagram, X, Facebook, or YouTube APIs.
- Use only data you have permission to process. Remove personal identifiers where possible.
- Do not use sentiment labels alone to make consequential decisions about people.
- For real deployment, add authentication, input/file limits, rate limiting, CSRF protection where appropriate, secure configuration, tests, logging, and a properly evaluated NLP model.
- `debug=True` is for local development only. Disable debug mode in deployment.
