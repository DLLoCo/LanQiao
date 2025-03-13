class Solution:

    def __init__(self):
        self.res=[]
        self.track=[]
        
    def traverse(self,target,start,candidates):
        if sum(self.track)==target:
            self.res.append(list(self.track))
            return
        
        if sum(self.track)>target:#! 忘记考虑，可能和直接超过target
            return
        
        for i in range(start,len(candidates)):
            self.track.append(candidates[i])
            self.traverse(target,i,candidates)#组合不可重复使用元素为i+1，排列为step+1
            self.track.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.traverse(target,0,candidates)
        return self.res
    
"""
    def traverse(self,target,candidates): #! 错误的写法,因为没有start,这是排列的写法
        if sum(self.track)==target:
            self.res.append(list(self.track))
            return
        
        if sum(self.track)>target:
            return
        
        for i in range(len(candidates)):
            self.track.append(candidates[i])
            self.traverse(target,candidates)#! 错误的写法,因为没有start,这是排列的写法
            self.track.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.traverse(target,candidates)#! 错误的写法,因为没有start,这是排列的写法
        return self.res
"""