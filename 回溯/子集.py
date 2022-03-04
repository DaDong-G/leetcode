# 给你一个整数数组
# nums ，数组中的元素
# 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集
# 不能
# 包含重复的子集。你可以按
# 任意顺序
# 返回解集。

# 输入：nums = [1, 2, 3]
# 输出：[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
class Solution:
    def subsets(self, nums):
        def dfs(p, r, s, start):
            res.append(p)
            if s == len(nums):
                return

            for i in range(start, len(nums)):
                if nums[i] in p:
                    continue
                # p.append(nums[i])
                dfs(p + [nums[i]], r, s + 1, i + 1)
                # p.pop()

            return r

        if len(nums) == 0:
            return []
        path = []
        res = []
        dfs(path, res, 0, 0)
        print(res)
        return res


s = Solution()
s.subsets([1, 2, 3])
