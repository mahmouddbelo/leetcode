class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        reversed_x = int(str(abs(x))[::-1])
        result = sign * reversed_x
        return result if -2**31 <= result <= 2**31 - 1 else 0
