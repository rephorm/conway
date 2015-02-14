def rect(w, h):
    return set([(i, j) for i in xrange(h) for j in xrange(w)])


def square(s):
    return rect(s, s)


def hbar(l):
    return rect(l, 1)


def vbar(l):
    return rect(1, l)


def glider():
    return set([(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
