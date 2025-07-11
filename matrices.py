def main():
    A = [
        [1, 2],
        [3, 4]
    ]

    B = [
        [4, 3],
        [2, 1]
    ]

    # Print A + B
    print(add_matrices(A,B))

    # Print the SECOND column of B (computers count from zero)
    print(matrix_column(B,1))

    # Print A * B
    print(mat_mul(A,B))

    def f(v):
        assert len(v) == 2
        return [v[1], v[0]]

    C = [
        [0, 1],
        [1, 0]
    ]

    v = [4, 5]

    # The linear map f and the matrix C have the same effect on
    # their input vectors.
    print(f(v))
    print(apply_map(C, v))



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
def dot_product(x, y):
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


def apply_map(A, x):
    assert len(A) == len(x)
    return [
        dot_product(A[i], x) for i in range(len(x))
    ]

def mat_mul(A, B):
    assert len(A[0]) == len(B)
    n = len(A)
    m = len(B[0])
    return [
        apply_map(A, matrix_column(B, j)) for j in range(m)
    ]


if __name__ == "__main__":
    main()
