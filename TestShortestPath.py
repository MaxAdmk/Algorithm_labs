import unittest

from ShortestPath import build_graph, find_shortest_path

class TestShortestPath(unittest.TestCase):
    def test_shortest_path(self):
        matrix = [
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
        ]
        start = (0, 0)
        end = (7, 5)

        self.assertEqual(find_shortest_path(matrix, start, end), 12)


if __name__ == '__main__':
    unittest.main()
