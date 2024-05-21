class Solution:
    def maxProfit(self,prices):

        left = 0
        right= 1
        maximum_profit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]

            if prices[left] > prices[right] :
                left = right
            else :
                 maximum_profit = max(maximum_profit,profit)
            right += 1
        

        return  maximum_profit

    

             
        