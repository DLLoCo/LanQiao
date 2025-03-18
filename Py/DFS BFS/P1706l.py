n=int(input())
status=[0]*10
num=[0]*10
ans=[0]*10


"""
i step n 分别代表 ： 
i是循环查找1-n个数的状态，加入到ans中 ，
step是当前的dfs到达第几层，
n是1-n，组合数的个数        
"""
def dfs(step):

    if step==n+1:
        for i in range(1,n+1):
            print(f"{ans[i]:5d}",end="")
        print()
        return
    
    for i in range(1,n+1): #
        if status[i]==0:
            ans[step]=num[i] #! ans[i]=num[i]
            # print(ans)
            status[i]=1
            dfs(step+1) #! dfs(n+1)
            status[i]=0
    
for i in range(1,n+1):
    num[i]=i

dfs(1)
