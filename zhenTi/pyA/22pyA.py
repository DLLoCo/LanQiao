import sys
input=sys.stdin.readline
n=int(input())
ll=[0]+[int(i) for i in input().split()]
m=int(input())
d=[0]*(n+2)
cnt=[0]*(n+2)
ans1=0
ans=0
for i in range(m):
  l,r=map(int,input().split())
  d[l]+=1
  d[r+1]-=1

for i in range(1,n+1):
  cnt[i]=cnt[i-1]+d[i]

for i in range(1,n+1):
  ans1+=cnt[i]*ll[i]

cnt.sort(reverse=True)
ll.sort(reverse=True)
for i in range(n):
  ans+=cnt[i]*ll[i]
  
print(ans-ans1)