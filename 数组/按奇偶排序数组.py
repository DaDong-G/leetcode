# 给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。
#
# 返回满足此条件的 任一数组 作为答案。
#
#  
#
# 示例 1：
#
# 输入：nums = [3,1,2,4]
# 输出：[2,4,3,1]
# 解释：[4,2,3,1]、[2,4,1,3] 和 [4,2,1,3] 也会被视作正确答案。
# 示例 2：
#
# 输入：nums = [0]
# 输出：[0]
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sort-array-by-parity
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# from collections import deque
# class Solution:
#     def sortArrayByParity(self, nums):
#         n = len(nums)
#         # c = 0
#         q = deque()
#         for i in nums:
#             if i % 2 == 0:
#                 q.appendleft(i)
#             else:
#                 q.append(i)
#         return list(q)


# 原地排序大法


class Solution:
    def sortArrayByParity(self, nums):
        i = 0
        j = len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2 == 0:
                i += 1

            while i < j and nums[j] % 2 == 1:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return nums


s = Solution()
d = s.sortArrayByParity([3, 1, 2, 4])
print(d)
