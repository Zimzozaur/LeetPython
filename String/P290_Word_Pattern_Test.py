import unittest
from P290_Word_Pattern import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        pattern = "abba"
        s = "dog cat cat dog"
        res = self.s.wordPattern(pattern, s)
        self.assertEqual(True, res)

    def test_2(self):
        pattern = "abba"
        s = "dog cat cat fish"
        res = self.s.wordPattern(pattern, s)
        self.assertEqual(False, res)

    def test_3(self):
        pattern = "aaaa"
        s = "dog cat cat dog"
        res = self.s.wordPattern(pattern, s)
        self.assertEqual(False, res)

    def test_not_equal_len(self):
        pattern = 'aca'
        s = 'dog cat'
        res = self.s.wordPattern(pattern, s)
        self.assertEqual(False, res)

    def test_same_animal_other_letter(self):
        pattern = 'abba'
        s = 'dog dog dog dog'
        res = self.s.wordPattern(pattern, s)
        self.assertEqual(False, res)

    def test_2_animals_on_same_letter(self):
        pattern = 'aba'
        s = 'dog cat cat'
        res = self.s.wordPattern(pattern, s)
        self.assertEqual(False, res)


