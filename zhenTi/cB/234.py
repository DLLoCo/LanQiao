# <DFS+graph>
## 过了百分之35,还有一些bug不知道在哪
import sys
#! 与dfs不同
# import heapq
from collections import deque
input=sys.stdin.readline
# 请在此输入您的代码           
t=int(input())

#zuo you shang xia
dxx=[0,0,-1,1]
dyy=[-1,1,0,0]
# zuoshang 顺时针
dx=[-1,0,1,1,1,0,-1,-1]
dy=[1,1,1,0,-1,-1,-1,0]
# x行 y列
#! 最外围没有判断,可能被阻挡
def check(m,n,vis):
    for i in range(1,m+1):
        if i==1 or i==m:
            for j in range(1,n+1):
                if vis[i][j]!=1:
##                    print(i,j)
                    return 0,(i,j)
        else:
            if vis[i][1]!=1:
##                print(i,1)
                return 0,(i,1)
            if vis[i][-1]!=1:
##                print(i,-1)
                return 0,(i,-1)
    return 1,(None,None)

def bbfs(root):
    global cnt
    global vis
    cnt+=1
    q=deque()
    q.append(root)
    while q:
        tmp=q.popleft()
        x,y=tmp[0],tmp[1]
        vis[x][y]=1
        for i in range(4):
            nx=x+dxx[i]
            ny=y+dyy[i]
            if nx<1 or nx>m or ny<1 or ny>n or vis[nx][ny]==1:
                continue
            if a[nx][ny]==1:
                vis[nx][ny]=1
                q.append((nx,ny))

def bfs(root):
    global vis
    q1=deque()
    q1.append(root)
    while q1:
        tmp=q1.popleft()
        x,y=tmp[0],tmp[1]
        vis[x][y]=1
#!!!! 如果第一个root(1,1),就是岛屿,不能直接走了,样例见官网题给第二个
        if a[x][y]==1:
            bbfs((x,y))
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<1 or nx>m or ny<1 or ny>n or vis[nx][ny]==1:
                continue
            if a[nx][ny]==1:
                bbfs((nx,ny))
##                print("bbfs")
##                for i in range(6):
##                    print(vis[i])
##                print("cnt",cnt)
            else:
                vis[nx][ny]=1
                q1.append((nx,ny))
##                print("bfs")
##                for i in range(6):
##                    print(vis[i])
for _ in range(t):
##    cnt=0
    cnt=0
    key=0
    m,n=map(int,input().split())
    a=[[0]*(n+1) for i in range(m+1)]
    vis=[[0]*(n+1) for i in range(m+1)]
    for i in range(1,m+1):
        row=input()
        for j in range(1,n+1):
            a[i][j]=int(row[j-1])
##    for i in range(6):
##        print("a")
##        print(a[i])
    bfs((1,1))
    res=check(m,n,vis)
##    print(res)
    while res[0]!=1:
        bfs(res[1])
        res=check(m,n,vis)
##        print(res)
    print(cnt)

##6 10
##1001100101
##0111111011
##1100111001
##1001000010
##1101110100
##1101111101

##8 5
##01001
##11110
##01110
##11110
##01101
##11111
##11000
##10100

##2 9
##011110110
##000100010
##def a():
##    return 1,(2,3)
##a=a()
##print(a[0],a[1])
