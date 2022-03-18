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
        for i in dp:
            print(i)
        return s[begin:begin + max_len]


a = Solution()
s = "aadssdb"
a.longestPalindrome(s)
