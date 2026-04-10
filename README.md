# Apple Product Sentiment Analyzer
An application that extracts consumer discussions from Reddit, performs multi-dimensional sentiment analysis using LLMs (OpenAI and Anthropic), and visualizes Apple product feature performances.

---

## Overview
This project automates market sentiment analysis for Apple products by aggregating Reddit discussions and using large language models to evaluate user feedback.

It transforms unstructured social media data into structured insights across key Apple product features including battery life, performance, design, and usability.

The system reduces manual review analysis by converting large amounts of Reddit discussion into clear feature scores, making it easier to understand the data.

---

## Key Features
- **Reddit Data Collection:** Uses the Reddit API (PRAW) to fetch real-time product discussions and filter relevant posts.
- **AI Analysis:** Uses OpenAI (GPT models) and Anthropic (Claude 3.5) models to analyze customer opinions
- **Data Cleaning:** Removes duplicates and organizes the data for processing
- **Dashboard:** Tkinter-based GUI with textual summaries and Matplotlib visualizations
- **Structured Output:** Uses Pydantic to ensure AI responses follow a consistent JSON format for easy analysis

---

## Analyzed Product Features
The system evaluates reviews across the following product attributes/features:
- Battery Life
- User Interface
- Aesthetic Design
- Build Material
- Price / Value
- Processor Speed
- Longevity / Reliability
- Customer Service

## Tech Stack
- **Languages:** Python 3.9+
- **AI/LLM:** OpenAI API
- **Data Processing:** Pandas, NumPy
- **API Integration:** PRAW (Reddit API), dotenv
- **Visualization:** Matplotlib, Tkinter (GUI)
- **Data Validation:** Pydantic

---

## Project Structure

├── AI_Models/
│   ├── claude.py                # Claude-based product attribute analyzer (multi-feature review scoring + reporting)
│   ├── openai_analyzer.py       # OpenAI-based sentiment + feature analysis pipeline using structured outputs
│   ├── main.py                  # End-to-end sentiment pipeline orchestrator (Reddit → AI → Visualization)
│   ├── reviews.py               # Reddit scraping module using PRAW (fetches and saves product discussions)
│   ├── visual.py                # Tkinter + Matplotlib GUI for displaying analysis results
│   ├── requirements.txt         # Python dependencies for AI models + analysis pipeline
│
├── Data_Cleaning/
│   ├── data_cleaning.py        # JSONL → CSV cleaning pipeline (deduplication, filtering, normalization)
│   ├── requirements.txt        # Dependencies for data preprocessing stage
│   ├── sub_dataset.jsonl       # Raw dataset sample (Reddit/web scraped data)
│
├── Sentiment_Analyzer/
│   ├── reddit_<product>.csv    # Generated Reddit review datasets (output of scraping step)
│
├── web_scraping/
│   ├── reddit_<product>.csv    # Raw scraped Reddit posts before analysis
│
├── README.md

---

## Setup and Installation
1. Clone the repository
   
2. Install dependencies:
   pip install -r requirements.txt

3. Configure Environment Variables:
   Create a .env file in the root directory
   REDDIT_CLIENT_ID='your_id'
   REDDIT_CLIENT_SECRET='your_secret'
   OPENAI_API_KEY='your_openai_key'
   ANTHROPIC_API_KEY='your_claude_key'

---

## How It Works
1. **Extraction** (reviews.py)
- Searches Reddit for product-related queries (e.g., "iPhone 14 review")
- Extracts post title, body, author, tags, and timestamp
- Cleans and stores results in a structured CSV file

2. **Analysis** (AI_Models/)
- Loads cleaned Reddit data
- Sends review text to OpenAI using structured prompts
- Evaluates sentiment across multiple product features
- Returns structured output using Pydantic models

3. **Visualization** (visual.py)
The DataVisualizer class launches a Tkinter-based desktop window showing:
- A textual summary of the AI's findings
- A horizontal bar chart comparing scores across all Apple product features

---

## Use Case Example
**Input:** "iPhone 14"
**Process:** 
- Scrapes Reddit posts related to user input (iPhone 14)
- Sends posts to OpenAI for feature-based sentiment scoring
- Aggregates results into structured analysis
**Output:**
- Dashboard shows strengths and weaknesses such as:
     - High: Processor Speed, Design
     - Lower: Price, Battery Life

---

## Collaborators:
Annabelle Hirmiz, Jay Li, Paul Steitz
