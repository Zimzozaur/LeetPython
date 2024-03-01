# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

class SparseVector:
    """
    Take list as input and turns it into HashMap
    where key is index and value is value
    This class is iterable just loops over the HashMap
    """
    def __init__(self, nums: list[int]):
        self.has_map = {key: value for key, value in enumerate(nums) if value > 0}

    def __iter__(self):
        return self.has_map

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for key, value in vec.has_map.items():
            if key in self.has_map:
                res += value * self.has_map.get(key)
        return res



