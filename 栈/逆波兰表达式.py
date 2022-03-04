class Solution:
    def evalRPN(self, tokens):

        stack = []
        #  减法 除法 都是栈底下的 在前面
        for token in tokens:
            try:
                num = int(token)
            except:
                n2 = stack.pop()
                n1 = stack.pop()

                if token == "+":
                    num = n2 + n1

                elif token == "*":
                    num = n2 * n1

                elif token == "/":
                    num = int(n1 / n2)

                else:
                    num = int(n1 - n2)

            finally:
                stack.append(num)

        return num
a = Solution()
n = a.evalRPN(["4","13","5","/","+"])
print(n)