from dataclasses import dataclass


@dataclass
class NewsPost:
    """A class that stores data from a new post"""

    news_title: str
    source_url: str


@dataclass
class RedditPost:
    """A class that stores data from a reddit post"""

    post_title: str
    post_link: str
    subreddit: str


@dataclass
class JobPost:
    """A class that stores data from a job post"""

    job_title: str
    company_name: str
    job_url: str
    job_location: str = "remote"
