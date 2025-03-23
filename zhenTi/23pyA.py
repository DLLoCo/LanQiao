import sys
input = sys.stdin.readline
n=int(input())
s=[[]for i in range(10)]
cnt=[0]*10
ans=0
for i in range(n):
    a,w=map(int,input().split())
    s[a].append(w)
    cnt[a]+=1
for i in range(10):
    s[i].sort()
##print(s,cnt)
 
key=int(n/10)
for i in range(10):
    if cnt[i]>key:
        res=cnt[i]-key
        ans+=sum(s[i][0:res])
 
print(ans)
