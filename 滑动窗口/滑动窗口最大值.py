# 239. 滑动窗口最大值
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回 滑动窗口中的最大值 。

# 示例 1：
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# 示例 2：
#
# 输入：nums = [1], k = 1
# 输出：[1]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sliding-window-maximum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路 双端单调队列，保证队首到队尾是单调递减，队列中保存数组下标方便计算。
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        queue = deque()
        result = []
        left = 0
        for right in range(len(nums)):
            #  如果队列不为0 ， 或者当前元素 大于队列里面的元素， 就将queue里面的元素剔除。
            while len(queue) > 0 and nums[right] >= nums[queue[len(queue) - 1]]:
                queue.pop()
            queue.append(right)
            # 如果队列里面的队首元素 在left 的左边，说明已经在窗口外了，剔除。
            if queue[0] < left:
                queue.popleft()

            # 如果已经形成了窗口
            if right + 1 >= k:
                result.append(nums[queue[0]])
                left += 1
        return result


s = Solution()
r = s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], k = 3)
print(r)