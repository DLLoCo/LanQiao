import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import heapq
n,m=map(int,input().split())
q=[]
for i in range(m):
    x,y,w=map(int,input().split())
    heapq.heappush(q,(w,x,y))

s=[i for i in range(n+1)]
ans=0
cnt=0
"""
wrong:
##def find(x):
##    if x==s[x]:
##        return s[x]
##    s[x]=find(x)
"""
def find(x):
    global s
    if x!=s[x]:
        s[x]=find(s[x])#?
    return s[x]

def merge(x,y):
    global s
    rtx=find(x)
    rty=find(y)
    if rtx!=rty:
        s[rtx]=rty

def connect(x,y):
    rtx=find(x)
    rty=find(y)
    if rtx==rty:
        return 1
    else:
        return 0

while q:
    w,x,y=heapq.heappop(q)
    rtx=find(x)
    rty=find(y)
    if rtx==rty:
        continue
    s[rtx]=rty
    ans+=w
    cnt+=1

if cnt==n-1:
    print(ans)
else:
    print("orz")
