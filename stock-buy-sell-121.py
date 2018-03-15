'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
'''


class Solution(object):
    def maxProfit_bruteforce(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if prices == []:
            return 0


        flag = 0
        for i in range(len(prices)-1):
            if prices[i+1] < prices[i]:
                continue
            else:
                flag = 1
                break

        if flag == 0:
            return 0

        diff = 0

        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[i] > prices[j]:
                    continue
                elif prices[i] < prices[j]:
                    if prices[j] - prices[i] > diff:
                        diff = prices[j] - prices[i]
        return diff

    def maxProfit_linear(self, profits):

        profit = 0
        minPrice = float('inf')

        for i in profits:
            profit = max(profit, i - minPrice)
            minPrice = min(minPrice, i)

        return profit


o = Solution()
x = o.maxProfit_bruteforce([7, 1, 5, 3, 6, 4])
print x
x = o.maxProfit_linear([7, 1, 5, 3, 6, 4])
print x
