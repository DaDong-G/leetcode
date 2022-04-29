# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
#

# 示例 1：
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：
#
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 示例 3：
#
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# [0,1,0,3,2,3]
# 思路 这道题的 dp[i] 保存的是 从头到当前i 上升的最长子序列是多少。
# 如图

# i     [0,1,2,3,4,5]
# nums =[0,1,0,3,2,3]
#     1 [1,0,0,0,0,0]
#     2 [1,2,0,0,0,0]
#     3 [1,2,3,0,0,0]
#     4 [1,2,3,3,0,0]
#     5 [1,2,3,3,4,4]

class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            t_max = 0
            for j in range(0, i):
                # print(i, j)
                if nums[i] > nums[j]:
                    t_max = max(t_max, dp[j])
            dp[i] = t_max + 1
        print(dp)
        return dp[-1]

        # c += 1
        # print(c)



s = Solution()
d = s.lengthOfLIS([1, 2, 4, 3, 5, 4, 7, 2])
# print(d)
# [0, 1, 0, 3, 2, 3]
# [1, 2, 3, 3, 4, 4, 5, 2]
# [1, 2, 3, 3, 4, 4, 5, 2]