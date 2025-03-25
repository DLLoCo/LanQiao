![alt text](<屏幕截图 2025-03-22 162915.png>)
## 常见方法
1. 元组直接赋值
```py
s=(1,6)
v,w=s
print(v,w)
# output:
# 1 6
```
3. list，str:
 list 没有find()方法，str有find()方法。
 都有index()方法。

4. list 字母也可以排序。
## 优化：

2. 优化读取速度，如果input 太多太长：
~~~py
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)  # 增加递归深度限制
~~~


## date库
### 注意：
- datetime(year, month, day)中的year范围是1~9999
---
1. 常见对象：
date：日期对象，只有年月日
time：时间对象，只有时分秒
datetime：日期时间对象，有年月日时分秒
timedelta：时间间隔，即两个时间点之间的长度


2. 常见方法：
strftime：日期转字符串
strptime：字符串转日期
date：获取日期对象
time：获取时间对象
now：获取当前日期时间对象
total_seconds()：将timedelta对象转换为总秒数
weekday()：返回星期几的数字，星期一为0，星期日为6。
isoweekday()：返回星期几的数字，星期一为1，星期日为7。
- 示例：
~~~py
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

from datetime import datetime
date_string = "2023-04-20 12:34:56"
date_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(date_object)
# output:
# 2023-04-20 12:34:56

from datetime import datetime
date1 = datetime(2023, 4, 20)
date2 = datetime(2023, 4, 25)
delta = date2 - date1
print(delta.days)
# output:
# 5

from datetime import timedelta
delta = timedelta(days=5)
total_seconds = delta.total_seconds()
print(total_seconds)
# output:
# 432000.0

from datetime import date
today = date.today()
print(today)
print(today.weekday())
print(today.isoweekday  ())
# output:
# 
# 6
~~~

## 日期题目
1. 优美写法：
~~~py
def leap(y):                         #判断闰年
    return y % 400 == 0 or y % 4 == 0 and y % 100 != 0
ans = 0
d = [31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(2000, 1999999+1):      #年
    if leap(i):   d[1] = 29
    else:         d[1] = 28
    for j in range(1, 12+1):          #月
        for k in range(1, d[j-1]+1):  #日
            if (i % j) == 0 and (i % k) == 0:
                ans += 1
ans += 1        # 2000000.1.1  不要忘记这个日期
print(ans)      # 输出：35813063
# 运行时间很长，直接提交代码会超时。这是填空题，提交结果就行。
~~~