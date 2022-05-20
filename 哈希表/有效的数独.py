# 请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
#  
#
# 注意：
#
# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
# 空白格用 '.' 表示。
# 输入：board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# 输出：true
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/valid-sudoku
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            res_x = []
            res_j = []
            for j in range(9):
                if board[i][j] in res_x and board[i][j] != ".":
                    return False
                res_x.append(board[i][j])

                if board[j][i] in res_j and board[j][i] != ".":
                    return False
                res_j.append(board[j][i])


        res = []
        for i in range(0, 3):
            for j in range(0,  3):
                if board[i][j] in res and board[i][j] != ".":
                    return False
                res.append(board[i][j])

        res = []
        for i in range(0, 3):
            for j in range(3,  6):
                if board[i][j] in res and board[i][j] != ".":
                    return False
                res.append(board[i][j])

        res = []
        for i in range(0, 3):
            for j in range(6,  9):
                if board[i][j] in res and board[i][j] != ".":
                    return False
                res.append(board[i][j])


        res = []
        for i in range(3, 6):
            for j in range(0,  3):
                if board[i][j] in res and board[i][j] != ".":
                    return False
                res.append(board[i][j])

        res = []
        for i in range(3, 6):
            for j in range(3, 6):
                if board[i][j] in res and board[i][j] != ".":
                    return False
                res.append(board[i][j])
                # print(i, j)

        res = []

        for i in range(3, 6):
            for j in range(6,  9):
                if board[i][j] in res and board[i][j] != ".":
                    return False
                res.append(board[i][j])
        res = []

        for i in range(6, 9):
            for j in range(0, 3):
                if board[i][j] in res and board[i][j] != ".":
                    return False
                res.append(board[i][j])

            # break
        res = []
        for i in range(6, 9):
            for j in range(3, 6):
                if board[i][j] in res and board[i][j] != ".":
                    return False
                res.append(board[i][j])

        res = []
        for i in range(6, 9):
            for j in range(6, 9):
                if board[i][j] in res and board[i][j] != ".":
                    return False
                res.append(board[i][j])
        return True
        # i_x += 3
        # for x in range(jgg_i, jgg_i + 3):
        #     for y in range(jgg_j, jgg_j + 3):
        #         print(board[x][y], x, y)
        # jgg_i = i // 3
        # jgg_j = jgg_j + 3
        # if jgg_j > 8:
        #     jgg_j = 0
        # break


#
# board = [[".", ".", ".",  ".", "8", ".",  ".", ".", "."],
#          [".", ".", ".",  ".", ".", ".",  "5", ".", "."],
#          [".", ".", ".",  ".", "4", ".",  ".", "2", "."],
#
#          [".", ".", ".",  "3", ".", "9",  ".", ".", "."],
#          [".", ".", "1",  "8", ".", ".",  "9", ".", "."],
#          [".", ".", ".",  ".", ".", "5",  "1", ".", "."],
#
#          [".", ".", "3",  ".", ".", "8",  ".", ".", "."],
#          [".", "1", "2",  ".", "3", ".",  ".", ".", "."],
#          [".", ".", ".",  ".", ".", "7",  ".", ".", "1"]]
board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]
s = Solution()
s = s.isValidSudoku(board)
print(s)
