# 213.
# 打家劫舍
# II
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都
# 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你
# 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
#
#
#
# 示例
# 1：
#
# 输入：nums = [2, 3, 2]
# 输出：3
# 解释：你不能先偷窃1号房屋（金额 = 2），然后偷窃3号房屋（金额 = 2）, 因为他们是相邻的。
# 示例
# 2：
#
# 输入：nums = [1, 2, 3, 1]
# 输出：4
# 解释：你可以先偷窃1号房屋（金额 = 1），然后偷窃3号房屋（金额 = 3）。偷窃到的最高金额 = 1 + 3 = 4 。
# 示例
# 3：
#
# 输入：nums = [1, 2, 3]
# 输出：3
# 这道题和打家劫舍1 几乎一样，只是针对不同的数组
class Solution:
    def rob(self, nums):
        if len(nums) <= 2:
            return max(nums)
        return max(self.max_rob(nums[:-1]), self.max_rob(nums[1:]))

    def max_rob(self, nums):

        n = len(nums)
        if n <= 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


s = Solution()
d = s.rob([200,3,140,20,10])
print(d)
