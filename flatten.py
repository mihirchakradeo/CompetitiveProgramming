
class Solution:

    def __init__(self):
        self.res = []

    def flatten(self, nums, i):
        if i > len(nums)-1:
            return

        if type(nums[i]) is list:
            self.flatten(nums[i],0)
            self.flatten(nums,i+1)
        else:
            self.res.append(nums[i])
            self.flatten(nums,i+1)


        return self.res






o = Solution()
x = o.flatten([1,[2,3],4,[5,6,[7,8]]],0)
print x
