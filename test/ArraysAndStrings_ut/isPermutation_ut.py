import unittest
import ArraysAndStrings.Check_Permutation

class MyTestCase(unittest.TestCase):
    def test_not_permutations(self):
        str1 = ['abcde', 'hello world', 'qwerty']
        str2 = ['abcdf', 'dlrowolleh', 'qwertyu']

        for i in range(0, len(str1)):
            result = ArraysAndStrings.Check_Permutation.isPermutation(str1[i], str2[i])
            self.assertFalse(result, 'Error: ' + str1[i] + ' is not a permuation of ' + str2[i])

    def test_permutations(self):
        str1 = ['abcde', 'hello world', 'qwerty', '']
        str2 = ['abcde', 'dlrow olleh', 'ywertq', '']

        for i in range(0, len(str1)):
            result = ArraysAndStrings.Check_Permutation.isPermutation(str1[i], str2[i])
            self.assertTrue(result, 'Error: ' + str1[i] + ' is a permutation of ' + str2[i])




if __name__ == '__main__':
    unittest.main()
