#Time Limit Exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        m = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices) ):
                s = prices[j] - prices[i]
                m = max(m,s)
                
        return m
    
#Time good 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l,r = 0,1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1

        return maxP