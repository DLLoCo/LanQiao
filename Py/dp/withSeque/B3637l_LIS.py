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
"""
import bisect

n = int(input())
s = list(map(int, input().split()))

tail = []
for num in s:
    idx = bisect.bisect_left(tail, num)
    if idx == len(tail):
        tail.append(num)
    else:
        tail[idx] = num

print(len(tail))
"""