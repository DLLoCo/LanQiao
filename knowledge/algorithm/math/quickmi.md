# 快速幂
1. 思路：
- 快速幂的本质是分治算法。
- 举个例子，如果我们要计算 x^64，我们可以按照以下步骤进行：
- 首先计算 x^2，然后计算 x^4，然后计算 x^8，然后计算 x^16，然后计算 x^32，最后计算 x^64。
- 这样，我们就只需要进行 6 次乘法，而不是 63 次。

2. 代码：
~~~py
def quick(a,b,p):
    if b==0:
        return 1
    ans=1
    while b:
        if b&1==1:
            ans=(ans*a)%p
        #! a=(a*a)%p 不在 if 模块中
        a=(a*a)%p
        #! 不要写成 b>>1
        b>>=1
    return ans

a,b,p=map(int,input().split())

print(quick(a,b,p))
~~~
3. 时间复杂度：
- O(logn)
