# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
#
# 叶子节点 是指没有子节点的节点。
#
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# 输出：true
# 解释：等于目标和的根节点到叶节点路径如上图所示。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        result = []
        if root is None:
            return False

        def dfs(node, p):
            if node.left is None and node.right is None:
                if sum(p + [node.val]) == targetSum:
                    result.append(p + [node.val])

                return

            if node.left:
                dfs(node.left, p + [node.val])

            if node.right:
                dfs(node.right, p + [node.val])

        path = []
        dfs(root, path)
        if result:
            return True
        # return result
        return False



r = TreeNode(2)
r.left = TreeNode(4)
r.right = TreeNode(3)
r.left.left = TreeNode(5)
s = Solution()
d = s.hasPathSum(r,11)
print(d)