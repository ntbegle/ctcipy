import unittest
import LinkedLists.ReturnKToLast

class MyTestCase(unittest.TestCase):
    def test_one(self):
        l = [1]
        k = 0
        result = LinkedLists.ReturnKToLast.getKToLast(l, k)
        print(result)
        self.assertEqual(result, l[0])

    def test_invalid(self):
        l = [1,2,3,4]
        k = 5
        result = LinkedLists.ReturnKToLast.getKToLast(l, k)
        print(result)
        self.assertEqual(None, result)

    def test_mid(self):
        l = [1,2,3,4,5,6,7,8,9,10]
        k = 5
        result = LinkedLists.ReturnKToLast.getKToLast(l, k)
        print(result)
        self.assertEqual(l[len(l)-1-k], result)

    def test_last(self):
        l = [1,2,3,4,5,6,7,8,9,10]
        k = 0
        result = LinkedLists.ReturnKToLast.getKToLast(l, k)
        print(result)
        self.assertEqual(l[len(l)-1-k], result)

if __name__ == '__main__':
    unittest.main()
