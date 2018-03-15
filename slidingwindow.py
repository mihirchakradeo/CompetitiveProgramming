'''
Sliding window can be used to solve substring matching problems in linear time
Example: finding length of largest substring with non repeating characters
eg- abcabcbb: 3
'''

class Solution:
    def sliding_window(self, s):

        start = 0
        maxlen = 0
        d = {}

        for end in range(len(s)):
            if s[end] in d:
                start = max(start, d[s[end]]+1)
            d[s[end]] = end
            maxlen = max(maxlen, end-start+1)

        return maxlen

o = Solution()
x = o.sliding_window("abcabcbb")
print x
