import unittest


def generate_pumpkin_order(m, n):
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    order = []
    for i in range(m):
        if i % 2 == 0:
            for j in range(n):
                matrix[i][j] = i * n + j + 1
        else:
            for j in range(n - 1, -1, -1):
                matrix[i][j] = i * n + (n - 1 - j) + 1

    for row in matrix:
        order.extend(row)

    return order


class TestGeneratePumpkinOrder(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(generate_pumpkin_order(5, 5),
                         [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18, 17, 16, 21, 22, 23, 24, 25])

    def test_case_2(self):
        self.assertEqual(generate_pumpkin_order(6, 1), [1, 2, 3, 4, 5, 6])

    def test_case_3(self):
        self.assertEqual(generate_pumpkin_order(2, 4), [1, 2, 3, 4, 8, 7, 6, 5])


if __name__ == '__main__':
    print(generate_pumpkin_order(6, 1))
    unittest.main()

