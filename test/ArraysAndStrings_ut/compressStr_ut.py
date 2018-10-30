import unittest
import ArraysAndStrings.String_Compression

class MyTestCase(unittest.TestCase):
    def test_compressStr(self):
        inputStrs = ['aabcccccaaa', '', 'abcd']
        outputStrs = ['a2b1c5a3', '', 'abcd']

        for inStr, outStr in zip(inputStrs, outputStrs):
            result = ArraysAndStrings.String_Compression.compressStr(inStr)
            self.assertEquals(outStr, result)


if __name__ == '__main__':
    unittest.main()
