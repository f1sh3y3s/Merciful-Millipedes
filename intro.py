from typing import Any

from prompt_toolkit import HTML
from prompt_toolkit.application import Application
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import (
    ConditionalContainer, Float, FloatContainer, HSplit, Window
)
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.dimension import LayoutDimension as D
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import Button, Dialog

from crossword_widget.puzzle_widget import crossword_model
from sections.job import job_layout

# KEY BINDINGS
kb = KeyBindings()


@kb.add('j')
def _(event: Any) -> None:
    """Toggle job window"""
    JobStates.show_job = not JobStates.show_job


@kb.add('c')
def _(event: Any) -> None:
    """Toggle crossword window"""
    PuzzleStats.show_puzzle = not PuzzleStats.show_puzzle


@kb.add('q')
def _(event: Any) -> None:
    """Key bindings for quitting application"""
    event.app.exit()


with open("ascii_image.txt", "r") as file:
    ASCII_NAME = "".join(i for i in file.readlines())
    file.close()

intro_text = """
Hello and welcome to (newspaper name goes here). The most trusted news page in all the lands. Here you will 
recieve the latest news on all topics ranging from World News to National News to Sports and various other 
sections.

To enter the page, <b> Please enter 'o' </b>
To exit the current page, <b>Please enter 'Q' </b>
"""
intro_page_split = HSplit([FloatContainer(content=HSplit([Window(content=FormattedTextControl(text=ASCII_NAME),height=D.exact(1),),
    Window(content=FormattedTextControl(HTML(intro_text)), height=10)],style='bg:#fefefe fg:#000', padding=1, padding_char="-"), floats=[Float(width=100, height=30, top=3, bottom=2,
    content=ConditionalContainer(content=job_layout, filter=Condition(lambda: JobStates.show_job))),
	Float(width=100, height=30, top=3, bottom=2,
    content=ConditionalContainer(content=crossword_model(), filter=Condition(lambda: PuzzleStats.show_puzzle)))
	]),
])


def job_page() -> None:
    """Button for starting job"""
    JobStates.show_job = not JobStates.show_job


def crossword_page() -> None:
    """Button for starting puzzle"""
    PuzzleStats.show_puzzle = not PuzzleStats.show_puzzle


job_button = Button(text="JOB", handler=job_page)


crossword_button = Button(text="PLAY CROSSWORD", handler=crossword_page)


class PuzzleStats:
    """Store state of puzzle window"""

    show_puzzle = False


class JobStates:
    """Store state of job window"""

    show_job = False


dialog = Dialog(title='NewsPaper', body=intro_page_split, buttons=[job_button, crossword_button],
                width=D(),
                modal=False)

app = Application(layout=Layout(intro_page_split),key_bindings=kb, full_screen=True)


app.run()
