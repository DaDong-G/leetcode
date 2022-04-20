# 给定一个二叉树
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
#
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
class Solution:
    def connect(self, root: Node):
        if root is None:
            return []
        queue = deque()
        root.next = None
        queue.append([root])

        while queue[0]:
            node_list = queue.popleft()
            temp_list = []
            n = len(node_list)
            i = 0
            while i < n:
                node_list[i].next = node_list[i+1]
                if node_list[i].left:
                    temp_list.append(node_list[i].left)
                if node_list[i].right:
                    temp_list.append(node_list[i].right)
                i += 1

            node_list[n-1].next = None
            queue.append(temp_list)
        return root




q = Node(1)
q.left = Node(2)
q.right = Node(2)
q.left.left = Node(3)
q.left.right = Node(4)
q.right.left = Node(4)
q.right.right = Node(3)
s = Solution()
s.connect(q)

