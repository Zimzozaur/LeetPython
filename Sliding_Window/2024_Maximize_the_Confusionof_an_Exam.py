# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """
        Return the maximum number of consecutive 'T's or 'F's in the answerKey
        after performing the change char operation up to k times.
        :param answerKey:
        :param k:
        :return:

        We need to use two pointers
        We create dict with two keys - F and T.
        They start at the beginning of string
        Add +1 to the same key
        Repet until the smaller key is greater than k
            if yes - decrease key[pointerOne] by 1 and move pointerOne
        """

        bool_dict = {"F": 0, "T": 0}
        longest = 0
        curr_len = 0
        i = 0  # Pointer 1
        j = 0  # Pointer 2

        while j < len(answerKey):
            bool_dict[answerKey[j]] = bool_dict.get(answerKey[j]) + 1  # +1 to char
            curr_len += 1
            j += 1

            while min(bool_dict.get("F"), bool_dict.get("T")) > k:  # If more chars to change than K
                bool_dict[answerKey[i]] = bool_dict.get(answerKey[i]) - 1  # -1 to char
                curr_len -= 1
                i += 1

            if curr_len > longest:
                longest = curr_len

        return longest


if __name__ == '__main__':
    sol = Solution()
    x = "TTTTTTTTTFTTTTTTTTTT"
    k = 1
    print(sol.maxConsecutiveAnswers(x, k))
