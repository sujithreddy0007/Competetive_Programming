#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [float('inf')] * V
        dist[src] = 0
        for _ in range(V-1):
            for u,v,wt in edges:
                if dist[u] == float('inf'):
                    continue
                if dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
        for _ in range(1):
            for u,v,wt in edges:
                if dist[u]+wt < dist[v]:
                    return [-1]
        for i in range(V):
            if dist[i] == float('inf'):
                dist[i] = 10**8
        return dist