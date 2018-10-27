import unittest
import ArraysAndStrings.Is_Unique

class MyTestCase(unittest.TestCase):
    def test_unique(self):
        strs = ['abcd', 'a', 'ab', 'ab cd']
        for s in strs:
            result = ArraysAndStrings.Is_Unique.is_unique(s)
            self.assertTrue(result, 'Error: String ' + s + ' was incorrectly marked as not unique')

    def test_not_unique(self):
        strs = ['aabcd', 'abcdd', 'abccde', 'abcda', 'abcdbe']
        for s in strs:
            result = ArraysAndStrings.Is_Unique.is_unique(s)
            self.assertFalse(result, 'Error: String ' + s + ' was incorrectly marked as unique.')


if __name__ == '__main__':
    unittest.main()
