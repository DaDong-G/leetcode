# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在两个不同下标i和j，
# 使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。
#
# 如果存在则返回 true，不存在返回 false。
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,1], k = 3, t = 0
# 输出：true
# 示例 2：
#
# 输入：nums = [1,0,1,1], k = 1, t = 2
# 输出：true
# 示例 3：
#
# 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出：false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/contains-duplicate-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 暴力解法
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t) -> bool:
        n = len(nums)
        for j in range(k):
            i = 0
            j += 1
            while j < n:
                if abs(nums[i] - nums[j]) <= t:
                    print(i, j)
                    print(nums[i], nums[j])
                    return True
                j += 1
                i += 1
        return False
