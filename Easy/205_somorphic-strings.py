class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        map1=[]
        map2=[]
        for indexx in s:
            map1.append(s.index(indexx))
        for indexx in t:
            map2.append(t.index(indexx))  
        if map1==map2:
            return True
solution=Solution()
print(solution.isIsomorphic('egg','add'))          

