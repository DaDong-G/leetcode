# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#
#  
# 示例 1：
#
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
# 示例 2：
#
# 输入：nums = [0]
# 输出：[[],[0]]
#

# 输入 nums = [1,1,2]
# 输出: [1, 1, 2],[1, 2, 1],[2, 1, 1]
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subsets-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 同一层树枝不可以重复
# 同一枝树枝不能重复
class Solution:
    def subsetsWithDup(self, nums):
        res = []  # 存放符合条件结果的集合
        path = []  # 用来存放符合条件结果

        def backtrack(nums, startIndex):
            res.append(path[:])
            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:  # 我们要对同一树层使用过的元素进行跳过
                    continue
                path.append(nums[i])
                backtrack(nums, i + 1)  # 递归
                path.pop()  # 回溯

        nums = sorted(nums)  # 去重需要排序
        backtrack(nums, 0)
        return res


nums = [4, 4, 4, 1, 4]
s = Solution()
d = s.subsetsWithDup(nums)
print(d)
