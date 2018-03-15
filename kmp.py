'''
KMP string matching algorithm

Time: O(m+n)
Space: O(n)

m = len(s1), n = len(s2)

Renditioned from Tushar Roy's Video: https://www.youtube.com/watch?v=GTJr8OvyEVQ
Use example: abxabcabcaby, abcaby
'''


class Solution:

    def kmp(self, s1, s2):

        lps = self.get_lps(s2)

        i = 0
        j = 0

        while i < len(s1):

            if j == len(lps):
                return True

            # print i,s1,j,lps

            if s1[i] == s2[j]:
                i += 1
                j += 1

            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1

        if j == len(s2):
            return True
        else:
            return False


    def get_lps(self, s):
        #getting the least prefix string
        lps = [0]*len(s)
        lps[0] = 0
        j = 0
        i = 1

        while i < len(s):

            if s[i] == s[j]:
                lps[i] = j + 1
                j += 1
                i += 1

            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps


o = Solution()
x = o.kmp("abxabcabcaby", "abcaby")
print x
