import unittest

from thedaily import get_top_news_from_googlenews


class TestGoogleNewsScraper(unittest.TestCase):
    """Unit Tests to test the scraper"""

    def test_hot_news(self) -> None:
        """Tests the scraper with no topic"""
        return self.assertNotEqual(len(get_top_news_from_googlenews()), 0)

    def test_sports_news(self) -> None:
        """Tests the scraper with a basic topic"""
        return self.assertNotEqual(len(get_top_news_from_googlenews("sports")), 0)
