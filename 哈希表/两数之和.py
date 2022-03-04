# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i in range(len(nums)):
            if target - nums[i] in h:
                return [i, h[target - nums[i]]]
            h[nums[i]] = i
        return []


nums = [3,2,4]
target = 6
a = Solution()
p = a.twoSum(nums,target)
print(p)