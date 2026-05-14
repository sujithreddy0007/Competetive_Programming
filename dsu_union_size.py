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
            return

        if self.size[pu] < self.size[pv]:
            self.par[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.par[pv] = pu
            self.size[pu] += self.size[pv]
obj = DSU()