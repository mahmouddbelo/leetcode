class Solution(object):
    def sortedSquares(self, nums):
        squared =[x**2 for x in nums]
        return sorted(squared)
    
        