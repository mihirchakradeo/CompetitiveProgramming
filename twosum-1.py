'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution(object):
    def twoSumNaive(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: nums[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]

    def twoSumHashing(self, nums, target):
        d = dict()
        for i in range(len(nums)):
            d[nums[i]] = i
        print d
        for i in d:
            diff = abs(i - target)
            print "i, diff: ",i,diff
            if d.has_key(diff) and d.get(diff) != d[i]:
                return [d[i],d[diff]]   

        return False


s = Solution()
x = s.twoSumHashing([3,3],6)
print x
