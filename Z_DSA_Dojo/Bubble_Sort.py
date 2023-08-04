def bubble_sort(arr):

    # Holds number of iterations to perform
    k = len(arr)

    while k > 1:
        curr = arr[0]
        for i in range(1, k):
            # Swap when curr is bigger
            if arr[i] < curr:
                temp = arr[i]
                arr[i - 1] = temp
                arr[i] = curr
            # Swap curr to bigger value
            else:
                curr = arr[i]
        k -= 1


if __name__ == '__main__':
    data_set = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print(data_set)
    print()
    bubble_sort(data_set)
    print(data_set)


