import numpy as np


class Matrix_Calculator:

    # Initial Data
    matrix = np.array([[1, 0, 0],
                       [0, 1, 0],
                       [0, 0, 1]])

    # View the result matrix
    def view_matrix(self):
        for row in self.matrix:
            for col in row:
                print(col, end = ' ')
            print('')
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
        return self.matrix

    # Check if matrix1 and matrix2 have the same amount of rows and columns
    def check_equality(self, matrix1, matrix2):
        is_good = True
        if len(matrix1) != len(matrix2):
            is_good = False

        for row1 in matrix1:
            for row2 in matrix2:
                if len(row1) != len(row2):
                    is_good = False

        return is_good

    def sum_sub_matrix(self, matrix1, matrix2, sum):
        if not self.check_equality(matrix1, matrix2):
            print("Error! Matrices must have the same amount of rows and columns.")
            return "Error"

        row = len(matrix1)
        col = len(matrix1[0])
        temp_array = []
        temp_row = []
        for i in range(0,row):
            for j in range(0, col):
                if sum:
                    temp_row.append(matrix1[i][j] + matrix2[i][j])
                else:
                    temp_row.append(matrix1[i][j] - matrix2[i][j])
            temp_array.append(temp_row)
            temp_row = []

        self.matrix = np.array(temp_array)
        return self.matrix

    def transposition(self, initial_matrix):

        row = len(initial_matrix)
        col = len(initial_matrix[0])
        temp_array = []
        temp_row = []
        for i in range(0,col):
            for j in range(0, row):
                temp_row.append(initial_matrix[j][i])
            temp_array.append(temp_row)
            temp_row = []

        self.matrix = np.array(temp_array)
        return self.matrix