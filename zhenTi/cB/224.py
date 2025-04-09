# <滑动窗口 + 二维前缀和>
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
a=[[0]*(m+1)for i in range(n+1)]
ans=0
for i in range(1,n+1):
    row=[0]
    row+=[int(i) for i in input().split()]
    for j in range(1,m+1):
        a[i][j]=row[j]
        a[i][j]=a[i][j]+a[i-1][j]+a[i][j-1]-a[i-1][j-1]
for i in range(1,n+1):
    #! for j in range(i+1,n+1):只有一行考虑错误,i==j才是只有一行
    for j in range(i,n+1):
        l,r,sm=1,1,0
        while r<m+1:
            while a[j][r]-a[j][l-1]-a[i-1][r]+a[i-1][l-1]>k:
                l+=1
#+ 这一步是关键,
            ans+=r-l+1
            r+=1
#- 循环 时间复杂度O(n^4)
##        for l in range(1,m+1):
##            r=l
            #!不要越界,判断先后:while a[j][r]-a[j][l-1]-a[i-1][r]+a[i-1][l-1]<=k and r<m+1:
##            while r<m+1 and a[j][r]-a[j][l-1]-a[i-1][r]+a[i-1][l-1]<=k:
####                print(j,r,i,l)
####                print(a[j][r],a[j][l-1],a[i-1][r],a[i-1][l-1])
####                print(a[j][r]-a[j][l-1]-a[i-1][r]+a[i-1][l-1])
##                r+=1
##                ans+=1
print(ans)
        