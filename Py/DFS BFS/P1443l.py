from collections import deque
dx=[2,2,-2,-2,1,-1,1,-1]
dy=[1,-1,1,-1,2,2,-2,-2]

class node:
    def  __init__(self,x,y):
        self.x=x
        self.y=y
"""
1.n，m从1开始，在棋盘中，所以n,m!=0
2.矩阵n*m：n行，m列
"""
n,m,x,y=map(int,input().split())
ans=[[-1 for _ in range(m+1)] for _ in range(n+1)]#! n+1/n ans=[[-1 for _ in range(n)] for _i in range(m)]，ans=[[-1 for _ in range(n+1)] for _i in range(m+1)]
status=[[0 for _ in range(m+1)] for _ in range(n+1)]

now=node(x,y)
ans[x][y]=0
status[x][y]=1
##print(ans)
q=deque()
q.append(now)
while q:
    now=q.popleft()
    for i in range(8):
        nx,ny=now.x+dx[i],now.y+dy[i]
        if nx<1  or nx>n or ny<1 or ny>m or status[nx][ny]==1:
            continue
        status[nx][ny]=1
        ans[nx][ny]=ans[now.x][now.y]+1
        q.append(node(nx,ny))

for i in range(1,n+1):
    for j in range(1,m+1):
        print(f"{ans[i][j]:<5d}",end="")
    print()
    

