# 2024：
# 两千以上：不行
    # 千 2
    # 百 0 不行
    # 十 2
    # 个 1/3
# 两千到一千：
#预算
# 一千以内：125
    # 百：1 3 5 7 9
    # 十：0 2 4 6 8
    # 个：1 3 5 7 9
# 一百以内：20
    # 十：2 4 6 8 
    # 个：1 3 5 7 9 
# 十以内：5

#综上：最高位分奇偶；算最高位的；预算剩余的，直接加
n=int(input())
ans=0
for i in range(1,n+1):
    i=str(i)
    i=i[::-1]
    for j in range(1,len(i)+1):
        # print(i,j)
        if j%2==1:
            if int(i[j-1])%2!=1:
                break
        else:
            if int(i[j-1])%2!=0:
                break
    else:
        ans+=1
        print(i,ans)
print(ans)