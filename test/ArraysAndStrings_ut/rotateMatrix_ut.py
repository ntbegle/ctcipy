import unittest
import ArraysAndStrings.Rotate_Matrix

class MyTestCase(unittest.TestCase):
    def test_rotate4(self):
        matrix = [[1,2,3,4], [5,6,7,8], [9,1,2,3], [4,5,6,7]]
        verify_matrix = [[4, 8, 3, 7], [3, 7, 2, 6], [2, 6, 1, 5], [1, 5, 9, 4]]
        rotMatrix = ArraysAndStrings.Rotate_Matrix.rotateMatrix(matrix)
        ArraysAndStrings.Rotate_Matrix.printMatrix(rotMatrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                self.assertEqual(rotMatrix[i][j], verify_matrix[i][j])

    def test_rotate5(self):
        matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        verify_matrix = [[5,10,15,20,25],[4,9,14,19,24],[3,8,13,18,23],[2,7,12,17,22],[1,6,11,16,21]]
        rotMatrix = ArraysAndStrings.Rotate_Matrix.rotateMatrix(matrix)
        ArraysAndStrings.Rotate_Matrix.printMatrix(rotMatrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                self.assertEqual(rotMatrix[i][j], verify_matrix[i][j])

    # def test_rotate5(self):
    #     matrix = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]
    #     rotMatrix = ArraysAndStrings.Rotate_Matrix.rotateMatrix(matrix)
    #     ArraysAndStrings.Rotate_Matrix.printMatrix(rotMatrix)

if __name__ == '__main__':
    unittest.main()
