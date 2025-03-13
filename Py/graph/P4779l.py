import array,heapq
def dijkstra(start):
    vis=[0]*(n+1)
    s=[]
    dis[start]=0
    heapq.heappush(s,(0,start))
    while s:
        d,u=heapq.heappop(s)
        if vis[u]:continue
        vis[u]=1
        print(g[u])
        for v,w in g[u]:
            # if vis[v]:
            #     continue
            #or dis[v]=min(dis[v],d+w)
            if d+w<dis[v]:
                dis[v]=d+w
                heapq.heappush(s,(dis[v],v))


n,m,start=map(int,input().split())
g=[[] for _ in range(n+1)]
for i in range(m):
    u,v,w=map(int,input().split())
    g[u].append((v,w))

INF=1<<64
dis=[INF]*(n+1)
dijkstra(start)

for i in range(1,n+1):
    print(dis[i],end=' ')