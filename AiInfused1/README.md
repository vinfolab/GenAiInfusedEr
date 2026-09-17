# v1.0.0 - Website Insighter

Excited to share my first AI app - "Website Insighter"!

## Git Tag

tag v1.0.0
Tagger: vinfolab <vinfolab@gmail.com>
Date: Thu Sep 17 22:11:40 2026 +0530
Message: Gen AI application using OpenAI provider API call i.e. client.chats.completions.create() from OpenAI Python SDK

### What it does:

Paste any website URL and get an instant AI-powered summary in your preferred style - from executive briefings to casual overviews.

#### Tech Stack:

- Python + Gradio (UI)
- OpenAI Python SDK (LLM integration)
- Model: openai/gpt-oss-120b via client.chat.completions.create()
- Requests + BeautifulSoup4 (web scraping)

##### Key Learning:

This project taught me how to combine web scraping with LLM capabilities to extract meaningful insights from any website content.

The app scrapes the webpage, cleans the HTML (removing scripts, nav, footer), and sends the content to the LLM for intelligent summarization.

---

# v1.1.0 — LangChain Framework Implementation

This version introduces a basic **LangChain** workflow demonstrating how prompts, language models, and output parsers can be composed into a sequential processing pipeline using **LangChain Expression Language (LCEL)**.

## Git Tag

tag v1.1.0
Tagger: vinfolab <vinfolab@gmail.com>
Date: Thu Sep 17 22:59:45 2026 +0530
Message: This version introduces a basic LangChain workflow demonstrating how prompts, language models, and output parsers can be composed into a sequential processing pipeline using LangChain Expression Language (LCEL).

### Key Components

The implementation uses the following components:

- **`ChatPromptTemplate`** — Defines and formats the prompt using dynamic input variables / place holders.
- **`ChatOpenAI`** — Integrates with OpenAI's chat-based language model.
- **`StrOutputParser`** — Parses the model response and returns the generated text as a string.
- **`Gradio`** — Used as the UI interface to provide a simple interactive front end for submitting inputs and displaying the generated output.

#### Chain Workflow

These components are composed into a single chain using the pipe (`|`) operator:

chain = prompt | model | parser

The workflow is initiated using:

result = chain.invoke(input)

The input flows sequentially through each component:

User Input
│
▼
Gradio UI
│
▼
ChatPromptTemplate
│
▼
ChatOpenAI
│
▼
StrOutputParser
│
▼
Final String Output
│
▼
Gradio UI

##### Dependencies

The implementation uses the following LangChain libraries:

- `langchain-core` — Provides core abstractions such as prompts, runnables, and output parsers.
- `langchain-openai` — Provides the OpenAI model integration used by `ChatOpenAI`.
- `gradio` — Provides the interactive web-based UI for the application.

This version establishes the foundation for building more advanced LangChain workflows by combining a Gradio UI with reusable Langchain components into executable chains.
