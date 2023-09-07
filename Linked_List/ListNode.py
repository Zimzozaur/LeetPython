class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_generator(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return ListNode(arr[0])

    head = ListNode(arr[0])
    temp = head
    for num in arr[1:]:
        temp.next = ListNode(num)
        temp = temp.next

    return head