# 峰值元素是指其值严格大于左右相邻值的元素。
#
# 给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞ 。
#
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
# 示例 1：
#
# 输入：nums = [1,2,3,1]
# 输出：2
# 解释：3 是峰值元素，你的函数应该返回其索引 2。
# 示例 2：
#
# 输入：nums = [1,2,1,3,5,6,4]
# 输出：1 或 5
# 解释：你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
#
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-peak-element
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 每次判断
# 如果nums[mid] > nums[mid + 1] 说明左边一定有峰值。
# 如果nums[mid] > nums[mid - 1] 说明右边一定有峰值。
# 需要注意的是，如果确定了一端存在峰值，就始终在一端进行搜寻。
class Solution:
    def findPeakElement(self, nums):
        if len(nums) <= 3:
            return nums.index(max(nums))
        left = 0
        right = len(nums) - 1
        n = len(nums) - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2

            print(left, mid, right)
            if mid != n:
                if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                    return mid

                if nums[mid] < nums[mid + 1]:
                    left = mid + 1
                    continue
            else:
                return mid
            if mid != 0:
                if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                    return mid

                if nums[mid] < nums[mid - 1]:
                    right = mid - 1
            else:
                return mid

        return mid

s = Solution()
s.findPeakElement([3,4,3,2,1])
# def findPeakElement(self, nums: List[int]) -> int:
#     n = len(nums)
#     i, j = 0, n - 1
#     while i <= j:
#         mid = i + (j - i) // 2
#         if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == n-1 or nums[mid] > nums[mid+1]):
#             return mid
#         if nums[mid] < nums[mid+1]:
#             i = mid + 1
#         else:
#             j = mid - 1
