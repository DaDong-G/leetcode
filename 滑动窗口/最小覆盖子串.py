# 76. 最小覆盖子串 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 注意：
#
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
#  
#
# 示例 1：
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 示例 2：
#
# 输入：s = "a", t = "a"
# 输出："a"
# 示例 3:
#
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-window-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import Counter


# 解题步骤
# 双指针l ,r ， r 每次往右走，判断当前s[l:r]中是否包含子串，如果不包含就继续往右边走、
# 如果当前l 至 r  s[l:r] 中包含，那么就移动左边的指针l += 1, 然后在判断是否包含子串。
class Solution:
    def check(self, t_frequency, c_frequency):
        flag = True
        for k, v in t_frequency.items():
            if c_frequency[k] < t_frequency[k]:
                flag = False

        # for alpha in t:
        #     # 如果不存在，标记一下False
        #     if alpha not in word_string:
        #         flag = False
        #     else:
        #         if s[l:r].count(alpha) < t_frequency[alpha]:
        #             flag = False
        return flag

    def minWindow(self, s: str, t: str):
        if s is None or t is None:
            return ""
        if len(t) > len(s):
            return ""
        t_frequency = Counter(t)
        min_len = len(s) * 100
        result = ""
        l = 0
        r = 1
        n = len(s)
        while r <= n:
            # print(l,r)
            word_string = s[l:r]
            c_frequency = Counter(s[l:r])

            while self.check(t_frequency, c_frequency):
                # print(word_string)

                if len(word_string) < min_len:
                    result = word_string
                    min_len = len(word_string)

                l += 1
                while s[l:l + 1] not in t:
                    l += 1
                word_string = s[l:r]
                c_frequency = Counter(s[l:r])

            while s[r:r + 1] not in t and r < n:
                r += 1
            r += 1
        if min_len > n:
            return ""
        else:
            return result


s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"
s_s = Solution()
f = s_s.minWindow(s, t)
print(f)
