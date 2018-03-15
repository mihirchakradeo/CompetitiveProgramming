'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        d = dict()
        d = {"(":")", "[":"]", "{":"}"}

        stack = []

        stack.append(s[0])
        for i in s[1:]:

            #this handles case like this: "[ ] )"
            if stack == []:
                stack.append(i)
                continue

            #top of stack == stack[-1]

            #this handles case of only closing bracket
            if stack[-1] not in d:
                return False

            #this handles matching sub brackets
            elif d[stack[-1]] == i:
                stack.pop()
                continue

            stack.append(i)

        if stack == []:
            return True
        else:
            return False
