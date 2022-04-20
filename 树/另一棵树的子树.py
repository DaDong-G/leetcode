# 给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。
#
# 二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。
#
#  
#
# 示例 1：
#
#
# 输入：root = [3,4,5,1,2], subRoot = [4,1,2]
# 输出：true
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subtree-of-another-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode):
        res = []

        def dfs(r: TreeNode, s: TreeNode):
            if r.val == s.val:
                res.append(self.helper(r, s))

            if r.left:
                dfs(r.left, s)

            if r.right:
                dfs(r.right, s)

        dfs(root, subRoot)
        print(res)
        if True in res:
            return True
        return False
            # return res[0]

        # return res

    def helper(self, root: TreeNode, subRoot: TreeNode):

        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False
        # print(root.val,subRoot.val)
        if root.val != subRoot.val:
            return False

        return self.helper(root.left, subRoot.left) and self.helper(root.right, subRoot.right)


p = TreeNode(1)
p.left = TreeNode(1)
# p.right = TreeNode(5)
# p.left.left = TreeNode(1)
# p.left.right = TreeNode(2)

q = TreeNode(1)
# q.left = TreeNode(1)
# q.right = TreeNode(2)
# q.left.left = TreeNode(8)
s = Solution()
d = s.isSubtree(p, q)
print(d)