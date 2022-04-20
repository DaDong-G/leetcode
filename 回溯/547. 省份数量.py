# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
#
# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
#
# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
#
# 返回矩阵中 省份 的数量。
#
#  [[1,0,0,1],
#   [0,1,1,0],
#   [0,1,1,1],
#   [1,0,1,1]]
#
# 示例 1：
#[1,1,0]
#[1,1,0]
#[0,0,1]
# 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# 输出：2
# 示例 2：
#
#
# 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# 输出：3
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-provinces
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
isConnected = [[1,1,0],
               [1,1,0],
               [0,0,1]]

directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
class Solution:
    def findCircleNum(self, grid):

        def dfs(grid, r, c):

            for d in directs:
                # 注意这里一定不能写成 r += d[0]

                # print(i, j)
                if 0 <= r + d[0] < len(grid) and len(grid[0]) > c + d[1] >= 0 and grid[r + d[0]][c + d[1]] == 1:
                    # print(i, j)
                    grid[r + d[0]][c + d[1]] = 0
                    # print(grid)
                    dfs(grid, r + d[0], c + d[1])

        nr = len(grid)
        if nr == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island += 1
                    dfs(grid, i, j)
        print(island)
        return island
s = Solution()
s.findCircleNum(isConnected)