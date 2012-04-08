#!/usr/bin/env python
import curses
from morse_parser import *

try:
	screen = curses.initscr()

	# Configure terminal mode
	curses.noecho()
	curses.cbreak()

	_buffer = ''
	_parser = MorseParser()

	screen.addstr('Reading Morse... (Use dots[.], dashes[-] or whitespaces): \n')

	while True:
		try:
			_char = screen.getch()

			# Whitespace
			if _char == 0x20:
				if _parser.has_code(_buffer):
					screen.addstr(_parser.parse(_buffer))
					screen.refresh()

				_buffer = ''

			# No whitespace, add char to buffer
			else:
				_buffer += chr(_char)

		except IOError: pass
finally:
	curses.nocbreak(); curses.echo()
	curses.endwin()