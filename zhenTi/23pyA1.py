import sys
input=sys.stdin.readline

n=int(input())
x=[int(i) for i in input().split()]
y=[int(i) for i in input().split()]
z=[int(i) for i in input().split()]
##print(x,y,z)
a=[]
b=[]
c=[]
ans=0
res=0
sum1=0

for i in range(n):
    a.append(x[i]-y[i]-z[i])
    b.append(y[i]-z[i]-x[i])
    c.append(z[i]-x[i]-y[i])

a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
##print(a,b,c)
for i in range(n):
    sum1+=a[i]
    if sum1>0:
        res+=1
ans=max(ans,res)
res=0
sum1=0
for i in range(n):
    sum1+=b[i]
    if sum1>0:
        res+=1
ans=max(ans,res)
res=0
sum1=0
for i in range(n):
    sum1+=c[i]
    if sum1>0:
        res+=1
ans=max(ans,res)
if ans==0:
    ans=-1
    
print(ans)
