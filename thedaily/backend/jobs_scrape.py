from typing import List

import requests
from bs4 import BeautifulSoup
from random_user_agent.params import OperatingSystem
from random_user_agent.user_agent import UserAgent

BASE_URL = "https://www.indeed.com/"


def get_top_jobs_from_indeed() -> List[str]:
    """
    This function scrapes google news for top news in any topic.

    Returns
    -------
    news: List
        A list of jobs around the location from the ip
    """
    url = BASE_URL + "jobs?l=remote&sort=date"
    agent = UserAgent(operating_systems=[OperatingSystem.LINUX.value]).get_random_user_agent()

    response = requests.get(url, headers={'User-Agent': agent}, allow_redirects=True)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.find_all("div", {"class": "job_seen_beacon"})
