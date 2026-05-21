class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for a,b in connections:
            adj[a].append(b)
            adj[b].append(a)
        tin = [-1] * n
        low = [-1] * n
        timer = 1
        vist = [-1] * n
        bridges = []
        def dfs(node,par):
            nonlocal timer
            vist[node] = 1
            tin[node] = timer
            low[node] = timer
            timer += 1
            for nei in adj[node]:
                if nei == par:
                    continue
                if vist[nei] == -1:
                    dfs(nei,node)
                    low[node] = min(low[node],low[nei])
                    if tin[node] < low[nei]:
                        bridges.append([node,nei])
                else:
                    low[node] = min(low[node],low[nei])
        for i in range(n):
            if vist[i] == -1:
                dfs(i,-1)
        return bridges
