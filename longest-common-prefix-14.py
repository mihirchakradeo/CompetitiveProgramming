'''
Write a function to find the longest common prefix string amongst an array of strings.
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None:
            return ""

        d = dict()

        #creating hashmap
        for string in strs:

            if string == "":
                if string not in d:
                    d[string] = 1

            for i in range(len(string)):

                if i == 0:
                    if string[i] not in d:
                        d[string[i]] = 1
                else:
                    if string[:i] not in d:
                        d[string[:i]] = 1
                    else:
                        d[string[:i]] = len(string[:i])

        print d
        #retrieving key with largest value
        maximum = -1
        string = ""

        #first check if no common substring
        flag = 0
        for i in d:
            if d[i] > 1:
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:
            return ""

        for i in d:
            if d[i] > maximum:
                maximum = d[i]
                string = i
        return string


o = Solution()
x = o.longestCommonPrefix(["","b"])
print x
