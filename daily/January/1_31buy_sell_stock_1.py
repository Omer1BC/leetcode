class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        params:
            prices: list of prices
        return:
            p: maximum number of profit collected
        '''
        #Init profit and previous move
        p = 0
        prev = prices[0]

        for n in prices:
            #If stock is optimal to sell, increment the profit by that much
            if n > prev:
                p += n - prev
            prev = n
        return p
        # cache = {}
        # def prof(i,b):
        #     if i == len(prices):
        #         return 0
        #     if (i,b) in cache:
        #         return cache[(i,b)]
        #     else:
                
        #         if b:
        #             cache[(i,b)] = max(prof(i+1,not b) - prices[i],prof(i+1,b))
        #             return  cache[(i,b)]
        #         else:
        #             cache[(i,b)] = max(prof(i+1,not b) + prices[i],prof(i+1,b))
        #             return cache[(i,b)]
        # return prof(0,True)