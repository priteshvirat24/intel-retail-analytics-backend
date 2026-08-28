from app.crawlers.base import BaseCrawler, CrawlerResponse
from app.crawlers.http import HttpCrawler
from app.crawlers.playwright import PlaywrightCrawler
from app.crawlers.scrapy_bridge import ScrapyCrawlerBridge

__all__ = [
    "BaseCrawler",
    "CrawlerResponse",
    "HttpCrawler",
    "PlaywrightCrawler",
    "ScrapyCrawlerBridge",
]
