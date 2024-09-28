class Solution(object):
    def binaryGap(self, n):
        binary = bin(n)[2:]      
        positions = [i for i, bit in enumerate(binary) if bit == '1']      
        if len(positions) < 2:
            return 0     
        max_distance = max(positions[i] - positions[i - 1] for i in range(1, len(positions)))        
        return max_distance

# Example usage:
solution = Solution()
n = 22
print(solution.binaryGap(n))  # Expected output: 2 (binary representation "10110", distances: 2 and 1)
