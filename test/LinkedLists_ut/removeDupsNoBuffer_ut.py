import unittest
import LinkedLists.RemoveDuplicates

class MyTestCase(unittest.TestCase):
    def test_no_duplicates(self):
        l = [1, 2, 3, 4, 5]
        result = LinkedLists.RemoveDuplicates.removeDups(l)
        print(result)
        self.assertEqual(l, result)

    def test_duplicates(self):
        l = [1, 1, 2, 3, 4, 4]
        verify = [1,2,3,4]
        result = LinkedLists.RemoveDuplicates.removeDups(l)
        print(result)
        self.assertEqual(verify, result)

if __name__ == '__main__':
    unittest.main()
