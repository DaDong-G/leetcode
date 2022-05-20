# def getNext(p):
#     """
#     p为模式串
#     返回next数组，即部分匹配表
#     """
#     nex = [0] * (len(p) + 1)
#     nex[0] = -1
#     i = 0
#     j = -1
#     while i < len(p):
#         if j == -1 or p[i] == p[j]:
#             i += 1
#             j += 1
#             nex[i] = j  # 这是最大的不同：记录next[i]
#         else:
#             j = nex[j]
#     print(nex)
#     return nex
#
#
# def KMP(s, p):
#     """
#     s为主串
#     p为模式串
#     如果t里有p，返回打头下标
#     """
#     nex = getNext(p)
#     i = 0
#     j = 0  # 分别是s和p的指针
#     while i < len(s) and j < len(p):
#         if j == -1 or s[i] == p[j]:  # j==-1是由于j=next[j]产生
#             i += 1
#             j += 1
#         else:
#             j = nex[j]
#
#     if j == len(p):  # j走到了末尾，说明匹配到了
#         return i - j
#     else:
#         return -1
class Solution:
    def longestPrefix(self, s: str) -> str:

        n = len(s)
        pi = [0] * n

        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:  # 当前位置s[i]与s[j]不等
                j = pi[j - 1]  # j指向之前位置，s[i]与s[j]继续比较

            if s[i] == s[j]:  # s[i]与s[j]相等，j+1，指向后一位
                j += 1

            pi[i] = j
        print(pi)
        return s[:pi[-1]]


# s = getNext("abab")
c = Solution()
f = c.longestPrefix("ababd")
print(f)

# [-1,0,0,0,0]