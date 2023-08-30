# 42. 接雨水

class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = [0] * n, [0] * n
        ans = 0
        for i in range(1, len(heights)):
            l[i] = max(l[i - 1], heights[i - 1])
        for i in range(len(heights) - 2, 0, -1):
            r[i] = max(r[i + 1], heights[i + 1])
        for i in range(len(heights)):
            ans += max(0, min(l[i], r[i]) - heights[i])
        return ans

# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）

# 输入：height = [4,2,0,3,2,5]
# 输出：9