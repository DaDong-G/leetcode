# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
#
# 问总共有多少条不同的路径？
#
#  
#
# 示例 1：
#
#
# 输入：m = 3, n = 7
# 输出：28
# 示例 2：
# [x,x
#  x,x
#  x,x]
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下
# 示例 3：
#
# 输入：m = 7, n = 3
# 输出：28
# 示例 4：
#
# 输入：m = 3, n = 3
# 输出：6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-paths
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 这题看这个图就一目了然,dp是二维数组，每个dp[i][j] = dp[i-1][j] + dp[i][j-1]组成

# [[0, 0, 0, 0, 0, 0, 0],
# [ 0, 0, 0, 0, 0, 0, 0],
# [ 0, 0, 0, 0, 0, 0, 0]]


# [[1, 1, 1, 1,  1,  1,  1],
# [ 1, 2, 3, 4,  5,  6,  7],
# [ 1, 3, 6, 10, 15, 21, 28]]


class Solution:
    def uniquePaths(self, m: int, n: int):
        dp = [[0 for _ in range(n)] for _ in range(m)]
        print(dp)
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp)
        return dp[m - 1][n - 1]


s = Solution()
d = s.uniquePaths(m=3, n=7)
print(d)
