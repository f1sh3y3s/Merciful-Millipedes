
import os
from collections import defaultdict, namedtuple
from datetime import datetime
from itertools import chain
from typing import List, Optional

import puz
import xword_dl

'''
    To download crossword use `xword-dl tny --latest`
'''

Point = namedtuple("Point", "x y")


class CrossWord:
    """
    Create crossword puzzle object using .puz file.

    :param file_name: The path to puz file. A downloaded puz is supplied
    as default
    """

    TEST_PUZ_FILE = os.path.join(os.path.dirname(__file__), "nyk2.puz")  # puz

    def __init__(self, file_name: Optional[str] = TEST_PUZ_FILE) -> None:
        self.puzzle = puz.read(file_name) if file_name else puz.read(self.TEST_PUZ_FILE)
        self.author = self.puzzle.author
        self.title = self.puzzle.title  # date
        self.copyright = self.puzzle.copyright  # empty
        self.cursor_pos = Point(0, 0)
        self.row = defaultdict()
        self.cells = defaultdict(lambda: None)
        numbering = self.puzzle.clue_numbering()
        self.width = numbering.width
        self.height = numbering.height
        self.clues = {}
        self._generate_cells()
        self._add_across_and_down()
        self.style = 'bg:#fefefe fg:#000'

    def _generate_cells(self) -> None:
        """Create all cells in puzzle"""
        for i in range(15):
            for j in range(15):
                c = Cell(x=i, y=j)
                c.answer = self.puzzle.solution[j*self.width+i]
                self.cells[(j, i)] = c  # row, col

    def _add_across_and_down(self) -> None:
        """Add across and down clues and numbers"""
        numbering = self.puzzle.clue_numbering()
        small_nums = str.maketrans('1234567890', '₁₂₃₄₅₆₇₈₉₀')
        self.clues['across'] = []
        for i in numbering.across:
            row = int(i['cell']/numbering.width)
            col = i['cell'] % numbering.width
            self.cells[(row, col)].num = str(i['num']).translate(small_nums)
            self.clues['across'].append(str(i['num'])+". "+i['clue'])

        self.clues['down'] = []
        for i in numbering.down:
            row = int(i['cell']/numbering.width)
            col = i['cell'] % numbering.width
            self.cells[(row, col)].num = str(i['num']).translate(small_nums)
            self.clues['down'].append(str(i['num'])+". "+i['clue'])

    def generate_list(self) -> List:
        """Create a list contain (style,text) with cells"""
        bar = (self.style, "│")
        output = [self.generate_topline()]
        for i in range(self.height):
            output += [bar]
            output += chain.from_iterable([
                self.cells[(i, j)].as_tuple(False) if self.cursor_pos != (i, j)
                else self.cells[(i, j)].as_tuple(True)
                for j in range(self.width)
            ])
            output += [(self.style, "\n")]
            if i < self.height-1:
                output.append(self.generate_middleline())
            else:
                pass
        output.append(self.generate_bottomline())
        return output

    def change_cell_bgcolor(self, cell: tuple, color: str = "#fefefe") -> None:
        """Change single cell background color default value is #fefefe"""
        self.cells[cell].set_background(color)

    def generate_middleline(self) -> tuple:
        """Generate middle line in crossword"""
        line_sep = "├" + "┼".join([
            "───" for _ in range(self.width)]) + "┤\n"
        return (self.style, line_sep)

    def generate_topline(self) -> tuple:
        """Generate top line in crossword"""
        line_top = "┌" + "┬".join([
            "─" + "─" + "─" for _ in range(self.width)]) + "┐\n"
        return (self.style, line_top)

    def generate_bottomline(self) -> tuple:
        """Generate bottom line in crossword"""
        line_end = "└"+"┴".join([
            "───" for _ in range(self.width)]) + "┘\n"
        return (self.style, line_end)

    def move_left(self, step: int = 1) -> None:
        """Move color block left"""
        if self.cursor_pos.y == 0:
            self.cursor_pos = Point(self.cursor_pos.x, self.width-step)
        else:
            self.cursor_pos = Point(self.cursor_pos.x, self.cursor_pos.y-step)

    def move_right(self, step: int = 1) -> None:
        """Move color block right"""
        if self.cursor_pos.y < self.width - 1:
            self.cursor_pos = Point(self.cursor_pos.x, self.cursor_pos.y+step)
        else:
            self.cursor_pos = Point(self.cursor_pos.x, 0)

    def move_up(self, step: int = 1) -> None:
        """Move color block up"""
        if self.cursor_pos.x == 0:
            self.cursor_pos = Point(self.height - step, self.cursor_pos.y)
        else:
            self.cursor_pos = Point(self.cursor_pos.x-step, self.cursor_pos.y)

    def move_down(self, step: int = 1) -> None:
        """Move color block down"""
        if self.cursor_pos.x < self.height - 1:
            self.cursor_pos = Point(self.cursor_pos.x+step, self.cursor_pos.y)
        else:
            self.cursor_pos = Point(0, self.cursor_pos.y)

    def change_current_char(self, character: str) -> None:
        """Change cell character"""
        cell = self.cells[(self.cursor_pos)]
        if not cell.block:
            cell.change_current(character)

    def get_across(self) -> str:
        """Return across clues"""
        return "".join(self.clues["across"])

    def get_down(self) -> str:
        """Return down clues"""
        return "".join(self.clues["down"])

    def show_answer(self) -> None:
        """Set show answer in cells"""
        for _, cell in self.cells.items():
            cell.set_answer()


