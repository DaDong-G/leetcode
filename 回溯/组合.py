# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 你可以按 任何顺序 返回答案。
# 示例 1：
# [1,2,3,4]
#
# 输入：n = 4, k = 2
# 输出：
# [
#   [3,4],
#   [2,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# 输入：n = 4, k = 3
# 输出：
# [
#   [2,3,4],
#   [1,2,4],
#   [1,2,3],
# ]

# 示例 2：
#
# 输入：n = 1, k = 1
# 输出：[[1]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/combinations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


#  一个回溯求解的模板
class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def dfs(p, r, s, start):
            if s == k:
                res.append(p)
                return
            for i in range(start, n + 1):
                # 这里去掉就是全部的组合。
                if i in p:
                    continue
                dfs(p + [i], r, s + 1, i)

        # 最终结果
        res = []
        # 临时存储
        p = []
        dfs(p, res, 0, 1)

        return res


s = Solution()
s.combine(4, 3)

