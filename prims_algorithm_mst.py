import heapq
class Solution:
    def spanningTree(self, V, edges):
        
        adj = [[] for _ in range(V)]
        for a,b,c in edges:
            adj[a].append((b,c))
            adj[b].append((a,c))
        ans = 0
        pq = [(0,0)]
        vist = [-1] * V
        # vist[0] = 1
        while pq:
            dist,node = heapq.heappop(pq)
            if vist[node] == 1:
                continue
            vist[node] = 1
            ans += dist
            for nei , wt in adj[node]:
                if vist[nei] == -1:
                    heapq.heappush(pq,(wt,nei))
        return ans