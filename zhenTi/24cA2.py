def check(a):
    b=[[0]*6 for i in range(6)]
    pos=1
    for i in range(1,6):
        for j in range(1,6):
            b[i][j]=a[pos]
            pos+=1
#!不能在这里更新 l1=0   
    x1,x2=0,0
    for i in range(1,6):
        r1=0
##        r1=sum(b[i])
        l1=0
        for j in range(1,6):
            r1+=b[i][j]
            l1+=b[j][i]
            if i==j:
                x1+=b[i][j]
            if i+j==6:
                x2+=b[i][j]
        if r1==5 or r1==0 or l1==5 or l1==0:
            return 0
    if x1==0 or x1==5 or x2==0 or x2==5:
        return 0
    return 1

ans=0
#! (1<<25)-1 33554431 \\  1<<25-1 16777216
for i in range(((1<<25)-1)):
    cnt=0
    a=[0]*26
#! 如果这么写错误：因为判断i的第j位是否为0，j从0开始
# """
# for j in range(1,26):
#     a[j] = (i >> j) & 1
# """
##    for j in range(25):
##        a[j+1] = (i >> j) & 1
##        if((i>>j)&1):
##            cnt+=1
    for j in range(1,26):
        a[j]=i&1
        if i&1:
            cnt+=1
        #! i>>1 i的值没有改变
        i=(i>>1)
    if cnt==13 and check(a):
        ans+=1
        
print(ans)          
