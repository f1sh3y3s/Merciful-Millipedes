import json
import os

from bs4 import BeautifulSoup
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.document import Document
from prompt_toolkit.layout.containers import Container, ScrollOffsets, Window
from prompt_toolkit.layout.controls import BufferControl
from prompt_toolkit.layout.margins import ScrollbarMargin
from prompt_toolkit.widgets import Frame


def get_job_data() -> str:
    """Function for fetching job data"""
    base_dir = os.path.abspath('')
    filename = 'sections/job_data.json'
    abs_file = os.path.join(base_dir, filename)
    input_file = open(abs_file)
    json_array = json.load(input_file)
    job_document = ''
    for item in json_array:
        name = f'Title: {item["name"]}'
        company = f'Company: {item["company"]}'
        description_parser = BeautifulSoup(item['description'], 'html.parser').get_text('\n')
        description = f'Description: {description_parser}'
        blanks = ''
        for _ in range(2):
            for _ in range(100):
                blanks += '-'
            blanks += '\n'
        job_document += f'{name}\n{company}\n{description}\n{blanks}\n\n'
    return job_document


# get_job_data()

def popup_window(title: str, body: Container) -> Frame:
    """Return the layout for a pop-up window."""
    return Frame(body=body, title=title)


job_buffer = Buffer(name='job_window', read_only=True, document=Document(get_job_data(), 0),)
job_buffer_control = BufferControl(buffer=job_buffer)
body = Window(content=job_buffer_control, right_margins=[ScrollbarMargin(display_arrows=True)],
              scroll_offsets=ScrollOffsets(top=2, bottom=2), style='bg:#fefefe fg:#000')


job_layout = popup_window('Top Jobs', body)
