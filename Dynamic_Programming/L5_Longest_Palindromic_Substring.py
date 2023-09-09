# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(arr):
            if len(arr) == 1:
                return True
            arr1 = arr[:len(arr) // 2]
            if len(arr) % 2 == 1:
                arr2 = arr[len(arr) // 2 + 1:]
            else:
                arr2 = arr[len(arr) // 2:]
            arr2 = arr2[::-1]
            print((len(arr1), len(arr2)))
            for i in range(len(arr1)):
                if arr1[i] != arr2[i]:
                    return False
            return True

        time = 1
        for i in range(len(s) - 1, -1, -1):
            for j in range(time):
                if is_palindrome(s[j:i + j + 1]):
                    return s[j:i + j + 1]
            time += 1




if __name__ == '__main__':
    sol = Solution()
    s = "asdffdsaasdfdsa"
    print(sol.longestPalindrome(s))