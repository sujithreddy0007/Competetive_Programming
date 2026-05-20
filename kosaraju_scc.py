class Solution:
    
    def kosaraju(self, V, edges):
        # code here
        adj = [[] for _ in range(V)]
        rev = [[] for _ in range(V)]
        for a,b in edges:
            adj[a].append(b)
            rev[b].append(a)
        stack = []
        vist = [-1] * V
        def dfs(node):
            vist[node] = 1
            for nei in adj[node]:
                if vist[nei] == -1:
                    dfs(nei)
            stack.append(node)
        for i in range(V):
            if vist[i] == -1:
                dfs(i)
        vist = [-1] * V
        ans = 0
        def dfs2(node):
            vist[node] = 1
            for nei in rev[node]:
                if vist[nei] == -1:
                    dfs2(nei)
                
        while stack:
            while stack and vist[stack[-1]] != -1:
                stack.pop()
            if stack:
                dfs2(stack.pop())
                ans += 1
        return ans
            