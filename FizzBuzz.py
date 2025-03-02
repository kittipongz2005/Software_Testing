import unittest

def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    else:
        if x % 3 == 0:
            return "Fizz"
        else:
            if x % 5 == 0:
                return "Buzz"
            else:
                return str(x)

class TestFizzBuzz(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
    
    def test_case_2(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
    
    def test_case_3(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
    
    def test_case_4(self):
        self.assertEqual(fizzbuzz(7), "7")
    
    def test_case_5(self):
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
    
    def test_case_6(self):
        self.assertEqual(fizzbuzz(9), "Fizz")
    
    def test_case_7(self):
        self.assertEqual(fizzbuzz(10), "Buzz")
    
    def test_case_8(self):
        self.assertEqual(fizzbuzz(1), "1")