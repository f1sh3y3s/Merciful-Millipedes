from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.application import Application
from prompt_toolkit.document import Document
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.margins import ScrollbarMargin
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.controls import BufferControl,FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import Frame
from prompt_toolkit.layout import (HSplit, VSplit, FloatContainer, ConditionalContainer, Float, Window)
from prompt_toolkit.application import run_in_terminal

front_buffer = Buffer(document=Document('', 0), read_only=True, name='first_window')
front_buffer_control = BufferControl(buffer=front_buffer)

# Topic Assignment
topics = [
	"world",
    "local",
    "business",
    "technology",
    "entertainment",
    "sports",
    "science",
    "health"
] 

def slide(num):
	global topics
	text = f"Press {topics[num][0].upper()} for {topics[num]}"
	return text


body = HSplit([
	Window(content=front_buffer_control, height=1,
		right_margins=[ScrollbarMargin(display_arrows=True)]),
		VSplit([
			Window(FormattedTextControl(slide(0)), wrap_lines=True, cursorline=True),
            Window(FormattedTextControl(slide(1)), wrap_lines=True),
		], padding_char="|", padding=1), Window(height=1, char="-"),
		VSplit([
			Window(FormattedTextControl(slide(2)), wrap_lines=True, cursorline=True),
            Window(FormattedTextControl(slide(3)), wrap_lines=True),
		], padding_char="|", padding=1), Window(height=1, char="-"),
		VSplit([
			Window(FormattedTextControl(slide(4)), wrap_lines=True, cursorline=True),
            Window(FormattedTextControl(slide(5)), wrap_lines=True),
		], padding_char="|", padding=1), Window(height=1, char="-"),
		VSplit([
			Window(FormattedTextControl(slide(6)), wrap_lines=True, cursorline=True),
            Window(FormattedTextControl(slide(7)), wrap_lines=True),
		], padding_char="|", padding=1), Window(height=1, char="-"),
	
], style='bg:#fefefe fg:#000')


front_page_layout = Frame(body=body, title="Front Page")
