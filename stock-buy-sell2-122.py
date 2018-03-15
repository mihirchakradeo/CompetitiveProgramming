class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if prices == []:
            return 0

        if len(prices) == 1:
            return 0

        i = 0
        profit = 0

        while i < len(prices)-1:

            #find local minima
            while i < len(prices)-1 and prices[i] >= prices[i+1]:
                i += 1

            #store value of local minima in some temp
            temp = prices[i]

            #find local maxima
            while i < len(prices)-1 and prices[i] <= prices[i+1]:
                i += 1

            #calc profit
            profit += (prices[i] - temp)

        return profit
