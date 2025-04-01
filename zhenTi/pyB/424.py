#这题一看数据范围 n≤10^18就知道暴力会超时，所以这题一定有规律可循。
t=int(input())
for _ in range(t):
    n=int(input())
    if n%3==0:
        print(n*2)
    else:
        print(n)