# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
        and removing all non-alphanumeric characters, it reads the same forward and backward.
        Alphanumeric characters include letters and numbers.

        :param s:
        :return:

        Lower letter
        loop over is letter add to new string.
        Start with to pointers and chceck are letters the same
        """

        new_s = ""

        for letter in s:
            if letter.isalnum():
                new_s += letter.lower()

        pointer1 = 0
        pointer2 = len(new_s) - 1

        while pointer1 < pointer2:
            if new_s[pointer1] == new_s[pointer2]:
                pointer1 += 1
                pointer2 -= 1
            else:
                return False

        return True


if __name__ == '__main__':
    sol = Solution()
    word = "0P"
    print(sol.isPalindrome(word))
    print("amanaplanacanalpanama" == "amanaplanacanalpanama")
