# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
#
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
#
# 示例1:
#
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
# 示例 2:
#
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
# 示例 3:
#
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/word-pattern
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str_list = s.split(" ")
        p = len(str_list)
        n = len(pattern)
        if p != n:
            return False
        h1 = {}  # {"a":"dog",b:"dog"}
        h2 = {}  # {"dog":"a","dog":"b"}
        for i in range(p):
            if pattern[i] not in h1 and str_list[i] not in h2:
                h1[pattern[i]] = str_list[i]
                h2[str_list[i]] = pattern[i]
            if not (pattern[i] in h1 and str_list[i] in h2 and h1[pattern[i]] == str_list[i] and h2[str_list[i]] ==
                    pattern[i]):
                return False
        return True


s = Solution()
d = s.wordPattern("abba", "dog dog ss dog")
print(d)
