def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    rows, cols = len(A), len(A[0])

    transpose = []

    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(A[j][i])
        transpose.append(new_row)

    return np.array(transpose)