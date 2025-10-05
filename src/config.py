# src/config.py
import os

# Google/SerpApi key (use one method)
SERPAPI_KEY = os.getenv("SERPAPI_KEY", "e61729ec5671312e6ed18392f25ca8c38f3376e85916ac1cb103c3615409f519")

FALSE_PHRASES = [
    "misleading","misinformation","is it","is it true","not known","no proof",
    "no known","no scientific evidence","no evidence","not verified","hoax",
    "clickbait","not proven","denied","deny","unverified","false","fake",
    "fake news","falsely","myth","ridiculous","rumour"
]
