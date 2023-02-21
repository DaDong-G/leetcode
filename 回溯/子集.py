# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集
# 不能
# 包含重复的子集。你可以按
# 任意顺序
# 返回解集。
# https://leetcode-cn.com/problems/subsets/
# 输入：nums = [1, 2, 3]
# 输出：[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(start, p, s, r):
            if s == size + 1:
                return
            r.append(p)
            # print(p)
            for i in range(start, len(nums)):
                if nums[i] in p:
                    continue
                dfs(i, p + [nums[i]], s + 1, res)

        res = []
        p = []
        if len(nums) == 0:
            return []
        size = len(nums)
        dfs(0, p, 0, res)
        return res


s = Solution()
s.subsets([1, 2, 3])
