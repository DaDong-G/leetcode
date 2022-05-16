# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

# 示例：
#
# 输入：S = "ababcbaca defegde hijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/partition-labels
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# 1. 找到当前索引i 字符在字符串中的最后一个字符索引 j , 用max_n 保存下来最大的
# 2. 遍历i 到 j 看看这其中的字符有没有比  用max_n 大的，如果有就把用max_n替换了。
# 3. 遍历完了一轮就代表出现了一个可以分割的部分。
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        i = 0
        n = len(s)
        res = []
        while i < n:
            max_index = s.rfind(s[i])
            j = i
            # for j in range(i, max_index):
            while j < max_index:
                if s.rfind(s[j]) > max_index:
                    max_index = s.rfind(s[j])
                    # print(max_index)
                j += 1
            res.append(max_index - i + 1)
            i = max_index + 1
        return res
        # print(res)


s = Solution()
s.partitionLabels("qiejxqfnqceocmy")
