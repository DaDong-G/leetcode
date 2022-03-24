# DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。
#
# 例如，"ACGAATTCCG" 是一个 DNA序列 。
# 在研究 DNA 时，识别 DNA 中的重复序列非常有用。
#
# 给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/repeated-dna-sequences
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 示例 1：
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
# 示例 2：
#
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]

# 重点理解题目意思：      题目的意思是编写一个函数来查找子串，这个子串长度为10，在原字符串中出现超过一次。
from collections import Counter
class Solution:
    def findRepeatedDnaSequences(self, s: str):
        i = 0
        n = len(s)
        r_hash = Counter()
        r = set()
        while i + 10 <= n:
            r_hash[s[i:i+10]] += 1
            if r_hash[s[i:i+10]] > 1:
                r.add(s[i:i+10])
            i += 1
        # for i, v in r_hash.items():
        #     if v > 1:
        #         r.append(i)
        return list(r)

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

d = Solution()
f = d.findRepeatedDnaSequences(s)
print(f)