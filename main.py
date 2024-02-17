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


