# 713.乘积小于K的子数组给定一个正整数数组nums和整数k 。
# 请找出该数组内乘积小于k的连续的子数组的个数。

# 示例
# 1:
#
# 输入: nums = [10, 5, 2, 6], k = 100
# 输出: 8
# 解释:
# 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]。
# 需要注意的是[10, 5, 2]
# 并不是乘积小于100的子数组。
# 示例
# 2:
#
# 输入: nums = [1, 2, 3], k = 0
# 输出: 0
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        i = 0
        j = 0
        total = 1
        res = 0
        while j < len(nums):
            total *= nums[j]

            while total > k:
                total //= nums[i]
                i += 1

            #  每次右指针位移到一个新位置,都会产生 ：
            # [right]              [4]
            # [right - 1, right]   [4,3]
            # [right - 2, right - 1, right] [4,3,2]
            # [left, right-2, right-1,right] 这几种情况 , [4,3,2,1]
            res += j - i + 1
            print(i, j, total, res)
            j += 1
        return res


s = Solution()
s.numSubarrayProductLessThanK( [10, 5, 1], 100)
# while nums[j] == 0 or nums[j] > k:
#     total = 1
#
# if nums[j] > k:
#     j += 1
#     i = j
#     total = nums[j + 1]
#     continue
