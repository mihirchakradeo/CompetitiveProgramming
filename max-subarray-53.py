'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''



class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        Using Kadane's Algorithm
        Initialize:
            max_so_far = 0
            max_ending_here = 0

        Loop for each element of the array
          (a) max_ending_here = max_ending_here + a[i]
          (b) if(max_ending_here < 0)
                    max_ending_here = 0
          (c) if(max_so_far < max_ending_here)
                    max_so_far = max_ending_here
        return max_so_far
        '''

        prev = 0
        curr = float('-inf') - 1

        for i in nums:
            prev = prev + i

            if curr < prev:
                curr = prev

            if prev < 0:
                prev = 0

        return curr




    def maxSubArrayNaive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cnt = 1
        summation = -999
        temp = 0

        while cnt <= len(nums):
            print "Count: ",cnt
            for i in range(len(nums)-cnt+1):
                print "i:", i
                temp = 0
                for j in nums[i:i+cnt]:
                    print "j: ",j
                    temp += j
                print "summation, temp: ",summation, temp
                if temp > summation:
                    summation = temp

            cnt += 1
        return summation

o = Solution()
x = o.maxSubArray([-1])
print x
