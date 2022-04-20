# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
#
#  
#
# 示例 1:
# "asdcab"
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#  示例 2:
#
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []
        s_count = [0] * 26
        p_count = [0] * 26

        # print(ord("a") - 97)
        ans = []

        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1
            if s_count == p_count:
                ans.append(i+1)
        return ans



s = Solution()
s.findAnagrams("abab", "ab")
