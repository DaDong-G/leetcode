# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,2,3,2]
# 输出：3
# 示例 2：
#
# 输入：nums = [0,1,0,1,0,1,99]
# 输出：99
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/single-number-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处
import collections
class Solution:
    def singleNumber(self, nums):
        freq = collections.Counter(nums)
        print(freq)
        ans = [num for num, occ in freq.items() if occ == 1][0]
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/single-number-ii/solution/zhi-chu-xian-yi-ci-de-shu-zi-ii-by-leetc-23t6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

s = Solution()
d = s.singleNumber([30000, 500, 100, 30000, 100, 30000, 100])
print(d)
