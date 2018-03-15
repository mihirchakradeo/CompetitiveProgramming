'''
Given array with coefficients of polynomial with power index, find derivative
Example: 10x^3 + 4x^2 + 7x + 9 = [9,7,4,10] should return [7, 8, 30]
'''

def derivative(p):
    # res = []
    # for i in range(len(p)):
    #     if i == 0:
    #         continue
    #     res.append(i*p[i])
    # return res
    res = {}
    for i in p:
        if i == 0:
            res[i] = 0
            continue
        res[i] = i*p[i]
    return res
# p = [9,7,4,10]
d = {0:9, 1:7, 2:4, 3:10}
x = derivative(d)

print x
