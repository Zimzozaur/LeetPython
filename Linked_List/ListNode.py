from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_generator(arr: list) -> Optional[ListNode]:
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


def compare_ll(head1: ListNode, head2: ListNode) -> bool:
    while head1 and head2:
        if head1.val == head2.val:
            head1 = head1.next
            head2 = head2.next
        else:
            return False
    if head1 is None and head2 is None:
        return True
    return False
