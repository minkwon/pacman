import curses
import signal
import atexit


# Set up
stdscr = curses.initscr()
# Don't show what user pressed on screen
curses.noecho()
# No need to press enter to input key
curses.cbreak()
# keypad mode on
stdscr.keypad(True)


"""
    It clears the screen and
    returns the keyboard input

    It returns either

    'left', 'right', 'up', 'down', or 'bad'
"""
def get_input():
    stdscr.nodelay(False)
    c = stdscr.getch()
    stdscr.clear()
    if c == 260:
        return 'left'
    elif c == 261:
        return 'right'
    elif c == 259:
        return 'up'
    elif c == 258:
        return 'down'
    else:
        return 'bad'


"""
    Prints the string at row
"""
def print_on_screen(string, row):
    stdscr.addstr(row, 0, string)


def singal_cleanup(signal, frame):
    curses.endwin()
    exit(0)


def exit_cleanup():
    curses.endwin()
    exit(0)


# Even if you press Ctrl C, it will shutdown properly.
signal.signal(signal.SIGINT, singal_cleanup)
# At shutdown, cleanup
atexit.register(exit_cleanup)
