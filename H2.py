import unittest

def alternatingCharacters(s):
    deletions = 0

    # Iterate through the string starting from the second character
    for i in range(1, len(s)):
        # If current character is same as the previous one, increment deletions
        if s[i] == s[i - 1]:
            deletions += 1

    return deletions

class TestAlternatingCharacters(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    def test_case_2(self):
        self.assertEqual(alternatingCharacters("BBBBB"), 4)

    def test_case_3(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)

    def test_case_4(self):
        self.assertEqual(alternatingCharacters("BABABA"), 0)

    def test_case_5(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

    def test_case_6(self):
        self.assertEqual(alternatingCharacters("A"), 0)

    def test_case_7(self):
        self.assertEqual(alternatingCharacters("BBBBABBBBB"), 7)

    def test_case_8(self):
        self.assertEqual(alternatingCharacters("AAA"), 2)

    def test_case_9(self):
        self.assertEqual(alternatingCharacters("BB"), 1)

    def test_case_10(self):
        self.assertEqual(alternatingCharacters("AB"), 0)




