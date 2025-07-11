# For two vectors with "real" values, we define their sum as
# follows:
def add_vectors(x, y):
    n = len(x)
    assert n == len(y)
    return [x[i] + y[i] for i in range(n)]


# And scalar multiplication like so:
def scalar_multiplication(a, x):
    n = len(x)
    return [a * x[i] for i in range(n)]


# The inner product of two vectors:
def inner_product(x, y):
    n = len(x)
    assert n == len(y)
    return sum([x[i] * y[i] for i in range(n)])


# The sum of two matrices:
def add_matrices(A, B):
    n = len(A)
    assert n == len(B)
    return [add_vectors(A[i], B[i]) for i in range(n)]


# Scalar multiplication with a matrix:
def scalar_matrix(a, A):
    n = len(A)
    return [scalar_multiplication(a, A[i]) for i in range(n)]


def zero_vector(n):
    return [0 for _ in range(n)]


def zero_matrix(n, m):
    return [zero_vector(m) for _ in range(n)]


def matrix_column(A, j):
    n = len(A)
    return [A[i][j] for i in range(n)]


def mat_mul(A, B):
    assert len(A[0]) == len(B)
    n = len(A)
    m = len(B[0])
    return [
        [
            inner_product(A[i], matrix_column(B, j)) for j in range(m)
        ] for i in range(n)
    ]

A = [
    [1, 2],
    [3, 4]
]

B = [
    [4, 3],
    [2, 1]
]


print(add_matrices(A,B))

print(matrix_column(B,1))

print(mat_mul(A,B))
