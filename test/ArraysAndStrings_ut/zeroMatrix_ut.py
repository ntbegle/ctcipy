import unittest
import ArraysAndStrings.Zero_Matrix
import ArraysAndStrings.Rotate_Matrix

class MyTestCase(unittest.TestCase):
    def checkMatrix(self, computedMatrix, verifyMatrix):
        self.assertEqual(len(computedMatrix), len(verifyMatrix))
        self.assertEqual(len(computedMatrix[0]), len(verifyMatrix[0]))
        for row in range(len(computedMatrix)):
            for col in range(len(computedMatrix[0])):
                self.assertEqual(computedMatrix[row][col], verifyMatrix[row][col])

    def test_no_zeros(self):
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        retMatrix = ArraysAndStrings.Zero_Matrix.zeroMatrix(matrix)
        ArraysAndStrings.Rotate_Matrix.printMatrix(retMatrix)
        self.checkMatrix(retMatrix, matrix)

    def test_zero_in_first_col(self):
        matrix = [[1,2,3,4],[0,2,3,4],[1,2,3,4],[1,2,3,4]]
        validMatrix = [[0,2,3,4],[0,0,0,0],[0,2,3,4],[0,2,3,4]]
        retMatrix = ArraysAndStrings.Zero_Matrix.zeroMatrix(matrix)
        ArraysAndStrings.Rotate_Matrix.printMatrix(retMatrix)
        self.checkMatrix(retMatrix, validMatrix)

    def test_zero_in_first_row(self):
        matrix = [[1,2,3,0],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
        validMatrix = [[0,0,0,0],[1,2,3,0],[1,2,3,0],[1,2,3,0]]
        retMatrix = ArraysAndStrings.Zero_Matrix.zeroMatrix(matrix)
        ArraysAndStrings.Rotate_Matrix.printMatrix(retMatrix)
        self.checkMatrix(retMatrix, validMatrix)

    def test_zero_in_middle(self):
        matrix = [[1,2,3,4],[1,2,0,4],[1,2,3,4],[1,2,3,4]]
        validMatrix = [[1,2,0,4],[0,0,0,0],[1,2,0,4],[1,2,0,4]]
        retMatrix = ArraysAndStrings.Zero_Matrix.zeroMatrix(matrix)
        ArraysAndStrings.Rotate_Matrix.printMatrix(retMatrix)
        self.checkMatrix(retMatrix, validMatrix)

    def test_multiple_zeros(self):
        matrix = [[1,2,3,4],[1,2,3,4],[1,2,0,4],[0,2,3,4]]
        validMatrix = [[0,2,0,4],[0,2,0,4],[0,0,0,0],[0,0,0,0]]
        retMatrix = ArraysAndStrings.Zero_Matrix.zeroMatrix(matrix)
        ArraysAndStrings.Rotate_Matrix.printMatrix(retMatrix)
        self.checkMatrix(retMatrix, validMatrix)

if __name__ == '__main__':
    unittest.main()
