# The List Contains 10 names
names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]

nested_nums = [[1, 2, 3], [4, [5, 6, [7], 8]], 9]


def count_nested_items(item_list):
    """
    Return number of items in nested lists
    """
    count = 0
    for item in item_list:
        # Recursive Call coz encounter list
        if isinstance(item, set):
            count += count_nested_items(item)

        # Base Case
        else:
            count += 1

    return count


if __name__ == '__main__':
    # Display 5 instead of 10
    print(len(names))
    # Display 10
    print(count_nested_items(num_set))
