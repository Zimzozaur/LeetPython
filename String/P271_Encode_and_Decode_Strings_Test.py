import unittest
from P271_Encode_and_Decode_Strings import Codec



class EncodeTest(unittest.TestCase):
    def setUp(self):
        self.c = Codec()

    def test_1_len_empty(self):
        arr = ['']
        res = self.c.encode(arr)
        self.assertEqual('齉0齉', res)

    def test_2_len_empty(self):
        arr = ['', '']
        res = self.c.encode(arr)
        self.assertEqual('齉0齉齉0齉', res)

    def test_4_len_words(self):
        arr = ['pen', 'pineapple', 'apple', 'pen']
        res = self.c.encode(arr)
        self.assertEqual('pen齉3齉pineapple齉9齉apple齉5齉pen齉3齉', res)


class DecodeTest(unittest.TestCase):
    def setUp(self):
        self.c = Codec()

    def test_1_len_empty(self):
        s = '齉0齉'
        res = self.c.decode(s)
        self.assertEqual([''], res)

    def test_2_len_empty(self):
        s = '齉0齉齉0齉'
        res = self.c.decode(s)
        self.assertEqual(['', ''], res)

    def test_4_len_words(self):
        s = 'pen齉3齉pineapple齉9齉apple齉5齉pen齉3齉'
        res = self.c.decode(s)
        self.assertEqual(['pen', 'pineapple', 'apple', 'pen'], res)


class LeetCodeTest(unittest.TestCase):
    def setUp(self):
        self.c = Codec()

    def test_leetcode_1(self):
        arr = ["Hello", "World"]
        res = self.c.decode(self.c.encode(arr))
        self.assertEqual(arr, res)

    def test_leetcode_2(self):
        arr = [""]
        res = self.c.decode(self.c.encode(arr))
        self.assertEqual(arr, res)

    def test_1_len_char(self):
        arr = ['X']
        res = self.c.decode(self.c.encode(arr))
        self.assertEqual(arr, res)

    def test_4_len_words(self):
        arr = ['pen', 'pineapple', 'apple', 'pen']
        res = self.c.decode(self.c.encode(arr))
        self.assertEqual(arr, res)

    def test_4_len_2_empty(self):
        arr = ['pen', '', 'apple', '']
        res = self.c.decode(self.c.encode(arr))
        self.assertEqual(arr, res)

    def test_4_len_tag_char(self):
        arr = ['齉齉齉齉齉齉', '齉齉齉齉齉', '齉齉齉齉齉齉齉', '齉齉齉齉齉齉齉齉齉齉齉齉']
        res = self.c.decode(self.c.encode(arr))
        self.assertEqual(arr, res)

    def test_4_len_numbers(self):
        arr = ['123', '1234', '12345', '0']
        res = self.c.decode(self.c.encode(arr))
        self.assertEqual(arr, res)







