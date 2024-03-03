import unittest
import Matrix_Calculator as mc
m = mc.Matrix_Calculator()

class Tests(unittest.TestCase):

    def test_check_equal_true(self):
        matrix0 = mc.np.array([[1, 3],
                             [1, 0],
                             [1, 2]])
        matrix1 = mc.np.array([[0, 0],
                             [7, 5],
                             [2, 1]])

        result = m.check_equality(matrix0, matrix1)
        self.assertTrue(result)

    def test_check_equal_false(self):
        matrix0 = mc.np.array([[1, 3],
                             [1, 0]])
        matrix1 = mc.np.array([[0, 0],
                             [7, 5],
                             [2, 1]])

        result = m.check_equality(matrix0, matrix1)
        self.assertFalse(result)

    def test_multiply_by_number(self):
        matrix0 = mc.np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])
        num = 2

        result = m.multiply_by_number(num, matrix0)
        expected = mc.np.array([[2, 4, 6],
                            [8, 10, 12],
                            [14, 16, 18]])

        self.assertTrue((result == expected).all())

    def test_sub_sum_error(self):
        matrix0 = mc.np.array([[1, 3],
                               [1, 0]])
        matrix1 = mc.np.array([[0, 0],
                               [7, 5],
                               [2, 1]])
        result = m.sum_sub_matrix(matrix0, matrix1, True)
        expected = 'Error'
        self.assertEqual(result, expected)

    def test_sum(self):
        matrix0 = mc.np.array([[1, 3],
                               [1, 0],
                               [1, 2]])
        matrix1 = mc.np.array([[0, 0],
                               [7, 5],
                               [2, 1]])
        result = m.sum_sub_matrix(matrix0, matrix1, True)
        expected = mc.np.array([[1, 3],
                               [8, 5],
                               [3, 3]])
        self.assertTrue((result == expected).all())

    def test_sub(self):
        matrix0 = mc.np.array([[1, 3],
                               [1, 0],
                               [1, 2]])
        matrix1 = mc.np.array([[0, 0],
                               [7, 5],
                               [2, 1]])
        result = m.sum_sub_matrix(matrix0, matrix1, False)
        expected = mc.np.array([[1, 3],
                               [-6, -5],
                               [-1, 1]])
        self.assertTrue((result == expected).all())

    def test_transposition(self):
        matrix = mc.np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])
        result = m.transposition(matrix)
        expected = mc.np.array([[1, 4, 7],
                                [2, 5, 8],
                                [3, 6, 9]])
        self.assertTrue((result == expected).all())

if __name__ == '__main__':
    unittest.main()
