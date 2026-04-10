Apple Product Sentiment Analyzer
An application that extracts consumer discussions from Reddit, performs multi-dimensional sentiment analysis using LLMs (OpenAI and Anthropic), and visualizes Apple product feature performances.

Overview
This project automates market sentiment analysis for Apple products by aggregating large amounts of Reddit discussions and using large language models to evaluate
user opinions. It generates structured insights on specific features such as battery life, build quality, and user interface for faster understanding of consumer feedback.

Key Features
- Reddit Data Collection: Uses the Reddit API (PRAW) to fetch real-time product discussions.
- AI Analysis: Uses OpenAI (GPT-5/4) and Anthropic (Claude 3.5) models to analyze customer opinions.
- Data Cleaning: Removes duplicates and organizes the data for processing
- Dashboard: Shows results in a simple Tkinter app with bar graphs.
- Structured Output: Uses Pydantic to ensure AI responses follow a consistent JSON format for easy analysis.

Tech Stack
- Languages: Python 3.9+
- AI/LLM: OpenAI API, Anthropic SDK, Pydantic
- Data Science: Pandas, NumPy, VADER Sentiment
- API/Web: PRAW (Reddit API), Dotenv
- Visualization: Matplotlib, Tkinter (GUI)

Project Structure
├── AI_Models/
│   ├── claude_analyzer.py    # Logic for Anthropic-based feature scoring
│   ├── openai_analyzer.py    # Logic for OpenAI-based analysis with Pydantic
│   └── sub_dataset.jsonl     # Sample raw data for testing
├── Data_Cleaning/
│   └── data_cleaning.py      # Stream-based JSON processing and deduplication
├── Sentiment_Analyzer/       # Storage for generated CSV reports
├── web_scraping/             # Raw scraped data output
├── main.py                   # Main entry point for the pipeline
├── reviews.py                # Reddit API extraction logic
├── visual.py                 # Tkinter GUI and Matplotlib charts
└── requirements.txt          # Project dependencies


Setup and Installation
1. Clone the repository:
   
2. Install dependencies:
   pip install -r requirements.txt

3. Configure Environment Variables:
   Create a .env file in the root directory
   REDDIT_CLIENT_ID='your_id'
   REDDIT_CLIENT_SECRET='your_secret'
   OPENAI_API_KEY='your_openai_key'
   ANTHROPIC_API_KEY='your_claude_key'

How It Works
1. Extraction (reviews.py)
The system searches specific subreddits for product keywords, cleaning text and extracting tags to filter out irrelevant content.

2. Analysis (AI_Models/)
The pipeline passes cleaned reviews to Claude or GPT with a specialized prompt. It asks the model to rate eight specific attributes on a scale of 1-10 including:
- Battery Life, UI, Aesthetics, Built Material, Price, Longevity, Processor Speed, and Customer Service

3. Visualization (visual.py)
The DataVisualizer class launches a desktop window showing:
- A textual summary of the AI's findings.
- A horizontal bar chart comparing scores across all Apple product features.

Use Case Example
Input: "iPhone 14"
Action: The tool scrapes recent posts from Reddit
Result: The UI shows the data.

Collaborators:
Annabelle Hirmiz, Jay Li, Paul Steitz
