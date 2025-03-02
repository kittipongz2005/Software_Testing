import unittest

def gridChallenge(grid):
    # Sort each row of the grid in ascending order
    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))

    # Check if the columns are in ascending order
    for col in range(len(grid[0])):
        for row in range(1, len(grid)):
            if grid[row][col] < grid[row - 1][col]:
                return "NO"
    
    return "YES"

class TestGridChallenge(unittest.TestCase):

    def test_case_1(self):
        grid = [
            "ebacd",
            "fghij",
            "olmkn",
            "trpqs",
            "xywuv"
        ]
        self.assertEqual(gridChallenge(grid), "YES")  # Expected output is YES

    def test_case_2(self):
        grid = [
            "abcde",
            "fghij",
            "klmno",
            "pqrst",
            "uvwxy"
        ]
        self.assertEqual(gridChallenge(grid), "YES")  # Already in order, should return YES

    def test_case_3(self):
        grid = [
            "edcba",
            "jihgf",
            "onmlk",
            "utsrq",
            "zyxwv"
        ]
        self.assertEqual(gridChallenge(grid), "YES")  # Columns are not in order, should return NO

    def test_case_4(self):
        grid = [
            "aabbc",
            "abcdd",
            "bbcca",
            "deaaa",
            "ccbbc"
        ]
        self.assertEqual(gridChallenge(grid), "NO")  # Not all columns are in order, should return NO

    def test_case_5(self):
        grid = [
            "a",
            "b",
            "c"
        ]
        self.assertEqual(gridChallenge(grid), "YES")  # Single character grid, should return YES

    def test_case_6(self):
        grid = [
            "abc",
            "cba",
            "bca"
        ]
        self.assertEqual(gridChallenge(grid), "YES")  # Can be rearranged to a valid grid, should return YES