""" ANSI terminal drawing. """

import contextlib
from life import move

ALIVE = 'o'

CLEAR = '\033[2J'
HIDE_CUR = '\033[?25l'
SHOW_CUR = '\033[?25l'
DRAW_FORMAT = '\033[%d;%df' + ALIVE


def draw1(x):
    return DRAW_FORMAT % x


def draw(xs, dx=(1, 1)):
    ps = [(i, j) for i, j in move(xs, dx) if i > 0 and j > 0]
    print CLEAR + ''.join(map(draw1, ps))


@contextlib.contextmanager
def hidden_cursor():
    print HIDE_CUR
    try:
        yield
    finally:
        print SHOW_CUR
