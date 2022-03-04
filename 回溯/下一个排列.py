# 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列（即，组合出下一个更大的整数）。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须 原地 修改，只允许使用额外常数空间。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/next-permutation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[1,3,2]
# 示例 2：
#
# 输入：nums = [3,2,1]
# 输出：[1,2,3]
# 示例 3：
#
# 输入：nums = [1,1,5]
# 输出：[1,5,1]
# 示例 4：
#
# 输入：nums = [1]
# 输出：[1]
import copy


# 如果从左往右都是降序说明这个数是最大的组合，
# 如果这个数存在从左往右存在升序的，那么就可以确定有比他大的组合，从后往前找到第一组升序组合，例如1, 2, 3, 4, 6, 5
# 就要找到[4，6],因为只有里的4改变才能找到下一个比它大的。
# 然后 找从后往前查找，最后一个数字 到 4 里面 第一个 大于4 的数字。（因为后半部分是降序的，）
# 最后 交换位置, 将6 到最后的数字进行升序
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = None
        size = len(nums)
        # 第一步 从后往前找到 第一个 升序的组合(i,j)
        for i in range(size - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                l = i - 1
                break
        # 如果是降序就返回最小的
        if l is None:
            return nums.reverse()
        # 第二部 从后往前找到第一个比 nums[l]  大的数字，进行调换。
        for i in range(size - 1, l, -1):
            if nums[i] > nums[l]:
                t = nums[i]
                nums[i] = nums[l]
                nums[l] = t
                break
        print(nums , l)
        # 第三步 将 i 后面的数字进行降排列，因为降序最大，意思就是在换了一个数字的情况下让后面最大。
        print(nums)
        # print(nums)
        # return nums
        # return nums


s = Solution()
s.nextPermutation([5,4,7,5,3,2])
# 2 ,1 ,3

#
# a = [4, 5, 6, 3, 2, 1]
# # a[2:].sort()
# a[2:][:][:].sort()
# print(a)

# t = a[2:]
# print(t)
# t.sort()
# a = a[:2]
# print(a)
# a.extend(t)
# print(a)
# 5
# 123456
# 123465
# 123546
# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         i = len(nums) - 2
#         while i >= 0 and nums[i] >= nums[i + 1]:
#             i -= 1
#         if i >= 0:
#             j = len(nums) - 1
#             while j >= 0 and nums[i] >= nums[j]:
#                 j -= 1
#             nums[i], nums[j] = nums[j], nums[i]
#
#         left, right = i + 1, len(nums) - 1
#         while left < right:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#             right -= 1

# 从后向前查找第一个相邻升序的元素对 (i,j)，满足 A[i] < A[j]。此时 [j,end) 必然是降序
# 在 [j,end) 从后向前查找第一个满足 A[i] < A[k] 的 k。A[i]、A[k] 分别就是上文所说的「小数」、「大数」
# 将 A[i] 与 A[k] 交换
# 可以断定这时 [j,end) 必然是降序，逆置 [j,end)，使其升序,为了后半部分最小
# 如果在步骤 1 找不到符合的相邻元素对，说明当前 [begin,end) 为一个降序顺序，则直接跳到步骤 4
# 该方法支持数据重复，且在 C++ STL 中被采用。
