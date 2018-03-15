'''
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
'''


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        #top = image[r-1][c]
        #down = image[r+1][c]
        #left = image[r][c-1]
        #right = image[r][c+1]


        import copy
        res = copy.deepcopy(image)

        # self.print_m(image)
        # print len(image), len(image[0])
        stack = list()
        visited = list()

        stack.append((sr,sc))

        currColor = image[sr][sc]

        while stack:
            # print "------------------------"
            r, c = stack.pop()

            # print "(",r,", ",c,") ","v:",visited,"s:",stack

            if (r,c) in visited:
                # print "r,c in visited"
                continue

            if r>=0 and c>=0 and r<=len(image) and c<=len(image[0]):
                #top
                if  r!=0 and image[r-1][c] == currColor:
                    # print "top"
                    stack.append((r-1,c))

                #down
                if r!=len(image)-1 and image[r+1][c] == currColor:
                    # print "down"
                    stack.append((r+1,c))

                #left
                if c!=0 and image[r][c-1] == currColor:
                    # print "left"
                    stack.append((r,c-1))

                #right
                if  c!=len(image[0])-1 and image[r][c+1] == currColor:
                    # print "right"
                    stack.append((r,c+1))


                visited.append((r,c))

                res[r][c] = newColor

                # print "v:",visited, "s:",stack

        return res

    def print_m(self, image):
        for i in range(len(image)):
            print image[i]
        print
