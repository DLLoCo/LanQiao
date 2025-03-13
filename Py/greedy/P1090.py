n=int(input())
s=list(int(i)for i in input().split())
ans=0

#sort append pop
while len(s)>1:
    s.sort(reverse=True)
    n1=s.pop()
    n2=s.pop()
    ans+=n1+n2
    s.append(n1+n2)
##    print(s)
if n==1:
    ans=sum(s)
print(ans)
