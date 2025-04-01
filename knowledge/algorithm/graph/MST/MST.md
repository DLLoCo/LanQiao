# 定义：
最小生成树：
- 包含图中所有节点的子图
- 是一棵树
  - 是无环的
  - 是连通的
- 总长度最小

# Prim
1. 思路(**本质贪心**)：
    - 从任意一个节点开始，每次选择与当前节点相连的最短边，将该边加入最小生成树，并将该边的另一端节点加入当前节点集合。
    - 重复上述步骤，直到所有节点都被加入最小生成树。
    - 时间复杂度：
    - 空间复杂度：$O(n+m)logn$
2. 代码：
    - 用邻接矩阵表示图
    - 用数组表示当前节点集合
    - 用数组表示当前节点到其他节点的最短距离
   ~~~py
   # Dijstra 类似,优先队列
   def prim(graph):
       n = len(graph)
       visited = [False] * n
       dist = [float('inf')] * n
       dist[0] = 0
       for _ in range(n):
           u = min(range(n), key=lambda x: dist[x] if not visited[x] else float('inf'))
           visited[u] = True
           for v in range(n):

   ~~~
# Kruskal
1. 思路(**本质贪心**)：
    - 将所有边按权值从小到大排序
    - 依次考虑每条边，如果该边的两个端点不在同一个连通分量中，则将该边加入最小生成树
    - 重复上述步骤，直到所有节点都被加入最小生成树
    - 时间复杂度：$O(mlogm+m)$
    - 空间复杂度：$O(m)$
  
2. 代码：
    - 用并查集表示连通分量
    - 用数组表示所有边
    - 用数组表示当前节点到其他节点的最短距离
~~~py
def kruskal(graph):
    n = len(graph)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((i, j, graph[i][j]))
    edges.sort(key=lambda x: x[2])
    parent = list(range(n))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        parent[find(x)] = find(y)
    ans = 0
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            ans += w
    return ans
~~~