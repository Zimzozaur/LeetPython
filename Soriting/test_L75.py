import unittest
from L75_Sort_Colors import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_small_input(self):
        """Test input up to size 10"""
        input1 = [2, 1, 0]
        answer1 = [0, 1, 2]
        self.sol.sortColors(input1)
        self.assertEqual(input1, answer1)

        input2 = [2, 1, 1, 0, 0, 0]
        answer2 = [0, 0, 0, 1, 1, 2]
        self.sol.sortColors(input2)
        self.assertEqual(input2, answer2)

        input3 = [2, 2, 1, 1, 0, 1, 1, 2, 2]
        answer3 = [0, 1, 1, 1, 1, 2, 2, 2, 2]
        self.sol.sortColors(input3)
        self.assertEqual(input3, answer3)

        input4 = [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0]
        answer4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2]
        self.sol.sortColors(input4)
        self.assertEqual(input4, answer4)

    def test_medium_input(self):
        """Test input up to size 20"""
        input1 = [2, 1, 1, 1, 0, 0, 0, 1, 1, 2, 2, 0, 0, 0, 1, 2]
        answer1 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
        self.sol.sortColors(input1)
        self.assertEqual(input1, answer1)

        input2 = [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2]
        answer2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2]
        self.sol.sortColors(input2)
        self.assertEqual(input2, answer2)

    def test_big_input(self):
        """Test input up to size 30"""
        input1 = [0, 1, 2, 0, 0, 1, 1, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
        answer1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        self.sol.sortColors(input1)
        self.assertEqual(input1, answer1)


if __name__ == '__main__':
    unittest.main()
