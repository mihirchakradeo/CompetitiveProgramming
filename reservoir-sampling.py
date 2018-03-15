import random

class Solution:

    def __init__(self):
        self.res = []
        self.k = 10

    def reservoir_sampling(self, num):
        if len(self.res) >= self.k:
            r = random.randint(0,len(self.res)-1)
            if r < len(self.res):
                self.res[r] = num
        else:
            self.res.append(num)

o = Solution()
stream = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for i in range(len(stream)):
    o.reservoir_sampling(stream[i])
    print o.res
