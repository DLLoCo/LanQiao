import sys
input = sys.stdin.readline
n=int(input())
for i in range(n):
    t=[i for i in input()]
    s=[i for i in input()]
    ti=0
    si=0
    ans=0
    for i in range(len(s)):
        if t[i]==s[i]:
            continue
        else:
            if i==0 or i==len(s):
                ans=-1
                break
            if (i!=len(s) or i!=0) and s[i-1]!=s[i] and s[i]!=s[i+1]:
                s[i]=t[i]
                ans+=1
            else:
                ans=-1
                break
    print(ans)