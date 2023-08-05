# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        """
        Count how many students are not able to buy a sandwich
        students is a queue of 0 and 1
        sandwiches is a stack of 0 and 1

        If both a student and a sandwich have the same value,
        then both are eliminated.

        If both a student and a sandwich have other value,
        the student goes to the end of the queue

        Function returns the number of students that cannot eat a sandwich.
        """

        hungry = 0

        while hungry != len(students):

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                hungry = 0
            else:
                students.append(students.pop(0))
                hungry += 1

            if len(students) == 0:
                return 0

        return hungry


if __name__ == '__main__':
    studs = [1, 0, 0, 0]
    sans = [1, 1, 0, 0]

    sol = Solution()
    print(sol.countStudents(studs, sans))
