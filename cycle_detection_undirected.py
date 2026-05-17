class Solution:
    def isCycle(self, V, edges):
        adj = [[] for _ in range(V)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        vist = [-1] * V
        def dfs(root,par):
            vist[root] = 1
            for nei in adj[root]:
                if nei == par:
                    continue
                if vist[nei] == 1:
                    return True
                res = dfs(nei,root)
                if res:
                    return True
            return False
        for i in range(V):
            if vist[i] == -1:
                if dfs(i,-1):
                    return True
        return False