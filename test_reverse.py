import unittest
from reverse import neg

class Testreverse(unittest.TestCase):

    def test_int(self):
        result = neg(5)
        self.assertIsInstance(result, int)

    def test_neg(self):
        result = neg(5)
        self.assertEqual(result, -5)


if __name__ == '__main__':
    unittest.main()