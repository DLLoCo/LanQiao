n=int(input())
vis=[0]*(n+1)
check=[[0 for _ in range(n+1)]for _ in range(n+1)]
##ans=[]
result=0
a=[0]*(n+1)

"""


"""

def judge(i,step):
    b1=i-step
    b2=i+step
    for j in range(1,step):
        if 1<=j+b1<=n:
            if check[j][j+b1]==1:
                return 0
        if 1<=b2-j<=n: #! 右对角线忘记
            if check[j][b2-j]==1:
                return 0
    return 1

def dfs(step):
    global result
    if step>n:
##        ans.append(tmp.copy()) #！ list数组的底层
        result+=1
        if result<4:
            for i in range(1,n+1):
                print(a[i],end=" ")
            print()
        return

    for i in range(1,n+1):
        if vis[i]==1 or (not judge(i,step)):
            continue
        vis[i]=1
        check[step][i]=1
        a[step]=i
        dfs(step+1)
        vis[i]=0
        check[step][i]=0 #！ 这个状态忘记撤回

dfs(1)

##for i in range(3):
##    for j in range(n):
##        print(ans[i][j],end=" ")
##    print()
print(result)

##n = int(input())
##vis = [0] * (n + 1)
##check = [[0] * (n + 1) for _ in range(n + 1)]
##ans = []
##result = 0
##tmp = []
##
##def judge(i, step):
##    for j in range(1, step):
##        # 检查左上对角线：(j, i - (step - j))
##        left_col = i - (step - j)
##        if 1 <= left_col <= n and check[j][left_col] == 1:
##            return False
##        # 检查右上对角线：(j, i + (step - j))
##        right_col = i + (step - j)
##        if 1 <= right_col <= n and check[j][right_col] == 1:
##            return False
##    return True
##
##def dfs(step):
##    global result, tmp
##    if step > n:
##        ans.append(tmp.copy())  # 必须存储副本
##        result += 1
##        return
##
##    for i in range(1, n + 1):
##        if vis[i] == 0 and judge(i, step):
##            vis[i] = 1
##            check[step][i] = 1
##            tmp.append(i)
##            dfs(step + 1)
##            # 回溯
##            tmp.pop()
##            vis[i] = 0
##            check[step][i] = 0  # 必须重置棋盘状态
##
##dfs(1)
##print(result)
##for solution in ans:
##    print(' '.join(map(str, solution)))
