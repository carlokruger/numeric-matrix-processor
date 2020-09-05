X = []
Y = []
a = []
b = []

multiplier = 0.0


def get_matrix_size():
    return [int(i) for i in input().split()]


def get_matrix(size):
    matrix = []
    for _ in range(size[0]):
        matrix.append([int(val) if val.isdigit() else float(val) for val in input().split()])
    return matrix


def get_constant():
    con = input()
    if con.isdigit():
        return int(con)
    else:
        return float(con)


def constant_multiplication(X, multiplier):
    result = X
    for i in range(len(result)):
        # iterate through columns
        for j in range(len(result[0])):
            result[i][j] *= multiplier
    return result


def print_matrix(result):
    for item in result:
        print(' '.join(str(x) for x in item))


def print_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("0. Exit")


def add_matrices(A, B):
    result = A
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] += B[i][j]
    return result


def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
    return M


def matrix_multiply(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C


while True:
    print_menu()
    action = input("Your choice:")

    if action == "0":
        break

    elif action == "1":
        print("Enter size of first matrix:")
        a = get_matrix_size()
        print("Enter first matrix:")
        X = get_matrix(a)
        print("Enter size of second matrix:")
        b = get_matrix_size()
        print("Enter second matrix:")
        Y = get_matrix(b)
        if a[0] != b[0] or a[1] != b[1]:
            print("The operation cannot be performed.")
            print()
        else:
            print_matrix(add_matrices(X, Y))
            print()

    elif action == "2":
        print("Enter size of first matrix:")
        a = get_matrix_size()
        print("Enter matrix:")
        X = get_matrix(a)
        print("Enter constant:")
        multiplier = get_constant()
        print_matrix(constant_multiplication(X, multiplier))
        print()

    elif action == "3":
        print("Enter size of first matrix:")
        a = get_matrix_size()
        print("Enter first matrix:")
        X = get_matrix(a)
        print("Enter size of second matrix:")
        b = get_matrix_size()
        print("Enter second matrix:")
        Y = get_matrix(b)
        if a[1] != b[0]:
            print("The operation cannot be performed.")
            print()
        else:
            print_matrix(matrix_multiply(X, Y))
            print()
