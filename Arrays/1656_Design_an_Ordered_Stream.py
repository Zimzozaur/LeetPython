# https://leetcode.com/problems/design-an-ordered-stream/
class OrderedStream:
    """
    This class builds dict
    Keys are numbers from 1 to n.
    Values are arrays of letters.
    """
    def __init__(self, n: int):
        self.pointer = 1
        self.dict = {}

    def insert(self, idKey: int, value: str) -> list[str]:
        """
         Inserts the pair (idKey, value) into the stream,
         then returns the largest possible chunk of currently inserted values
         that appear next in the order.
        :param idKey:
        :param value:
        :return:
        """
        self.dict[idKey] = value  # Adds to pair to dict
        if idKey == self.pointer:
            # Check does a pointer point to the inserted pair.
            return_array = []
            while True:
                # True while pointers points to data in dict
                return_array.append(self.dict.get(self.pointer))
                self.pointer += 1
                if self.dict.get(self.pointer) is None:
                    # When a pointer points to None
                    return return_array
        return []


if __name__ == '__main__':
    sol = OrderedStream(5)
    print(sol.insert(3, "c"))
    print(sol.insert(1, "a"))
    print(sol.insert(2, "b"))
    print(sol.insert(5, "e"))
    print(sol.insert(4, "d"))
