# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。
# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 示例 2：
#
# 输入：nums = [1]
# 输出：1
# 示例 3：
#
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# nums = [1]
nums = [1, 1, 3]


class Solution:
    def maxSubArray(self, nums):
        # 保存前几位数的和 比如 pre_sum[5] 代表前五位数的和  pre[5] - pre[2] 代表 第3 到 第5 位数的和。
        pre_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        # 2 - 3的和
        # print(pre_sum[3] - pre_sum[1])
        max_num = -99999
        # 这个逻辑很重要， 以 [1,1,3]    第二个数字、 第三个数字的和  就是  S3 - S1
        # 如果仅仅是求 第索引为2的数字 那么就是S[3] - S[2]
        # nums = [1, 1, 3] , 前缀和 pre_mums = [0, 1, 2, 5]
        # pre_mums[0] = 0
        # pre_mums[1] = nums[0]
        # pre_mums[2] = nums[0] + nums[1]
        # pre_mums[3] = nums[0] + nums[1] + nums[2]
        # pre_mums[3] = nums[0] + nums[1] + nums[2] + nums
        # 注意偏移， nums[1]到nums[2] 就等于 等于pre_sum[3] - pre_sum[1]
        # 注意偏移， nums[0]到nums[2] 就等于 等于pre_sum[3] - pre_sum[0]

        # 需要遍历出来的数 [0 , 1],[0 , 2],[0, 3],[1,2],[1,3],[2,3]
        # 遍历所有连续子序列求和的方法
        print(pre_sum)
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if pre_sum[j + 1] - pre_sum[i] > max_num:
                    max_num = pre_sum[j + 1] - pre_sum[i]

        return max_num
            # gap += 1


# print(sum(nums[1:3]))
s = Solution()
d = s.maxSubArray(nums)
# print(d)
