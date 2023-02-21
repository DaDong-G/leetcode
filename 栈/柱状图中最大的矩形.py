# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#  
#
# 示例 1:
#
#
#
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
# 示例 2：
#
#
#
# 输入： heights = [2,4]
# 输出： 4
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/largest-rectangle-in-histogram
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 这道题用到了一个非常巧妙的方法，使用的数据结构是单调栈来解决了问题。

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = list()
        res, i = 0, 0
        while i < len(heights):
            if not stack or (heights[i] >= heights[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                k = stack.pop()
                if stack:
                    d = i - stack[-1] - 1
                # 这个一定是 全局的最小值 所以要 乘以 当前位置
                else:
                    d = i
                res = max(res, heights[k] * d)

        while stack:
            k = stack.pop()
            if stack:
                d = i - stack[-1] - 1
            else:
                d = i
            res = max(res, heights[k] * d)

        return res

# s = []
# s.pop()

s = Solution()#                 2 3
d = s.largestRectangleArea([2,1,2])
print(d)
# print(d)







