class Solution(object):
    def reversePrefix(self, word, ch):
        index = word.find(ch)
        if index == -1:
            return word
        
        # Reverse the segment from the start to the index of ch (inclusive)
        reversed_segment = word[:index+1][::-1]
        
        # Concatenate the reversed segment with the rest of the word
        result = reversed_segment + word[index+1:]
        
        return result

# Testing the function
solution = Solution()
print(solution.reversePrefix("abcdefd", "d")) 
