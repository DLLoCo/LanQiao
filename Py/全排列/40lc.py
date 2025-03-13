class Solution:
    def __init__(self):
        self.res=[]
        self.track=[]

    def traverse(self,start,candidates,target):
        if sum(self.track)==target:
            self.res.append(list(self.track))
            return

        if sum(self.track)>target:#! 忘记考虑，可能和直接超过target
            return

        for i in range(start,len(candidates)):
            if i>start and candidates[i]==candidates[i-1]:
                continue

            self.track.append(candidates[i])
            self.traverse(i+1,candidates,target)
            self.track.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        self.traverse(0,candidates,target)

        return self.res