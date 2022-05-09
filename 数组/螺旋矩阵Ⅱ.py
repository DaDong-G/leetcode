class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        dp = [ [0 for _ in range(n)] for _ in range(n)]
        top, down, left, right = 0, n - 1, 0, n - 1
        nums = 1

        while top <= down and left <= right:
            #  最上层
            for i in range(left, right + 1):
                dp[top][i] = nums
                nums += 1
                # print(i)
                # print(res)
            # 最右层
            for i in range(top + 1, down + 1):
                dp[i][right] = nums
                nums += 1

            if right > left and down > top:
                # 最左层
                for i in range(right - 1, left - 1, -1):
                    # print(i)
                    dp[down][i] = nums
                    nums += 1
                # 最右层
                for i in range(down - 1, top, -1):
                    dp[i][left] = nums
                    nums += 1
            left += 1
            right -= 1
            top += 1
            down -= 1

        return dp
s =   Solution()
s.generateMatrix(3)