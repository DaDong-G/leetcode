# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
#
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
#
# 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
#  
#
# 示例 1:
#
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
# 示例 2:
#
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/product-of-array-except-self
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# [1,2,6,24]
# [1,2,3,4 ]


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        if nums.count(0) >= 2:
            return [0] * n

        if nums.count(0) == 1:
            res = 1
            for i in nums:
                if i != 0:
                    res *= i
            r = [0] * n
            r[nums.index(0)] = res
            return r

        r = [0] * n
        res = 1
        for i in range(n):
            res *= nums[i]

        for i in range(n):
            r[i] = res // nums[i]
        return r


s = Solution()
d = s.productExceptSelf([1,2,3,4])
print(d)