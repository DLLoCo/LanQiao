import sys
input=sys.stdin.readline
# 请在此输入您的代码
s=[ i for i in input().strip()]
for _ in range(pow(2,64)):
  if len(s)==0:
    print("EMPTY")
    break
  key=set()
  n=len(s)
  i=1
  cnt=0
  while i<=n-2:
    if (s[i]==s[i-1] and s[i]!=s[i+1]): 
      key.add(i)
      key.add(i+1)
      i+=1
    elif (s[i]!=s[i-1] and s[i]==s[i+1]):
      key.add(i)
      key.add(i-1)
      i+=1
    else:
      i+=1
  if not key:
    print("".join(a))
    break

  else:
    a=[]
    for i in range(n):
      if i not in key:
        a.append(s[i])
  s=a.copy()  
#!
# 1."""
#   while key:
#     a.pop(key.pop()-cnt)
#     cnt+=1  
# 有错误，cnt为了修正pop后key的下标变化
# 但是如果key从索引大的开始pop，会导致key的下标变化
# """
#2."""
#   while key:
#    key=list(key)
#    key.sort()
#    a.pop(key.pop())
#一直pop。sort，时间复杂度太高
# """
# 3. copy不如造一个新的数组
# if a==s:
#   print("".join(a))
#   break
# s=a.copy() 
