from reviews import Reddit
from AI_Models.openai_analyzer import AIModelAnalyzer
from visual import DataVisualizer
from dotenv import load_dotenv
import os

class SentimentPipeline:
    """
    Manages the end-to-end Apple product review sentiment analysis

    Steps:
    1. Extracts reviews from Reddit
    2. Analyzes feature-specific sentiment using AI models
    3. Visualizes results with interactive dashboard
    """

    def __init__(self, api_key: str):
        # Initializes Reddit client, AI model analyzer, and visualization tools
        self.reddit_client = Reddit()
        self.analyzer = AIModelAnalyzer(api_key=api_key)
        self.visualizer = DataVisualizer()

    def run_analysis(self):
        """
        Executes the full workflow:
        1. Gets user input for product name
        2. Extracts product reviews from Reddit and saves to CSV
        3. Loads reviews and performs multi-dimensional sentiment analysis
        4. Visualizes results using interactive dashboards
        """

        item = self.visualizer.get_user_input()                                         # Prompts user for product to analyze
        outfile = self.reddit_client.get_csv_reviews(item)                              # Extracts reviews from Reddit and saves them to a CSV file
        reviews = self.analyzer.load_reviews_from_csv(outfile, product_name=item)       # Loads reviews from CSV for analysis
        result = self.analyzer.analyze_reviews(reviews)                                 # Multi-dimensional sentiment analysis
        self.visualizer.show_results(result)                                            # Displays results with a chart

# Loads API keys and environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
    
if __name__ == "__main__":
    pipeline = SentimentPipeline(api_key)
    pipeline.run_analysis()