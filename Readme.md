# Agentic Python Blog Writer

A fully autonomous blog-writing agent built using Python, Google Gemini AI, and async APIs.  
It plans topics, researches news, writes full blogs, optimizes SEO, and exports clean outputs.

---

## Features

- Topic planning based on input
- Async research (news, keywords, quotes)
- AI blog writing using Google Gemini 1.5 Pro
- SEO optimization (title, meta description, keywords, reading time, readability score)
- Fallback handling for API failures
- Export final blog in `.md` + SEO metadata in `.json`

---

## ⚙ Setup Instructions

1. Clone or download the project files.

2. Install required libraries:

```bash
pip install -r requirements.txt
```

## Make env file as

GEMINI_API_KEY=your_gemini_api_key_here
NEWSDATA_API_KEY=your_newsdata_api_key_here

## Example CLI Usage

python main.py "How Python is used in AI" --tone "educational"
