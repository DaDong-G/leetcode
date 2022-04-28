# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
#
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
#
#  
#
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
#      注意，你可以重复使用字典中的单词。
# 示例 3：
#
# 输入: s = "catsanddog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-break
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 这道题的精髓在于dp[i] 保存的是 s[0:i-1] 是存在可以拼成的单词。
# 如图
# 0 1 2 3 4 5 6 7 8 9 10
#   c a t s s a n d d o g
# T F F T t F F F T F F T
# 还是需要两个指针，往返扫描，具体看代码

class Solution:
    def wordBreak(self, s: str, wordDict):
        n = len(s)
        dp = [True] + [False] * n
        # 需要 1 - n + 1，索引对齐
        for i in range(1, n + 1):
            for j in range(0, i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
        return dp[-1]

        # print(i,j)


s = Solution()
d = s.wordBreak(s="applepenapple", wordDict=["apple", "pen"])
# d = "123"
# print(d[0:2])
