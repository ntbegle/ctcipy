import unittest
import ArraysAndStrings.One_Away


class MyTestCase(unittest.TestCase):
    def test_one_away(self):
        strs1 = ['pale', 'pales', 'pale', '', 'ppale', 'apple']
        strs2 = ['ple', 'pale', 'bale', 'a', 'pale', 'aple']

        for i in range(len(strs1)):
            result = ArraysAndStrings.One_Away.isOneAwayToEq(strs1[i], strs2[i])
            self.assertTrue(result, 'Error: ' + strs1[i] + ' is only one edit away from ' + strs2[i])

    def test_not_one_away(self):
        strs1 = ['pale', 'palepa', '', 'pale']
        strs2 = ['bake', 'pale', 'pa', 'bales']

        for i in range(len(strs1)):
            result = ArraysAndStrings.One_Away.isOneAwayToEq(strs1[i], strs2[i])
            self.assertFalse(result, 'Error: ' + strs1[i] + ' is not one edit away from ' + strs2[i])

if __name__ == '__main__':
    unittest.main()
