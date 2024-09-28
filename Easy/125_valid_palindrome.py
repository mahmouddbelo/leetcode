class Solution(object):
    def isPalindrome(self, s):
        S = ''.join(char.lower() for char in s if char.isalnum())
        return S == S[::-1]