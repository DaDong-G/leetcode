# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
#
#  
#
# 进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
#
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/single-number-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 示例 1：
#
# 输入：nums = [1,2,1,3,2,5]
# 输出：[3,5]
# 解释：[5, 3] 也是有效的答案。
# 示例 2：
#
# 输入：nums = [-1,0]
# 输出：[-1,0]
# 示例 3：
#
# 输入：nums = [0,1]
# 输出：[1,0]

#
class Solution:
    def singleNumber(self, nums):
        x = 0
        # 遍历后的x 就是 x1、x2 两个不相同的数的异或结果
        for i in nums:
            x ^= i
        print(x)
        # 找出最低位为1 的位置， 说明x1 或 x2 中 有一个数在这个位上值为1，另一个数在这个位上值为0。
        # 进一步拓展，就是有一类数这个位上值为1，另外一类数这个位上的值为0
        # x & -x 代表将最低位的1 取出，前面的全为0. 即 lowest_bit 一定是一个只有一个1 ，其余的全是0的数。
        if x and self.isPowerOfTwo(x):
            lowest_bit = 1
        else:
            lowest_bit = x & -x
        # print(lowest_bit)
        n1 = 0
        n2 = 0
        for num in nums:

            print(num,bin(num), lowest_bit,(num  >>  lowest_bit) ,(num  >>  lowest_bit) & 1)
            # if ((num  >>  lowest_bit) & 1) == 1:
            #     n1 ^= num
            # else:
            #     n2 ^= num
        # return n1 , n2

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        elif (n & (n - 1) == 0):
            return True
        else:
            return False


s = Solution()
d = s.singleNumber([-1638685546,-2084083624,-307525016,-930251592,-1638685546,1354460680,623522045,-1370026032,-307525016,-2084083624,-930251592,472570145,-1370026032,1063150409,160988123,1122167217,1145305475,472570145,623522045,1122167217,1354460680,1145305475])
# a = 4
print(bin(623522045),(623522045 >> 2) & 1)
# a = 8
# print(bin(a))

# print(4 ^ 0)
# print((a >> 3))
