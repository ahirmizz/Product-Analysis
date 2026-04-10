Apple Product Sentiment Analyzer
An engineering and AI pipeline that extracts consumer discussions from Reddit, performs multi-dimensional sentiment analysis using LLMs (OpenAI and Anthropic),
and visualzies Apple product feature performances.

Overview
This project automates market sentiment analysis for Apple products by aggrgegating large amounts of Reddit discussions and using large language models to evaluate
user opinions. It generates structured insights on specific features such as battery life, build quality, and user interface for faster and more efficient
understanding of consumer feedback.

Key Features
- Reddit Data Collection: Uses the Reddit API (PRAW) to ffetch real-time product discussions.
- AI Analysis: Uses OpenAI (GPT-5/4) and Anthropic (Claude 3.5) models to analyze customer opinions.
- Data Cleaning: Removes duplicates and organizes the data for processing
- Dashboard: Shows results in a simple Tkinter app with bar graphs.
- Structured Output: Uses Pydantic to ensure AI responses follow a consistent JSON format for easy analysis.

Tech
- Languages: Python 3.9+
- AI/LLM: OpenAI API, Anthropic SDK, Pydantic
- Data Science: Pandas, NumPy, VADER Sentiment
- API/Web: PRAW (Reddit API), Dotenv
- Visualization: Matplotlib, Tkinter (GUI)

Project Structure


Setup and Intallation


How It Works


Use Case Example


Author
