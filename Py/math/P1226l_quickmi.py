a,b,q=map(int,input().split())
# a^b b=sum 2^k
a0,b0=a,b
ans=1

while b:
    if b & 1:
        ans*=a
    a=(a*a)%q
    b >>=1

ans=ans%q
print(f"{a0}^{b0} mod {q}={ans}")  
