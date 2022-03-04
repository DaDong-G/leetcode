class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")

        s = s.replace("(-","(0-")

        if s[0] == "-":
            s = "0" + s
        s = "(" + s + ")"
        print(s)
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
                    print(op_stack, nums_stack)
                    self.cal(op_stack, nums_stack)
                    print(op_stack, nums_stack)
                op_stack.pop()
                print(op_stack, nums_stack)
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
        print(op_stack, nums_stack, i,n)
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
            print(x , y ,ans)
        if op == "*":
            ans = x * y
        if op == "/":
            ans = x / y
        num_stack.append(int(ans))

s = "1-(-2)"
d = Solution()
f = d.calculate(s)
print(f)
