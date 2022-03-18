class Solution:
    def mySqrt(self, x: int):
        a = x
        for i in range(20):
            x = x - ((x*x*x*x - a) / (4 * (x*x*x)))
        print(x)
        return x


s = Solution()
s.mySqrt(16)
