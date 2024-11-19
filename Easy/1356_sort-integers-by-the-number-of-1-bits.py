from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Sort using a custom key: (number of 1's in binary, value)
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