class Cell:
    """
    Cell is a single block in puzzle

    :param answer: answer in cell
    :param num: numbering in cell
    :param x: column number
    :param y: row number
    """

    def __init__(
        self,
        answer: str = "",
        num: str = "",
        x: int = 0,
        y: int = 0
    ):
        self.answer: str = answer.rjust(1)
        self.num: str = num
        self.x: int = x  # column number
        self.y: int = y  # row number
        self.style_fg = '#000'
        self.style_bg = '#fefefe'
        self.style_bg_selected = "green"
        self.on_cursor = False
        self.check_ans = False  # show answers
        self.current = ""
        self.block = self.answer == "."

    def __repr__(self) -> str:
        return self.answer if self.answer != "." else "▐" + "█" + "▌"

    def as_tuple(self, selected: bool) -> tuple:
        """Return tuple (style,text) format"""
        if self.check_ans:
            current = self.num.ljust(2) + self.answer
        else:
            current = self.num.ljust(2)+self.current.rjust(1)
        return ((
            "fg:"+self.style_fg + " bg:"  # apply foreground color
            + (self.style_bg_selected if selected else self.style_bg),
            current
            if self.answer != "." else "▐" + "█" + "▌"), ('bg:#fefefe fg:#000', "│"))

    def set_background(self, color: str) -> None:
        """Set backgroundcolor of cell"""
        self.style_bg = color

    def on_cursor(self, enable: bool) -> None:
        """Make cell selected view"""
        self.on_cursor = enable

    def change_current(self, character: str) -> None:
        """Set current showing character"""
        self.current = character

    def is_block(self) -> bool:
        """Return true if cell is a block"""
        return self.answer == "."

    def set_answer(self) -> None:
        """Show answer in cell"""
        if self.check_ans:
            self.check_ans = False
        else:
            self.check_ans = True


def download_crossword() -> str:
    """
    Download NYT crossword using xword-dl

    :return: file path to puz file
    """
    name = datetime.strftime(datetime.now(), "%Y%m%d")
    file_path = os.path.join(os.path.abspath(os.path.curdir), name+".puz")
    try:
        nyk = xword_dl.NewYorkerDownloader()
        obj = nyk.download(nyk.find_latest())
        xword_dl.save_puzzle(obj, file_path)
        return file_path
    except xword_dl.requests.ConnectionError:
        return None
