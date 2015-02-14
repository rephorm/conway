import shapes
import unittest


class ShapesTest(unittest.TestCase):

    def testSquare(self):
        self.assertEquals(set([]),
                          shapes.square(0))
        self.assertEquals(set([(0, 0)]),
                          shapes.square(1))
        self.assertEquals(set([(0, 0), (1, 0), (0, 1), (1, 1)]),
                          shapes.square(2))

    def testHbar(self):
        self.assertEquals(set([(0, 0), (0, 1)]),
                          shapes.hbar(2))
        self.assertEquals(set([(0, 0), (0, 1), (0, 2), (0, 3)]),
                          shapes.hbar(4))

