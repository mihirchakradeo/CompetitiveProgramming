'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''



class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        size = len(digits)

        total = 0

        #convert array to int
        for i in range(len(digits)):
            temp = (10**i) * (digits.pop())
            total += temp

        total += 1

        print total
        print "size:",size
        #convert int to array
        # for j in range(size, 0, -1):
        #
        #     temp1 = (total) / (10**(j-1))
        #     print temp1
        #     temp2 = (total) % (10**(j-1))
        #     digits.append(temp1)
        #     total = temp2
        #
        # return digits
        a = list()
        for i in range(size+1):
            a.append(total%10)
            total = total/10
        print a.reverse()


o = Solution()
x = o.plusOne([9,9,9])
print x
