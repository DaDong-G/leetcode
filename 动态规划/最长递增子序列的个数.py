# 给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。
#
# 注意 这个数列必须是 严格 递增的。
#
#  [1,3,5,4,7]
#  [1,1,1,2,2]
#
# 示例 1:
#
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
# 示例 2:
#
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        cnt = [0] * n
        # 个数
        dp[0] = 1
        # 长度
        max_count = 1
        for i in range(1, n):
            f = False
            temp_max_cnt = 0
            # print(max_number)
            for j in range(0, i):
                # print(i,j)
                if nums[j] >= nums[i]:
                    dp[i] = dp[i - 1] + 1
                    cnt[i] = cnt[i - 1]
                    f = True
                    break
                temp_max_cnt += 1
            print(temp_max_cnt)
            if not f:
                dp[i] = dp[i - 1]
        print(dp)
        return dp[-1]
        # print(dp)


s = Solution()
s.findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2])
# [1, 2, 4, 3, 5, 4, 7, 2]
# [1, 2, 3, 3, 4, 4, 5, 5]
