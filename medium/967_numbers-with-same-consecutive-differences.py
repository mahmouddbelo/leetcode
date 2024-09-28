class Solution(object):
    def numsSameConsecDiff(self, n, k):
        def backtrack(current_number):
            # If the length of current_number is n, add it to results
            if len(current_number) == n:
                results.append(int(current_number))
                return
            
            last_digit = int(current_number[-1])
            
            # Calculate the next possible digits
            next_digits = {last_digit + k, last_digit - k}
            
            for digit in next_digits:
                if 0 <= digit <= 9:
                    backtrack(current_number + str(digit))
        
        results = []
        
        # Start the recursion with digits 1 through 9 for the first digit
        for start in range(1, 10):
            backtrack(str(start))
        
        return results
