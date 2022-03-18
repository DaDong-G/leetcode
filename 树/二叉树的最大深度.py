# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        m_size = []
        if root is None:
            return 0

        def dfs(node, size):
            if node.left is None and node.right is None:
                m_size.append(size)
                return
            if node.left:
                dfs(node.left, size + 1)
            if node.right:
                dfs(node.right, size + 1)
        dfs(root, 1)
        return max(m_size)



class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        # print(root.val)
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1


p = TreeNode(1)
p.left = TreeNode(2)
p.left.left = TreeNode(3)
p.right = TreeNode(4)
s = Solution()
s.maxDepth(p)
