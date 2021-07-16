from typing import Any

from prompt_toolkit.application import Application
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import (
    ConditionalContainer, HSplit, VSplit, Window, WindowAlign
)
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.widgets import Frame

from .crossword import CrossWord


class FrameState:
    """Store state of clue panel visibility"""

    show_clues = False


crossword = CrossWord()

kb_for_puzzle = KeyBindings()

#
# key binidings for puzzle
# , , WindowAlign HSplit, VSplit


@kb_for_puzzle.add('left')
def _(event: Any) -> None:
    crossword.move_left()
    refresh()


@kb_for_puzzle.add('right')
def _(event: Any) -> None:
    crossword.move_right()
    refresh()


@kb_for_puzzle.add('up')
def _(event: Any) -> None:
    crossword.move_up()
    refresh()


@kb_for_puzzle.add('down')
def _(event: Any) -> None:
    crossword.move_down()
    refresh()


@kb_for_puzzle.add('a')
def _(event: Any) -> None:
    crossword.change_current_char("A")
    refresh()


@kb_for_puzzle.add('b')
def _(event: Any) -> None:
    crossword.change_current_char("B")
    refresh()


@kb_for_puzzle.add('c')
def _(event: Any) -> None:
    crossword.change_current_char("C")
    refresh()


@kb_for_puzzle.add('d')
def _(event: Any) -> None:
    crossword.change_current_char("D")
    refresh()


@kb_for_puzzle.add('d')
def _(event: Any) -> None:
    crossword.change_current_char("D")
    refresh()


@kb_for_puzzle.add('e')
def _(event: Any) -> None:
    crossword.change_current_char("E")
    refresh()


@kb_for_puzzle.add('f')
def _(event: Any) -> None:
    crossword.change_current_char("F")
    refresh()


@kb_for_puzzle.add('g')
def _(event: Any) -> None:
    crossword.change_current_char("G")
    refresh()


@kb_for_puzzle.add('h')
def _(event: Any) -> None:
    crossword.change_current_char("H")
    refresh()


@kb_for_puzzle.add('i')
def _(event: Any) -> None:
    crossword.change_current_char("I")
    refresh()


@kb_for_puzzle.add('j')
def _(event: Any) -> None:
    crossword.change_current_char("J")
    refresh()


@kb_for_puzzle.add('k')
def _(event: Any) -> None:
    crossword.change_current_char("K")
    refresh()


@kb_for_puzzle.add('l')
def _(event: Any) -> None:
    crossword.change_current_char("L")
    refresh()


@kb_for_puzzle.add('m')
def _(event: Any) -> None:
    crossword.change_current_char("M")
    refresh()


@kb_for_puzzle.add('n')
def _(event: Any) -> None:
    crossword.change_current_char("N")
    refresh()


@kb_for_puzzle.add('o')
def _(event: Any) -> None:
    crossword.change_current_char("O")
    refresh()


@kb_for_puzzle.add('p')
def _(event: Any) -> None:
    crossword.change_current_char("P")
    refresh()


@kb_for_puzzle.add('q')
def _(event: Any) -> None:
    crossword.change_current_char("Q")
    refresh()


@kb_for_puzzle.add('r')
def _(event: Any) -> None:
    crossword.change_current_char("R")
    refresh()


@kb_for_puzzle.add('s')
def _(event: Any) -> None:
    crossword.change_current_char("S")
    refresh()


@kb_for_puzzle.add('t')
def _(event: Any) -> None:
    crossword.change_current_char("T")
    refresh()


@kb_for_puzzle.add('u')
def _(event: Any) -> None:
    crossword.change_current_char("U")
    refresh()


@kb_for_puzzle.add('v')
def _(event: Any) -> None:
    crossword.change_current_char("V")
    refresh()


@kb_for_puzzle.add('w')
def _(event: Any) -> None:
    crossword.change_current_char("W")
    refresh()


@kb_for_puzzle.add('x')
def _(event: Any) -> None:
    crossword.change_current_char("X")
    refresh()


@kb_for_puzzle.add('y')
def _(event: Any) -> None:
    crossword.change_current_char("Y")
    refresh()


@kb_for_puzzle.add('z')
def _(event: Any) -> None:
    crossword.change_current_char("Z")
    refresh()


@kb_for_puzzle.add('`')
def _(event: Any) -> None:
    crossword.show_answer()
    refresh()


def refresh() -> None:
    """Refresh puzzle panel"""
    puzzle_panel.text = crossword.generate_list()


def show_copyrights_and_controls() -> str:
    """Show author and copyrights and controls"""
    return "© {} {} NY Times | press Tab for see the {}".format(
        crossword.author, crossword.copyright,
        "clues" if not FrameState.show_clues else "crossword")


def show_title() -> str:
    """Show author and copyrights"""
    return "{}".format(crossword.title)


#
# crossword container
#
puzzle_panel = Window(content=FormattedTextControl(
    lambda: crossword.generate_list(),
    show_cursor=False,
    focusable=True,
    key_bindings=kb_for_puzzle),
    align=WindowAlign.CENTER,
    style='bg:#fefefe fg:#000',
    allow_scroll_beyond_bottom=True,
    get_vertical_scroll=lambda x: 1
)
status_bar = Window(
    FormattedTextControl(show_copyrights_and_controls),
    height=1,
    style="reverse"
)
clue_panel_across = Window(
    FormattedTextControl("Across :\n"+crossword.get_across()),
    wrap_lines=True,
    align=WindowAlign.LEFT)
clue_panel_down = Window(
    FormattedTextControl("Down :\n"+crossword.get_down()),
    wrap_lines=True,
    align=WindowAlign.LEFT)
clue_panel = VSplit([
    clue_panel_across,
    Window(width=4, char=" "),
    clue_panel_down, ])

# conditonalcontainer used for hide and show windows
puzzle_view = ConditionalContainer(
    puzzle_panel,
    filter=Condition(lambda: not FrameState.show_clues))

clue_view = ConditionalContainer(
    clue_panel, filter=Condition(lambda: FrameState.show_clues))

kb_for_app = KeyBindings()


@kb_for_app.add("c-q")
def _(event: Any) -> None:
    event.app.exit()


kb_for_main = KeyBindings()


@kb_for_main.add("tab")
def _(event: Any) -> None:
    FrameState.show_clues = not FrameState.show_clues


body = HSplit([
    puzzle_view, clue_view, status_bar],
    key_bindings=kb_for_main)


def crossword_model() -> Frame:
    """Return crossword puzzle frame with clues"""
    return Frame(body, title=crossword.title, style='bg:#fefefe fg:#000')


if __name__ == "__main__":
    application = Application(
        layout=Layout(crossword_model()),
        key_bindings=kb_for_app,
        full_screen=True)
    application.run()
