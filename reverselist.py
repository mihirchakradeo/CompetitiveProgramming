def recursive_reverselist(l):
    if len(l) == 1:
        return l
    else:
        first = l[0]
        x = recursive_reverselist(l[1:])
        return  x + [first]


def permutation_recursive(start, end, p, res):
    if start==end:
        res.append(p[:])
    else:
        for i in range(start,end):
            p[start],p[i] = p[i],p[start]
            permutation_recursive(start+1,end,p,res)
            p[start],p[i] = p[i],p[start]
    return res



l = [1,2,3,4]
res = []
x = recursive_reverselist(l)
print x

l = [1,2,3]
res = []
x = permutation_recursive(0,len(l),l,res)
print x
