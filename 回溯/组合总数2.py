# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 注意：解集不能包含重复的组合。 
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def combinationSum2(self, candidates, target):
        path = []
        res = []
        n = len(candidates)
        used = [0] * n
        candidates.sort()
        print(candidates)


        def dfs(p, r, t, used, start):
            if t == target :
                r.append(p)
                if p == [1, 2,5]:
                    print(used,start,"............")
                return

            if t > target:
                return

            for i in range(start, n):
                if used[i] == 1:
                    continue
                if i > 0 and candidates[i] == candidates[i- 1] and used[i - 1] == 0:
                    continue

                t += candidates[i]
                used[i] = 1
                dfs(p + [candidates[i]], res, t, used, i)
                used[i] = 0
                t -= candidates[i]

        dfs(path, res, 0, used, 0)
        return res

candidates = ([1, 2, 2, 5])
# candidates.sort()
# target = 5
s = Solution()
s.combinationSum2([10,1,1,2,7,6,1,5], 8)

#                                                            []
#
#
#                used = [1,0,0,0]      used = [0,1,0,0]        used = [0,0,1,0]            used = [0,0,0,1]
#                 1                      2                      2                            5
#               /   \
#              /     \
#             /       \
#   used = [1,0,0,0]  used = [1,1,0,0]
#          1           2

