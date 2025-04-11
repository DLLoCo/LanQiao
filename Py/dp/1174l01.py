import os
import sys

# 请在此输入您的代码
N,C=map(int,input().split())
c=[0]*(N+1)
w=[0]*(N+1)
for i in range(1,N+1):
  c[i],w[i]=map(int,input().split())
"""
状态转移方程理解：
1.因为状态转移方程分为两种情况，第i个物品装的进去，装不进去
2.如果装不进去，等于同等空间下装前i-1个物品的值，因为你没装，
不是等于dp[i][j]=dp[i][j-1]，否则一直装不进去不是那一行都是0，但是等于同等空间下装前i-1个物品的值

"""

'''
法二：
“选择”；外循环：容量变化（根据状态转移方程）；内循环：物品个数
import os
import sys

# 请在此输入您的代码
N,C=map(int,input().split())
c=[0]*(N+1)
w=[0]*(N+1)
for i in range(1,N+1):
  c[i],w[i]=map(int,input().split())

def DP(N,C):
  dp=[[0]*(N+1) for i in range(C+1)]
  for j in range(1,C+1):
    for i in range(1,N+1):
      if c[i]>j:
        dp[j][i]=dp[j][i-1]
      else:
        dp[j][i]=max(dp[j][i-1],dp[j-c[i]][i-1]+w[i])
  return dp[C][N]

print(DP(N,C))
'''

"""
法一：
“选择”；外循环：物品个数；内循环：容量变化（根据状态转移方程）
"""
def DP(N,C):                        
  dp=[[0]*(C+1)for i in range(N+1)]
  for i in range(1,N+1):
    for j in range(1,C+1):
      if c[i]>j: #! 不是c[i]>j-sum(c[1,i-1]),即第i个物品体积不是要装进背包剩余空间。 因为状态转移方程分为两种情况，第i个物品装的进去，装不进去
        dp[i][j]=dp[i-1][j] #! dp[i][j]=dp[i][j-1]
      else:
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-c[i]]+w[i])
  return dp[N][C]

print(DP(N,C))