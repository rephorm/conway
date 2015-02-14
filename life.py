""" Conway's Game of Life on an infinite board.
"""

import collections

_R = xrange(-1, 2)
_O = [(i, j) for i in _R for j in _R if i or j]


def move1(x, dx):
    """ For x = (i, j), dx = (di, dj), returns x + j = (i + di, j + dj). """
    return tuple(a + b for a, b in zip(x, dx))


def move(xs, dx):
    """ Returns cells that are neighbors of x = (i,j) """
    return set([move1(x, dx) for x in xs])


def neighbors(x):
    """ Returns cells that are neighbors of x = (i,j) """
    return move(_O, x)


def count_neighbors(living):
    """ Returns dict of (x,y) => num_neighbors for all cells. """
    n = collections.Counter()
    for x in map(neighbors, living):
        n.update(x)
    return dict(n)


def step(living):
    """ Returns next state. """
    return set([k for k, v in count_neighbors(living).iteritems()
                if (k in living and v == 2) or v == 3])

if __name__ == "__main__":
    import shapes, term, time

    living = shapes.hbar(9)
    dx = (6, 6)
    with term.hidden_cursor():
        while True:
            term.draw(living, dx)
            living = step(living)
            time.sleep(0.1)
