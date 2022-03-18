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
    def combinationSum2(self, candidates, target ):
        def dfs(p, r, t,used):
            # print(t)
            if t < 0:
                return

            if t == 0:
                p.sort()
                if p not in res:
                    res.append(p)
                # print(p)
                return

            for i in range(len(candidates)):
                if used[i] != 1:
                    if i > 0 and candidates[i] == candidates[i-1] and used[i-1] == 0 :
                        continue
                    used[i] = 1
                    dfs(p + [candidates[i]], r, t - candidates[i], used)
                    used[i] = 0

        path = []
        res = []

        use = [0 for _ in range(len(candidates))]
        dfs(path, res, target,use)
        return  res


candidates = ([1, 2, 2, 5])
candidates.sort()
target = 5
s = Solution()
s.combinationSum2(candidates, target)
