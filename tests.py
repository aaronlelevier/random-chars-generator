import unittest

from randoms import Randoms


class RandomsTests(unittest.TestCase):

    def setUp(self):
        self.r = Randoms()

    def test_letters(self):
        self.assertTrue(len(self.r.letters()), 10)

    def test_lowercase(self):
        l = self.r.lowercase()
        self.assertTrue(len(l), 10)
        self.assertEqual(l, l.lower())

    def test_uppercase(self):
        u = self.r.uppercase()
        self.assertTrue(len(u), 10)
        self.assertEqual(u, u.upper())

    def test_digits(self):
        d = self.r.digits()
        self.assertTrue(len(d), 10)
        self.assertIsInstance(int(d), int)

    def test_integer(self):
        i = self.r.integer()
        self.assertIsInstance(i, int)

    def test_float(self):
        f = self.r.float()
        self.assertIsInstance(f, float)

    def test_length(self):
        self.assertEqual(len(self.r.letters(20)), 20)

if __name__ == '__main__':
    unittest.main()