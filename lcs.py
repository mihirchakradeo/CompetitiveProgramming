'''
Length of LCS:
LCS for input Sequences ABCDGH and AEDFHR is ADH of length 3.
LCS for input Sequences AGGTAB and GXTXAYB is GTAB of length 4
'''

class Solution:


    def __init__(self):
        self.d = dict()
        self.d[("","")] = 0

    def lcs_recursive(self, a, b, m, n):

        if m == 0 or n == 0:
            return 0

        if a[m-1] == b[n-1]:
            return 1 + self.lcs_recursive(a, b, m-1, n-1)

        else:
            return max(self.lcs_recursive(a, b, m, n-1), self.lcs_recursive(a, b, m-1, n))


    def lcs_memoized(self, a, b, m, n):

        if (a,b) in self.d:
            return self.d[(a,b)]

        if m == 0 or n == 0:
            return 0

        if a[m-1] == b[n-1]:
            self.d[(a,b)] = 1 + self.lcs_recursive(a, b, m-1, n-1)

        else:
            self.d[(a,b)] =  max(self.lcs_recursive(a, b, m, n-1), self.lcs_recursive(a, b, m-1, n))

        return self.d[(a,b)]


a = "AGGTAB"
m = len(a)
b = "GXTXAYB"
n = len(b)

o = Solution()
x = o.lcs_recursive(a, b, m, n)
print x
x = o.lcs_memoized(a, b, m, n)
print x
