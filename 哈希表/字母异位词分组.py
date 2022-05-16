# 49.# 字母异位词分组
# 给你一个字符串数组，请你将 字母异位词组合在一起。可以按任意顺序返回结果列表。
# 字母异位词是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
# 示例
# 1:输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
# 示例
# 2:输入: strs = [""]
# 输出: [[""]]
# 示例
# 3:
# 输入: strs = ["a"]
# 输出: [["a"]]
# 思路
# map = [Counter({'e': 1, 'a': 1, 't': 1}), Counter({'t': 1, 'a': 1, 'n': 1}), Counter({'b': 1, 'a': 1, 't': 1})] 、
# map 代表着一个哈希表，只要出现的字母数量一样，说明就是字母异位词分组,map有几个counter，就可以分成几组
from collections import Counter
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = []
        res = []
        for i in strs:
            p = Counter(i)
            if p not in map:
                map.append(Counter(i))
                res.append([i])
            else:
                res[map.index(Counter(i))].append(i)
        print(res)
        print(map)

s = Solution()
s.groupAnagrams( ["eat", "tea", "tan", "ate", "nat", "bat"])