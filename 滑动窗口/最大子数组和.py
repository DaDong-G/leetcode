# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。
#
#  -2 1 -3 4 -1 2 1 -5 4
#
# 示例 1：
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 示例 2：
#
# 输入：nums = [1]
# 输出：1
# 示例 3：
#
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/maximum-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if nums[i] + dp[i - 1] < nums[i]:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i - 1]
        return max(dp)


s = Solution()
s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
