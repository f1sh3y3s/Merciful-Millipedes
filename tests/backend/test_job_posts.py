import unittest

from thedaily import get_top_jobs_from_indeed


class TestSubRedditScraper(unittest.TestCase):
    """Unit Tests to test the scraper"""

    def test_r_all(self) -> None:
        """Tests indeed jobs scraper for results"""
        return self.assertNotEqual(len(get_top_jobs_from_indeed()), 0)
