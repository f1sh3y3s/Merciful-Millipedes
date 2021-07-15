from typing import List, Optional

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from random_user_agent.params import OperatingSystem
from random_user_agent.user_agent import UserAgent

from ..models import RedditPost

BASE_URL = "https://old.reddit.com"
NEW_BASE_URL = "https://reddit.com"


def get_top_posts_from_subreddit(subreddit: str, sort_by: [Optional] = "hot") -> List[str]:
    """
    This function scrapes through the subreddit of your choice and returns the top 24 posts from it.

    Parameters
    ----------
    subreddit: str
        The name of the subreddit that you want to scrape.
    sort_by: {"hot","new","rising","controversial","top"},optional
        The order to sort the posts by
    """
    if sort_by.lower() not in ["hot", "new", "rising", "controversial", "top"]:
        raise ValueError("The available values of sort_by are only Hot, New, Rising, Controversial, Top")

    url = BASE_URL + "/r/" + subreddit + "/" + sort_by
    agent = agent = UserAgent(operating_systems=[OperatingSystem.LINUX.value]).get_random_user_agent()

    response = requests.get(url, headers={'User-Agent': agent})
    soup = BeautifulSoup(response.text, 'html.parser')

    main_domain = max(
        domain.text for domain in soup.find_all("span", {"class": "domain"})
    )

    posts = [
        domain.parent.parent.parent
        for domain in soup.find_all("span", {"class": "domain"})
        if domain.text == main_domain  # This will get rid of the ads on the page
    ]

    return list(map(sterilize_post, posts))


def sterilize_post(post: Tag) -> RedditPost:
    """This function coverts bs4 tag to a sterilized model object"""
    url = NEW_BASE_URL + post.find("a").get("href")
    title = post.find("a").text
    subreddit = post.find("span", {"class": "domain"}).text[6:-1]

    return RedditPost(post_link=url, post_title=title, subreddit=subreddit)
