# 给你一个长度为
# n的整数数组nums和一个目标值target。请你从nums中选出三个整数，使它们的和与target最接近。 返回这三个数的和。
#
# 假定每组输入只存在恰好一个解。
# 示例1：
#

[-1, 2, 1, -4]
[-4, -1, 1, 2]


# 输入：nums = [-1, 2, 1, -4], target = 1
# 输出：2
# 解释：与target最接近的和是2(-1 + 2 + 1 = 2) 。
# 示例
# 2：
#
# 输入：nums = [0, 0, 0], target = 1
# 输出：0
#
# 提示：
#
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        min_r = 9999
        r = 0
        for i in range(n - 2):
            j, k = i + 1, n - 1
            # print(i)
            while True:

                if j >= k:
                    break

                t = nums[i] + nums[k] + nums[j]
                # print(i, j, k , "       " , t)
                if abs(target - t) < abs(min_r):
                    # print(min_r)
                    min_r = target - t
                    r = t

                if t > target:
                    k -= 1
                else:
                    j += 1

        return r


s = Solution()
d = s.threeSumClosest([-1,2,1,-4], 1)
print(d)
