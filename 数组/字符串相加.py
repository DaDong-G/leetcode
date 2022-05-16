# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
#
# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
#
#  
#
# 示例 1：
#
# 输入：num1 = "11", num2 = "123"
# 输出："134"
# 示例 2：
#
# 输入：num1 = "456", num2 = "77"
# 输出："533"
# 示例 3：
#
# 输入：num1 = "0", num2 = "0"
# 输出："0"
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/add-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def addStrings(self, num1: str, num2: str):
        r = 0
        i = len(num1)-1
        j = len(num2)-1
        res = ""
        while i >= 0 and j >= 0:
            t = int(num1[i]) + int(num2[j]) + r
            if t >= 10:
                t = (int(num1[i]) + int(num2[j]) + r) % 10
                r = 1
            else:
                r = 0
            res = str(t) + res
            i -= 1
            j -= 1
        if i >= 0:
            while i >= 0:
                t = int(num1[i]) + r
                if t >= 10:
                    t = (int(num1[i]) + r) % 10
                    r = 1
                else:
                    r = 0
                res = str(t) + res
                i -= 1

        if j >= 0:
            while j >= 0:
                t = int(num2[j]) + r
                if t >= 10:
                    t = (int(num2[j]) + r) % 10
                    r = 1
                else:
                    r = 0
                res = str(t) + res
                j -= 1
        if r != 0:
            res = str(r) + res
        print(res)
        return res

s = Solution()
s.addStrings("6",
"501")