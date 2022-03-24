# 给定一个含有 n 个正整数的数组和一个正整数 target 。
#
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
# 示例 1：
#
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 示例 2：
#
# 输入：target = 4, nums = [1,4,4]
# 输出：1
# 示例 3：
#
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
#
# t = 4  n = [1,2,3,1,2,5,2]
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# class Solution:
#     def minSubArrayLen(self, target: int, nums):
#         i, j = 0, 0
#         if nums is None:
#             return 0
#         if sum(nums) < target:
#             return 0
#         n = len(nums)
#         max_len = n + 1
#         while j < n:
#             j += 1
#             # 先移动右边的，如果i:j 小于 target,就继续移动j ， 否则移动i + 1， 滑动窗口
#             while target <= sum(nums[i:j]):
#                 if j-i < max_len:
#
#                     max_len = j-i
#                 i += 1
#
#         print(max_len)
#         return max_len

# 在原有基础进行优化， 使用一个total，来存取求得的和。
class Solution:
    def minSubArrayLen(self, target: int, nums):
        i, j = 0, 0
        if nums is None:
            return 0
        if sum(nums) < target:
            return 0
        n = len(nums)
        total = 0
        max_len = n + 1
        while j < n:
            total += nums[j]
            while target <= total:
                max_len = min(max_len, j - i + 1)
                total -= nums[i]
                i += 1
            j += 1
        return max_len


s = Solution()
f = s.minSubArrayLen(target=7, nums=[2,3,1,2,4,3])
print(f)