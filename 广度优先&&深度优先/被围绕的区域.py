# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#  
#
# 示例 1：
#
#
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 示例 2：
#
# 输入：board = [["X"]]
# 输出：[["X"]]
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/surrounded-regions
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import deque

# 如果该字母被标记过，则该字母为没有被字母 X 包围的字母 O，我们将其还原为字母 O；
# 如果该字母没有被标记过，则该字母被字母 X 包围的字母 O，我们将其修改为字母 X。


direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]


class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.x = len(board)
        self.y = len(board[0])
        self.duplicate_node = set()
        for j in range(self.y):
            self.dfs(0, j, board)
            self.dfs(self.x - 1, j, board)
        for i in range(self.x):

            self.dfs(i, 0, board)
            self.dfs(i, self.y - 1, board)
        #
        print(board)
        for i in range(self.x):
            for j in range(self.y):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        print(board)

    def dfs(self, x, y, board):
        stack = [(x, y)]
        self.duplicate_node.add((x, y))

        while len(stack) > 0:
            node = stack.pop()
            x = node[0]
            y = node[1]
            if x < 0 or y < 0 or x > self.x - 1 or y > self.y - 1 or board[x][y] != "O":
                continue
            # print(x, y, board[x][y])
            board[x][y] = "A"

            for d in direct:
                n_x = node[0] + d[0]
                n_y = node[1] + d[1]
                if n_x < 0 or n_y < 0 or n_x > self.x - 1 or n_y > self.y - 1 or board[x][y] != "O":
                    continue
                if (n_x, n_x) in self.duplicate_node:
                    continue
                stack.append((n_x, n_y))


board = [["O","O","O"],["O","O","O"],["O","O","O"]]

# s = [["A", "X", "X", "A", "X"],
#      ["X", "O", "O", "X", "A"],
#      ["X", "O", "X", "A", "X"],
#      ["A", "X", "A", "A", "A"],
#      ["X", "X", "A", "X", "A"]]

t = [['A', 'X', 'X', 'A', 'X'],
     ['X', 'A', 'A', 'X', 'A'],
     ['X', 'A', 'X', 'A', 'X'],
     ['A', 'X', 'A', 'A', 'A'],
     ['X', 'X', 'A', 'X', 'A']]



g = [['X', 'O', 'X', 'O', 'X', 'O'],
     ['O', 'X', 'X', 'X', 'X', 'X'],
     ['X', 'X', 'X', 'X', 'X', 'O'],
     ['O', 'X', 'O', 'X', 'O', 'X']]


s = Solution()
s.solve(board)
