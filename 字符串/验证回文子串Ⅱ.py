# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
#
#  
#
# 示例 1:
#
# 输入: s = "aba"
# 输出: true
# 示例 2:
#
# 输入: s = "abca"
# 输出: true
# 解释: 你可以删除c字符。
# 示例 3:
#
# 输入: s = "abc"
# 输出: false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-palindrome-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l , r = 0 , len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # s1 = s[:r] + s[r + 1:]
                # s2 = s[:l] + s[l + 1:]
                if s[l] == s[r-1] or s[l+1] == s[r]:
                    return True
                else:
                    return False
                # break
            l += 1
            r -= 1
        return True


s = "abbca"

d = Solution()
c = d.validPalindrome(s)
print(c)
