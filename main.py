# Matrix Calculator main for custom testing methods
import Matrix_Calculator as mc
m = mc.Matrix_Calculator()

# Using view method
m.view_matrix()

# Using multiply by number method
Init = mc.np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
Num = 2
m.multiply_by_number(Num, Init)
m.view_matrix()
# Using sum
Init1 = mc.np.array([[1, 3],
                     [1, 0],
                     [1, 2]])
Init2 = mc.np.array([[0, 0],
                     [7, 5],
                     [2, 1]])
m.sum_sub_matrix(Init1, Init2, True)
m.view_matrix()

# Using subtraction
m.sum_sub_matrix(Init1, Init2, False)
m.view_matrix()
# Using transposition
m.transposition(Init1)
m.view_matrix()
m.transposition(Init)
m.view_matrix()