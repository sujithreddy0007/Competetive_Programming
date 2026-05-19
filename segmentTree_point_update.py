from typing import List
class SGTree:
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(self.nums)
        self.seg = [0] * (4*self.n)
        self.build(0,0,self.n-1)
    def build(self,ind,low,high):
        if low == high:
            self.seg[ind] =  self.nums[low]
            return
        mid = (low + high)//2
        self.build(ind*2+1,low,mid)
        self.build(ind*2+2,mid+1,high)
        self.seg[ind] = self.seg[ind*2+1] + self.seg[ind*2+2]
    def update(self, index: int, val: int) -> None:
        def upd(ind,low,high):
            if low == high:
                self.seg[ind] = val
                self.nums[index] = val
                return
            mid = (low+high)//2
            if index <= mid:
                upd(ind*2+1,low,mid)
            else:
                upd(ind*2+2,mid+1,high)
            self.seg[ind] = self.seg[ind*2+1] + self.seg[ind*2+2]
        upd(0,0,self.n-1)

    def sumRange(self, left: int, right: int) -> int:
        def query(ind,low,high):
            if left <= low and high <= right:
                return self.seg[ind]
            elif high < left or right < low:
                return 0
            else:
                mid = (low + high)//2
                leftAns = query(ind*2+1,low,mid)
                rightAns = query(ind*2+2,mid+1,high)
                return leftAns + rightAns
        return query(0,0,self.n-1) 



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)