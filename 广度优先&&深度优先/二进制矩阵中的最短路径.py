# 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。
#
# 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：
#
# 路径途经的所有单元格都的值都是 0 。
# 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
# 畅通路径的长度 是该路径途经的单元格总数。
#
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shortest-path-in-binary-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。、


# 广度优先遍历
direct = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] != 0:
            return -1
        length = len(grid)
        if length == 1:
            return 1

        queue = deque()
        queue.append([(0, 0)])
        x = len(grid)
        y = len(grid[0])

        duplicate = set()
        duplicate.add((0, 0))
        path = 1
        while queue[0]:
            node_list = queue.popleft()
            temp_node_list = []
            for node in node_list:
                i = node[0]
                j = node[1]
                for d in direct:
                    n_x = i + d[0]
                    n_y = j + d[1]
                    # 如果 x 超出了边界，不执行
                    if n_x < 0 or n_x >= x:
                        continue
                    # 如果 y 超出了边界， 不执行
                    elif n_y < 0 or n_y >= y:
                        continue
                    # 如果节点已经访问过，不执行
                    elif (n_x, n_y) in duplicate:
                        continue
                    # 如果节点值等于1 不执行
                    elif grid[n_x][n_y] == 1:
                        continue

                    elif n_x == x - 1 and n_y == y - 1:
                        return path + 1
                    temp_node_list.append((i + d[0], j + d[1]))
                    duplicate.add((i + d[0], j + d[1]))
            path += 1
            queue.append(temp_node_list)

        if (x - 1, y - 1) not in duplicate:
            return -1
        return path



grid = [[0, 1],
        [1, 0]]
# grid = [[0,0,0],
#         [1,1,0],
#         [1,1,1]]
s = Solution()
d = s.shortestPathBinaryMatrix(grid)
print(d)
# from collections import deque
#
# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         if grid[0][0] != 0:
#             return -1
#         length = len(grid)
#         if length == 1:
#             return 1
#         que = deque()
#         visited = {}
#         que.appendleft((0,0))
#         visited[(0,0)] = True
#         start = 1
#         while que:
#             for _ in range(len(que)):
#                 ind, con = que.pop()
#                 for pos_h, pos_v in [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]:
#                     new_ind = ind + pos_h
#                     new_con = con + pos_v
#                     if 0 <= new_ind < length and 0 <= new_con < length and grid[new_ind][new_con] == 0 and not visited.get((new_ind, new_con)):
#                         if new_ind == length - 1 and new_con == length - 1:
#                             return start + 1
#                         que.appendleft((new_ind, new_con))
#                         visited[(new_ind, new_con)] = True
#             start += 1
#         return -1

