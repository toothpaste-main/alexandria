"""Terminal text editor.

Wraps lines of text wider than 72 characters.
"""
import curses
import os
import time

BUFFER_SIZE = 10

SCROLL_INCREMENT = 1
PAGE_INCREMENT = BUFFER_SIZE

def clear():
    """Clear console screen."""
    # If Windows then 'cls' else 'clear'.
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def load(file_name):
    contents = []
    with open(file_name) as f:
        for line in f:
            contents.append(line.removesuffix('\n'))
    return contents

def render(stdscr, contents):
    edges = [0, BUFFER_SIZE]
    while True:
        stdscr.erase()

        # Move cursor up and down.
        match stdscr.getch():
            case curses.KEY_UP:
                if edges[0] > 0:
                    edges = [e-SCROLL_INCREMENT for e in edges]
            case curses.KEY_DOWN:
                if edges[1] < len(contents):
                    edges = [e+SCROLL_INCREMENT for e in edges]
            case curses.KEY_PPAGE:
                i = min(PAGE_INCREMENT, edges[0])
                edges = [e-i for e in edges]
            case curses.KEY_NPAGE:
                i = min(PAGE_INCREMENT, len(contents)-edges[1])
                edges = [e+i for e in edges]
            

        # Print buffer.
        buffer = contents[edges[0]:edges[1]]
        for y, line in enumerate(buffer):
            stdscr.addstr(y, 0, line)

        stdscr.refresh()

        time.sleep(0.1)


def main(stdscr):
    stdscr.keypad(True)

    # Don't wait for key press to refresh the screen.
    stdscr.nodelay(True)

    stdscr.clear()
    contents = load('alexandria/the_frogs_&_the_ox.txt')
    render(stdscr, contents)


curses.wrapper(main)
