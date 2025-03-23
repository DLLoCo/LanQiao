import heapq
n,m,k=map(int,input().split())
s,e=map(int,input().split())
MAX=5*1e7
MAX2=1e4
g=[[]for i in range(n*(k+1))]

for i in range(m):
    a,b,w=map(int,input().split())
    g[a].append((w,b))
    g[b].append((w,a))
    for i in range(1,k+1):#! 建图逻辑
        g[a+(i-1)*n].append((0,b+i*n))#! i写成k了
        g[b+(i-1)*n].append((0,a+i*n))
        g[a+i*n].append((w,b+i*n))
        g[b+i*n].append((w,a+i*n))

##print(g,len(g))
q=[]
dp=[MAX]*((k+1)*n)
vis=[0]*((k+1)*n)
dp[s]=0
heapq.heappush(q,(0,s))
##ans=MAX
while q:
    d,now=heapq.heappop(q)
    if vis[now]==1:
        continue
    vis[now]=1
    for i in range(len(g[now])):
        w,b=g[now][i]
        if vis[b]==1:
            continue
        if dp[b]>w+dp[now]:
            dp[b]=w+dp[now]
            heapq.heappush(q,(dp[b],b))
##            print(q)

ans=dp[e]
for i in range(1,k+1):#!ans=min(ans,dp[e+k*n])
    ans=min(ans,dp[e+i*n])
##print(ans,dp)
print(ans)
