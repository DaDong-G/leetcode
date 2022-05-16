# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 示例 1：
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
# 示例 2：
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/trapping-rain-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 存粹的暴力解法
# class Solution:
#     def trap(self, height):
#         n = len(height)
#         res = 0
#         for i in range(1, n - 1):
#             max_left = max(height[0:i + 1])
#             max_right = max(height[i:n])
#             # max_right = 0, 0
#             # for j in range(0, i + 1):
#             #     max_left = max(max_left, height[j])
#             # for j in range(i, n):
#             #     max_right = max(max_right, height[j])
#             res += min(max_right, max_left) - height[i]
#         print(res)
#         return res

# 动态规划解题方法
# 设置两个数组 max_left[]  max_right[]， 提前将每个位置 最左边，最右边的最大值存储进来。
class Solution:
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0
        res = 0
        left_max = [0] * n
        left_max[0] = height[0]
        right_max = [0] * n
        right_max[-1] = height[-1]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(1, n - 1):
            res += min(right_max[i], left_max[i]) - height[i]
        return res


# 双指针的方法



s = Solution()
s.trap([4, 2, 0, 3, 2, 5])
