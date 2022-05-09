# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 输入：matrix = [[1,2,3],
#                [4,5,6],
#                [7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 00,01,02,12,22,21,20,10,11

# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]]


# 按层次进行遍历

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        top, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        res = []

        while top <= down and left <= right:
            for i in range(left, right + 1):
                # print(i)
                res.append(matrix[top][i])
                # print(res)

            for i in range(top + 1, down + 1):
                res.append(matrix[i][right])
            if right > left and down > top:
                for i in range(right - 1, left - 1, -1):
                    # print(i)
                    res.append(matrix[down][i])
                for i in range(down - 1, top, -1):
                    # print(i)
                    res.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            down -= 1
        return res

            # break


s = Solution()
s.spiralOrder([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]])
