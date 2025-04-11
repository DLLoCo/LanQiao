![alt text](<屏幕截图 2025-03-22 162915.png>)
~~~py
math.log(100000,2)
>>> 16.609640474436812
~~~
## 技巧
1. **暴力解法**：
- 总结：
  - 暴力可以思考转换题目意思完再暴力
  - 也可以直接无脑按照题目意思直接暴力

eg:24cA5:
~~~plain
小蓝随手写出了含有 n
 个正整数的数组 {a1,a2,…,an}，他发现可以轻松地算出有多少个有序二元组 (i,j)满足 aj是 ai的一个因数。

因此他定义一个整数对 (x1,y1) 是一个整数对 (x2,y2) 的 “因数” 当且仅当 x1 和 y1 分别是 x2 和 y2 的因数。
他想知道有多少个有序四元组 (i,j,k,l) 满足 (ai,aj) 是 (ak,al) 的因数，其中 i,j,k,l 互不相等。

输入格式
输入的第一行包含一个正整数 n。

第二行包含 n个正整数 a1,a2,…,an，相邻整数之间使用一个空格分隔。

输出格式
输出一行包含一个整数表示答案。

数据范围
对于 20%
 的评测用例，1≤n≤50；
对于 40%
 的评测用例，1≤n≤104；
对于所有评测用例，1≤n,ai≤105。

输入样例：
5
3 6 2 2 7
输出样例：
4
样例解释
四元组 (1,4,2,3)：(3,2)为 (6,2) 的因子；

四元组 (1,3,2,4)：(3,2) 为 (6,2) 的因子；

四元组 (4,1,3,2)：(2,3) 为 (2,6) 的因子；

四元组 (3,1,4,2)：(2,3) 为 (2,6) 的因子。
~~~
```c

//参考：因数计数-圣甲虫滚地球的代码
#include <bits/stdc++.h>
using namespace std;
int N[10100];
int cnt;
int main()
{
  int n;  cin>>n;
  for(int i=1;i<=n;i++)   cin>>N[i];
  for(int i=1;i<=n;i++)
    for(int j=1;j<=n;j++)
      if(i!=j)
        for(int k=1;k<=n;k++)
          if(k!=i&&k!=j)
            for(int l=1;l<=n;l++)
              if(l!=k&&l!=j&&l!=i)
                if(N[k]%N[i]==0&&N[l]%N[j]==0)     cnt++;

  cout<<cnt;
  return 0;
}
```
2. **对拍**：
- 总结：
  - 直接输出特殊解：比如`如果没有则输出-1`

eg:
~~~plain
10%无脑解：10%得分根本不用编码，因为题目说“如果不能满足条件，输出 −1”。
直接输出-1就能得20%分，即4分。
这意思就是所有人都能得4分，不会零蛋。
~~~
---
## 数据结构选择：
1. 
**需要动态维护优先队列** → 用堆（如实时处理流式数据）。

**只需一次性排序** → 直接用 sort，更快更简洁。
- 原因：
  - **数组排序**  
    若每次插入新元素后都调用 `sort()`，单次插入的时间复杂度为 **O(n log n)**（假设使用快速排序）。  
    **总时间复杂度**：插入 n 个元素需要 **O(n² log n)**，远高于堆的 **O(n log n)**。


假设插入 n 个元素并维护顺序：

| **操作**       | 插入 1 个元素 | 插入 n 个元素 | 总时间复杂度 |
|----------------|---------------|---------------|--------------|
| 堆（优先队列）  | O(log n)      | O(n log n)    | **O(n log n)** |
| 数组排序        | O(n log n)    | O(n² log n)   | **O(n² log n)** |

---
### 降低时间复杂度：
1. 
pc.pop(0)，每次循环都将m的第一个元素弹出。如果m是用列表实现的，那么每次pop(0)的时间复杂度是O(n)，因为列表需要移动所有后续元素。而如果n是1e5的话，这样的操作会导致总的时间复杂度是O(n^2)，这会超时。
而正确的代码并没有使用pop操作，而是通过一个指针i来遍历排序后的列表。这样，整个处理过程是线性的，时间复杂度为O(n log n)（排序的时间复杂度）加上O(n)的处理时间，这在n=1e5时是可以接受的。

