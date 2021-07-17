from typing import Any

from prompt_toolkit import HTML
from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import (
    Float, FloatContainer, HSplit, Window, WindowAlign
)
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout

from crossword_widget import crossword_model
from front_page import front_layout
from pong_game_easy import game
from reddit import reddit_layout
from sections.job import job_layout

model = crossword_model()
jb_layout = job_layout
fr_layout = front_layout
rd_layout = reddit_layout

with open("ascii_image.txt", "r") as file:
    ASCII_NAME = "".join(i for i in file.readlines())
    file.close()

ASCII_NAME = ASCII_NAME.translate(str.maketrans({".": " ", "!": " ", ":": " "}))
intro_text = """
Hello and welcome to (newspaper name goes here). The most trusted news page in all the lands. Here you will
  the latest news on all topics ranging from World News to National News to Sports and various other
 sections.

To change between the pages, <b> Please enter 'tab' </b>
To go back, <b> Please enter 'shift-tab' </b>
To exit the current page, <b>Please enter 'Q' </b>
Want to break out of terminal? <b>Press P to play pong </b>
"""


class NewspaperState:
    """Hold attributes for Newspaper"""

    state = "center"
    current_float = None  # hold current float element
    models = [fr_layout, jb_layout, model, rd_layout]  # all float elements
    window_no = 0  # remeber what float in
    float_active = False  # check i float is active
    main_window = None  # hold main window for focus


body = FloatContainer(
    content=HSplit([Window(
        FormattedTextControl(ASCII_NAME), align=WindowAlign.CENTER, style='bg:#fefefe fg:#000'),
        Window(
            FormattedTextControl(HTML(intro_text)),
            align=WindowAlign.CENTER,
            style='bg:#fefefe fg:#000')]), floats=[])


def next_page(event: Any) -> None:
    """Go to next page"""
    if not NewspaperState.main_window:
        NewspaperState.main_window = event.app.layout.current_window
    if not NewspaperState.float_active:
        obj = NewspaperState.models[NewspaperState.window_no % len(NewspaperState.models)]
        _float = Float(obj, width=100)
        NewspaperState.window_no += 1
        body.floats.insert(0, _float)
        NewspaperState.current_float = _float
        NewspaperState.float_active = True
        event.app.layout.focus(obj)
    else:
        _float = NewspaperState.current_float
        if _float in body.floats:
            body.floats.remove(_float)
            NewspaperState.float_active = False
            event.app.layout.focus(NewspaperState.main_window)
            NewspaperState.float_active = False


def previous_page(event: Any) -> None:
    """Go to previos page"""
    if not NewspaperState.main_window:
        NewspaperState.main_window = event.app.layout.current_window
    if not NewspaperState.float_active:
        page_num = NewspaperState.window_no - 1
        if page_num < 0:
            page_num = len(NewspaperState.models) - 1
        obj = NewspaperState.models[page_num % len(NewspaperState.models)]
        _float = Float(obj, width=100)
        NewspaperState.window_no = page_num
        body.floats.insert(0, _float)
        NewspaperState.current_float = _float
        NewspaperState.float_active = True
        event.app.layout.focus(obj)
    else:
        _float = NewspaperState.current_float
        if _float in body.floats:
            body.floats.remove(_float)
            NewspaperState.float_active = False
            event.app.layout.focus(NewspaperState.main_window)
            NewspaperState.float_active = False


# 2. Key bindings
kb = KeyBindings()


@kb.add("q")
def _(event: Any) -> None:
    """Quit application."""
    event.app.exit()


@kb.add("tab")
def _(event: Any) -> None:
    next_page(event)


@kb.add("s-tab")
def _(event: Any) -> None:
    previous_page(event)


@kb.add("p")
def _(event: Any) -> None:
    game()


# 3. The `Application`
application = Application(
    layout=Layout(body),
    key_bindings=kb,
    full_screen=True,
    enable_page_navigation_bindings=True,)


def run() -> None:
    """Run application"""
    application.run()


if __name__ == "__main__":
    run()
