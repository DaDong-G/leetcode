# 75.颜色分类
# 给定一个包含红色、白色和蓝色、共n个元素的数组nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。我们使用整数0、 1和2
# 分别表示红色、白色和蓝色。必须在不使用库的sort函数的情况下解决这个问题。
#
#
#
# 示例
# 1：
#
# 输入：nums = [2, 0, 2, 1, 1, 0]

# [1,0,1,2,1,1,1]
# if num[i] > num[j]:
#    交换 i, j
# [0,0,1,2,1,1,2]
# [0,0,1,2,1,1,2]
# 输出：[0, 0, 1, 1, 2, 2]
# 示例
# 2：
#
# 输入：nums = [2, 0, 1]
# 输出：[0, 1, 2]

from collections import Counter


# 先统计出来 0 ， 1 ，2 出现的个数，然后根据索引，依次往里填入。
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        c = Counter(nums)
        i, j, k = c[0], c[1], c[2]
        for f in range(len(nums)):
            if i > f:
                nums[f] = 0
            elif i + j > f:
                nums[f] = 1
            else:
                nums[f] = 2


s = Solution()
s.sortColors([2, 2, 2, 1, 1, 1, 1, 0])

