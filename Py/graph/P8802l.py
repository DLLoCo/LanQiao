n,m=map(int,input().split())
c=[int(i) for i in input().split()]
c[0]=0#city 1 #! 不要忘了c[0],以及不要写成c[1]
c[n-1]=0#city N
INF=1e9
dis=[INF]*(n+1)
dis[1]=0
#？ 存储图
# g=[[] for _ in range(n+1)]
g=[]
for i in range(m):
    u,v,w=map(int,input().split())
    g.append((u,v,w))
    g.append((v,u,w))
    # g[u].append((v,w))
    # g[v].append((u,w))
    
# 法二：
# for _ in range(n-1):
#     for i in range(1,n+1):
#         for v,w in g[i]:#！ 写成g(i)/g(u)
#             dis[v]=min(dis[v],dis[i]+w+c[v-1])#! 不要忘了c[v-1]

for i in range(n):
    for u,v,w in g:#！ 写成g[i]
        dis[v]=min(dis[v],dis[u]+w+c[v-1])#! 不要忘了c[v-1]

print(dis[n])
