class DSU :
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
    def find_par(self,node):
        if self.par[node] == node:
            return node
        self.par[node] = self.find_par(self.par[node])
        return self.par[node]
    def unionByrank(self,u,v):
        ulp_u = self.find_par(u)
        ulp_v = self.find_par(v)
        
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.par[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.par[ulp_v] = ulp_u
        else:
            self.par[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
