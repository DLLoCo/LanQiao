n,t=map(int,input().split())
s=[]
for i in range(n):
    m,v=map(int,input().split())
    s.append([m,v])

t2=0
ans=0

s.sort(key=lambda x:x[1]/x[0],reverse=True)

for i in range(n):
    t2+=s[i][0]
    if t2>t:
        t3=t-(t2-s[i][0])
        ans+=s[i][1]*(t3/s[i][0])
        break
    ans+=s[i][1]

print(f"{ans:0.2f}")
