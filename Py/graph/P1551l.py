n,m,p=map(int,input().split())
s=[i for i in range(n+1)]

def find(x):
    global s
    if x!=s[x]:
        s[x]=find(s[x])#?
    return s[x]#?or x

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
