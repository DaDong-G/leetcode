# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
# 0 , 1 , 1, 2, 3, 5,8,13
# f(n) = f(n - 1) + f(n - 2)
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
# class Solution:
#     def fib(self, n: int) -> int:
#         a, b = 0, 1
#         for _ in range(n):
#             a, b = b, a + b
#         return a % 1000000007


s = Solution()
d = s.fib(3)
print(d)
