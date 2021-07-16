from prompt_toolkit import HTML, print_formatted_text, prompt
from prompt_toolkit.application import Application, run_in_terminal
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.filters import has_focus
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import (
    ConditionalContainer, Float, FloatContainer, HSplit, VSplit, Window
)
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout

from Newspaper import front_buffer, front_buffer_control, front_page_layout
from sections.job import job_buffer, job_buffer_control, job_layout

# KEY BINDINGS
kb = KeyBindings()


@kb.add('o')
def _(event):
    """Toggling"""
    app.layout.current_control = front_buffer_control


@kb.add('j')
def _(event):
    """Toggle window"""
    if app.layout.current_control == job_buffer_control:
        app.layout.focus_previous()
    else:
        app.layout.current_control = job_buffer_control


@kb.add('q')
def _(event):
	event.app.exit()

@kb.add('b')
def _(event):
	app.layout.focus_previous()

# Layout
buffer1 = Buffer()

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

intro_page = HSplit([
	# Controls the Key Binding controls
	Window(content=BufferControl(buffer=buffer1), width=1, height=1),

	# The Main Intro Page
	FloatContainer(content=HSplit([
		# WILL CONTAIN THE NEWSPAPER HEADING 
		Window(content=FormattedTextControl(text=ASCII_NAME), height=10),
		Window(content=FormattedTextControl(HTML(intro_text)), height=10),

	], style='bg:#fefefe fg:#000', padding=1, padding_char="-"), 
	floats=[Float(width=100, height=30, top=3, bottom=2,
        content=ConditionalContainer(content=front_page_layout, filter=has_focus(front_buffer))),
				Float(width=100, height=30, top=3, bottom=2,
        content=ConditionalContainer(content=job_layout, filter=has_focus(job_buffer)))
				]),
])

app = Application(layout=Layout(intro_page), key_bindings=kb, full_screen=True)
app.run()
