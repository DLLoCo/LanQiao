import sys

N=101
#!? M=1001
M=sys.maxsize
ans=[[M for _ in range(N)] for _ in range(N) ]
n,m=map(int,input().split())

for i in range(m):
    u,v,w=map(int,input().split())
    ans[u][v]=min(ans[u][v],w)
    ans[v][u]=ans[u][v]

for i in range(1,n+1):
    ans[i][i]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            ans[i][j]=min(ans[i][j],ans[i][k]+ans[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        print(ans[i][j],end=" ")
    print()
