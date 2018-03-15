class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        #m and n are num of ele in nums1 and nums2

        if n == 0:
            return nums1

        if m == 0:
            nums1[:] = nums2[:]
            return nums1

        ctr = len(nums1) - 1

        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[ctr] = nums1[m-1]
                m -= 1
                ctr -= 1

            elif nums1[m-1] < nums2[n-1]:
                nums1[ctr] = nums2[n-1]
                n -= 1
                ctr -= 1

        if n > 0:
            nums1[:n] = nums2[:n]

        return nums1

o = Solution()
x = o.merge([1,2,3,0,0,0],3,[2,5,6],3)
print x
