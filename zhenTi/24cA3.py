import sys
input=sys.stdin.readline
n,s=map(int,input().split())
p=[]
c=[]
pc=[]
ans=0
for i in range(n):
    pi,ci=map(int,input().split())
    p.append(pi)
    c.append(ci)
    pc.append([pi,ci])
#- 思路：每一次都取花费最小值，迭代
#+ 优解：本质就是找到刻意组队的最大次数，之后只能逐个训练
##"""#-
##while sum(c)>0:
##    s2=sum(p)
##    if s<s2:
##        times=min(c)
##        ans+=s*times
##        for i in range(len(c)):
##            if c[i]>0:
##                c[i]-=times
##            if c[i]==0:
##                p[i]=0
##        while 0 in c:
##            c.remove(0)
##            p.remove(0)
##    else:
##        for i in range(len(c)):
##            if c[i]>0:
##                ans+=c[i]*p[i]
##                c[i]=0
##                #! c[i]-=p[i] 混淆c,p
##print(ans)
##"""

#+
s2=0
pc.sort(key=lambda x:x[1])
for i in range(n):
    s2+=pc[i][0]
# 找到组团最大次数
while s<s2:
    times=pc[0][1]
    ans=s*times
#!    pc.pop(0)
    s2-=pc[0][0]
    pc.pop(0)
#计算剩余单个士兵
for i in pc:
    ans+=i[0]*(i[1]-times)
print(ans)

#++ 最优解：
##n,s=map(int,input().split())
##bi=0
##cns=0
##li=[]
##for _ in range(n):
##    li.append(list(map(int,input().split())))
##li=sorted(li,key=lambda x:x[1])
##for i in range(n):
##    bi+=li[i][0]
##ci=0
##i=0
##while i!=n:
##    if li[i][1]==ci:
##        bi-=li[i][0]
##        i+=1
##        continue
##    if bi>=s:
##        cns+=s
##        ci+=1
##    else:
##        cns=cns+(li[i][1]-ci)*li[i][0]
##        i+=1
##print(cns)
##

###--:
##pc.pop(0)，每次循环都将m的第一个元素弹出。如果m是用列表实现的，那么每次pop(0)的时间复杂度是O(n)，因为列表需要移动所有后续元素。而如果n是1e5的话，这样的操作会导致总的时间复杂度是O(n^2)，这会超时。
##
##而正确的代码并没有使用pop操作，而是通过一个指针i来遍历排序后的列表。这样，整个处理过程是线性的，时间复杂度为O(n log n)（排序的时间复杂度）加上O(n)的处理时间，这在n=1e5时是可以接受的。
