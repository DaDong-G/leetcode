# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# [3 , a2,c]
# 栈+ 数组
# 示例 1：

# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
# 示例 2：
# s = [3,a2,c]
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
# 示例 3：
#
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
# 示例 4：
#
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"


# class Solution:
#     def decodeString(self, s: str) -> str:
#         n = len(s)
#
#         def decode(s, i):
#             number = 0
#             res = ""
#             while i < n:
#                 if s[i].isdigit():
#                     number = number * 10 + int(s[i])
#
#                 elif s[i] == '[':
#                     temp, i = decode(s, i + 1)
#                     res += temp * number
#                     number = 0
#
#                 elif s[i] == "]":
#                     return res, i
#                 else:
#                     res += s[i]
#                 i += 1
#                 # print(res)
#             return res
#         return decode(s, 0)


# 使用栈的方法
#  使用 [数字, 字符] 为数据结构 例如 [[3, 'a'], [2, 'cdd']]    a3[cdd2[b]]
#  总体按照 弹出上一层数字 * 当前的字符串。
class Solution:
    def decodeString(self, s: str):
        decode_stack = []
        number = 0
        res = ""
        # 遍历每一个字符
        for i in s:
            # 如果是左括号，需要将左括号前面的数据先进栈
            if i == "[":
                # 其实，有几层括号，就要加入多少的栈。
                decode_stack.append([number, res])
                number, res = 0, ""

            # 如果是右括号， 需要将里面的算完，加在外边
            elif i == "]":
                print(decode_stack)
                n, t = decode_stack.pop()
                # n 是上一层中的最后一个数字， t 是上一层中的字母，需要将 上一层的字母t + 上一层的数字n  * 下一层[]内的字母
                res = t + n * res

            elif i.isdigit():
                number = number * 10 + int(i)
            else:
                res += i
        return res


d = "a3[c2[b]]"
s = Solution()
f = s.decodeString(d)
print(f)
