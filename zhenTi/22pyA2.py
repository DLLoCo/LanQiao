n=int(input())
ans=4
# x,y两个长方形，比较是否可以合并为一个：可以+=0，else+=2
def jdg(x,y,res):
    x.sort()
    y.sort()
    # 长宽分别相等
    if x[0]==y[0] and x[1]==y[1]:
        res+=0
##        print(res)
        return 3,res
    # x[0]==y[0] 为公共边
    elif x[0]==y[0]:
        res+=0
##        print(res)
        return 1,res
    # x[0]==y[1] 为公共边
    elif x[0]==y[1]:
        res+=0
##        print(res)
        return 2,res
    # x[1]==y[1] 为公共边
    elif x[1]==y[1]:
        res+=0
##        print(res)
        return 4,res
    # x[1]==y[0] 为公共边
    elif x[1]==y[0]:
        res+=0
##        print(res)
        return 5,res
    else:
        res+=2
##        print(res)
        return 0,res
def jdg2(x,y,z,res):# x,y先拼在一起
    t1=x[0]+y[0]
    t2=x[0]+y[1]
    t3=x[1]+y[0]
    t4=x[1]+y[1]
    if z[0]==t1 or z[0]==t2 or z[0]==t3 or z[0]==t4:
        res+=0
##        print(res)

    elif z[1]==t1 or z[1]==t2 or z[1]==t3 or z[1]==t4:
        res+=0
##        print(res)
    else:
        res+=2
##        print(res)
    return res
for i in range(n):
    a1,b1,a2,b2,a3,b3=map(int,input().split())
    x=[a1,b1]
    y=[a2,b2]
    z=[a3,b3]
    res1,res2,res3=4,4,4
    # 1,2
    key=jdg(x,y,res1)[0]
##    print("key=",key)
    res1=jdg(x,y,res1)[1]
    if key==1:
        m=[y[0],x[1]+y[1]]
        res1=jdg(m,z,res1)[1]
    elif key==2:
        m=[x[0],x[1]+y[0]]
        res1=jdg(m,z,res1)[1]
    elif key==4:
        m=[x[1],x[0]+y[0]]
        res1=jdg(m,z,res1)[1]
    elif key==5:
        m=[x[1],x[0]+y[1]]
        res1=jdg(m,z,res1)[1]
    elif key==3:
        m=[x[1],x[0]+y[0]]
        res1=jdg(m,z,res1)[1]
        m=[x[0],x[1]+y[1]]
        res1=min(res1,jdg(m,z,res1)[1])
    else:
        res1=jdg2(x,y,z,res1)
    # 1,3
    key=jdg(x,z,res2)[0]
##    print("key=",key)
    res2=jdg(x,z,res2)[1]
    if key==1:
        m=[x[0],x[1]+z[1]]
        res2=jdg(m,y,res2)[1]
    elif key==2:
        m=[x[0],x[1]+z[0]]
        res2=jdg(m,y,res2)[1]
    elif key==4:
        m=[x[1],x[0]+y[0]]
        res2=jdg(m,y,res2)[1]
    elif key==5:
        m=[x[1],x[0]+z[1]]
        res2=jdg(m,y,res2)[1]
    elif key==3:
        m=[x[1],x[0]+z[0]]
        res2=jdg(m,y,res2)[1]
        m=[x[0],x[1]+z[1]]
        res2=min(res2,jdg(m,y,res2)[1])
    else:
        res2=jdg2(x,z,y,res2)
    # 2,3
    key=jdg(y,z,res3)[0]
##    print("key=",key)
    res3=jdg(y,z,res3)[1]
    if key==1:
        m=[y[0],y[1]+z[1]]
        res3=jdg(m,x,res3)[1]
    elif key==2:
        m=[y[0],y[1]+z[0]]
        res3=jdg(m,x,res3)[1]
    elif key==4:
        m=[y[1],y[0]+z[0]]
        res3=jdg(m,x,res3)[1]
    elif key==5:
        m=[y[1],y[0]+z[1]]
        res3=jdg(m,x,res3)[1]
    elif key==3:
        m=[y[1],y[0]+z[0]]
        res3=jdg(m,x,res3)[1]
        m=[x[0],x[1]+y[1]]
        res3=min(res3,jdg(m,x,res3)[1])    
    else:
        res3=jdg2(y,z,x,res3)

    ans=min(res1,res2,res3)
    print(ans)
##    print(res1,res2,res3)
