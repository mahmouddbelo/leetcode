class Solution(object):
    def missingNumber(self, nums):
        for num in range(0,len(nums)+1):
            if num not in nums:
                return num

        