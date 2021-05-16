import palindrome
class TestPal:
    def test1(self):
        assert palindrome.palindrome("rotator") == True

    def test2(self):
        assert palindrome.palindrome("Madam") == True

    def test3(self):
        assert palindrome.palindrome("step on no pets") == True