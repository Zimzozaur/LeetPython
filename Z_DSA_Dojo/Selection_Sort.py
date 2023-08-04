import random


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        min_val = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_val]:
                min_val = j

        temp = arr[i]
        arr[i] = arr[min_val]
        arr[min_val] = temp


if __name__ == '__main__':
    data_set = [random.randint(0, 1000) for num in range(1000)]
    print(data_set)
    print()
    selection_sort(data_set)
    print(data_set)
