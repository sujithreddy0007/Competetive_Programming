class SG :
    def __init__(self,nums):
        self.nums = nums
        self.n = len(self.nums)
        self.seg = [0] * (4*self.n+1)
        self.lazy = [0] * (4*self.n+1)
        self.build(0,0,self.n-1)
    def build(self,ind,low,high):
        if low == high:
            self.seg[ind] = self.nums[low]
            return
        mid = (low+high)//2
        self.build(ind*2+1,low,mid)
        self.build(ind*2+2,mid+1,high)
        self.seg[ind] = self.seg[ind*2+1]+self.seg[ind*2+2]
    def update(self,left,right,val):
        def upd(ind,low,high):
            if self.lazy[ind] != 0:
                self.seg[ind] += (high-low+1)*self.lazy[ind]
                if low != high:
                    self.lazy[ind*2+1] += self.lazy[ind]
                    self.lazy[ind*2+2] += self.lazy[ind]
                self.lazy[ind] = 0
            if right < low or high < left:
                return
            elif left <= low and high <= right:
                self.seg[ind] += (high-low+1)*val
                if low != high:
                    self.lazy[ind*2+1] += val
                    self.lazy[ind*2+2] += val
                return
            mid = (low+high)//2
            upd(ind*2+1,low,mid)
            upd(ind*2+2,mid+1,high)
            self.seg[ind] = self.seg[ind*2+1]+self.seg[ind*2+2]
        upd(0,0,self.n-1)
    def sumRange(self,left,right):
        def query(ind,low,high):
            if self.lazy[ind] != 0:
                self.seg[ind] += (high-low+1)*self.lazy[ind]
                if low != high:
                    self.lazy[ind*2+1] += self.lazy[ind]
                    self.lazy[ind*2+2] += self.lazy[ind]
                self.lazy[ind] = 0
            if right < low or high < left:
                return 0
            elif left <= low and high <= right:
                return self.seg[ind]
            mid = (low+high)//2
            leftAns = query(ind*2+1,low,mid)
            rightAns = query(ind*2+2,mid+1,high)
            return leftAns + rightAns
        return query(0,0,self.n-1)
