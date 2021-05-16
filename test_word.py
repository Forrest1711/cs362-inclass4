import wordCount


class TestWord:
    def test1(self):
        str = "How many words are in this sentence?"
        assert wordCount.wordCount(str) == 7

    def test2(self):
        str = "Does it recognize every word in sentences with an em-dash or parenthese in them(for instance this one)?"
        assert wordCount.wordCount(str) == 18

    def test3(self):
        str = "Does it count numbers like 420 ?"
        assert wordCount.wordCount(str) == 6
