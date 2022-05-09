# 119. 杨辉三角 II
# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
# 示例 1:
#
# 输入: rowIndex = 3
# 输出: [1,3,3,1]
# 示例 2:
#
# 输入: rowIndex = 0
# 输出: [1]
# 示例 3:
#
# 输入: rowIndex = 1
# 输出: [1,1]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/pascals-triangle-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp = [[0 for _ in range(rowIndex + 1)] for _ in range(rowIndex + 1)]
        for i in dp:
            print(i)
        dp[0][0] = 1

        for i in range(1, rowIndex + 1):
            for j in range(0,i+1):
                print(i-1,j-1)
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

        for i in range(0, rowIndex + 1):
            dp[i] = dp[i][:i +1]

        return dp


s = Solution()
s.getRow(4)
