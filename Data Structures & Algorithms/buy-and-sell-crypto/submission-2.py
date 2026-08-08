class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] < prices[i]:
                    j += 1
                else:
                    newProfit = prices[j] - prices[i]
                    output = max(output, newProfit)
        return output