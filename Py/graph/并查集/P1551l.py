n,m,p=map(int,input().split())
s=[i for i in range(n+1)]

def find(x):
    global s
    if x!=s[x]:
        s[x]=find(s[x])#?
    return s[x]#?or x

# 法二:一般递归写法
# def find(u):
#     global s
#     # 寻找根节点,and压缩路径
#     if s[u]==u:
#         return u
#     s[u]=find(s[u])
#     # 递归返回根节点
#     return s[u]
#!!!!     return s[u]必须写上,否则其他非root节点没有返回值,mergy报错
#!! mergy:u v (1 2) 再mergy 1 3 find(1)没有返回值,mergy报错 
#!![0, 2, 2, 3, 4, 5, 6]
def merge(x,y):
    global s
    if find(x)!=find(y):
##          s[x]=y
        s[find(x)]=find(y)
    return

def connect(x,y):
    global s
    if find(x)==find(y):
        print("Yes")
    else:
        print("No")

for i in range(m):
    x,y=map(int,input().split())
    merge(x,y)


for i in range(p):
    x,y=map(int,input().split())
    connect(x,y)
