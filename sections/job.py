import json
import os
import sys

from bs4 import BeautifulSoup
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import (
    focus_next, focus_previous
)
from prompt_toolkit.layout import Dimension, HSplit, ScrollablePane, VSplit
from prompt_toolkit.layout.containers import Container
from prompt_toolkit.widgets import Frame, TextArea

sys.path.insert(0, '..')
from thedaily.backend.scrapers.jobs_scrape import \
    get_top_jobs_from_indeed  # noqa: E402

kb = KeyBindings()

kb.add("up")(focus_next)
kb.add("down")(focus_previous)


def get_job_data() -> str:
    """Function for fetching job data"""
    job_list = get_top_jobs_from_indeed()
    job_document = ''

    if len(job_list) > 0:
        json_array = job_list
        rows = len(json_array) // 3
        cols = 3
        hs = []
        hs.append(VSplit([Frame(TextArea(text='Use arrow to navigate', read_only=True))]))
        for i in range(rows):
            frame = VSplit([
                Frame(
                    TextArea(
                        text=f'{json_array[i*cols+j]}\n', wrap_lines=True, style='bg:#fefefe fg:#000',
                        read_only=True), width=Dimension()) for j in range(3)])

            hs.append(frame)
        return hs
    else:
        base_dir = os.path.abspath('')
        filename = 'sections/job_data.json'
        abs_file = os.path.join(base_dir, filename)
        input_file = open(abs_file)
        json_array = json.load(input_file)
        for item in json_array:
            name = f'Title: {item["name"]}'
            company = f'Company: {item["company"]}'
            description_parser = BeautifulSoup(item['description'], 'html.parser').get_text('\n')
            description = f'Description: {description_parser}'
            job_document += f'{name}\n{company}\n{description}\n{create_blank_lines()}\n\n'
    return job_document


def create_blank_lines() -> str:
    """Function for creating separate lines between job post"""
    blanks = ''
    for _ in range(2):
        for _ in range(97):
            blanks += '-'
        blanks += '\n'
    return blanks


def popup_window(title: str, body: Container) -> Frame:
    """Return the layout for a pop-up window."""
    return Frame(body=body, title=title)


body = ScrollablePane(HSplit(get_job_data(), key_bindings=kb, style='bg:#fefefe fg:#000'))

job_layout = popup_window('Top Jobs', body)
