import sys
input = sys.stdin.readline## 防止超时

MOD=80112002
n,m=map(int,input().split())
g=[[]for i in range(n+1)]
s=[0]*(n+1)
ans=0

ind=[0]*(n+1)
outd=[0]*(n+1)

q=[]

for i in range(m):
    x,y=map(int,input().split())
    ind[y]+=1
    outd[x]+=1
    g[x].append(y)

for i in range(1,n+1):
    if ind[i]==0:
        s[i]=1
        q.append(i)

while q:
    now=q.pop()
    for i in range(len(g[now])):
        y=g[now][i]
        s[y]=(s[y]+s[now])%MOD
        ind[y]-=1
        if ind[y]==0:
            q.append(y)

for i in range(1,n+1):
    if outd[i]==0:
        ans=(ans+s[i])%MOD
print(ans)
