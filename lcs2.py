'''
Reconstructing the lcs
'''

class Solution:

    def lcs_dp(self, a, b, m, n):
        d = [[0]*(n+1) for j in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    d[i][j] = 0

        for i in range(1,m+1):
            for j in range(1,n+1):
                if a[i-1] != b[j-1]:
                    d[i][j] = max(d[i][j-1], d[i-1][j])
                elif a[i-1] == b[j-1]:
                    d[i][j] = 1 + d[i-1][j-1]

        for i in range(m+1):
            print d[i]

        #Reconstructing
        seq = list()
        i = m
        j = n
        while i != 0 and j != 0:
            if d[i][j] == d[i][j-1] or d[i][j] == d[i-1][j]:
                #letter not in seq
                #check where the number came from
                if d[i][j] == d[i][j-1]:
                    #move left
                    j -= 1
                elif d[i][j] == d[i-1][j]:
                    #move up
                    i -= 1
            elif d[i][j] == d[i-1][j-1] + 1:
                #came from diagonal -> include letter
                seq.append(b[j-1])
                i -= 1
                j -= 1

        return seq[::-1]


a = "dbbc"
m = len(a)
b = "cbbd"
n = len(b)

o = Solution()
x = o.lcs_dp(a, b, m, n)
print x
