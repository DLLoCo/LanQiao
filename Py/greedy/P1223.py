n=int(input())
s=[]
ans=0
tmp=list(input().split())

for i in range(n):
    t=tmp[i]
    s.append([i+1,int(t)])

s.sort(key=lambda x:(x[1],x[0]))


for i in range(n):
    print(s[i][0],end=" ")
    ans+=(n-i-1)*s[i][1] # ! n-i-1 表示后面有多少个比他大的数字,不是n-1

print()
print(f"{(ans/n):0.2f}")
"""
收获
1. 修改输出方式，使最后一个序号后面没有空格
for i in range(n-1):
    print(s[i][0], end=" ")
print(s[n-1][0])  # 最后一个序号单独输出，不加空格
2.lambda x:(x[1],x[0])：而是返回一个包含多个元素的元组作为排序键。
Python在比较元组时会按照以下规则进行：
首先比较元组的第一个元素，如果第一个元素相等，
则比较第二个元素，依此类推
"""