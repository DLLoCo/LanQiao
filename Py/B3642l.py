class node:
    def __init__(self, val=None):
        self.val = val
        self.l = None
        self.r = None
n=int(input())
root=node(1)
nodes=[None]*(n+1)
for i in range(1, n+1):
        nodes[i] = node(i)

  
for i in range(1,n+1):
    l,r=map(int,input().split())
    nodes[i].l = nodes[l] if l != 0 else None
    nodes[i].r = nodes[r] if r != 0 else None

"""
1.如何写入一颗二叉树
2.节点 python的类怎么写
3.pretraverse(nodes[1],1)
4.#!     if step == n 要加，or node==None

"""

def pretraverse(node,step): #!     if step == n 要加，or node==None
    if step == n or node==None: #! node.val,如果点是None，没有node.val
        return
    print(node.val,end=" ")
    pretraverse(node.l,step+1)
    pretraverse(node.r,step+1)

def traverse(node,step):
    if step == n or node==None:
        return
    traverse(node.l,step+1)
    print(node.val,end=" ")
    traverse(node.r,step+1)

def backtraverse(node,step):
    if step == n or node==None:
        return
    backtraverse(node.l,step+1)
    backtraverse(node.r,step+1)
    print(node.val,end=" ")

pretraverse(nodes[1],1) #! pretraverse(root,1)
print()
traverse(nodes[1],1)
print()
backtraverse(nodes[1],1)
print()
