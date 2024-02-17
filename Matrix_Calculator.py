import numpy as np


class Matrix_Calculator:

    # Initial Data
    rows = 3
    columns = 3
    matrix = np.array([[1, 0, 0],
                       [0, 1, 0],
                       [0, 0, 1]])

    # View the result matrix
    def view_matrix(self):
        for row in self.matrix:
            for col in row:
                print(col, end = ' ')
            print('')

    # Multiply matrix by a number and view the result
    def multiply_by_number(self, number, initial_matrix):
        temp_array = []
        temp_row = []
        for row in initial_matrix:
            for col in row:
                temp_row.append(number * col)
            temp_array.append(temp_row)
            temp_row = []

        self.matrix = np.array(temp_array)
        self.view_matrix()