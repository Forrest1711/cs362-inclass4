import palindrome
import unittest


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(palindrome.palindrome("rotator"), True)

    def test2(self):
        self.assertEqual(palindrome.palindrome("Madam"), True)

    def test3(self):
        self.assertEqual(palindrome.palindrome("step on no pets"), True)


if __name__ == '__main__':
    unittest.main()
