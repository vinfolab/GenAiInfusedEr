# Website Insighter

Excited to share my first AI app - "Website Insighter"!

## What it does:

Paste any website URL and get an instant AI-powered summary in your preferred style - from executive briefings to casual overviews.

## Tech Stack:

- Python + Gradio (UI)
- OpenAI Python SDK (LLM integration)
- Model: openai/gpt-oss-120b via client.chat.completions.create()
- Requests + BeautifulSoup4 (web scraping)

## Key Learning:

This project taught me how to combine web scraping with LLM capabilities to extract meaningful insights from any website content.

The app scrapes the webpage, cleans the HTML (removing scripts, nav, footer), and sends the content to the LLM for intelligent summarization.
