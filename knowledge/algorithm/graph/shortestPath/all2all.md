# Floyd
1. 原理
	- 本质**dp**

2. 实现：
```py
def floyd_warshall(graph):
    # 初始化距离矩阵
    distance = {node: {n: float('inf') for n in graph} for node in graph}
    for node in graph:
        distance[node][node] = 0
        for neighbor, weight in graph[node].items():
            distance[node][neighbor] = weight

    # 遍历所有节点作为中间节点
    for k in graph:
        # 遍历所有节点对
        for i in graph:
            for j in graph:
                # 如果通过节点k使得i到j的距离更短，则更新距离
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance
```