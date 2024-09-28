class Solution(object):
    def lengthOfLastWord(self, s):
        words=s.split()
        return len(words[-1])

solution=Solution() 
s="mahmoud belooo"
print(solution.lengthOfLastWord(s))       
        
        