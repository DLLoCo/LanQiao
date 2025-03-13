class Solution:
    def __init__(self):
        self.res=[]
        self.track=[]
        self.vis=[]

    def traverse(self,step,nums):
        if step>len(nums):
            self.res.append(list(self.track))
            return

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1] and not self.vis[i - 1]:#！ 注意这个条件，见下
                continue
            
            if self.vis[i]==1:
                continue
            
            self.vis[i]=1
            self.track.append(nums[i])
            self.traverse(step+1,nums)
            self.track.pop()
            self.vis[i]=0

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.vis=[0]*len(nums)
        nums.sort()

        self.traverse(1,nums)

        return self.res
    
"""
假设输入为 nums = [1,2,2']
如下答案：
[
    [1,2,2'],[1,2',2],
    [2,1,2'],[2,2',1],
    [2',1,2],[2',2,1]
]
如何设计剪枝逻辑，把这种重复去除掉？

答案是，保证相同元素在排列中的相对位置保持不变。

比如说 nums = [1,2,2'] 这个例子，我保持排列中 2 一直在 2' 前面。
so:
// 新添加的剪枝逻辑，固定相同的元素在排列中的相对位置
if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
    // 如果前面的相邻相等元素没有用过，则跳过
    continue;
}
"""