from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create a hashmap to store the last seen index of each element
        index_map = {}
        
        # Iterate through the list, tracking the index of each element
        for i, num in enumerate(nums):
            # Check if the element is in the map and if the condition is satisfied
            if num in index_map and i - index_map[num] <= k:
                return True
            # Update the last seen index of the element in the map
            index_map[num] = i
        
        # If no such pair is found, return False
        return False
