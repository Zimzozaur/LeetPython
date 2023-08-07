# https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Performs binary search on 2D Matrix
        :param matrix:
        :param target:
        :return:
        """
        for array in matrix:

            if array[-1] < target:
                continue

            pointer_1 = 0
            pointer_2 = len(array) - 1
            pointer_3 = int((pointer_2 + pointer_1) / 2)

            while pointer_1 <= pointer_2:  # Runs until the last digit is wrong

                if array[pointer_3] == target:  # When found
                    return True

                elif array[pointer_3] < target:  # When to small move pointer_1 one above
                    pointer_1 = pointer_3 + 1

                else:
                    pointer_2 = pointer_3 - 1  # When to big move pointer_2 one below

                pointer_3 = int((pointer_2 + pointer_1) / 2)  # Recalculate pointer

        return False


if __name__ == '__main__':
    sol = Solution()

    mat = [[1]]
    target = 0

    print(sol.searchMatrix(mat, target))
