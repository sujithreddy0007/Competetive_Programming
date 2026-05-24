from collections import deque
class Solution:
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        for a,b in edges:
            adj[a].append(b)
        vist = [-1] * V
        stack = []
        def dfs(root):
            vist[root] = 1
            for nei in adj[root]:
                if vist[nei] == -1:
                    dfs(nei)
            stack.append(root)
        
        for i in range(V):
            if vist[i] == -1:
                dfs(i)
        ans = []
        while stack:
            ans.append(stack.pop())
        return ans
        
        