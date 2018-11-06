#given an NxN matrix, rotate matrix counter clockwise by 90 degrees

#1 2 3 4       4 8 3 7
#5 6 7 8       3 7 2 6
#9 1 2 3  ---> 2 6 1 5
#4 5 6 7       1 5 9 4

import copy

def rotateMatrix(matrix):
    matrixLen = len(matrix)
    rotMatrix = copy.deepcopy(matrix)

    for rowIdx in range(matrixLen):
        for colIdx in range(matrixLen):
            rotMatrix[rowIdx][colIdx] = matrix[colIdx][matrixLen - rowIdx - 1]
    return rotMatrix

def rotateMatrixInPlace(matrix):
    matrixLen = len(matrix)

    for i in range(matrixLen // 2):
        for j in range(i, matrixLen - 1 - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][matrixLen - 1 - i]
            matrix[j][matrixLen - 1 - i] = matrix[matrixLen - 1 - i][matrixLen - 1 - j]
            matrix[matrixLen - 1 - i][matrixLen - 1 - j] = matrix[matrixLen - 1 - j][i]
            matrix[matrixLen - 1 - j][i] = temp

    return matrix


def printMatrix(matrix):
    print('\n', end='')
    for rowVal in matrix:
        for colVal in rowVal:
            print(str(colVal) + ',', end='')
        print('\n', end='')
    print('\n', end='')