class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # profit = 0 
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices), 1):
        #         p = prices[j] - prices[i]
          
        #         if  profit<p :
        #             profit = p
                  

        # return profit

       
        profit = 0 
        l = 0 
        r  = 1

        while r < len(prices):
           


            if  prices[l]> prices[r]:
                l = r

            else :
                 p  =  prices[r] - prices[l]

                 if p> profit:
                        profit =  p


           

          
            r += 1

        return profit