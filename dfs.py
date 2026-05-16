class Solution:
    def dfs(self, adj):
        n = len(adj)
        ans = []
        vist = [-1] * n
        def func(root):
            nonlocal ans,vist
            ans.append(root)
            vist[root] = 1
            for nei in adj[root]:
                if vist[nei] == -1:
                    func(nei)
        func(0)
        return ans