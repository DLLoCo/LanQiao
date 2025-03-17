n=int(input())
s=[int(i) for i in input().split()]
dp=[1]*n

#dp[i]=
for i in range(n):
    for j in range(i):
        if s[j]<s[i]:
            dp[i]=max(dp[i],dp[j]+1)

dp.sort()
print(dp[n-1])
