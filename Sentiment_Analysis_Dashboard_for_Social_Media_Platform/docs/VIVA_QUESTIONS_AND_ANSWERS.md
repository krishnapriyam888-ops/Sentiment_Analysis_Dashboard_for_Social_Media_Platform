# Viva / Campus Presentation Questions and Answers
## Sentiment Analysis Dashboard for Social Media Platform (Flask)

Use these as study notes. Answer in your own words and be ready to explain the actual code and demo.

## 1. Project introduction

**Q1. What is the title of your project?**  
The title is *Sentiment Analysis Dashboard for Social Media Platform*.

**Q2. What is the main objective?**  
To demonstrate how social-media-style text can be categorized as positive, neutral, or negative and summarized in a dashboard.

**Q3. Why did you choose this project?**  
Social platforms contain large amounts of opinions and feedback. Sentiment analysis can help summarize broad user reactions more quickly than reading every post manually.

**Q4. What problem does it solve?**  
It provides a simple interface to inspect sample posts, analyze new text, compare sentiment counts, filter posts, and import/export CSV datasets.

**Q5. Who are the intended users?**  
For the prototype: students, researchers, community managers, and analysts who want to explore opinion data. It is not intended for consequential decisions about individuals.

**Q6. What is the scope?**  
The current version analyzes supplied text and bundled sample data. It does not collect live posts from social platforms.

**Q7. What is the project output?**  
A browser-based dashboard showing sentiment counts, charts, a post table, a single-text analyzer, and CSV import/export.

**Q8. What is novel or useful about the project?**  
It brings text analysis, dataset exploration, visual summaries, and API endpoints into one small web application.

## 2. Sentiment analysis and NLP

**Q9. What is sentiment analysis?**  
It is a natural language processing (NLP) task that identifies the opinion or emotional polarity expressed in text, often as positive, neutral, or negative.

**Q10. What is NLP?**  
Natural Language Processing is a field of AI that helps computers process, analyze, and generate human language.

**Q11. What is polarity?**  
Polarity is the direction of sentiment, commonly positive or negative, with neutral used when neither direction is detected.

**Q12. What method does this project use?**  
A lexicon-based method. It checks whether tokens appear in predefined positive and negative word lists.

**Q13. What is a sentiment lexicon?**  
A dictionary that associates words with sentiment categories or sentiment scores.

**Q14. How is the score calculated?**  
`(positive_hits - negative_hits) / max(positive_hits + negative_hits, 1)`. The score is between -1 and +1 for this implementation.

**Q15. How do you interpret the score?**  
A positive score means more positive keywords were found; a negative score means more negative keywords were found; zero is neutral under the implementation's rules. It is not a probability.

**Q16. Why use a lexicon method?**  
It is easy to explain, fast, transparent, and does not require a model download or training dataset. Its simplicity is also a limitation.

**Q17. What are the limitations?**  
It can miss sarcasm, context, negation, spelling variations, emojis, slang, mixed-language text, and domain-specific meanings. For example, "not good" may be wrongly interpreted as positive because "good" is in the positive list.

**Q18. Is this machine learning?**  
The current sentiment classifier is rule-based/lexicon-based, not a trained machine-learning model. Flask is the web framework; it does not itself perform sentiment analysis.

**Q19. How could you improve accuracy?**  
Use a labeled dataset, preprocess carefully, compare a TF-IDF plus Logistic Regression baseline with a transformer model, evaluate on held-out data, and document limitations.

**Q20. What is tokenization?**  
Breaking text into smaller units, often words or subwords. This project uses a regular expression to extract alphabetic tokens.

**Q21. What is preprocessing?**  
Steps such as cleaning text, tokenizing, normalizing case, handling URLs, emojis, punctuation, and language-specific text. This demo lowercases text and extracts alphabetic tokens.

**Q22. What are precision, recall, and F1-score?**  
Precision is the fraction of predicted positives that are correct; recall is the fraction of actual positives found; F1 is the harmonic mean of precision and recall. For three classes, report per-class and macro/weighted metrics.

**Q23. What is a confusion matrix?**  
A table comparing actual labels with predicted labels, showing correct and incorrect classifications by class.

**Q24. How would you evaluate this project?**  
Prepare manually labeled examples, split data into training/validation/test sets if training a model, compare predictions with true labels, and report accuracy, precision, recall, F1, and confusion matrix. The current sample data is only a demonstration and is not an evaluation dataset.

## 3. Flask and web development

**Q25. What is Flask?**  
Flask is a lightweight Python web framework used to build web applications and HTTP endpoints.

**Q26. Why Flask instead of a larger framework?**  
The project is small and needs simple routes and template rendering. Flask has a low setup overhead and is easy to explain in a college demonstration.

