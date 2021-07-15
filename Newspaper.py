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

# Shortening this long thing
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

def sorting(w_list):
    main_L = [Window(content=front_buffer_control, height=1,
		right_margins=[ScrollbarMargin(display_arrows=True)])]

    for j in range(4):
    	side_L = []

    	for i in range(2*j, (2*j)+2):
	        txt = f"Please press {w_list[i][0].upper()} for {w_list[i].capitalize()} News"
	        side_L += [Window(FormattedTextControl(txt), wrap_lines=True, cursorline=True, align=WindowAlign.CENTER)]

    	split_section =[VSplit(side_L, padding_char="|", padding=1), Window(height=1, char="-")]
    	main_L+=split_section

    return main_L

body = HSplit(sorting(topics), style='bg:#fefefe fg:#000')


front_page_layout = Frame(body=body, title="Front Page")
