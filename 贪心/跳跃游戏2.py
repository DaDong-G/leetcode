# 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 假设你总是可以到达数组的最后一个位置。
#
#  
#
# 示例 1:
#
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 示例 2:
#
# 输入: nums = [2,3,0,1,4]
# 输出: 2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/jump-game-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 跳跃游戏 无论如何 先把 可以跳的最远距离的列表写出来 即 num[i] + i
# [2, 3, 1, 1, 4]
# [0, 1, 2, 3, 4]
# [2, 4, 4, 4, 8]

class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        n = len(nums)
        # 跳跃次数
        count = 0
        # max_step = 0

        current = 0

        while True:
            # next = 0
            next = {}
            for i in range(nums[current]):
                next_step_index = current + i
                s = nums[next_step_index]
                if current >= n - 1:
                    return count + 1

                # next.append(nums[next_step_index] + next_step_index)
                next[nums[next_step_index] + next_step_index] = next_step_index
                print(next_step_index, s, nums[next_step_index] + next_step_index)

                # print(next_step_index,next)
                # next_step = nums[new_step] + current
                # print(new_step,next_step)
            print(max(next), next[max(next)])
            # break
            current = next[max(next)]

            # print(current)
            count += 1


            if current >= n - 1:
                return count

            # break
        # break
        # print(rightmost)


# [1,2,1,1,1]
# [0,1,2,3,4]
# [1,3,3,4,5]

a = Solution()
s = a.jump([2, 3, 1, 1, 4])
print(s)
