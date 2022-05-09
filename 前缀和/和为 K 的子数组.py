# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
#
#  [1,1,1,1]
#  []
#
# 示例 1：
#
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：
#
# 输入：nums = [1,2,3], k = 3
# 输出：2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/subarray-sum-equals-k
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#   [1, 2, 3]
# [0,1, 3, 6]
# 这里需要注意的一点 这里面的子数组是连续的

# 前缀和 + hash
#   [1, 1, 1, 1, 2, 4, 4] , target = 2
# [0,1, 2, 3, 4, 6, 10,14]
# h = {4: 1, 6: 2, 10: 3, 14: 4} # hash 中村的值
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i + 1] = dp[i] + nums[i]
        print(dp)
        c = 0
        h = {}
        for i in range(n):
            if dp[i + 1] == k:
                h[k] = 1
                c = 1

            elif dp[i + 1] - nums[i] in h:
                h[dp[i + 1]] = h[dp[i + 1] - nums[i]] + 1
                c = h[dp[i + 1]]
        return c

        # print(c)

s = Solution()
d = s.subarraySum([-1,-1,1], 1)
print(d)