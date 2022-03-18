# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
from copy import copy


class Solution:
    def permuteUnique(self, nums):
        def dfs(n, p, depth, res, use):
            if depth == size:
                print(p)
                res.append(p.copy())
                return

            for i in range(len(nums)):
                # 如果没有使用过
                if use[i] == 0:
                    if i > 0 and n[i] == n[i-1] and use[i-1] == 0:
                        print(i)
                        continue
                    use[i] = 1
                    p.append(n[i])
                    # p + [n[i]]  就不需要进行进栈，出栈了。
                    dfs(n, p, depth + 1, res, use)
                    use[i] = 0
                    p.pop()

        size = len(nums)
        if size == 0:
            return []

        path = []
        res = []
        used = [0 for _ in range(len(nums))]
        nums.sort()
        dfs(nums, path, 0, res, used)
        print(len(res))
        return res


nums = [1, 1,3]
a = Solution()
a.permuteUnique(nums)
# class Solution:
#
#     def permuteUnique(self, nums):
#
#         def dfs(nums, size, depth, path, used, res):
#             if depth == size:
#                 res.append(path.copy())
#                 return
#             for i in range(size):
#                 if not used[i]:
#
#                     if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
#                         continue
#
#                     used[i] = True
#                     path.append(nums[i])
#                     dfs(nums, size, depth + 1, path, used, res)
#                     used[i] = False
#                     path.pop()
#
#         size = len(nums)
#         if size == 0:
#             return []
#
#         nums.sort()
#
#         used = [False] * len(nums)
#         res = []
#         dfs(nums, size, 0, [], used, res)
#         return res