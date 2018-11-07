import unittest
import ArraysAndStrings.String_Rotation

class MyTestCase(unittest.TestCase):
    def test_no_rotation(self):
        str1 = 'waterfall'
        str2 = 'waterfall'
        result = ArraysAndStrings.String_Rotation.isRotation(str1, str2)
        self.assertTrue(result)

    def test_one_rotation(self):
        str1 = 'waterfall'
        str2 = 'aterfallw'
        result = ArraysAndStrings.String_Rotation.isRotation(str1, str2)
        self.assertTrue(result)

    def test_one_neg_rotation(self):
        str1 = 'waterfall'
        str2 = 'llwaterfa'
        result = ArraysAndStrings.String_Rotation.isRotation(str1, str2)
        self.assertTrue(result)

    def test_not_substring(self):
        str1 = 'waterfall'
        str2 = 'waterllaf'
        result = ArraysAndStrings.String_Rotation.isRotation(str1, str2)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
