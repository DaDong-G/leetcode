# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
#
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rotate-image
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[7,4,1],[8,5,2],[9,6,3]]
# 输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# 输出：         [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
import copy

matrix = [[1,2,3],[4,5,6],[7,8,9]]
#        [[7,4,1],[8,5,2],[9,6,3]]
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_m = []
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(matrix[j][i])
            temp.reverse()
            new_m.append(temp)
        for i in range(r):
            for j in range(c):
                matrix[i][j] = new_m[i][j]

        print(matrix)

s = Solution()
s.rotate(matrix)
