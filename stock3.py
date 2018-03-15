'''
Stock problem in which you have to make k transactions
'''


class Solution:

    def stock_dp(self, profits, k):
        d = [[0]*(len(profits)) for _ in range(k+1)]
        self.print_d(d)

        for i in range(len(d)):
            for j in range(len(d[0])):
                if i == 0 or j == 0:
                    d[i][j] = 0
                    continue

                #not selling, best selling
                temp = max((profits[j]-profits[m]+d[i-1][m]) for m in range(0,j))
                # print temp
                d[i][j] = max(d[i][j-1], temp)
        self.print_d(d)
        return d



    def print_d(self, d):
        for i in range(len(d)):
            print d[i]

        print


profits = [2,5,7,1,4,3,1,3]
k = 3
o = Solution()
x = o.stock_dp(profits, k)
print x[-1][-1]
