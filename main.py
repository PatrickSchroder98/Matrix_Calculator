# Matrix Calculator
import Matrix_Calculator as mc
m = mc.Matrix_Calculator()

# Testing view method
m.view_matrix()
print('')

# Testing multiply by number method
Init = mc.np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
Num = 2
m.multiply_by_number(Num, Init)
print('')

# Testing sum
Init1 = mc.np.array([[1, 3],
                     [1, 0],
                     [1, 2]])
Init2 = mc.np.array([[0, 0],
                     [7, 5],
                     [2, 1]])
m.sum_sub_matrix(Init1, Init2, True)

print('')

# Testing subtraction
m.sum_sub_matrix(Init1, Init2, False)

