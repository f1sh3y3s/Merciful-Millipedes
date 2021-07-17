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
from thedaily.backend.scrapers.news_scrape import \
    get_top_news_from_googlenews  # noqa: E402

kb = KeyBindings()


kb.add("up")(focus_next)
kb.add("down")(focus_previous)


def get_news_data() -> str:
    """Function for fetching job data"""
    topics = ['world', 'business', 'technology', 'entertainment', 'sports', 'science', 'health']
    all_news = []
    for topic in topics:
        news = get_top_news_from_googlenews(topic)
        all_news.append(news[:6])
    rows = len(all_news) // 2
    cols = 2
    hs = []
    for t_idx in range(rows):
        frame = ScrollablePane(VSplit([Frame(TextArea(text=f'Topic: {topics[t_idx*cols + j]}\n\n{formatted_string(all_news[j + t_idx])}\n',
                               wrap_lines=True, style='bg:#fefefe fg:#000'),
                               width=Dimension()) for j in range(2)]))
        hs.append(frame)
    return hs


def formatted_string(arr: List) -> str:
    """Function for formatting string"""
    return '\n*'.join([str(elem) for elem in arr])


def popup_window(title: str, body: Container) -> Frame:
    """Return the layout for a pop-up window."""
    return Frame(body=body, title=title)


body = ScrollablePane(HSplit(get_news_data(), key_bindings=kb, style='bg:#fefefe fg:#000'))

front_layout = popup_window('Top Jobs', body)
