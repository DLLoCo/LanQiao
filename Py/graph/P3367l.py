import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)  # 增加递归深度限制
n,m=map(int,input().split())
s=[i for i in range(n+1)]

def find(x):
    global s
    #标准的递归写法
    if x!=s[x]:
        s[x]=find(s[x])
    return s[x]#?or x
    
"""
1.find：
2.merge：
s[x]=y-->s[x]=find(y)
输入
6 5 3
1 2
1 5
3 4
5 2
1 3
1 4
2 3
5 6
返回
yes
no（应该是yes）
no
- 初始状态：s = [0, 1, 2, 3, 4, 5, 6]
- merge(1, 2)：s = [0, 2, 2, 3, 4, 5, 6]
- merge(1, 5)：s = [0, 5, 2, 3, 4, 5, 6]（注意这里1已经指向了5，但2仍然是独立的）
"""
def merge(x,y):
    global s
    rootx=find(x)
    rooty=find(y)
    if rootx!=rooty:
        s[rootx]=rooty#! s[x]=y 
    return

def connect(x,y):
    global s
    if find(x)==find(y):
        print("Y")
    else:
        print("N")

for i in range(m):
    z,x,y=map(int,input().split())
    if z==1:
        merge(x,y)
    else:
        connect(x,y)
"""
1.input = sys.stdin.readline ：这是一个输入优化技巧。默认的 input() 函数在处理大量输入时效率较低，
而 sys.stdin.readline() 速度更快。这行代码将 input 重新定义为 sys.stdin.readline ，
使得每次调用 input() 时实际上调用的是更高效的 sys.stdin.readline() 。
这在处理大规模输入数据时能显著提高性能。
2.# sys.setrecursionlimit(10**6) ：这行代码设置了 Python 的递归深度限制。
3.def merge(x,y):
    global s
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        s[root_x] = root_y
    return
"""