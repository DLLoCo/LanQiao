import sys
# 思路：
# 1. 回文串，从两端开始处理
# 2. 贪心：每次修改每个值都看看能不能带着相邻的值一起修改，每次取最值
input=sys.stdin.readline
n=int(input())
ll=[int(i) for i in input().split()]
ans=0
l=0
r=n-1
while l<=r:
  if ll[l]==ll[r]:
    l+=1
    r-=1
  else:
    key=ll[r]-ll[l]
    ans+=abs(key)
    if (ll[l+1]<ll[r-1] and ll[l]<ll[r]) or (ll[l+1]>ll[r-1] and ll[l]>ll[r]):
    #! if (ll[l+1]<ll[r-1] and ll[l]<ll[r]) or (ll[l+1]<ll[r-1] and ll[l]<ll[r]):
      if ll[l]<ll[r]:
        ll[l+1]=min(ll[l+1]+key,ll[r-1])
      else:
        ll[r-1]=min(ll[r-1]-key,ll[l+1])
        #! ll[r-1]=min(ll[r-1]-key,ll[l-1])
    r-=1
    l+=1
print(ans)