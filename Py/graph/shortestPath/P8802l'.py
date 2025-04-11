import array,heapq
"""
1.题目条件：不要忘了c[v-1]
2.添加双向边
3.易错：n与n+1不要忘了c[0],以及不要写成c[1]
"""

def dijkstra(start):
    vis=[0]*(n+1)
    s=[]
    dis[start]=0
    heapq.heappush(s,(0,start))
    while s:
        d,u=heapq.heappop(s)
        if vis[u]:continue
        vis[u]=1
        for v,w in g[u]:
            # if vis[v]:
            #     continue
            #or dis[v]=min(dis[v],d+w)
            if d+w+c[v-1]<dis[v]:#！ 不要忘了c[v-1]
                dis[v]=d+w+c[v-1] #！ 不要忘了c[v-1]
                heapq.heappush(s,(dis[v],v))


n,m=map(int,input().split())
start=1
c=[int(i) for i in input().split()]
c[0]=0#city 1 #! 不要忘了c[0],以及不要写成c[1]
c[n-1]=0#city N
g=[[] for _ in range(n+1)]
for i in range(m):
    u,v,w=map(int,input().split())
    g[u].append((v,w))
    g[v].append((u,w))  #！ 添加双向边
    
INF=1<<64
dis=[INF]*(n+1)
dijkstra(start)

print(dis[n])