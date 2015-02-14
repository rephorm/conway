""" Conway's Game of Life on an infinite board.

Throughout the following, points are represented by tuples (i,j).
"""

import collections

_R = xrange(-1, 2)
_OFFSETS = [(i, j) for i in _R for j in _R if i or j]


def move1(x, dx):
    """ Move x = (i, j) by dx = (di, dj). """
    return tuple(a + b for a, b in zip(x, dx))


def move(xs, dx):
    """ Returns result of moving each point in xs by dx. """
    return set([move1(x, dx) for x in xs])


def neighbors(x):
    """ Returns cells that are neighbors of x = (i,j). """
    return move(_OFFSETS, x)


def neighbor_counts(living):
    """ Returns dict of pt => num_neighbors for all pts with neighbors. """
    n = collections.Counter()
    for x in map(neighbors, living):
        n.update(x)
    return dict(n)


def step(living):
    """ Returns set of living cells after time-stepping. """
    return set([k for k, v in neighbor_counts(living).iteritems()
                if (k in living and v == 2) or v == 3])


if __name__ == "__main__":
    import shapes
    import term
    import time

    living = set.union(
        move(shapes.hbar(9), (5, 5)),
        move(shapes.hbar(9), (13, 5)),
    )
    with term.hidden_cursor():
        while True:
            term.draw(living)
            living = step(living)
            time.sleep(0.1)
