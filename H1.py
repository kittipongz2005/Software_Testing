import unittest

def funnyString(s):
    r = s[::-1]  # Reverse the string
    diff_s = [abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s))]
    diff_r = [abs(ord(r[i]) - ord(r[i - 1])) for i in range(1, len(r))]
    
    return "Funny" if diff_s == diff_r else "Not Funny"

class TestFunnyString(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_case_2(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_case_3(self):
        self.assertEqual(funnyString("abcd"), "Funny")

    def test_case_4(self):
        self.assertEqual(funnyString("a"), "Funny")  # Single character is always Funny

    def test_case_5(self):
        self.assertEqual(funnyString("aa"), "Funny")  # Identical characters

