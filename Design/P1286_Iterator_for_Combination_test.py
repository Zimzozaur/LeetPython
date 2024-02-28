import unittest
from P1286_Iterator_for_Combination import CombinationIterator


def all_combinations(string, chars):
    result = []

    for i in range(len(string) - chars + 1):
        if chars == 1:
            result.append(string[i])
            continue
        for j in range(1, len(string) - chars + 2):
            if chars == 2 and i < j:
                result.append(string[i] + string[j])
                continue
            for x in range(2, len(string) - chars + 3):
                if chars == 3 and i < j < x:
                    result.append(string[i] + string[j] + string[x])
                    continue
                for y in range(3, len(string) - chars + 4):
                    if chars == 4 and i < j < x < y:
                        result.append(string[i] + string[j] + string[x] + string[y])

    return result


class CombinationGeneratorTest(unittest.TestCase):
    def test_3_letters_1_len(self):
        answer = ['a', 'b', 'c']
        res = all_combinations('abc', 1)
        self.assertEqual(answer, res)

    def test_3_letters_2_len(self):
        answer = ['ab', 'ac', 'bc']
        res = all_combinations('abc', 2)
        self.assertEqual(answer, res)

    def test_3_letters_3_len(self):
        answer = ['abc']
        res = all_combinations('abc', 3)
        self.assertEqual(answer, res)

    def test_4_letters_1_len(self):
        answer = ['a', 'b', 'c', 'd']
        res = all_combinations('abcd', 1)
        self.assertEqual(answer, res)

    def test_4_letters_2_len(self):
        answer = ['ab', 'ac', 'ad', 'bc', 'bd', 'cd']
        res = all_combinations('abcd', 2)
        self.assertEqual(answer, res)

    def test_4_letters_3_len(self):
        answer = ['abc', 'abd', 'acd', 'bcd']
        res = all_combinations('abcd', 3)
        self.assertEqual(answer, res)

    def test_4_letters_4_len(self):
        answer = ['abcd']
        res = all_combinations('abcd', 4)
        self.assertEqual(answer, res)

    def test_5_letter_2_len(self):
        answer = ['ab', 'ac', 'ad', 'ae', 'bc', 'bd', 'be', 'cd', 'ce', 'de']
        res = all_combinations('abcde', 2)
        self.assertEqual(answer, res)


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.char = 'abc'
        self.num = 2
        self.comb = CombinationIterator(self.char, self.num)

    def test_does_class_exist(self):
        assert isinstance(self.comb, CombinationIterator), "obj is not an instance of CombinationIterator"

    def test_self_string(self):
        self.assertEqual(self.char, self.comb.string)

    def test_self_position(self):
        self.assertEqual(list(self.comb.positions), [0, 1])

    def test_self_limits(self):
        self.assertEqual(self.comb.limits, [1, 2])

    def test_self_has_next(self):
        self.assertEqual(self.comb.has_next, True)

    def test_hasNext(self):
        self.assertEqual(self.comb.hasNext(), True)


class TestAllGeneratedCombinations(unittest.TestCase):

    def test_3_letters_1_len(self):
        comb = CombinationIterator('abc', 1)
        answer = all_combinations('abc', 1)
        res = [comb.next() for _ in range(3)]
        self.assertEqual(answer, res)

    def test_3_letters_2_len(self):
        comb = CombinationIterator('abc', 2)
        answer = all_combinations('abc', 2)
        res = [comb.next() for _ in range(3)]
        self.assertEqual(answer, res)

    def test_3_letters_3_len(self):
        comb = CombinationIterator('abc', 3)
        answer = all_combinations('abc', 3)
        res = [comb.next() for _ in range(1)]
        self.assertEqual(answer, res)

    def test_4_letters_1_len(self):
        comb = CombinationIterator('abcd', 1)
        answer = all_combinations('abcd', 1)
        res = [comb.next() for _ in range(4)]
        self.assertEqual(answer, res)

    def test_4_letters_2_len(self):
        comb = CombinationIterator('abcd', 2)
        answer = all_combinations('abcd', 2)
        res = [comb.next() for _ in range(6)]
        self.assertEqual(answer, res)

    def test_4_letters_3_len(self):
        comb = CombinationIterator('abcd', 3)
        answer = all_combinations('abcd', 3)
        res = [comb.next() for _ in range(4)]
        self.assertEqual(answer, res)

    def test_4_letters_4_len(self):
        comb = CombinationIterator('abcd', 4)
        answer = all_combinations('abcd', 4)
        res = [comb.next() for _ in range(1)]
        self.assertEqual(answer, res)

    def test_5_letters_2_len(self):
        comb = CombinationIterator('abcde', 2)
        answer = all_combinations('abcde', 2)
        res = [comb.next() for _ in range(10)]
        self.assertEqual(answer, res)


class TestHasNextMethod(unittest.TestCase):
    def test_3_letters_1_len(self):
        comb = CombinationIterator('abc', 1)
        [comb.next() for _ in range(1)]  # Max is 3
        self.assertEqual(True, comb.hasNext())
        [comb.next() for _ in range(1)]  # Max is 3
        self.assertEqual(True, comb.hasNext())
        [comb.next() for _ in range(1)]  # Max is 3
        self.assertEqual(False, comb.hasNext())

    def test_10_times_hasNext(self):
        comb = CombinationIterator('abcde', 2)
        for _ in range(9):
            comb.next()
            self.assertEqual(True, comb.hasNext())
        comb.next()
        self.assertEqual(False, comb.hasNext())
