# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-search
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"


# 单词搜索，使用回溯算法，每次有四个方向。
class Solution:
    def exist(self, board, word: str):
        def dfs(i, j, mark, board, word):
            # 递归结束条件，如果所有的单词都遍历了一遍就结束。
            if len(word) == 0:
                return True
            coordinate = [[i - 1, j], [i, j - 1], [i, j + 1], [i + 1, j]]
            for c in coordinate:
                if 0 <= c[0] < len(board) and len(board[0]) > c[1] >= 0 and board[c[0]][c[1]] == word[0]:

                    if mark[c[0]][c[1]] == 1:
                        continue
                    mark[c[0]][c[1]] = 1
                    # 这里的word每次要+1
                    print(board[c[0]][c[1]])
                    if dfs(c[0], c[1], mark, board, word[1:]):
                        return True
                    else:
                        mark[c[0]][c[1]] = 0

        m = len(board)
        n = len(board[0])

        mark = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    mark[i][j] = 1
                    if dfs(i, j, mark, board, word[1:]):
                        return True
                    else:
                        mark[i][j] = 0
        return False


s = Solution()
print(s.exist(board, word))
