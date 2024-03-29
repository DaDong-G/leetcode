# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
#
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
#

# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右

# [[0,0,0],
# [0,1,0],
# [0,0,0]]


# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/unique-paths-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# [[0, 0, 0, 0, 0, 0, 0],
# [ 0, 1, 0, 1, 0, 0, 0],
# [ 0, 0, 0, 0, 0, 0, 0]]


# [[1, 1, 1, 1,  1,  1,  1],
# [ 1, 0, 1, 0,  1,  2,  3],
# [ 1, 1, 2, 2,  3,  5,  8]]
# 这道题和不同路径1 几乎一样，使用动态规划，只不过遇到了障碍物绕过。
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        for i in range(len(dp)):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                dp[i][0] = 0
                break

        for i in range(len(dp[0])):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                dp[0][i] = 0
                break
            # for j in range(len(dp[0])):
        # print(dp)
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        for i in range(1, n):
            for j in range(1, m):
                # 说明有障碍物
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


s = Solution()
d = s.uniquePathsWithObstacles([[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

print(d)

