class Solution:
    def __init__(self):
        self.res=[]
        self.track=[]

    def dfs(self,step,nums):

        if step>len(nums):
            self.res.append(list(self.track))
            return
        
        for i in range(len(nums)):
            if nums[i] in self.track:
                continue
            
            self.track.append(nums[i])
            self.dfs(step+1,nums)
            self.track.pop()


    def permute(self, nums: List[int]) -> List[List[int]]:
        self.dfs(1,nums)
        return self.res