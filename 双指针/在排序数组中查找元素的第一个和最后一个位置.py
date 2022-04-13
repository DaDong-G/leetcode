# 34.
# 在排序数组中查找元素的第一个和最后一个位置
# 给定一个按照升序排列的整数数组nums，和一个目标值target。找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值target，返回[-1, -1]。
#
# 进阶：
#
# 你可以设计并实现时间复杂度为O(logn) 的算法解决此问题吗？
#
#
# 示例
# 1：
#
# 输入：nums = [5, 7, 7, 8, 8, 10], target = 8
# 输出：[3, 4]
# 示例
# 2：
#
# 输入：nums = [5, 7, 7, 8, 8, 10], target = 6
# 输出：[-1, -1]
# 示例
# 3：
#
# 输入：nums = [], target = 0
# 输出：[-1, -1]

# 如果二分查找找到了，
# 最前面的就要 r = mid - 1
# 最后面的就要 l = mid + 1
# 例如 [8,8,8,8,8,8] 找到了第三个8 ，那么前面的还得继续， 后面的也还得继续
class Solution:
    def searchRange(self, nums, target: int):
        left = 0
        right = len(nums) - 1
        index1 = -1
        index2 = -1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                index1 = mid
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1

            if nums[mid] > target:
                right = mid - 1

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                index2 = mid
                left = mid + 1
            if nums[mid] < target:
                left = mid + 1

            if nums[mid] > target:
                right = mid - 1

        return [index1,index2]



nums = [5, 7, 7, 8, 8,8,8, 10]
target = 8
s = Solution()
s.searchRange(nums, target)
