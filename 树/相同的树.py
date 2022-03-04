# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。



# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 深度优先
class Solution:
    def isSameTree(self, p, q):
        def dfs(p, q):
            if p is None and q is None:
                return True

            if not p or not q:
                return False
            if p.val != q.val:
                return False

            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)



p = TreeNode(1)
p.left = TreeNode(2)
# p.left.left = TreeNode(3)

q = TreeNode(1)
q.right = TreeNode(3)


s = Solution()
d = s.isSameTree(p , q)
print(d)
