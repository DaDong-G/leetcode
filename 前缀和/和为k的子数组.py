
# 前缀和 思想
# 这个逻辑很重要
# 如果仅仅是求 第索引为2的数字 那么就是S[3] - S[2]
# nums = [1, 1, 3] , 前缀和 pre_mums = [0, 1, 2, 5]
# pre_mums[0] = 0
# pre_mums[1] = nums[0]
# pre_mums[2] = nums[0] + nums[1]
# pre_mums[3] = nums[0] + nums[1] + nums[2]
# pre_mums[3] = nums[0] + nums[1] + nums[2] + nums
# 注意偏移， nums[1]到nums[2] 就等于 等于pre_sum[3] - pre_sum[1]
# 注意偏移， nums[0]到nums[2] 就等于 等于pre_sum[3] - pre_sum[0]
# 注意偏移， nums[2]到nums[3] 就等于 等于pre_sum[4] - pre_sum[2]
# [j....i] 数组的和就是  pre[i+1] - pre[j]
# 就是 pre[r + 1] - pre[l]
# 方法 一
# class Solution:

#     def subarraySum(self, nums, k: int) -> int:
#         pre_nums = [0] * (len(nums) + 1)
#         for i in range(nums):
#             pre_nums[i+1] = pre_nums[i] + nums[i]
#         c = 0
#         for i in range(nums):
#             for j in range(i , nums):
#                 if pre_nums[j + 1] - pre_nums[i] == k:
#                     c += 1
#         return c
from collections import defaultdict

# 方法二
# class Solution:
#     def subarraySum(self, nums, k: int) -> int:
#         count = 0
#         for i in range(len(nums)):
#             sums = 0
#             for j in range(i, len(nums)):
#                 sums += nums[j]
#                 if sums == k:
#                     count += 1
#         print(count)
#         return count
#
# s = Solution()
# s.subarraySum([1,1,2],2)

# 方法三 前缀和+ 哈希
# pre[i + 1] = pre[i] + nums[i]
# [j..i] 这个子数组和为 k 这个条件我们
# pre[i+1] - pre[j] == k
# pre[j] = pre[i + 1] - k
