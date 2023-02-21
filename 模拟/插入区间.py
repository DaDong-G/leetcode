# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
#  
# 示例 1：
#
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
# 示例 2：
#
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
# 示例 3：
#
# 输入：intervals = [], newInterval = [5,7]
# 输出：[[5,7]]
# 示例 4：
#
# 输入：intervals = [[1,5]], newInterval = [2,3]
# 输出：[[1,5]]
# 示例 5：
#
# 输入：intervals = [[1,5]], newInterval = [2,7]
# 输出：[[1,7]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/insert-interval
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return newInterval
        res = []
        l, r = newInterval
        f = False
        for i, j in intervals:
            if l > j:
                res.append([i, j])
            elif i > r:
                if f:
                    res.append([l, r])
                    f = False
                res.append([i, j])

            else:
                l = min(i, l)
                r = max(r, j)
                f = True
                print(l, r)
        if f:
            res.append([l, r])

        if [l, r] == newInterval and [l, r] not in res:
            res.append([l, r])
        res.sort()
        return res


s = Solution()
d = s.insert([[1, 5]], [0, 0])
print(d)
# s = Solution()
# s.insert([], [1, 3])
