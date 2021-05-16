import wordCount
import unittest


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(wordCount.wordCount(
            "How many words are in this sentence?"), 7)

    def test2(self):
        self.assertEqual(wordCount.wordCount(
            "Does it recognize every word in sentences with an em-dash or parenthese in them(for instance this one)?"), 18)

    def test3(self):
        self.assertEqual(wordCount.wordCount(
            "Does it count numbers like 420 ?"), 6)


if __name__ == '__main__':
    unittest.main()
