# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.
        :param s:
        :return:
        """
        string_len = len(s)
        hash_set = set()
        longest = 0

        if string_len == 0:  # Always 0
            return 0
        elif string_len == 1: # Always 1
            return 1

        pointer_one = 0
        pointer_two = 1
        hash_set.add(s[pointer_one])  # Starts with one element

        # Loops over the string
        while pointer_two < string_len:

            # If pointerTwo points to duplicate
            if s[pointer_two] in hash_set:
                # Check is substring longer
                if len(hash_set) > longest:
                    longest = len(hash_set)
                # Moves pointerOne and remove chars until stands on duplicate
                while s[pointer_one] != s[pointer_two]:
                    hash_set.remove(s[pointer_one])
                    pointer_one += 1
                pointer_one += 1  # Move one forward to stand on char to delete if pointerTwo on duplicate

            hash_set.add(s[pointer_two])  # Adds element coz not a duplicate
            pointer_two += 1           # Moves a pointer to next char

        # Check is last substring longer
        if len(hash_set) > longest:
            longest = len(hash_set)

        return longest


if __name__ == '__main__':
    sol = Solution()
    x = "dvd12d12345 56432105 asdfghjkl"
    print(sol.lengthOfLongestSubstring(x))
