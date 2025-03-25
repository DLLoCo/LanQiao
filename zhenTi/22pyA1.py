from math import *
n=int(input())
ans=0

for i in range(2,floor(n**0.5)):
    if n%i==0:
        ans+=1
        while  n%i==0:
            n=int(n/i)

if n>1:
    ans+=1

print(ans)
