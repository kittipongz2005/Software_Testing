import unittest

def cat_and_mouse(x, y, z):
    distance_a = abs(x - z)
    distance_b = abs(y - z)

    if distance_a < distance_b:
        return "Cat A"
    elif distance_b < distance_a:
        return "Cat B"
    else:
        return "Mouse C"

class TestCatAndMouse(unittest.TestCase):


    def test_case_1(self):
        self.assertEqual(cat_and_mouse(1, 5, 3), "Mouse C")


    def test_case_2(self):
        self.assertEqual(cat_and_mouse(1, 2, 3), "Cat B")

    def test_case_3(self):
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")
        

    def test_case_4(self):
        self.assertEqual(cat_and_mouse(10, 20, 15), "Mouse C")
    
    def test_case_5(self):
        self.assertEqual(cat_and_mouse(5, 10, 6), "Cat A")
        
    def test_case_6(self):
        self.assertEqual(cat_and_mouse(10, 10, 10), "Mouse C")
        
    def test_case_7(self):
        self.assertEqual(cat_and_mouse(1, 3, 0), "Cat A")
    
    def test_case_8(self):
        self.assertEqual(cat_and_mouse(3, 5, 0), "Cat A")