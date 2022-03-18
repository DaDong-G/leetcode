# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案
# 示例 1：

# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
class Solution:
    def permute(self, nums):
        def dfs(p, s, r):
            if s == len(nums):
                r.append(p)
                print(p)
                return
            for i in range(len(nums)):
                if nums[i] in p:
                    continue
                print(p)
                dfs(p + [nums[i]], s + 1, r)

        size = len(nums)
        if size == 0:
            return
        p = []
        res = []
        dfs(p, 0, res)
        # print(res)
        return res
nums = [1, 2, 3]
a = Solution()
a.permute(nums)


