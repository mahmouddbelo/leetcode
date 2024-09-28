from math import gcd
from functools import reduce
from typing import List

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # Calculate the GCD of all elements in the array
        total_gcd = reduce(gcd, nums)
        # Check if the GCD is 1
        return total_gcd == 1
