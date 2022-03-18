# 给你一个二叉树的根节点 root ， 检查它是否轴对称。

# 输入：root = [1,2,2,3,4,4,3]
# 输出：true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 思路
# 双指针访问这个树,
# 其实类似于 判断两个树 是否是相同的

class Solution:
    def isSymmetric(self, root):
        def dfs(left, right):
            if left is None and right is None:
                return True

            if not left or not right:
                return False

            if left.val != right.val:
                return False
            print(left.val,right.val)

            dfs(left.left, right.right)
            dfs(left.right, right.left)

        return dfs(root, root)


q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(2)
q.left.left = TreeNode(3)
q.left.right = TreeNode(4)
q.right.left = TreeNode(4)
q.right.right = TreeNode(3)
s = Solution()
s.isSymmetric(q)
