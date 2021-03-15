import unittest
import reverse

class Testreverse(unittest.TestCase):

    def test_int(self):
        result = reverse.neg(5)
        self.assertIsInstance(result, int)

    def test_neg(self):
        result = reverse.neg(5)
        self.assertEqual(result, -5)


if __name__ == '__main__':
    unittest.main()