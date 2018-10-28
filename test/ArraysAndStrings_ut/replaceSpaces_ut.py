import unittest
import array

import ArraysAndStrings.To_URL

class MyTestCase(unittest.TestCase):
    def test_urlify(self):
        strs = [[], [' '], [' ', 'a', 'b', 'c'], ['a', 'b', ' ', ' ', 'c', 'd'], [' ', 'a', 'b', 'c', ' ']]
        numSpaces = [0, 1, 1, 2, 2]
        expectedStr = ['', '%20', '%20abc', 'ab%20%20cd', '%20abc%20']

        for i in range(len(strs)):
            testArr = strs[i].copy()
            testArr.extend(['-']*numSpaces[i]*2)
            resultArr = ArraysAndStrings.To_URL.replaceSpaces(testArr, len(strs[i]))
            resultStr = ''.join(resultArr)
            self.assertEqual(resultStr, expectedStr[i], 'Error: ' + resultStr + ' not equal to expected str ' + expectedStr[i])


if __name__ == '__main__':
    unittest.main()
