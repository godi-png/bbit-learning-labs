"""Module for retrieving newsfeed information."""

from dataclasses import dataclass
from datetime import datetime
import json

from app.utils.redis import REDIS_CLIENT


@dataclass
class Article:
    """Dataclass for an article."""

    author: str
    title: str
    body: str
    publish_date: datetime
    image_url: str
    url: str


def get_all_news() -> list[Article]:
    """Get all news articles from the datastore."""
    # 1. Use Redis client to fetch all articles
    # 2. Format the data into articles
    # 3. Return the as a list of articles sorted by most recent
    articles_json = REDIS_CLIENT.get_entry("all_articles")
    article_list = list()
    for x in articles_json:
        article_list.append(Article(x["author"], x["title"], x["text"], x["published"], x["thread"]["main_image"], x["url"]))
    return article_list

def get_featured_news() -> Article | None:
    """Get the featured news article from the datastore."""
    # 1. Get all the articles
    # 2. Select and return the featured article
    sorted_articles = sorted(get_all_news(), key = lambda x: datetime.fromisoformat(x.publish_date))
    return sorted_articles