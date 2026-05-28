def dot_prod(a, b):
    return sum(x * y for x, y in zip(a, b))

def matrix_mult(A, B):
    if not A or len(A[0]) != len(B):
        return None
    return [[dot_prod(row, col) for col in zip(*B)] for row in A]

matrix_A = [[7.04, 2, -4, 2], [6, -1, 3.5, 4], [8, -8, -4, 9]]
matrix_B = [[8, 2], [-3.789, 7], [9, 4], [6, 6.7]]
result = matrix_mult(matrix_A, matrix_B)

for row in result:
    print([f"{val:.3f}" for val in row])