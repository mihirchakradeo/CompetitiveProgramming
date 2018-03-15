'''
Dijkstra's SSSP Algorithm
Can be used to solve graph/network problems in quadratic time
Time Complexity can be improved with heaps
'''
class Solution:

    def sssp(self, nodes, n, k):

        graph = {}

        for i in nodes:
            graph[i[0]] = []

        for i in nodes:
            graph[i[0]].append((i[1],i[2]))
        print "Graph: ", graph

        visited = [False for i in range(n+1)]
        print "Visited: ", visited

        d = {i:float('inf') for i in range(1,n+1)}

        d[k] = 0

        print "Distances: ",d

        while True:

            #get the next min node
            curr = -1
            curr_dist = float('inf')

            for i in range(1,n+1):
                if not visited[i] and d[i] < curr_dist:
                    curr = i
                    curr_dist = d[i]
                    print "Consider: ",curr,curr_dist

            if curr < 0:
                break
            visited[curr] = True

            if curr in graph:
                for next, cost in graph[curr]:
                    print next,cost
                    d[next] = min(d[next], cost + d[curr])
        print d

o = Solution()
x = o.sssp([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
print x
