# https://leetcode.com/problems/sort-the-students-by-their-kth-score/
class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        """
        Look at index k in every array and sort them in descending order.
        :param score:
        :param k:
        :return:
        """
        return_array = [score.pop()]  # Adds first array to array
        while score:
            add_array = score.pop()
            added = False
            for i in range(len(return_array)):
                # Loops over the return_array to find smaller int to insert array into array
                if add_array[k] > return_array[i][k]:
                    return_array.insert(i, add_array)
                    added = True
                    break

            if not added:
                # If the smallest, add at the end
                return_array.append(add_array)

        return return_array


if __name__ == '__main__':
    sol = Solution()
    test = []
    for j in range(100):
        test.append([j, j - 1, j * 2, -j * 2])

    print(test)
    print()
    k = 3
    print(sol.sortTheStudents(test, k))

