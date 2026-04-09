class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Start with a very high number so the first price becomes the new min
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # 1. Update our 'buy' price if we find a new low
            if price < min_price:
                min_price = price
            
            # 2. See how much profit we'd make if we sold TODAY
            current_profit = price - min_price
            
            # 3. If this profit is the best we've seen, remember it
            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit