'''
Given number of coins (1,2,3,...,k), find number of ways to get some total n
'''


class Solution:

    def change_recursive(self, a, m, n):

        if n < 0:
            return 0

        if n == 0:
            return 1

        #when no coins remaining, but total not matched
        if m <= 0 and n > 0:
            return 0

        #ways obtained by not including a coin + including a coin
        w = self.change_recursive(a, m-1, n) + self.change_recursive(a, m, n-a[m-1])

        return w


    def change_dp(self, a, m, n):
        t = [[0 for c in range(n+1)] for r in range(m)]
        for i in range(m):
            print i, t[i]

        print

        for i in range(m):
            for j in range(n+1):
                if i == 0 :
                    t[i][j] = 1

                if i > j:
                    t[i][j] = t[i-1][j]
                else:
                    t[i][j] = t[i-1][j] + t[i][j-i]


        for i in range(m):
            print t[i]



o = Solution()
x = o.change_recursive([1,2,3], 3, 5)
print x
x = o.change_dp([1,2,3], 3, 5)
print x
