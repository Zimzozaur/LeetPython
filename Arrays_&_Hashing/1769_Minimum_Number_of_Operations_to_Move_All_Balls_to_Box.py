# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        """
        You are given binary string boxes of length n,
        where boxes[i] is '0' if the ith box is empty,
        and '1' if it contains one ball.

        In one operation, you can move one ball from a box to an adjacent box.
        Box i is adjacent to box j if abs(i - j) == 1.

        Return an array answer of size n,
        where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

        I: "110"     I: "10"   I:"100"       I: "0 0 1 0 1 1"
        O: [1,1,3]   O: [0,1]  O: [0,1,2]    O: [11,8,5,4,3,4]

        Speed: 0(n^2)
            For every number check distance for every other number.

        Speed: 0(n)
            Build an array of full box indexes.
            loop over all boxes and count the distance
        :param boxes:
        :return:
        """
        len_arr = len(boxes)
        full_boxes = []
        return_arr = []

        for i in range(len_arr):
            # Adds indexes of full boxes
            if boxes[i] == "1":
                full_boxes.append(i)

        for i in range(len_arr):
            sum_box = 0
            for j in full_boxes:
                # Count absolute distances to every box
                if j != i:
                    sum_box += abs(i - j)
            return_arr.append(sum_box)

        return return_arr


if __name__ == '__main__':
    sol = Solution()
    x = "0"
    print(sol.minOperations(x))
