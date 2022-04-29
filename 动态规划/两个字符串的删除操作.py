# 给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。
#
# 每步 可以删除任意一个字符串中的一个字符。
#
#  
#
# 示例 1：
#
# 输入: word1 = "sea", word2 = "eat"
# 输出: 2
# 解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"
# 示例  2:
#
# 输入：word1 = "leetcode", word2 = "etco"
# 输出：4
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        if n == 0:
            return m
        if m == 0:
            return n
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        p = dp[m][n]
        res = m + n - 2 * p
        return res


s = Solution()
s.minDistance(word1="sea", word2="eat")
