import re
from datetime import datetime
from typing import List, Dict, Optional

import pandas as pd
import praw
from pathlib import Path


class Reddit:
    def __init__(self):
        # Reddit API credentials
        self.client_id = "HXZPaigOHwekwXJnzrzcpg"
        self.client_secret = "Lp_gNkS3REot4SpeYAQ7xqRm-6pZyw"
        self.user_agent =  "reddit-sentiment/1.0"

        if not self.client_id or not self.client_secret:
            raise RuntimeError(
                "Missing Reddit credentials. Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET."
            )
        
        # Initializes PRAW Reddit client
        self.reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent,
            ratelimit_seconds=5,
        )

        # Regex patterns for extracting tags and hashtags from titles
        self.TAG_PATTERN = re.compile(r"\[(.*?)\]")  
        self.HASHTAG_PATTERN = re.compile(r"(#\w+)")


    def extract_tags(self, title: str, flair: Optional[str]) -> List[str]:
        """Extracts unique tags from post title and flair"""
        tags = []
        if flair:
            tags.append(flair.strip())

        if title:
            tags.extend([t.strip() for t in self.TAG_PATTERN.findall(title)])
            tags.extend([h.strip("#") for h in self.HASHTAG_PATTERN.findall(title)])

        # Normalize to lowercase to remove duplicates
        seen = set()
        normed = []
        for t in tags:
            key = t.lower()
            if key not in seen:
                seen.add(key)
                normed.append(t)
        return normed
    
    
    def clean_text(self, text: str) -> str:
        """Removes URLs and extra spaces from text"""
        if not text:
            return ""
        text = re.sub(r"http\S+|www\.\S+", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text
    
    
    def fetch_posts(self, reddit, query: str, limit_posts: int, sort: str,
                    subreddits: Optional[List[str]] = ['all']):
        """Generator: fetch posts from given subreddits"""
        for sub in subreddits:
            subreddit = reddit.subreddit(sub)
            results = subreddit.search(query=query, sort=sort, limit=limit_posts)
            for post in results:
                yield post
    

    def get_csv_reviews(self, item) -> pd.DataFrame:
        """Fetch Reddit reviews for an Apple product and save to CSV"""
        item = item
        records: List[Dict] = []
        seen_posts = set()

        # Fetch posts
        for post in self.fetch_posts(reddit=self.reddit, query=f'{item} review', limit_posts=50, sort='relevance'):
            if post.id in seen_posts:
                continue
            seen_posts.add(post.id)

            title = self.clean_text(getattr(post, "title", "") or "")

            selftext = self.clean_text(getattr(post, "selftext", "") or "")

            # Skip posts with no body text or posts that were deleted/removed
            if not selftext:
                continue
            if selftext.lower() in ("[deleted]", "[removed]"):
                continue

            # Adds post data to records
            records.append({
                "post_id": post.id,
                "title": title,
                "created_utc": datetime.fromtimestamp(getattr(post, "created_utc", 0)).strftime("%Y-%m-%d %H:%M:%S"),
                "author": str(getattr(post, "author", "Reddit User")),
                "tags": self.extract_tags(title, getattr(post, "link_flair_text", None)),
                "review_texts": selftext
            })

        # Saves to CSV
        df = pd.DataFrame.from_records(records)
        project_root = Path(__file__).resolve().parent.parent
        outdir = project_root / "Sentiment_Analyzer"
        outdir.mkdir(parents=True, exist_ok=True)

        ts = datetime.now().strftime("%H-%M-%S")
        outfile = outdir / f"reddit_{item}_{ts}.csv"
        df.to_csv(outfile, index=False)
        return outfile

if __name__ == "__main__":
    reddit_analyzer = Reddit()
    item = input("Enter Item: ")
    reddit_analyzer.get_csv_reviews(item)