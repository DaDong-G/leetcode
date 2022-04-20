# 给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj,
# endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。
#
# 返回这 两个区间列表的交集 。
#
# 形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b 。
#
# 两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。

# 输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]


# [[0,2],  [5,10],  [13,23], [24,25]]
# [[1,5],  [8,12],  [15,24], [25,26]]


# 输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# 示例 2：

# 输入：firstList = [[1,3],[5,9]], secondList = []
# 输出：[]
# 示例 3：
#
# 输入：firstList = [], secondList = [[4,8],[10,12]]
# 输出：[]
# 示例 4：
#
# 输入：firstList = [[1,7]], secondList = [[3,10]]
# 输出：[[3,7]]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/interval-list-intersections
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def intervalIntersection(self, firstList, secondList):
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        i = 0
        j = 0

        res = []
        while i < len(firstList) and j < len(secondList):
            f1 = firstList[i][0]
            f2 = firstList[i][1]
            s1 = secondList[j][0]
            s2 = secondList[j][1]

            if s2 >= f1 and f2 >= s1:
                res.append([max(f1, s1), min(f2, s2)])
            if s2 > f2:
                i += 1
            else:
                j += 1
        # print(res)
        return res


s = Solution()
s.intervalIntersection([[8,15]],
                       [[2, 6], [8, 10], [12, 20]])
# s.intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]])

# [[8,15]]
# [[2,6],[8,10],[12,20]]

# [[4,11]]
# [[1,2],[8,11],[12,13],[14,15],[17,19]]