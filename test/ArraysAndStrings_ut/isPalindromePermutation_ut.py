import unittest
import ArraysAndStrings.Check_Permutation

class MyTestCase(unittest.TestCase):
    def test_palindromes(self):
        strs = ['taco cat', 'aab', '']
        for s in strs:
            result = ArraysAndStrings.Check_Permutation.isPalindromePermutation(s)
            self.assertTrue(result, 'Error: ' + s + ' is a palindrome permutation')

    def test_not_palindromes(self):
        strs = ['taco catt', 'abc']
        for s in strs:
            result = ArraysAndStrings.Check_Permutation.isPalindromePermutation(s)
            self.assertFalse(result, 'Error: ' + s + ' is not a palindrome permutation')


if __name__ == '__main__':
    unittest.main()
