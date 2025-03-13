class Solution:
    def __init__(self):
        self.res=[]
        self.track=[]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.traverse(0,nums)
        return self.res
    
    def traverse(self,start,nums):

        self.res.append(list(self.track))

        for i in range(start,len(nums)):
            self.track.append(nums[i])
            self.traverse(i+1,nums)#! i+1,不是start+1
            self.track.pop()
        
        return