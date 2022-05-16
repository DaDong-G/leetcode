# 给定一个包含大写字母和小写字母的字符串 s ，返回 通过这些字母构造成的 最长的回文串 。
#
# 在构造过程中，请注意 区分大小写 。比如 "Aa" 不能当做一个回文字符串。
#
#  
#
# 示例 1:
#
# 输入:s = "abccccdd"
# 输出:7
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
# 示例 2:
#
# 输入:s = "a"
# 输入:1
# 示例 3:
#
# 输入:s = "bb"
# 输入: 2
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-palindrome
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        res = 0
        odd = 0
        for _, v in c.items():
            if v % 2 == 0:
                res += v
            else:
                odd = 1
                res += v - 1

        if res % 2 == 0 and odd != 0:
            return res + 1

        return res


"vvvvaabbe"
s = Solution()
d = s.longestPalindrome("ccc")

print(d)
