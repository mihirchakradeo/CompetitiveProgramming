'''
Facebook interview question:
Given an array of unique elements, return all possible subsets
[1,2] -> [], [1], [2], [1,2]
'''

class Solution:
    #
    # def __init__(self):
    #     self.subset = list()
    #
    # def subsets_iterative(self, a):
    #
    #     self.subset.append([])
    #     for i in range(len(a)):
    #         for j in range(i+1, len(a)+1):
    #             print i,j
    #             self.subset.append(a[i:j])
    #     return self.subset
    #
    #
    # def subsets_backtracking(self, a, temp, start):
    #     self.subset.append(temp[:])
    #     for i in range(start, len(a)):
    #         temp.append(a[i])
    #         self.subsets_backtracking(a, temp, i+1)
    #         temp.pop()
    #
    #     return self.subset

    def subset(self, nums)
        res = []
        path = []
        i = 0
        nums.sort()
        self.dfs(nums, i, path, res)
        return res

    def dfs(self, nums, i, path, res):
        if path not in res:
            res.append(path)
        for j in range(i,len(nums))):
            self.dfs(nums,j+1,path+[nums[j]],res)


o = Solution()
x = o.subsets_iterative([1,2])
print x

x = o.subsets_backtracking([1,2], [], 0)
print x
