# 给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）
#
#  graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。

#  
#
# 示例 1：
# 输入：graph = [[1,2],[3],[3],[]]
# 输出：[[0,1,3],[0,2,3]]
# 解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3
# 示例 2：
#
#
#
# 输入：graph = [[4,3,1],[3,2,4],[3],[4],[]]
# 输出：[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/all-paths-from-source-to-target
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def allPathsSourceTarget(self, graph):
        if graph is None:
            return []
        def dfs(p, s, res):
            if s == size - 1:
                print(p)
                res.append(p)
                return
            for i in graph[s]:
                dfs(p + [i], i, res)

        size = len(graph)
        res = []
        path = [0]
        dfs(path, 0, res)
        print(res)
        return res


graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
s = Solution()
s.allPathsSourceTarget(graph=graph)
