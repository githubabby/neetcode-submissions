class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 10 1 5 6 7 1
        # bs
        #   bs
        #    b s
        #    b   s
        #    b     s
        b,s,p,i = 0,0,0,0
        while i<len(prices):
            if prices[i]>prices[s]:
                s=i
                p = max(p, prices[s]-prices[b])
            if prices[i]<prices[b]:
                b=i
                s=i
            i+=1
        return p

    