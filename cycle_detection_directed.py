class Solution:
    def isCyclic(self, V, edges):
        adj = [[] for _ in range(V)]
        for a,b in edges:
            adj[a].append(b)
        vist = [-1] * V
        def dfs(root):
            vist[root] = 2
            for nei in adj[root]:
                if vist[nei] == 2:
                    return True
                if vist[nei] == -1:
                    res = dfs(nei)
                    if res:
                        return True
            vist[root] = 1
            return False
        for i in range(V):
            if vist[i] == -1:
                res = dfs(i)
                if res:
                    return True
        return False