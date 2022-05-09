# 334.
# 递增的三元子序列给你一个整数数组nums ，判断这个数组中是否存在长度为3的递增子序列。
#
# 如果存在这样的三元组下标(i, j, k)
# 且满足
# i < j < k ，使得
# nums[i] < nums[j] < nums[k] ，返回true ；否则，返回false 。
#
#
#
# 示例
# 1：
#
# 输入：nums = [1, 2, 3, 4, 5]
# 输出：true
# 解释：任何
# i < j < k
# 的三元组都满足题意
# 示例
# 2：
#
# 输入：nums = [5, 4, 3, 2, 1]
# 输出：false
# 解释：不存在满足题意的三元组
# 示例
# 3：
#
# 输入：nums = [2, 1, 5, 0, 4, 6]
# 输出：true
# 解释：三元组(3, 4, 5)
# 满足题意，因为
# nums[3] == 0 < nums[4] == 4 < nums[5] == 6

# [0,4,1,3]


class Solution:
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False

        first = float('inf')
        second = float('inf')

        for i in nums:
            if i < first:
                first = i
                continue
            if first < i < second:
                second = i
                continue
            if i > second:
                return True
        return False



s = Solution()
d = s.increasingTriplet(
    [0, 4, 2, 1, 0, -1, -3])
print(d)
