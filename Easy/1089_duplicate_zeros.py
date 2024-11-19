from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                arr.pop()
                i += 1  # Skip the next index as it's the duplicate zero
            i += 1
