from typing import List, Optional

import requests
from bs4 import BeautifulSoup
from random_user_agent.params import OperatingSystem
from random_user_agent.user_agent import UserAgent

BASE_URL = "https://news.google.com"


def get_top_news_from_googlenews(topic: [Optional] = None) -> List[str]:
    """
    This function scrapes google news for top news in any topic.

    Parameters
    ----------
    topic: {"world","local","business","technology","entertainment","sports","science","health"},optional
        The topic to get the news from, the default is hot news

    Returns
    -------
    news: List
        A list of news from the given topic / hot news
    """
    if topic and topic.lower() not in [
        "world",
        "local",
        "business",
        "technology",
        "entertainment",
        "sports",
        "science",
        "health",
    ]:
        raise ValueError("""The available values of topics are only
                                                        World, Local, Business, Technology, Entertainment,
                                                        Sports, Science, Health""")

    topic_url = ""
    agent = UserAgent(operating_systems=[OperatingSystem.LINUX.value]).get_random_user_agent()

    if topic:
        if topic.lower() == "local":
            topic = "your local news"

        response = requests.get(BASE_URL, headers={'User-Agent': agent}, allow_redirects=True)
        soup = BeautifulSoup(response.text, 'html.parser')

        topic_tag = soup.find(lambda tag: tag.name == "span" and tag.text.lower() == topic.lower())
        topic_url = topic_tag.parent.parent.get("href")

    url = BASE_URL + topic_url

    response = requests.get(url, headers={'User-Agent': agent}, allow_redirects=True)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.find_all("h3")
