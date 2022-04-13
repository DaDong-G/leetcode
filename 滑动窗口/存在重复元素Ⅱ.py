# 219.存在重复元素II
# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。
# 如果存在，返回 true ；否则，返回 false 。
#
#
#
# 示例
# 1：
#
# 输入：nums = [1, 2, 3, 1], k = 3
# 输出：true
# 示例
# 2：
#
# 输入：nums = [1, 0, 1, 1], k = 1
# 输出：true
# 示例
# 3：
#
# 输入：nums = [1, 2, 3, 1, 2, 3], k = 2
# 输出：false

# 使用滑动窗口法,固定的窗口移动
# class Solution:
#     def containsNearbyDuplicate(self, nums, k):
#         n = len(nums)
#         for j in range(k):
#             i = 0
#             j += 1
#             while j < n:
#                 if nums[i] == nums[j]:
#                     print(i,j)
#                     print(nums[i],nums[j])
#                     return True
#                 j += 1
#                 i += 1
#         return False


# 哈希表
# class Solution:
#     def containsNearbyDuplicate(self, nums, k):
#         n = len(nums)
#         for j in range(k):
#             i = 0
#             j += 1
#             while j < n:
#                 if nums[i] == nums[j]:
#                     print(i,j)
#                     print(nums[i],nums[j])
#                     return True
#                 j += 1
#                 i += 1
#         return False
#
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        for j in range(k):
            i = 0
            j += 1
            while j < n:
                if nums[i] == nums[j]:
                    print(i, j)
                    print(nums[i], nums[j])
                    return True
                j += 1
                i += 1
        return False


nums = [1, 0, 1, 1]
k = 1

s = Solution()
f = s.containsNearbyDuplicate(nums, k)
print(f)