**Q27. What is a route?**  
A URL rule that maps a request to a Python function, such as `/` or `/api/analyze`.

**Q28. What is the purpose of `@app.route("/")`?**  
It maps the root URL to the dashboard view function.

**Q29. What is Jinja?**  
Flask's template engine. It inserts values into HTML templates and supports loops and conditional rendering.

**Q30. What is the difference between GET and POST?**  
GET retrieves a resource or data. POST sends data to be processed, such as text to analyze or a CSV file to upload.

**Q31. What is JSON?**  
JavaScript Object Notation is a lightweight text format for structured data. The API uses JSON request and response bodies.

**Q32. What is a REST API?**  
An API organized around resources and HTTP methods. This project exposes simple JSON endpoints; it is REST-style rather than a complete formal REST architecture.

**Q33. What does `/api/analyze` do?**  
It accepts JSON containing a `text` field, validates it, runs sentiment analysis, and returns the text, label, score, and keyword hit counts.

**Q34. What does `/api/posts` do?**  
It returns the sample posts and calculated dashboard statistics as JSON.

**Q35. What does `/health` do?**  
It returns a small status response so a developer can check that the app is running.

**Q36. What is `render_template()`?**  
A Flask helper that renders an HTML template, passing Python data into it.

**Q37. What is `request.get_json()`?**  
A Flask request helper that parses a JSON request body.

**Q38. Why use `jsonify()`?**  
It converts Python data into a JSON HTTP response.

**Q39. What is a virtual environment?**  
An isolated Python environment with its own installed packages, helping keep project dependencies separate from other projects.

**Q40. Why use `requirements.txt`?**  
It lists Python dependencies so another developer can install the same main packages using `pip install -r requirements.txt`.

## 4. Dashboard, charts, and dataset

**Q41. What is a dashboard?**  
A visual summary of important measures and trends in one interface.

**Q42. Why use charts?**  
Charts make class proportions and platform counts easier to understand at a glance.

**Q43. Which chart library is used?**  
Chart.js, loaded from a CDN in the HTML template.

**Q44. What does the doughnut chart show?**  
The counts of positive, neutral, and negative posts in the current dataset.

**Q45. What does the bar chart show?**  
The number of posts per platform in the current dataset.

**Q46. What is CSV?**  
Comma-Separated Values, a simple text format for tabular data.

**Q47. What columns are supported by CSV upload?**  
A required `text` column and optional `platform`, `author`, and `date` columns. Column names are matched case-insensitively.

**Q48. Where is uploaded data stored?**  
It is analyzed in the request and held in the browser's JavaScript memory after the response. The project does not persist uploads to a database.

**Q49. Why is there no database?**  
To keep the educational prototype small and easy to run. SQLite or PostgreSQL could be added for persistent storage.

**Q50. How does the search/filter work?**  
Client-side JavaScript filters the currently loaded post array by text/author, sentiment, and platform.

**Q51. How does CSV export work?**  
JavaScript creates a CSV string from the current dataset, creates a downloadable browser Blob, and triggers a download.

**Q52. What is the sample dataset?**  
A small illustrative set of synthetic posts created to demonstrate the dashboard. It is not scraped from real accounts.

## 5. Setup, testing, and debugging

**Q53. How do you run the project?**  
Create and activate `.venv`, install `requirements.txt`, run `python app.py`, and open `http://127.0.0.1:5000`.

**Q54. What is localhost?**  
The local computer. `127.0.0.1` is the loopback IP address.

**Q55. What is port 5000?**  
The default port used by Flask's development server in this app.

**Q56. How do you test the app manually?**  
Load the home page, analyze positive/negative/neutral examples, test empty input, filter the table, upload a valid CSV, try an invalid CSV, and export results.

**Q57. What happens if the text is empty?**  
The API returns HTTP 400 with a validation error.

**Q58. What happens if the text exceeds 5,000 characters?**  
The text analyzer API returns HTTP 400. This limit helps constrain the demo endpoint's input size.

**Q59. What if Flask is not found?**  
Activate the virtual environment and run `pip install -r requirements.txt`. Confirm the environment is active and the correct Python executable is being used.

**Q60. What if port 5000 is busy?**  
Stop the other process or change the port in `app.run()`, for example to `port=5001`.

**Q61. What is debugging?**  
Finding and correcting errors in software. Flask debug mode helps during local development but should not be enabled in production.

**Q62. What is a unit test?**  
A test of a small function or component in isolation, such as verifying the sentiment function for known input examples.

**Q63. What test cases should be shown in a viva?**  
Positive-only text, negative-only text, text with no known keywords, mixed positive/negative text, blank API input, oversized input, valid CSV, and invalid CSV.

