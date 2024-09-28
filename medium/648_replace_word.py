class Solution(object):
    def replaceWords(self, dictionary, sentence):
        words = sentence.split()  
        for i in range(len(words)):
            for j in dictionary:
                if words[i].startswith(j):
                    words[i] = j
                    break 
        return " ".join(words)  

solution = Solution()
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
result = solution.replaceWords(dictionary, sentence)
