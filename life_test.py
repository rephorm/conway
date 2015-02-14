import unittest

import life
import shapes

class LifeTest(unittest.TestCase):

    def testMove1(self):
        cases = [
            [(0, 0), (0, 0), (0, 0)],
            [(0, 0), (1, 0), (1, 0)],
            [(0, 0), (0, 1), (0, 1)],
            [(2, 3), (4, 5), (6, 8)],
            [(2, 3), (-2, -3), (0, 0)],
        ]
        for x, y, expected in cases:
            self.assertEqual(expected, life.move1(x, y))

    def testMove(self):
        self.assertEquals(set([]),
                          life.move([], (2, 3)))
        self.assertEquals(set([(2, 3)]),
                          life.move([(0, 0)], (2, 3)))
        self.assertEquals(set([(-5, -7), (-4, -3)]),
                          life.move([(0, 0), (1, 4)], (-5,-7)))

    def testNeighbors(self):
        self.assertEqual(set([
            (0, 0), (0, 1), (0, 2),
            (1, 0),         (1, 2),
            (2, 0), (2, 1), (2, 2),
        ]), life.neighbors((1, 1)))

    def testCountNeighborsSingle(self):
        self.assertEqual({
            (0, 0): 1,
            (0, 1): 1,
            (0, 2): 1,
            (1, 0): 1,
            (1, 2): 1,
            (2, 0): 1,
            (2, 1): 1,
            (2, 2): 1,
        }, life.neighbor_counts([(1, 1)]))

    def testCountNeighborsSquare(self):
        living = set([(1, 1), (1, 2), (2, 1), (2, 2)])

        # ____
        # _**_
        # _**_
        # ____
        self.assertEqual({
            (0, 0): 1,
            (0, 1): 2,
            (0, 2): 2,
            (0, 3): 1,
            (1, 0): 2,
            (1, 1): 3,
            (1, 2): 3,
            (1, 3): 2,
            (2, 0): 2,
            (2, 1): 3,
            (2, 2): 3,
            (2, 3): 2,
            (3, 0): 1,
            (3, 1): 2,
            (3, 2): 2,
            (3, 3): 1,
        }, life.neighbor_counts(living))

    def testStepStable(self):
        living = shapes.square(2)
        self.assertEqual(living, life.step(living))

    def testStepRotator(self):
        living = life.move(shapes.vbar(3), (0, 1))
        expected = life.move(shapes.hbar(3), (1, 0))
        self.assertEqual(expected, life.step(living))


if __name__ == "__main__":
    unittest.main()
