import unittest

def caesarCipher(s, k):
    encrypted_string = []
    
    # Ensure k is within the range of 0 to 25
    k = k % 26
    
    for char in s:
        if char.islower():
            # Shift within the lowercase letters
            new_char = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
            encrypted_string.append(new_char)
        elif char.isupper():
            # Shift within the uppercase letters
            new_char = chr(((ord(char) - ord('A') + k) % 26) + ord('A'))
            encrypted_string.append(new_char)
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_string.append(char)
    
    return ''.join(encrypted_string)



class TestCaesarCipher(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")

    def test_case_2(self):
        self.assertEqual(caesarCipher("abc", 3), "def")

    def test_case_3(self):
        self.assertEqual(caesarCipher("xyz", 5), "cde")

    def test_case_4(self):
        self.assertEqual(caesarCipher("Hello-World!", 1), "Ifmmp-Xpsme!")

    def test_case_5(self):
        self.assertEqual(caesarCipher("a", 26), "a")  # No change since 26 is a full rotation

    def test_case_6(self):
        self.assertEqual(caesarCipher("A B C", 3), "D E F")  # Uppercase letters and spaces

    def test_case_7(self):
        self.assertEqual(caesarCipher("abc-123", 4), "efg-123")  # Correct expected output

    def test_case_8(self):
        self.assertEqual(caesarCipher("abc-xyz", 1), "bcd-yza")  # Wrap around at the end of the alphabet

