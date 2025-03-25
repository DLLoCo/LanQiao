## 函数中的形式参数：

~~~py
def tmp(res):
    global res1
    print("id1=",id(res1))
    print("id=",id(res))
    res+=1
    return res

def tmp2(res):
    global res1
    print("id1=",id(res1))
    print("id=",id(res))
    res+=1
    res1=res

res1=0
print("id1=",id(res1))
tmp(res1)
print("改变后 未 赋值 res1",res1)

res1=tmp(res1)
print("改变后 已 赋值 res1",res1)

res1=0
tmp2(res1)
print(res1)
~~~
~~~
# 输出
id1= 140712719419800
id1= 140712719419800
id= 140712719419800
改变后 未 赋值 res1 0
id1= 140712719419800
id= 140712719419800
改变后 已 赋值 res1 1
id1= 140712719419800
id= 140712719419800
1
~~~