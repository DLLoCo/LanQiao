import sys
input = sys.stdin.readline
t,n=map(int,input().split())
c=[0]
w=[0]
for i in range(n):
    ci,wi=map(int,input().split())
    c.append(ci)
    w.append(wi)
dp=[0]*(t+1)

for i in range(1,n+1):
    for j in range(1,t+1):
        if c[i]>j:#!c[i]>i
            dp[j]=dp[j]#!dp[j]=dp[j-1]
        else:
            dp[j]=max(dp[j],dp[j-c[i]]+w[i])
print(dp[t])
    
"""
优化：
if n==1:
    print(t//c[1]*w[1])
else:
    for i in range(1,n+1):
        for j in range(c[i],t+1):
                dp[j]=max(dp[j],dp[j-c[i]]+w[i])
    print(dp[t])
"""
