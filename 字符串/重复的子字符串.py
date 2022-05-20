class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        print(s + s)
        print((s + s).find(s, 1) != len(s))


s = Solution()
s.repeatedSubstringPattern("abab")