3. 打表:
- [234 pyA1 数字诗意](https://www.acwing.com/solution/content/276177/)
```plain
首先可以知道这是等差数列，可以用 na1+n×(n−1)/2快速算出每一个值，

但是如果枚举a1和𝑛的话时间复杂度太高，可以先打表找思路，打表程序如下：
```
```py
10
3 5 6 7 9 10 11 12 13 14 15 17 18 19 20 21 22 24 25 26 27 28 30 33 34 35 36 38 39 40 42 44 45 46 49 50 51 52 54 55 56 57 60 63 65 68 69 70 72 75 76 77 81 84 85 90 91 92 95 99 100 105 108 115 117 125 126 135 145
```
```plain
1, 2, 4, 8, 16, 32...，即2^n(n=0,1,2…)的s数都不“蕴含诗意”
```
## 排序：
1. 元组排序：
```py
# 元组排序
# 先按照元组的第一个元素升序排序，如果第一个元素相同，再按照第二个元素降序排序
a = [(1, 2), (3, 4), (1, 3), (2, 1)]
a.sort(key=lambda x: (x[0], -x[1]))
print(a)
# output:
# [(1, 2), (1, 3), (2, 1), (3, 4)]
```
2. lambda 函数：
- lambda 函数是一种匿名函数，它可以接受任意数量的参数，但只能有一个表达式。
- lambda 函数的语法是：lambda arguments: expression
*arguments 是参数列表，expression 是表达式。*
- lambda 函数的返回值是表达式的结果。
~~~py
m=[list(map(int,input().split())) for i in range(n)]
#m根据子列表中第二个元素的值进行升序排序
m.sort(key=lambda x:x[1])
~~~
---
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
  ~~~py
  str.find(str, beg=0, end=len(string))
  ~~~

4. list 字母也可以排序。

5. list remove() 方法：
- remove() 方法用于移除列表中某个值的第一个匹配项。
- 语法：
~~~py
list.remove(obj)
~~~
- 参数：
obj -- 列表中要移除的对象。
- 返回值：
该方法没有返回值，但是会移除列表中的某个值的第一个匹配项。

6. (Dictionary) get() 函数返回指定键的值。

   - 语法
   ~~~py
   dict.get(key[, value]) 
   ~~~
   - 参数
   key -- 字典中要查找的键。
   value -- 可选，如果指定键的值不存在时，返回该默认值。
   返回值
   返回指定键的值，如果键不在字典中返回默认值 None 或者设置的默认值。

   - 实例
   ~~~py
   tinydict = {'Name': 'Runoob', 'Age': 27}
   print ("Age : %s" %  tinydict.get('Age'))
   # 没有设置 Sex，也没有设置默认的值，输出 None
   print ("Sex : %s" %  tinydict.get('Sex'))  
   # 没有设置 Salary，输出默认的值  0.0
   print ('Salary: %s' % tinydict.get('Salary', 0.0))

   # 输出结果
   Age : 27
   Sex : None
   Salary: 0.0
   get() 方法 Vs dict[key] 访问元素区别
   get(key) 方法在 key（键）不在字典中时，可以返回默认值 None 或者设置的默认值。

   dict[key] 在 key（键）不在字典中时，会触发 KeyError 异常。
   ~~~
7. 字符串翻转:
   ~~~py
   s = "hello"
   s = s[::-1]
   print(s)
   # output:
   # olleh
   s = "".join(reversed(s))
   ~~~
---
## 优化：

1. 优化读取速度，如果input 太多太长：
   ~~~py
   import sys
   input = sys.stdin.readline
   # sys.setrecursionlimit(10**6)  # 增加递归深度限制
   ~~~

---
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

## 进制转换库函数:
- hex 16
- oct 8
- bin 2
- int ( ,base=2/8/16)
1. 幸运数字 23jB
```py
d={"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
# 请在此输入您的代码
s=[]
n=1
while len(s)<2023:
    sh=[int(i) for i in str(n)]
    sh=sum(sh)
    # bi=int(str(bin(n))[2:])
    b=[int(i) for i in str(bin(n))[2:]]
    b=sum(b)
    # oc=int(str(oct(n))[2:])
    o=[int(i) for i in str(oct(n))[2:]]
    o=sum(o)
    # he=int(str(hex(n))[2:])
    h=0
    for i in str(hex(n))[2:]:
        if ord(i)>=97:
            h+=d[i]
        else:
            h+=int(i)
    if n%sh==0 and n%b==0 and n%o==0 and n%h==0:
        s.append(n)
    n+=1
print(s[-1])
```

## 概念：
1. **子树（Subtree）**：
树形数据结构中，子树（Subtree）是指从一个特定节点（称为子树的根）出发，向下延伸的**所有节点和边组成的树结构**。子树保留了原树的层次关系，是原树的一个**完整分支**。
~~~plain
树
        X
     / | \
    Y  Z  W
   / \    |
  P   Q   V
子树
    Y
   / \
  P   Q
~~~

## 格式化输出:
- 左对齐：{value:< width}
- 右对齐：{value:> width}
- 居中对齐：{value:^width}
```py
name = "Alice"
print(f"{name:<10}|{name:>10}|{name:^10}")
# output:
# Alice     |     Alice|   Alice
```