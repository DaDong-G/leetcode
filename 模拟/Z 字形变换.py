# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
#  
#
# 示例 1：
#
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"


# 示例 2：
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
# 解释：
# P     I     N
# A   L S   I G
# Y A   H R
# P     I
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/zigzag-conversion
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# r + r - 2 = 2r - 2  | 1 + r - 2 = r - 1

# P      I
# A    S I
# Y   R  G
# P H    I
# A      N
class Solution(object):
    def convert(self, s, r):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if r == 1 or r >= n:
            return s

        t = 2 * r - 2   

        # gap = 1 + r - 2 == r - 1
        # 中间的间隔
        gap = r - 1
        # 从左到右的宽度
        c = ((n // t) + 1) * gap

        dp = [["" for _ in range(c)] for _ in range(r)]
        # x 代表行
        x = 0
        # y 代表列
        y = 0
        for i, ch in enumerate(s):
            dp[x][y] = ch
            # 这里是关键
            if i % t < r - 1:  # 4
                # 向下移动
                x += 1
            else:
                # 向右上移动
                x -= 1
                y += 1

        res = ""
        for i in dp:
            for j in i:
                if j != "":
                    res += j
            # print(i, ch)
        return res


    # for i in range(c):
    #     for j in range(r):
    #         # print(j, i)
    #         if k < n:
    #             if k % t < r - 1:
    #                 print(k, t)
    #                 dp[j][i] = s[k]
    #         else:
    #             dp[j][i + 1] = s[k]
    #         k += 1

    # print(dp)


s = Solution()
s.convert("PAY", 4)
# 方法一：利用二维矩阵模拟
# 设 nn 为字符串 ss 的长度，r=\textit{numRows}r=numRows。对于 r=1r=1（只有一行）或者 r\ge nr≥n（只有一列）的情况，答案与 ss 相同，我们可以直接返回 ss。对于其余情况，考虑创建一个二维矩阵，然后在矩阵上按 Z 字形填写字符串 ss，最后逐行扫描矩阵中的非空字符，组成答案。
#
# 根据题意，当我们在矩阵上填写字符时，会向下填写 rr 个字符，然后向右上继续填写 r-2r−2 个字符，最后回到第一行，因此 Z 字形变换的周期 t=r+r-2=2r-2t=r+r−2=2r−2，每个周期会占用矩阵上的 1+r-2=r-11+r−2=r−1 列。
#
# 因此我们有 \Big\lceil\dfrac{n}{t}\Big\rceil⌈
# t
# n
# ​
#  ⌉ 个周期（最后一个周期视作完整周期），乘上每个周期的列数，得到矩阵的列数 c=\Big\lceil\dfrac{n}{t}\Big\rceil\cdot(r-1)c=⌈
# t
# n
# ​
#  ⌉⋅(r−1)。
#
# 创建一个 rr 行 cc 列的矩阵，然后遍历字符串 ss 并按 Z 字形填写。具体来说，设当前填写的位置为 (x,y)(x,y)，即矩阵的 xx 行 yy 列。初始 (x,y)=(0,0)(x,y)=(0,0)，即矩阵左上角。若当前字符下标 ii 满足 i\bmod t<r-1imodt<r−1，则向下移动，否则向右上移动。
#
# 填写完成后，逐行扫描矩阵中的非空字符，组成答案。
#
# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/zigzag-conversion/solution/z-zi-xing-bian-huan-by-leetcode-solution-4n3u/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
