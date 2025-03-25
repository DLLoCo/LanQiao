# 44min
"""
快速方法：日期库，只要不超过9999年
#艺术与篮球-lanqiao0825142311的代码
import datetime
date01 = datetime.date(2000, 1, 1)
date02 = datetime.date(2024, 4, 13)
day = datetime.timedelta(days=1)
x = [13, 1, 2, 3, 5, 4, 4, 2, 2, 2]
c = 0
while date01 <= date02:
    date = map(int, list(str(date01).replace('-', '')))
    ans = 0
    for i in date:
        ans += x[i]
    if ans > 50:
        c += 1
    date01 += day
print(c)
"""
def leap(y):
  if (y%4==0 and y%100!=0) or y%400==0:
    return 1
  else:
    return 0
d={0:13,1:1,2:2,3:3,4:5,5:4,6:4,7:2,8:2,9:2}
res=0
dd=[0,31,28,31,30,31,30,31,31,30,31,30,31]
for y in range(2000,2024):
#!  ans=0 的位置错了
# """
# for y in range(2000,2024):
#   ans=0
#   if leap(y):
#     dd[2]=29
#   else:
#     dd[2]=28
#   y1=y//1000
#   y2=(y-y1*1000)//100
#   y3=(y-y1*1000-y2*100)//10
#   y4=(y-y1*1000-y2*100-y3*10)
#   ans+=d[y1]+d[y2]+d[y3]+d[y4]
#   for i in range(1,13):
#     m1=i//10
#     m2=i%10
#     ans+=d[m1]+d[m2]
#     for j in range(1,dd[i]+1):
#       d1=j//10
#       d2=j%10
#       ans+=d[d1]+d[d2]
#       if ans>50:
#         res+=1
# """
  ans1=0
  if leap(y):
    dd[2]=29
  else:
    dd[2]=28
  y1=y//1000
  y2=(y-y1*1000)//100
  y3=(y-y1*1000-y2*100)//10
  y4=(y-y1*1000-y2*100-y3*10)
  ans1+=d[y1]+d[y2]+d[y3]+d[y4]
  for i in range(1,13):
    ans2=0
    m1=i//10
    m2=i%10
    ans2+=d[m1]+d[m2]
    for j in range(1,dd[i]+1):
      ans3=0
      d1=j//10
      d2=j%10
      ans3+=d[d1]+d[d2]
      if ans1+ans2+ans3>50:
        res+=1
#！ 忘记2024只到4.13
dd2=[0,31,29,31,13]
y=2024
ans1=0
y1=y//1000
y2=(y-y1*1000)//100
y3=(y-y1*1000-y2*100)//10
#！各位数的计算 y4!=y%1000 因为2010%1000=10
y4=(y-y1*1000-y2*100-y3*10)
ans1+=d[y1]+d[y2]+d[y3]+d[y4]
for i in range(1,5):
    ans2=0
    m1=i//10
    m2=i%10
    ans2+=d[m1]+d[m2]
    for j in range(1,dd2[i]+1):
      ans3=0
      d1=j//10
      d2=j%10
      ans3+=d[d1]+d[d2]
      if ans1+ans2+ans3>50:
        res+=1
#!忘记ans1
"""
dd2=[0,31,29,31,13]
for i in range(1,5):
    ans2=0
    m1=i//10
    m2=i%10
    ans2+=d[m1]+d[m2]
    for j in range(1,dd[i]+1):
      ans3=0
      d1=j//10
      d2=j%10
      ans3+=d[d1]+d[d2]
      if ans2+ans3>50:
        res+=1
"""
print(res)
