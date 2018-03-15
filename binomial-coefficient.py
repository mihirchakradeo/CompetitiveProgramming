'''
The Problem
Write a function that takes two parameters n and k and returns the value of Binomial Coefficient C(n, k).
For example, your function should return 6 for n = 4 and k = 2, and it should return 10 for n = 5 and k = 2.
'''

class Solution:

    def __init__(self):
        self.d = dict()
        self.d[(1,0)] = 1
        self.d[(1,1)] = 1

    def binomial_recursive(self, n, k):

        if n == k:
            return 1

        if k == 0:
            return 1

        return self.binomial_recursive(n-1, k) + self.binomial_recursive(n-1, k-1)


    def binomial_memoized(self, n, k):

        if (n,k) in self.d:
            return self.d[(n,k)]

        self.d[(n,k)] = self.binomial_recursive(n-1, k) + self.binomial_recursive(n-1, k-1)

        return self.d[(n,k)]

o = Solution()
x = o.binomial_recursive(6,3)
print x
x = o.binomial_memoized(6,3)
print x
