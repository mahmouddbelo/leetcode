class Solution(object):
    def maximumValue(self, strs):
        max_val = 0
        for s in strs:
            if s.isdigit():
                # If the string is a digit, convert it to an integer
                value = int(s)
            else:
                # Otherwise, the value is the length of the string
                value = len(s)
            max_val = max(max_val, value)
        return max_val
