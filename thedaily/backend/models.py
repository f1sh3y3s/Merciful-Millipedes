from dataclasses import dataclass
from typing import List


@dataclass
class NewsPost:
    """A class that stores data from a new post"""

    news_title: str
    source_url: str

    def __repr__(self) -> str:
        return f'{self.news_title}\n'


@dataclass
class RedditPost:
    """A class that stores data from a reddit post"""

    post_title: str
    post_link: str
    subreddit: str

    def __repr__(self) -> str:
        return f'{self.post_title}\nFull Post: {self.post_link}\n'


@dataclass
class JobPost:
    """A class that stores data from a job post"""

    job_title: str
    company_name: str
    job_url: str
    description: List[str]
    job_location: str = "remote"

    def __repr__(self) -> str:
        description_text = ''
        for data in self.description:
            description_text += f'{data}\n'
        return f'Title: {self.job_title}\nComapny: {self.company_name}\
        \nDescription: {description_text}\nRead More: {self.job_url}\n'
