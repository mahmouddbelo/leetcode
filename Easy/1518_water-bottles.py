class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total_drunk = 0
        empty_bottles = 0
        
        while numBottles > 0:
            # Drink all the current full bottles
            total_drunk += numBottles
            empty_bottles += numBottles
            
            # Exchange empty bottles for new full bottles
            numBottles = empty_bottles // numExchange
            # Remaining empty bottles after the exchange
            empty_bottles %= numExchange
        
        return total_drunk
    