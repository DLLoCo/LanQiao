##n=int(input())
####sa=[0]*(2*10**5+1)
##sa2=[]
##T=10**5
##s=[]
##x=[]
##ans=0
##cnt=0
##for i in range(n):
##    a,b=map(int,input().split())
##    if i==0:
##        ans=2
##        s.append((a,b))
####        sa[a+T]=1
##        sa2.append(a+T)
##        cnt+=1
##    else:
##        if (a,b) not in s:# bu =
##            if a+T not in sa2:
##                res=0
##                sa2.append(a+T)
####            if sa[a+T] != 0 or (a+T not in sa2):#! bu //
##                for j in range(len(s)):
##                    a1,b1=s[j]
##                    x1=(b1-b)/(a-a1)
##                    y1=a*x1+b
####                sa[a+T]=1
##                    if (x1,y1) not in x:
##                        x.append((x1,y1))
##                        ans+=(cnt+1)
##                        cnt+=1
##                        s.append((a,b))
##                    else:
##                        ans+=2
##                        cnt+=1
##                        s.append((a,b))
##                    ans+=
##            else:
##                ans+=1
##                cnt+=1
##                s.append((a,b))
##
##print(ans)
####print(sa2)
####print(s)
####print(x)
n=int(input())
s=[]
ans=0
for _ in range(n):
    a,b=map(int,input().split())
    if (a,b) not in s:# 去重
        x=set()
##        print(x)
        for j in range(len(s)):
            a1,b1=s[j]
            if a1 != a:
                x1=(b1-b)/(a-a1)
                y1=a*x1+b
                x.add((x1,y1))
##        print(x)
        ans+=(len(x)+1)
        s.append((a,b))
print(ans+1)
