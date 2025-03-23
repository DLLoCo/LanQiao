import heapq
n=int(input())
ind=[0]*(n+1)
vis=[0]*(n+1)
g=[[]for i in range(n+1)]
ans=[]
q=[]
for i in range(1,n+1):
    g[i]=[int(j) for j in input().split()]
    g[i].remove(0)
    for j in g[i]:
        ind[j]+=1

for i in range(1,n+1):
    if ind[i]==0:
        heapq.heappush(q,i)

while q:
    now=heapq.heappop(q)
    if vis[now]==1:
        continue
    vis[now]=1
    ans.append(now)
    for j in g[now]:
        ind[j]-=1
        if ind[j]==0:
            heapq.heappush(q,j)
##            print(q)

##print(g)
##print(ind)
##print(ans)
for i in range(len(ans)):
    print(ans[i],end=" ")
