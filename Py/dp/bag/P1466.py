#dp[n]=dp[n-i] for i in range()
n=int(input())
s=[i for i in range(1,n+1)]
def sum2(n):
    ans=0
    for i in range(1,n+1):
        ans+=i
    return ans
##print(sum2(n))
target=int(sum2(n)/2)
##print(target)

if sum2(n)%2==1:
    print(0)
else:
    dp=[0]*target

    dp[1]=0
    dp[2]=0

    for i in range(3,target+1):
        for j in range(1,n+1):
            dp[i]+=dp[i-j]
            
    print(dp[target])
