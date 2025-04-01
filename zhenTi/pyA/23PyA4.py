import os
import sys
n,m,a,b=map(int,input().split())
s=[[]for i in range(n)]
ans=0
for i in range(n):
    s[i]=[int(i) for i in input().split()]

for i in range(n-a+1):
    for j in range(m-b+1):
        ma=0
        mi=10**9
        for k in range(a):
            ma=max(ma,max(s[i+k][j:j+b]))
            mi=min(mi,min(s[i+k][j:j+b]))
        ans+=ma*mi
print(ans)