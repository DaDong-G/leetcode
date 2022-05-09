# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，
# 并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
#  
#
# 示例 1：
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2：
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-intervals
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        min_num = intervals[0][0]
        max_num = intervals[0][1]
        if len(intervals) == 1:
            return [[min_num,max_num]]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > max_num and intervals[i][1] >= max_num:
                res.append([min_num, max_num])
                min_num = intervals[i][0]
                max_num = intervals[i][1]
                continue

            min_num = min(min_num, intervals[i][0])
            max_num = max(max_num, intervals[i][1])

        if intervals[-1][0] > max_num and intervals[-1][1] >= max_num:
            res.append([min_num, max_num])
        else:
            min_num = min(min_num, intervals[-1][0])
            max_num = max(max_num, intervals[-1][1])
            res.append([min_num, max_num])
        print(res)

        return res


s = Solution()
s.merge([[1,4],[0,0]])
