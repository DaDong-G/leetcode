# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个下标。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
# 示例 2：
#
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/jump-game
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# dp[i] 用来存放当前i位置可以跳跃到的最大位置。dp[i] = max(dp[i-1], nums[i] + i)
# [0,1,2,3,4]
# [2,3,1,1,4]
# [2,4,4,4,8]
class Solution:
    def canJump(self, nums):
        n = len(nums)
        if nums[0] >= n - 1:
            return True
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1,n):
            dp[i] = max(dp[i-1],nums[i] + i)
            if i >= dp[i]:
                print(dp, i)
                return False
            if dp[i] >= n - 1:
                print(dp, i)
                return True
        print(dp)
        return True

s = Solution()
d = s.canJump([1,0])
print(d)
#      [2,3,1,1,4]
#dp =  [2,4,6,7,10]
#index=[0,1,2,3,4]

#

#      [0,1,2,3,4
#      [3,2,1,0,4]
#dp =  [3,3,3,3,