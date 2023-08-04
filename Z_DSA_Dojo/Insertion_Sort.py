import random


def insertion_sort(arr):

    # Loops from index 1 to end
    for i in range(1, len(arr)):
        curr = arr[i]
        # Loops from i - 1 to 0
        for j in range(i - 1, -1, -1):
            # Move current to the left
            if arr[j] > curr:
                temp = arr[j]
                arr[j] = curr
                arr[j + 1] = temp
            else:
                # If sorted break
                break


if __name__ == '__main__':
    data_set = [random.randint(0, 1000) for num in range(100)]
    print(data_set)
    print()
    insertion_sort(data_set)
    print(data_set)
