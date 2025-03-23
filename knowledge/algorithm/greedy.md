# 贪心

- 证明
贪心算法有两种证明方法：反证法和归纳法。一般情况下，一道题只会用到其中的一种方法来证明。
  - 反证法：如果交换方案中任意两个元素/相邻的两个元素后，答案不会变得更好，那么可以推定目前的解已经是最优解了。
  - 归纳法：先算得出边界情况（例如 n = 1）的最优解 $F_1$，然后再证明：对于每个 $n$，$F_{n+1}$都可以由 $F_{n} $推导出结果。
- 与动态规划差别：
  - 贪心算法：没有状态转移方程，在每一步选择中都采取在当前状态下最好或最优的选择，**与之前结果无关**。 

# 实现贪心算法

一般来说，贪心算法的实现步骤为：
1. 排序解法
1.排序：将所有候选项按贪心策略排序。
2.迭代选择：从排序后的序列中依次遍历，每次选择符合条件的元素（并更新状态），直至处理完所有元素或达到目标。
整体代码结构通常非常简洁明了。

- “关键字”排序，例如：
活动选择问题中按照结束时间排序
最小生成树中选择权值最小的边
某些硬币找零问题中选择面值最大的硬币（注意：这种策略只有在硬币面额满足特定条件时才正确）
```py
# 贪心算法框架模板
def greedy_solution(params):
    # 1. 预处理（如排序）
    data = preprocess(params)
    
    # 2. 初始化关键变量
    result = 0
    current_state = initial_value
    
    # 3. 遍历做贪心选择
    for item in data:
        if satisfies_condition(current_state, item):
            update(current_state, item)
            result += 1  # 或其他操作
    
    # 4. 返回最终解
    return result
```
2. 后悔解法
思路是无论当前的选项是否最优都接受，然后进行比较，如果选择之后不是最优了，则反悔，舍弃掉这个选项；否则，正式接受。如此往复。
### eg（活动选择问题）：
贪心策略：每次选择结束时间最早的活动。

反证法证明：
 假设存在一个最优解不包含结束时间最早的活动 ai。a1为最早时间，那么这个最优解可以把ai换成a1，那么这个解可能比最优解更优，矛盾。
递归应用此逻辑，贪心策略正确。
```py
from typing import List, Tuple

def activity_selection(activities: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    参数：
      activities - 一个列表，每个元素是 (start, end) 表示一个活动的开始和结束时间。
    返回：
      选择的活动列表，使得活动互不冲突且数量最多。
    """
    # 按照结束时间排序（贪心选择策略）
    activities.sort(key=lambda x: x[1])
    
    # 初始化结果列表和最后一个选中活动的结束时间
    selected = []
    last_end_time = -float('inf')
    
    for activity in activities:
        start, end = activity
        # 如果当前活动的开始时间不小于上一个选中活动的结束时间，则可以选择
        if start >= last_end_time:
            selected.append(activity)
            last_end_time = end  # 更新最后结束时间
    
    return selected

#示例
if __name__ == "__main__":
    # 每个元组表示 (start, end)
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    result = activity_selection(activities)
    print("选中的活动:", result)
```

### eg
- 题目描述：
  约翰的工作日从 0 时刻开始，有 $10^9$ 个单位时间。在任一单位时间，他都可以选择编号 1 到 N 的 $N(1 \leq N \leq 10^5) $项工作中的任意一项工作来完成。工作 i 的截止时间是 $D_i(1 \leq D_i \leq 10^9)$，完成后获利是 $P_i( 1\leq P_i\leq 10^9 )$。在给定的工作利润和截止时间下，求约翰能够获得的利润最大为多少。

- 解题思路：
1. 先假设每一项工作都做，将各项工作按截止时间排序后入队；
2. 在判断第 i 项工作做与不做时，若其截至时间符合条件，则将其与队中报酬最小的元素比较，若第 i 项工作报酬较高（后悔），则 `ans += a[i].p - q.top()`。
用优先队列（小根堆）来维护队首元素最小。
1. 当 `a[i].d<=q.size()` 可以这么理解从 0 开始到 `a[i].d` 这个时间段只能做 `a[i].d` 个任务，而若 `q.size()>=a[i].d` 说明完成 `q.size()` 个任务时间大于等于 `a[i].d` 的时间，所以当第 i 个任务获利比较大的时候应该把最小的任务从优先级队列中换出。
```py
from collections import defaultdict
from heapq import heappush, heappop

a = defaultdict(list)
for _ in range(int(input())):
    d, p = map(int, input().split())
    a[d].append(p)  # 存放对应时间的收益

ans = 0  # 记录总收益
q = []  # 小根堆维护最小值
l = sorted(a.keys(), reverse=True)
for i, j in zip(l, l[1:] + [0]):
    for k in a.pop(i):
        heappush(q, ~k)
    for _ in range(i - j):
        if q:  # 从堆中取出收益最多的工作
            ans += ~heappop(q)
        else:  # 堆为空时退出循环
            break
print(ans)
```
# 常见贪心算法问题及应用
除了活动选择问题，常见的贪心算法还包括：

最小生成树（如 Kruskal、Prim 算法）
单源最短路径（如 Dijkstra 算法）
区间覆盖问题、会议室安排
哈夫曼编码（构造最优前缀码）
部分背包问题（连续分割问题）

## 哈夫曼：

### eg：果子