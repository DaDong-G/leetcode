# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:
    def minDepth(self, node: TreeNode):
        m_size = []
        if node is None:
            return 0
        def dfs(node, size):
            if node.left is None and node.right is None:
                m_size.append(size)
                return

            if node.left:
                dfs(node.left, size + 1)
            if node.right:
                dfs(node.right, size + 1)
        dfs(node, 1)
        return min(m_size)

# [2,null,3,null,4,null,5,null,6]
# [2,null,3,null,4,null,5,null,6]
# r = TreeNode(2)
# r.right = TreeNode(3)
# r.right.right = TreeNode(4)
# r.right.right.right = TreeNode(5)
# r.right.right.right.right = TreeNode(6)
# r.left = TreeNode(4)
# r.right = TreeNode(None)
# r.left.left = TreeNode(3)
# r.left.left.left = TreeNode(4)
# r.right.right.right = TreeNode()
s = Solution()
s.minDepth(None)
