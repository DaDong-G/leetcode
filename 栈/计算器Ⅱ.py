# 给你一个字符串表达式s ，请你实现一个基本计算器来计算并返回它的值。
#
# 整数除法仅保留整数部分。
#
# 示例 1：
#
# 输入：s = "3+2*2"
# 输出：7
# 示例 2：
#
# 输入：s = " 3/2 "
# 输出：1
# 示例 3：
#
# 输入：s = " 3+5 / 2 "
# 输出：5
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/basic-calculator-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 双栈解法
# 事实上，我提供这套解决方案不仅仅能解决只有 + - ( )（224. 基本计算器） 或者 + - * /(227. 基本计算器 II) 的表达式问题，还能解决 + - * / ^ % ( ) 的完全表达式问题。
#
# 甚至支持自定义运算符，只要在运算优先级上进行维护即可。
#
# 对于「表达式计算」这一类问题，你都可以使用这套思路进行解决。我十分建议你加强理解这套处理逻辑。
# 表达式可以先将 (- 替换 (0- 方便计算
# 对于「任何表达式」而言，我们都使用两个栈 nums 和 ops：
#
# nums ： 存放所有的数字
# ops ：存放所有的数字以外的操作
# 然后从前往后做，对遍历到的字符做分情况讨论：
#
# 空格 : 跳过
# ( : 直接加入 ops 中，等待与之匹配的 )
# ) : 使用现有的 nums 和 ops 进行计算，直到遇到左边最近的一个左括号为止，计算结果放到 nums
# 数字 : 从当前位置开始继续往后取，将整一个连续数字整体取出，加入 nums
# + - * / ^ % : 需要将操作放入 ops 中。在放入之前先把栈内可以算的都算掉（只有「栈内运算符」比「当前运算符」优先级高/同等，才进行运算），使用现有的 nums 和 ops 进行计算，直到没有操作或者遇到左括号，计算结果放到 nums
# 我们可以通过 🌰 来理解 只有「栈内运算符」比「当前运算符」优先级高/同等，才进行运算 是什么意思：
#
# 因为我们是从前往后做的，假设我们当前已经扫描到 2 + 1 了（此时栈内的操作为 + ）。
#
# 如果后面出现的 + 2 或者 - 1 的话，满足「栈内运算符」比「当前运算符」优先级高/同等，可以将 2 + 1 算掉，把结果放到 nums 中；
# 如果后面出现的是 * 2 或者 / 1 的话，不满足「栈内运算符」比「当前运算符」优先级高/同等，这时候不能计算 2 + 1。
# 一些细节：
#
# 由于第一个数可能是负数，为了减少边界判断。一个小技巧是先往 nums 添加一个 0
# 为防止 () 内出现的首个字符为运算符，将所有的空格去掉，并将 (- 替换为 (0-，(+ 替换为 (0+（当然也可以不进行这样的预处理，将这个处理逻辑放到循环里去做）
# 从理论上分析，nums 最好存放的是 long，而不是 int。因为可能存在 大数 + 大数 + 大数 + … - 大数 - 大数 的表达式导致中间结果溢出，最终答案不溢出的情况
#
# 作者：AC_OIer
# 链接：https://leetcode-cn.com/problems/basic-calculator-ii/solution/shi-yong-shuang-zhan-jie-jue-jiu-ji-biao-c65k/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# class Solution:
#     op_priority = {'+': 0, '-': 0, '*': 1, '/': 1, '%': 1, '^': 2}
#
#     def calculate(self, s: str):
#         s = "(" + s.replace(" ", "").replace("(-", "(0-") + ")"
#         n = len(s)
#         # operators & numbers
#         op_stack, num_stack = [], []
#
#         i = 0
#         while i < n:
#             c = s[i]
#             i += 1
#
#             if c.isdigit():  # a number
#                 num = int(c)
#
#                 while i < n and s[i].isdigit():
#                     num = num * 10 + int(s[i])
#                     i += 1
#                 num_stack.append(num)
#         # print(num_stack)
#
#             elif c == '(':  # (
#                 op_stack.append(c)
#             elif c == ')':  # calculate until see '('
#                 while op_stack and op_stack[-1] != '(':
#                     self.calc(num_stack, op_stack)
#                 op_stack.pop()
#
#             else:
#                 print(c,op_stack)
#                 while op_stack and op_stack[-1] != '(':
#                     prev_op = op_stack[-1]
#                     print(prev_op, op_stack, c)
#                     if self.op_priority[prev_op] < self.op_priority[c]:
#                         break
#                     self.calc(num_stack, op_stack)
#                 op_stack.append(c)
#
#     def calc(self, num_stack: list, op_stack: list) -> None:
#         op, y, x = op_stack.pop(), num_stack.pop(), num_stack.pop() if num_stack else 0
#         ans = 0
#         if op == '+':
#             ans = x + y
#         elif op == '-':
#             ans = x - y
#         elif op == '*':
#             ans = x * y
#         elif op == '/':
#             ans = x / y
#         elif op == '%':
#             ans = x % y
#         elif op == '^':
#             ans = pow(x, y)
#         num_stack.append(int(ans))


# a = [1,2,3]
# c,d = a.pop() , a.pop()
# print(c,d)
# c = 3
# d = 2
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        s = s.replace("(-","(0-")
        s = "(" + s + ")"
        nums_stack = []
        op_stack = []
        n = len(s)
        op_priority = {"+": 1, "-": 1, "*": 2, "/": 2}
        i = 0
        while i < n:
            c = s[i]
            i += 1
            # 如果c 是数字，将一整串数字拼起来加入num栈
            if c.isdigit():
                num = int(c)
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                nums_stack.append(num)
            elif c == "(":
                op_stack.append(c)
            # 如果是又括号，就把括号里面的所有的先算出来，保存到num栈
            elif c == ")":
                while op_stack and op_stack[-1] != "(":
                    self.cal(op_stack, nums_stack)
                op_stack.pop()
            else:

                while op_stack and op_stack[-1] != "(":
                    pre_op = op_stack[-1]
                    # 如果新的符号优先级小于于栈内的， 可以将栈内的先算完。 比如 3 + 2 - 1 可以先将里面的 3 + 2算了
                    # 如果是 3 + 2 / 2 则不能先算3 + 2, 需要把/ 入栈。
                    # if op_priority[pre_op] < op_priority[c]:
                    if op_priority[pre_op] < op_priority[c]:
                        break

                    self.cal(op_stack, nums_stack)

                op_stack.append(c)

        return nums_stack[0]

    def cal(self, op_stack, num_stack):
        y = num_stack.pop()
        x = num_stack.pop()
        op = op_stack.pop()
        ans = 0
        if op == "+":
            ans = x + y
        if op == "-":
            ans = x - y
        if op == "*":
            ans = x * y
        if op == "/":
            ans = x / y
        num_stack.append(int(ans))


s = "3+ 2 * 2"
a = Solution()
d = a.calculate(s)
print(d)
