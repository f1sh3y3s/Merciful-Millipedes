import unittest

from thedaily import get_top_posts_from_subreddit


class TestSubRedditScraper(unittest.TestCase):
    """Unit Tests to test the scraper"""

    def test_r_all(self) -> None:
        """Tests scraper with r/all subreddit"""
        return self.assertNotEqual(len(get_top_posts_from_subreddit("all")), 0)
