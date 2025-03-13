class Solution:
    def __init__(self):
        self.res=[]
        self.track=[]

    def traverse(self,start,nums):
        self.res.append(list(self.track))

        for i in range(start,len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue

            self.track.append(nums[i])
            self.traverse(i+1,nums)#！ i+1不是start+1，见下
            self.track.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        self.traverse(0,nums)

        return self.res
    
''''
i+1不是start+1，如果是start+1，那么输入nums =[1,2,2]，会产生[2,2,2]
可以从78lc.py考虑
'''