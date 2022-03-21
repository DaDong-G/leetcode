# 示例 1:
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 维持一个窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        h = []
        max_len = 0
        i, j = 0, 0
        n = len(s)

        # for k in range(n):

        while j < n:
            if s[j] not in h:
                h.append(s[j])
                j += 1
                # print(j)
            else:
                max_len = max(max_len,len(h))
                h.pop(0)
                i += 1
        #     if s[i] in h:
        #         h.remove(s[i])
        #         if max_len < j + 1 - i:
        #             max_len = j + 1 - i
        #         i += 1
        #     else:
        #         h.add(s[i])
        #         j += 1

        return max(max_len,len(h))


s = Solution()
d = s.lengthOfLongestSubstring("au")
print(d)
