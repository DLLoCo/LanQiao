n1,n2,n3,n4=map(int,input().split())
s1=[0]
s2=[0]
s3=[0]
s4=[0]
vis=[[0],[0]*(n1+1),[0]*(n2+1),[0]*(n3+1),[0]*(n4+1)]
ans=0
##res=0
##print(id(res))
"""
怎么存储答案，在递归当中
"""

tmp=[[0]*(max(n1,n2,n3,n4)+1) for i in range(5)]
for i in input().split():
    s1.append(int(i))
for i in input().split():
    s2.append(int(i))
for i in input().split():
    s3.append(int(i))
for i in input().split():
    s4.append(int(i))

def dfs(step,n,s,res,index):
##    print(res)
    if step==n+1 or sum(tmp[index])>sum(s)/2:#! 
        res=min(res,sum(tmp[index]))
        print(id(res))
        print(res)
        return res

    for i in range(1,n+1):
##        print(134)
        if vis[index][i]==1:#!
            continue
        tmp[index][step]=s[i] #! 
##        print(tmp)
        vis[index][i]=1
        dfs(step+1,n,s,res,index)
        vis[index][i]=0

##ans1=dfs(1,n1,s1,0,1)
####print(ans1)
##ans2=dfs(1,n2,s2,0,2)
####print(res)
ans3=dfs(1,n3,s3,sum(s3),3)
ans4=dfs(1,n4,s4,sum(s4),4)
##ans=ans1+ans2+ans3+ans4
##print(ans)
