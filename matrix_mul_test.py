#!/usr/bin/env python3

import unittest
from matrix_mul import check_dim, multiply_mat


class TestMatrix(unittest.TestCase):

    def verify_dim(self):
        self.assertEqual(check_dim([[2,3],[2,4]]), (2, 2))
        self.assertEqual(check_dim([[2, 3, 4, 2], [3, 5, 7, 9], [7, 8, 9, 5]]), (3, 4))

    def not_matrix(self):
        self.assertEqual(check_dim([[2, 3, 4], [2, 3]]), 'This is not a valid  matrix')
        self.assertEqual(check_dim([[2, 3], [3, 4, 6], [6, 7, 8, 9, 10]]), 'This is not a valid  matrix')

    def valid_matrices(self):
        self.assertEqual(multiply_mat([[2, 2], [3, 3]], [[1, 2], [4, 5]]), True)
        self.assertEqual(multiply_mat([[2, 3, 4], [1, 2, 3]], [[1, 4, 9], [2, 4, 8]]), 'Cannot perform matrix multiplication')

    def matrix_ans(self):
        self.assertEqual(multiply_mat([[3, 8, 4],[8, 9, 6],[3, 2, 4]], [[4, 10],[6, 2],[9, 8]]), [[96, 78],[140, 146],[60, 66]])

unittest.main()

