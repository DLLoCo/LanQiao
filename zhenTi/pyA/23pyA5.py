# <思维+数学>
import sys
input=sys.stdin.readline
n=int(input())
l=[int(i) for i in input().split()]
cnt={}
l.sort()
for i in range(n):
    a=cnt.get(l[i],0)
    cnt[l[i]]=a+1
res=l[0]
m=len(cnt)
mx=l[-1]
while res<100001:
    key=res+1
    if cnt[res]%key==0:
        a=cnt.get(key,0)
        cnt[key]=a+int(cnt[res]/key)
        res+=1
    else:
        break
print(res)