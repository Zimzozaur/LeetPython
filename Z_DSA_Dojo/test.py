#
from random import randint
# x = 0
# y = 25
# lett = "QWERTYUIOPASDFGHJKLZXCVBNM"
# print([str(lett[randint(x, y)]) for num in range(100)])


# print(sorted([randint(1, 100) for num in range(20)]))
res = set()
nums = [[6,20,43,98],[6,20,67,74],[6,26,39,96],[6,26,42,93],[6,28,39,94],[6,28,42,91],[6,28,43,90],[9,20,42,96],[9,20,43,95],[9,26,39,93],[9,26,42,90],[9,28,39,91],[12,20,39,96],[12,20,42,93],[12,26,39,90],[12,39,42,74],[20,26,26,95],[20,26,28,93],[26,28,39,74]]
for num in nums:
    for n in num:
        res.add(n)

print(sorted(res))




# strings = ["apple", "banana", "cherry", "date", "fig"]
# longest_length = max(map(len, strings))
# print(longest_length)
