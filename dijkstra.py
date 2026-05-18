import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        adj = [[] for _ in range(V)]
        for a,b,c in edges:
            adj[a].append((b,c))
            adj[b].append((a,c))
        pq = [(0,src)]
        dist = [float('inf')] * V
        dist[src] = 0
        while pq:
            currDist,node = heapq.heappop(pq)
            if currDist > dist[node]:
                continue
            for nei, wei in adj[node]:
                newDist = currDist + wei
                if newDist < dist[nei]:
                    dist[nei] = newDist
                    heapq.heappush(pq,(newDist,nei))
        return dist
        