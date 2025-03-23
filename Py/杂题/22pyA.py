##def fra(n):
##    res=1
##    if n==1:
##        return 1
##    else:
##        for i in range(2,n+1):
##            res*=i
##        return res
##    
##def sum2(n):
##    res=0
##    if n==1:
##        return 1
##    else:
##        for i in range(1,n+1):
##            res+=i
##        return res
##sans=[None]*(100001)
##sans[1]=0
##MOD=998244353
##def ans(n,s=sans):
##    if sans[n] != None:
##        return sans[n]
##    res=(fra(n-1)*sum2(n-1)+n*ans(n-1))%MOD
##    sans[n]=res
##    return sans[n]
import sys
input=sys.stdin.readline
n=int(input())
fra=1
sum2=1
ans=0
MOD=998244353
if n==0:
    ans=0
if n==1:
    ans=0
else:
    for i in range(2,n+1):
        ans=(fra*sum2+i*ans)%MOD
        fra=(fra*i)%MOD
        sum2=(sum2+i)%MOD
print(ans)
