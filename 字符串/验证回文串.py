# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
#  
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 解释："amanaplanacanalpanama" 是回文串
# 示例 2:
#
# 输入: "race a car"
# 输出: false
# 解释："raceacar" 不是回文串


class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_list = []
        for i in s:
            if i.isdigit() or i.isalpha():
                s_list.append(i)

        l, r = 0,len(s_list) - 1
        while l < r:
            if s_list[l].lower() != s_list[r].lower():
                return False
            l += 1
            r -= 1
        return True



s = Solution()
d = s.isPalindrome("race a car")
print(d)
