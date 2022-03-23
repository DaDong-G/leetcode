# 给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
#
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。
# 示例 1：
#
# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
# 示例 2：
#
# 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# 输出：[]
# 示例 3：
#
# 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# 输出：[6,9,12]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import Counter


# 方法一 ： 1. 使用两个hash ,{'word': 2, 'good': 1, 'best': 1}, {'word': 0, 'good': 0, 'best': 0}
#          2. 每次移动1位的长度，然后在遍历words，然后判断两个hash的值是否一致。


# 方法二： 优化方法一，每次移动 one_word 的长度。
class Solution:
    def findSubstring(self, s: str, words):
        if not s or not words:
            return []
        word_fre = Counter(words)
        one_word_len = len(words[0])
        all_word_len = len(words) * one_word_len
        str_len = len(s)
        # i = 0
        r = []
        for f in range(one_word_len):
            i = f
            while i + all_word_len <= str_len:
                current_word_free = Counter()
                j, k = 0, one_word_len
                for _ in words:
                    # s[i + j : i + k] 是从i开始，一个单词的长度
                    w = s[i + j: i + k]
                    # print(w)
                    if w in words:
                        if current_word_free[w] > word_fre[w]:
                            break
                        else:
                            current_word_free[w] += 1
                    if w not in words:
                        break
                    # print(s[i + j: i + k])
                    j += one_word_len
                    k += one_word_len
                if current_word_free == word_fre:
                    r.append(i)
                # print(i)
                i += one_word_len
        print(r)
        return r

# 方法三 使用滑动窗口，这个窗口是可变的，如果超出去了，左边的就增加。
class Solution:
    def findSubstring(self, s: str, words):
        if not s or not words:
            return []
        word_fre = Counter(words)
        one_word_len = len(words[0])
        all_word_len = len(words)
        str_len = len(s)
        r = []
        for f in range(one_word_len):
            i, j = f, f
            k = 0
            current_word_free = Counter()
            while i + one_word_len <= str_len:
                w = s[j: j + one_word_len]
                j += one_word_len
                # 如果单词不在 words 列表里面，直接移到最右边
                if w not in word_fre:
                    i = j
                    current_word_free.clear()
                    k = 0
                else:
                    current_word_free[w] += 1
                    k += 1
                    # 如果单词超出，就移动最左边的单词，往右移动一个。
                    while current_word_free[w] > word_fre[w]:
                        left_word = s[i:i + one_word_len]
                        current_word_free[left_word] -= 1
                        k -= 1
                        i += one_word_len
                    if k == all_word_len:
                        r.append(i)
        return r


st = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo", "barr", "wing", "ding", "wing"]
s = Solution()
s.findSubstring(st, words)
