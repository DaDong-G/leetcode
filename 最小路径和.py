# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
# 示例 2：
#
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
#
# [1,2,3]
# [4,5,6]

# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/minimum-path-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# bfs + dp
class Solution:
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = grid[0][0]
        direct = [(1, 0), (0, 1)]
        queue = [(0, 0)]
        dup = set()
        while len(queue) != 0:
            node = queue.pop(0)
            i, j = node[0], node[1]

            for d in direct:
                x = i + d[0]
                y = j + d[1]
                if x >= n or y >= m:
                    continue
                if (x, y) in dup:
                    continue
                # break
                if y == 0:
                    dp[x][y] = dp[x - 1][y] + grid[x][y]
                elif x == 0:
                    dp[x][y] = dp[x][y - 1] + grid[x][y]
                # print(dp)
                else:
                    dp[x][y] = min(dp[x][y - 1] + grid[x][y], dp[x - 1][y] + grid[x][y])

                dup.add((x, y))
                queue.append((i + 1, j))
                queue.append((i, j + 1))


        return dp[-1][-1]


s = Solution()
s.minPathSum([[0]])
# [1,2,3]  [1,3,6]
# [4,5,6]  [5,8,12]