# 844. 比较含退格的字符串
# 给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。
#
# 注意：如果对空文本输入退格字符，文本继续为空。
#
#  
#
# 示例 1：
#
# 输入：s = "ab#c", t = "ad#c"
# 输出：true
# 解释：s 和 t 都会变成 "ac"。
# 示例 2：
#
# 输入：s = "ab##", t = "c#d#"
# 输出：true
# 解释：s 和 t 都会变成 ""。
# 示例 3：
#
# 输入：s = "a#c", t = "b"
# 输出：false
# 解释：s 会变成 "c"，但 t 仍然是 "b"。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/backspace-string-compare
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 双指针方法
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         i = len(s) - 1
#         j = len(t) - 1
#
#         while i >= 0 or j >= 0:
#             sk_i = 0
#             sk_j = 0
#
#             while i >= 0:
#                 # 如果 s[i] == # ， 那么就把 sk_i + 1
#                 if s[i] == "#":
#                     sk_i += 1
#                     i -= 1
#                 # 如果 sk_i > 0 说明之前有# 出现，这个字符是没有用的，就往前移动。
#                 elif sk_i > 0:
#                     sk_i -= 1
#                     i -= 1
#                 else:
#                     break
#
#             while j >= 0:
#                 if t[j] == "#":
#                     sk_j += 1
#                     j -= 1
#
#                 elif sk_j > 0:
#                     sk_j -= 1
#                     j -= 1
#                 else:
#                     break
#             if i >= 0 and j >= 0:
#                 if s[i] != t[j]:
#                     print(i, j)
#                     return False
#             #
#             i -= 1
#             j -= 1
#         # print(i,j)
#         if i != j:
#             return False
#         return True


# 方法二 使用栈
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s)
        j = len(t)
        i_stack = []
        j_stack = []
        for i in range(i):
            if s[i] != "#":
                i_stack.append(s[i])
            elif s[i] == "#" and len(i_stack) == 0:
                continue
            else:
                i_stack.pop()

        for i in range(j):

            if t[i] != "#":
                j_stack.append(t[i])

            elif t[i] == "#" and len(j_stack) == 0:
                continue
            else:
                j_stack.pop()

        if j_stack == i_stack:
            return True
        return False
s = Solution()
# d = s.backspaceCompare("a##cab##", "a##c")
d = s.backspaceCompare("bbbextm", "bbb#extm")

print(d)