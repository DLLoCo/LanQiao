## 应用：
1. **求滑动窗口区间最值**

    1. 思路（以最大值为例）：
       详见[acwing](https://www.acwing.com/file_system/file/content/whole/index/content/4139707/)
      - 如果当前的滑动窗口中有两个下标 i 和 j ，其中i在j的左侧（i < j），并且i对应的元素不大于j对应的元素（nums[i]≤nums[j]），则：
      当滑动窗口向右移动时，只要 i 还在窗口中，那么 j 一定也还在窗口中。这是由于 i 在 j 的左侧所保证的。
      因此，由于 nums[j] 的存在，nums[i] 一定不会是滑动窗口中的最大值了，我们可以将nums[i]永久地移除。
      因此我们可以使用一个队列存储所有还没有被移除的下标。在队列中，这些下标按照从小到大的顺序被存储，并且它们在数组nums中对应的值是严格单调递减的。

      - 当滑动窗口向右移动时，我们需要把一个新的元素放入队列中。

      - 为了保持队列的性质，我们会不断地将新的元素与队尾的元素相比较，如果新元素大于等于队尾元素，那么队尾的元素就可以被永久地移除，我们将其弹出队列。我们需要不断地进行此项操作，直到队列为空或者新的元素小于队尾的元素。

      - 由于队列中下标对应的元素是严格单调递减的，因此此时队首下标对应的元素就是滑动窗口中的最大值。

      - 窗口向右移动的时候。因此我们还需要不断从队首弹出元素保证队列中的所有元素都是窗口中的，因此当队头元素在窗口的左边的时候，弹出队头。
    2. 代码：
        1. 编写简单
       ~~~py
       def sliding_window(nums,k): #nums为一维数组,k为窗口大小
           max_result=[] #用来记录每次的最大值
           min_result=[] #用来记录每次的最小值
           q_max=[]      #记录一维数组中最大值的索引值
           q_min=[]      #记录一维数组中最小值的索引值
           for i,num in enumerate(nums): #i表示索引值,num表示索引值对应的值
               #维护最大值的单调递减队列
               #最大值队列存在,且队列中右边元素小于当前值则删除队列右边元素
               while q_max and nums[q_max[-1]]<num:
                   q_max.pop()
               #将当前值添加到队列的右边
               q_max.append(i)

               #维护最小值的单调递增队列
               #最小值队列存在,若队列最右边元素大于当前值则删除队列右边元素
               while q_min and nums[q_min[-1]]>num:
                   q_min.pop()
               #将当前值添加到队列的右边
               q_min.append(i)

               #移除窗口之外的索引值
               #i-k表示当前索引值的前k个元素,表示窗口的最左端
               #如果最大值/最小值的最左端位置与第一个索引值相同,则删除
               if q_max[0]==i-k:q_max.pop(0)
               if q_min[0]==i-k:q_min.pop(0)

               #当窗口大小达到k时,则记录此时的最大值和最小值
               if i>=k-1:
                   max_result.append(nums[q_max[0]])
                   min_result.append(nums[q_min[0]])
           
           #返回最后的结果    
           return max_result,min_result
       ~~~

        2. 易懂：
       ~~~py
        class MonotonicQueue:
          def __init__(self):
              self.maxq = []
          
          def push(self, n):
              # 将小于 n 的元素全部删除
              while self.maxq and self.maxq[-1] < n: 
                  self.maxq.pop()
              # 然后将 n 加入尾部
              self.maxq.append(n)
          
          def max(self):
              return self.maxq[0]
          
          def pop(self, n):
              if n == self.maxq[0]:
                  self.maxq.pop(0)

        class Solution(object):
          def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
              window = MonotonicQueue()
              res = []
              
              for i in range(len(nums)):
                  if i < k - 1:
                      # 先填满窗口的前 k - 1
                      window.push(nums[i])
                  else: 
                      # 窗口向前滑动，加入新数字
                      window.push(nums[i])
                      # 记录当前窗口的最大值
                      res.append(window.max())
                      # 移出旧数字
                      window.pop(nums[i - k + 1])
              return res
        ~~~
    3. 例题：
        23pyA4子矩阵（二维单调队列最值）[题解lanqiao](https://www.lanqiao.cn/problems/3521/learning/?page=1&first_category_id=1&second_category_id=3&name=%E5%AD%90%E7%9F%A9%E9%98%B5)