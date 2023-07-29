import random


def quick_sort(arr, left, right):
    """

    :param arr:
    :param left:
    :param right:
    :return:
    """

    if left >= right:
        return

    pivot = partition(arr, left, right)

    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)


def partition(arr, left, right):
    """
    Sorts list into left part, pivot and right
    :param arr:
    :param left:
    :param right:
    :return:
    """
    i = left - 1
    pivot = arr[right]

    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1


if __name__ == '__main__':

    array_to_sort = [8, 2, 5, 3, 9, 4, 7, 6, 1]

    sort_me = [random.randint(0, 1000) for i in range(100)]
    quick_sort(sort_me, 0, len(sort_me) - 1)
    print(sort_me)

