#zero a row and column where a 0 is found in a matrix


def zeroMatrix(matrix):
    firstRowHas0 = False
    firstColHas0 = False

    for row in range(len(matrix)):
        if matrix[row][0] == 0:
            firstColHas0 = True
            break
    for col in range(len(matrix[0])):
        if matrix[0][col] == 0:
            firstRowHas0 = True
            break
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if matrix[row][col] == 0:
                matrix[0][col] = 0
                matrix[row][0] = 0

    for row in range(len(matrix)):
        if matrix[row][0] == 0:
            for col in range(1,len(matrix[0])):
                matrix[row][col] = 0

    for col in range(len(matrix[0])):
        if matrix[0][col] == 0:
            for row in range(1,len(matrix[0])):
                matrix[row][col] = 0

    if firstRowHas0:
        for col in range(len(matrix[0])):
            matrix[0][col] = 0

    if firstColHas0:
        for row in range(len(matrix)):
            matrix[row][0] = 0

    return matrix