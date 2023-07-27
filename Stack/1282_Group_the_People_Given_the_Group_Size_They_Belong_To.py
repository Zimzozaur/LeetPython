# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        """
        Pointer starts at zero
        Take first number, then add it to the pointer.
        Loop over all the array and find the indexes of the same numbers and convert number to None
        Append the array of indexes to the result array.
        Start from the pointer position

        Examples

        Input: groupSizes = [3,3,3,3,3,1,3]
        Output: [[5],[0,1,2],[3,4,6]]

        Input: groupSizes = [2,1,3,3,3,2]
        Output: [[1],[0,5],[2,3,4]]

        Input: groupSize = [3, 7, 7, 7, 3, 3, 7, 3, 7, 2, 3, 7, 1, 3, 7, 2, 4, 4, 4, 4, 1]
        Output: [[0, 4, 5], [1, 2, 3, 6, 8, 11, 14], [7, 10, 13], [9, 15], [12], [16, 17, 18, 19], [20]]

        :param groupSizes:
        :return:
        """
        arr_len = len(groupSizes)
        pointer = 0
        return_array = []

        while pointer < arr_len:
            # Stops when a pointer comes to an end of an array
            find_me = groupSizes[pointer]  # Contains value of numbers to find
            current_array = []  # Holds the indexes of certain numbers

            for i in range(pointer, arr_len):
                # Starts at pointer ends at the end of the array
                if groupSizes[i] == find_me:
                    # When encounter a number that we are looking for
                    current_array.append(i)
                    groupSizes[i] = -1  # Changes the number to not add id twice

                if len(current_array) == find_me:
                    # When found enough indexes
                    return_array.append(current_array)
                    break

            while pointer != arr_len:
                # Stops when encountered a -1
                pointer += 1

                if pointer != arr_len:
                    # When not out of range
                    find_me = groupSizes[pointer]

                if find_me != -1:
                    # When encountered new number
                    break

        return return_array


if __name__ == '__main__':
    sol = Solution()
    x = [3, 7, 7, 7, 3, 3, 7, 3, 7, 2, 3, 7, 1, 3, 7, 2, 4, 4, 4, 4, 1]
    print(sol.groupThePeople(x))