## 6. Security, privacy, and ethics

**Q64. Is this connected to live social media?**  
No. It uses sample data and user-supplied text/CSV. It does not call social media APIs or scrape posts.

**Q65. Why not scrape social media?**  
Automated collection can violate platform terms, privacy expectations, and legal requirements. A real integration should use authorized APIs and follow their rules.

**Q66. Is sentiment analysis always correct?**  
No. Language is context-dependent and automated sentiment labels can be wrong or biased.

**Q67. What privacy precautions would you use in production?**  
Collect only permitted data, minimize personal information, restrict access, define retention rules, secure stored data, and document the purpose of processing.

**Q68. Is the current application production-ready?**  
No. It is a local educational prototype. It lacks authentication, database persistence, rate limiting, deployment hardening, monitoring, and a validated classifier.

**Q69. Why should debug mode be disabled in production?**  
Debug mode may expose sensitive diagnostic information and should only be used in trusted local development.

**Q70. What is bias in sentiment analysis?**  
A systematic error affecting some languages, dialects, communities, or topics more than others. A model should be evaluated on representative data.

## 7. Extensions and future scope

**Q71. How can you add real social media data?**  
Integrate authorized official APIs, handle OAuth and API permissions, respect rate limits and terms, and clearly show data provenance.

**Q72. How can you add a database?**  
Use SQLAlchemy with SQLite for a small local app or PostgreSQL for a larger deployment. Add models, migrations, and access controls.

**Q73. How can you support Malayalam?**  
Use a model and labeled dataset suitable for Malayalam, handle Unicode text correctly, and evaluate on Malayalam examples. The current English lexicon is not suitable for Malayalam sentiment classification.

**Q74. Can the app classify emotions like joy or anger?**  
Yes, with a suitable multi-class emotion model and labeled training/evaluation data. The current app only estimates polarity.

**Q75. How could you show sentiment over time?**  
Parse and validate dates, aggregate daily or weekly sentiment counts, and display a line chart.

**Q76. Could it detect spam or fake accounts?**  
Not currently. Spam and bot detection are separate tasks requiring different features and validation.

**Q77. How could you deploy it?**  
Use a production WSGI server such as Gunicorn or Waitress, configure secrets and environment variables, use HTTPS behind a suitable host/proxy, and disable debug mode.

**Q78. What is the difference between frontend and backend?**  
The frontend is the browser interface (HTML, CSS, JavaScript and charts); the backend is Python/Flask, which handles routing, input validation, sentiment scoring, and CSV parsing.

## 8. Short rapid-fire questions

- **Language used?** Python for backend; HTML, CSS, and JavaScript for frontend.
- **Framework?** Flask.
- **Chart library?** Chart.js.
- **Input?** Social post text or CSV.
- **Output?** Sentiment label, score, charts, and summary statistics.
- **Classes?** Positive, Neutral, Negative.
- **Storage?** No persistent database in this version.
- **Live API integration?** No.
- **Can it work offline?** Flask backend works locally after dependencies are installed, but Chart.js is loaded from a CDN; download/serve Chart.js locally if full offline operation is required.
- **Main limitation?** Small English keyword lexicon and no context understanding.
- **Main future improvement?** Train/evaluate a robust NLP model on representative labeled data.

## Suggested 2-minute project presentation

Good morning. My project is titled **Sentiment Analysis Dashboard for Social Media Platform**. The objective is to demonstrate how social-media-style text can be categorized into positive, neutral, and negative sentiment and summarized visually.

The backend is developed using Python and Flask. The frontend uses HTML, CSS, JavaScript, and Chart.js. The dashboard displays sentiment counts, platform coverage, and a searchable post table. Users can enter a post for analysis, upload a CSV dataset, and export analyzed results.

For this prototype, I implemented a lexicon-based method that counts words from positive and negative keyword lists and calculates a score between -1 and +1. This approach is easy to understand and does not need a trained model, but it can fail on sarcasm, negation, and context. The dataset is illustrative and the app does not collect live posts from social media.

Future improvements include using an evaluated machine-learning or transformer model, supporting Malayalam and other languages, adding persistent database storage, and integrating authorized social media APIs. Thank you.

## Demo checklist

1. Start Flask and open the dashboard.
2. Explain the four metric cards and both charts.
3. Enter a positive sentence and analyze it.
4. Enter a negative sentence and analyze it.
5. Demonstrate search and sentiment/platform filters.
6. Upload `sample_posts.csv` and explain the required `text` column.
7. Export the dataset as CSV.
8. Show `/api/posts`, `/api/analyze`, and `/health` if asked about APIs.
9. Explain the classifier's limitations honestly.
