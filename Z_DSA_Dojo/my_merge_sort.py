import random


def merge_sort(arr, start, end):
    """Divide an array into smaller arrays"""
    if end - start + 1 <= 1:
        return arr

    mid = (end + start) // 2

    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)

    merge(arr, start, mid, end)

    return arr


def merge(arr, start, mid, end):
    """Merge two arrays into one in ascending order"""

    left = arr[start: mid + 1]
    right = arr[mid + 1: end + 1]

    left_pointer = right_pointer = 0
    arr_pointer = start

    # Compare numbers
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            arr[arr_pointer] = left[left_pointer]
            left_pointer += 1
            arr_pointer += 1
        else:
            arr[arr_pointer] = right[right_pointer]
            right_pointer += 1
            arr_pointer += 1

    # Merge rest of left
    while left_pointer < len(left):
        arr[arr_pointer] = left[left_pointer]
        arr_pointer += 1
        left_pointer += 1

    # Merge rest of right
    while right_pointer < len(right):
        arr[arr_pointer] = right[right_pointer]
        arr_pointer += 1
        right_pointer += 1

    return arr


if __name__ == '__main__':
    arr_me = [random.randint(1, 1000) for num in range(4000)]
    print()
    print(merge_sort(arr_me, 0, len(arr_me)))
