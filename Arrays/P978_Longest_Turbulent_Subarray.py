# https://leetcode.com/problems/longest-turbulent-subarray/description/


class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        """
        take a number then check is next number bigger or smaller
        when decided - next number has to be the opposite

        broken streak:
            if numbers are no equal set operation to opposite and counter to 1
            if equal
        """
        if len(arr) == 1:
            return 1

        subMax = 0
        counter = 1

        operation = 'find'  # find, greater, lower
        before = arr[0]

        for num in arr[1:]:
            if operation == 'find':
                subMax = max(subMax, counter)
                counter = 1
                if num == before:
                    continue
                operation = 'lower' if before > num else 'greater'

            if operation == 'greater':
                if before < num:
                    counter += 1
                    operation = 'lower'
                else:
                    operation = 'find'
            else:
                if before > num:
                    counter += 1
                    operation = 'greater'
                else:
                    operation = 'find'
            before = num

        return subMax


