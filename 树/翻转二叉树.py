# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def invertTree(self, root):
#         def dfs(root):
#             if root is None:
#                 return
#
#             # a = TreeNode()
#             t = root.left
#             root.left = root.right
#             root.right = t
#             self.invertTree(root.left)
#             self.invertTree(root.right)
#
#         r = root
#         dfs(root)
#         return r


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        print(left, right)
        root.left, root.right = right, left
        return root


q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(2)
q.left.left = TreeNode(3)
q.left.right = TreeNode(4)
q.right.left = TreeNode(4)
q.right.right = TreeNode(3)
s = Solution()


# r = s.invertTree(q)
def pr_tree(node):
    if node is None:
        return node

    l = pr_tree(node.left)
    r = pr_tree(node.right)
    print(l, r)
    print(node.val)
    return node


pr_tree(q)
