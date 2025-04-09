t,n=map(int,input().split())
c=[0]
w=[0]
for i in range(n):
    ci,wi=map(int,input().split())
    c.append(ci)
    w.append(wi)
ans=0
dp=[[0]*(n+1) for _ in range(t+1)]
#!
"""
1. DP数组定义错误
    你定义了 dp = [[0]*n for _ in range(t)]，其中：
    i 从 0 到 t-1（行数为 t），表示背包容量。
    j 从 0 到 n-1（列数为 n），表示前 j+1 个物品。

    在01背包问题中，dp[i][j] 通常表示“使用前 j+1 个物品，背包容量为 i 时的最大价值”。但你的数组：
    容量只到 t-1（例如 t=70 时，最大容量是 69），无法表示容量 t。

    当 j=0 时，dp[i][j-1] 会访问 dp[i][-1]，导致索引越界。

    wrong:
    ##for j in range(n):
    ##    for i in range(t):
    ##        if c[j]>i+1:#! 
    ###！            dp[i][j]=dp[i-1][j]
    ##            dp[i][j]=dp[i][j-1]
    ##        else:#! 
    ###！            dp[i][j]=max(dp[i-1][j],dp[i-c[j]][j-1]+w[j])
    ##            dp[i][j]=max(dp[i][j-1],dp[i-c[j]][j-1]+w[j]) #！
    ##        ans=max(ans,dp[i][j])
    ##
2. 状态转移方程错误
    当 c[j] > i 时，应该使用 dp[i][j-1]，而不是 dp[i-1][j]。
    因为当 c[j] > i 时，第 j 个物品无法放入背包，所以只能在前 j-1 个物品中选择。
"""

for j in range(1,n+1):
    for i in range(1,t+1):
        if c[j]>i:#! 
#！            dp[i][j]=dp[i-1][j]
            dp[i][j]=dp[i][j-1]
        else:#! 
#！            dp[i][j]=max(dp[i-1][j],dp[i-c[j]][j-1]+w[j])
            dp[i][j]=max(dp[i][j-1],dp[i-c[j]][j-1]+w[j]) #！
        ans=max(ans,dp[i][j])
# answer 2:
##for i in range(1,t+1):
##    for j in range(1,n+1):
##        if c[j]>i:
##            dp[i][j]=dp[i][j-1]
##        else:
##            dp[i][j]=max(dp[i][j-1],dp[i-c[j]][j-1]+w[j])
##        ans=max(ans,dp[i][j])
print(dp)
print(dp[t][n])
##print(ans)
