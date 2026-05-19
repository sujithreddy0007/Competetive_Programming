#User function Template for python3
from typing import List
class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.size = [1] * n

    def find(self, node):
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])
        return self.par[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return True

        if self.size[pu] < self.size[pv]:
            self.par[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.par[pv] = pu
            self.size[pu] += self.size[pv]
        return False

class Solution:
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        dsu = DSU(V)
        edges.sort(key = lambda x : x[2])
        ans = 0
        for u,v,wt in edges:
            if dsu.union(u,v):
                continue
            ans += wt
            dsu.union(u,v)
        return ans