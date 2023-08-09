# https://leetcode.com/problems/design-linked-list/
class MyLinkedList:
    """Create Doubly Linked Lists"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = -1

    def get(self, index: int) -> int:
        """
        Get the value of the index node in the linked list.
        If the index is invalid, return -1.
        """
        if index > self.length:
            return -1

        temp = self.head

        for i in range(index):
            temp = temp.next

        return temp.val

    def addAtHead(self, val: int) -> None:
        """ Add a node of value val before the first element of the linked list."""
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.length == 0:
            self.head = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    def addAtTail(self, val: int) -> None:
        """ Add a node of value val after the last element of the linked list."""
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        elif self.length == 0:
            self.head.next = new_node
            new_node.prev = self.head
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals the length of the linked list,
        the node will be appended to the end of the linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return
        elif self.length + 1 < index:
            return
        elif index == self.length + 1:
            self.addAtTail(val)
            return
        elif self.length == 1 and index == 1:
            new_node = Node(val)
            self.head.next = new_node
            new_node.prev = self.head
            self.tail.prev = new_node
            new_node.next = self.tail
        else:
            temp = self.head
            new_node = Node(val)
            for i in range(index - 1):
                temp = temp.next

            after = temp.next
            after.prev = new_node
            before = temp
            before.next = new_node
            new_node.next = after
            new_node.prev = before

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """Delete the index-th node in the linked list if the index is valid."""
        if self.length < index:
            return
        if self.length == 0:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.length:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            prev = temp.prev
            after = temp.next
            prev.next = after
            after.prev = prev

        self.length -= 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next


class Node:
    """Create Node"""
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


if __name__ == '__main__':
    # node_list = MyLinkedList()

    # Arrays with method names and arguments
    method_names = ["addAtHead","addAtHead","addAtTail","addAtTail","addAtTail"]

    arguments = [[2],[1],[4],[5],[6]]

    # Initialize an instance of the class
    linked_list = MyLinkedList()

    # Iterate through the method names and arguments
    for i in range(len(method_names)):
        method_name = method_names[i]
        args = arguments[i]

        # Get the method object by name
        method = getattr(linked_list, method_name)

        # Call the method with the arguments
        result = method(*args)

        # Print the result
        print(f"Method: {method_name}, Args: {args}, Result: {result}")

    # commands_dict = {
    #     "addAtHead": node_list.addAtHead()
    # }
    #
    # node_list.addAtHead(1)
    # node_list.addAtTail(3)
    # node_list.addAtIndex(1, 2)
    # print(node_list.get(1))
    # node_list.deleteAtIndex(1)
    # print(node_list.get(1))

    # ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
    # [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
    # node_list.addAtHead(7)
    # node_list.addAtHead(2)
    # node_list.addAtHead(1)
    # node_list.addAtIndex(3, 0)
    # node_list.deleteAtIndex(2)
    # node_list.addAtHead(6)
    # node_list.addAtTail(4)
    # node_list.get(4)
    # node_list.addAtHead(4)
    # node_list.addAtIndex(5, 0)
    # node_list.addAtHead(6)



