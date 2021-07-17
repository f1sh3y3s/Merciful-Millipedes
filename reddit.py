import sys
from typing import List

from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import (
    focus_next, focus_previous
)
from prompt_toolkit.layout import Dimension, HSplit, ScrollablePane, VSplit
from prompt_toolkit.layout.containers import Container
from prompt_toolkit.widgets import Frame, TextArea

sys.path.insert(0, '..')
from thedaily.backend.scrapers.reddit_scrape import \
    get_top_posts_from_subreddit  # noqa: E402

kb = KeyBindings()


kb.add("up")(focus_next)
kb.add("down")(focus_previous)


def get_reddit_data() -> str:
    """Function for fetching reddit data"""
    topics = ['python', 'minecraft', 'todayilearned', 'programming', 'gaming', 'funny', 'GetMotivated']
    all_news = []
    found_topics = []
    for topic in topics:
        news = get_top_posts_from_subreddit(topic)
        if len(news) > 0:
            all_news.append(news[:6])
            found_topics.append(topic)
    rows = len(all_news) // 2
    cols = 2
    hs = []
    hs.append(VSplit([Frame(TextArea(text='Use arrow to navigate', read_only=True))]))
    for t_idx in range(rows):
        frame = ScrollablePane(VSplit([Frame(TextArea(text=f'Topic: {found_topics[t_idx*cols + j]}\n\n'
                                       f'{formatted_string(all_news[t_idx*cols + j])}\n',
                               wrap_lines=True, style='bg:#fefefe fg:#000', read_only=True),
                               width=Dimension()) for j in range(2)]))
        hs.append(frame)
    return hs


def formatted_string(arr: List) -> str:
    """Function for formatting string"""
    if arr and len(arr) > 0:
        return '\n*'.join([str(elem) for elem in arr])
    return ''


def popup_window(title: str, body: Container) -> Frame:
    """Return the layout for a pop-up window."""
    return Frame(body=body, title=title)


body = ScrollablePane(HSplit(get_reddit_data(), key_bindings=kb, style='bg:#fefefe fg:#000'))

reddit_layout = popup_window('Top Reddit Post', body)
