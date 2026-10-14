from flask import Flask, render_template, request, jsonify
from collections import Counter
from datetime import datetime
import re
import csv
import io

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-development-key"

# Lightweight demo lexicon. For production, use a trained model and validated datasets.
POSITIVE_WORDS = {
    "good", "great", "excellent", "amazing", "love", "loved", "like", "happy",
    "awesome", "best", "wonderful", "fantastic", "beautiful", "helpful", "success",
    "positive", "enjoy", "enjoyed", "perfect", "brilliant", "nice", "thank", "thanks",
    "recommend", "excited", "impressed", "fast", "easy", "clear", "useful", "cool"
}
NEGATIVE_WORDS = {
    "bad", "terrible", "awful", "hate", "hated", "worst", "angry", "sad",
    "disappointed", "poor", "negative", "slow", "broken", "problem", "issue",
    "fail", "failed", "boring", "ugly", "confusing", "hard", "annoying", "waste",
    "unhelpful", "late", "expensive", "bug", "bugs", "error", "complaint"
}

SAMPLE_POSTS = [
    {"platform":"Instagram", "author":"@campuslife", "text":"Amazing event today! Loved the energy and the helpful volunteers.", "date":"2026-10-14"},
    {"platform":"X", "author":"@studentvoice", "text":"The new app is confusing and slow. Please fix the login issue.", "date":"2026-10-14"},
    {"platform":"Facebook", "author":"Campus Updates", "text":"Great work by the placement team. This is a wonderful opportunity.", "date":"2026-10-13"},
    {"platform":"YouTube", "author":"@learner01", "text":"The lecture audio was poor and the video had errors.", "date":"2026-10-13"},
    {"platform":"Instagram", "author":"@happy_student", "text":"Nice library, helpful staff, and a beautiful campus.", "date":"2026-10-12"},
    {"platform":"X", "author":"@reviewer", "text":"I hate waiting so long for support. Very disappointing service.", "date":"2026-10-12"},
    {"platform":"Facebook", "author":"Student Club", "text":"Thanks to everyone! The workshop was useful and exciting.", "date":"2026-10-11"},
    {"platform":"YouTube", "author":"@viewer", "text":"The explanation was clear, but the session was a bit boring.", "date":"2026-10-11"},
    {"platform":"Instagram", "author":"@campusfood", "text":"Food was good and affordable. I really enjoyed it.", "date":"2026-10-10"},
    {"platform":"X", "author":"@student_help", "text":"There is a problem with the timetable. The update is late.", "date":"2026-10-10"},
]

def analyze_sentiment(text):
    """Return a transparent lexicon-based sentiment estimate and score."""
    tokens = re.findall(r"[a-zA-Z']+", (text or "").lower())
    pos = sum(token in POSITIVE_WORDS for token in tokens)
    neg = sum(token in NEGATIVE_WORDS for token in tokens)
    score = (pos - neg) / max(pos + neg, 1)
    if pos == 0 and neg == 0:
        label = "Neutral"
    elif score > 0:
        label = "Positive"
    elif score < 0:
        label = "Negative"
    else:
        label = "Neutral"
    return {"sentiment": label, "score": round(score, 2), "positive_hits": pos, "negative_hits": neg}

def enrich_posts(posts):
    result = []
    for index, post in enumerate(posts):
        analysis = analyze_sentiment(post.get("text", ""))
        result.append({
            "id": index + 1,
            "platform": post.get("platform", "Other"),
            "author": post.get("author", "Unknown"),
            "text": post.get("text", ""),
            "date": post.get("date", ""),
            **analysis
        })
    return result

def make_stats(posts):
    counts = Counter(post["sentiment"] for post in posts)
    total = len(posts)
    return {
        "total": total,
        "positive": counts.get("Positive", 0),
        "neutral": counts.get("Neutral", 0),
        "negative": counts.get("Negative", 0),
        "positive_pct": round(counts.get("Positive", 0) * 100 / total) if total else 0,
        "neutral_pct": round(counts.get("Neutral", 0) * 100 / total) if total else 0,
        "negative_pct": round(counts.get("Negative", 0) * 100 / total) if total else 0,
        "platforms": dict(Counter(post["platform"] for post in posts))
    }

@app.route("/")
def index():
    posts = enrich_posts(SAMPLE_POSTS)
    return render_template("index.html", posts=posts, stats=make_stats(posts))

@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    data = request.get_json(silent=True) or {}
    text = str(data.get("text", "")).strip()
    if not text:
        return jsonify({"error": "Please enter text to analyze."}), 400
    if len(text) > 5000:
        return jsonify({"error": "Text must be 5,000 characters or fewer."}), 400
    return jsonify({"text": text, **analyze_sentiment(text)})

@app.route("/api/posts", methods=["GET"])
def api_posts():
    posts = enrich_posts(SAMPLE_POSTS)
    return jsonify({"stats": make_stats(posts), "posts": posts})

@app.route("/upload", methods=["POST"])
def upload_csv():
    uploaded = request.files.get("file")
    if not uploaded or not uploaded.filename.lower().endswith(".csv"):
        return jsonify({"error": "Upload a CSV file."}), 400
    try:
        content = uploaded.stream.read().decode("utf-8-sig")
        reader = csv.DictReader(io.StringIO(content))
        if not reader.fieldnames or "text" not in [name.strip().lower() for name in reader.fieldnames]:
            return jsonify({"error": "CSV must include a 'text' column. Optional columns: platform, author, date."}), 400
        # Map case-insensitive column names to original names.
        names = {name.strip().lower(): name for name in reader.fieldnames}
        posts = []
        for row in reader:
            text_value = (row.get(names["text"]) or "").strip()
            if not text_value:
                continue
            posts.append({
                "text": text_value,
                "platform": (row.get(names.get("platform", "")) or "Other").strip(),
                "author": (row.get(names.get("author", "")) or "CSV upload").strip(),
                "date": (row.get(names.get("date", "")) or "").strip()
            })
        enriched = enrich_posts(posts)
        return jsonify({"posts": enriched, "stats": make_stats(enriched), "message": f"Analyzed {len(enriched)} rows."})
    except (UnicodeDecodeError, csv.Error) as exc:
        return jsonify({"error": f"Could not read CSV: {exc}"}), 400

@app.route("/health")
def health():
    return jsonify({"status": "ok", "app": "Sentiment Analysis Dashboard"})

if __name__ == "__main__":
    app.run(debug=True)
