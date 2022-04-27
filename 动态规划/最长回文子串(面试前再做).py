# 注意 遍历过程

# 0 1
# 1 2
# 2 3
# 3 4
# 4 5
# 5 6
# 0 2
# 1 3
# 2 4
# 3 5
# 4 6
# 0 3
# 1 4
# 2 5
# 2 5
# 3 4
# 3 6
# 0 4
# 1 5
# 2 6
# 0 5
# 1 6
# 0 6

#
# 示例 1：
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
#
# 输入：s = "cbbd"
# 输出："bb"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 递推开始
        # 先枚举子串长度 , 重点
        for L in range(2, n + 1):
            # print(L)
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break
                print(i, j)
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        print(i, j)
                        print(i + 1, j - 1)
                        # dp[i][j] = False
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        # print(dp)
        for i in dp:
            print(i)
        return s[begin:begin + max_len]


a = Solution()
s = "aadssdb"
a.longestPalindrome(s)
