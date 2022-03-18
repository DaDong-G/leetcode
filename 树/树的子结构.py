# Definition for a binary tree node.

# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

# B是A的子结构， 即 A中有出现和B相同的结构和节点值。

# 例如:
# 给定的树 A:

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 示例 1：
#
# 输入：A = [1,2,3], B = [3,1]
# 输出：false
# 示例 2：
#
# 输入：A = [3,4,5,1,2], B = [4,1]
# 输出：true


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 先对a进行深度有限，直到 有一个与b的root节点相同的节点出现
# 对a b 同时进行深度优先遍历。

class Solution:
    def helper(self, a, b):
        # 如果 a 完了， b也完了 就是True
        if a is None and b is None:
            return True

        if b is None:
            return True

        if not a or not b:
            return False

        if a.val != b.val:
            return False
        return self.helper(a.left, b.left) and self.helper(a.right, b.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode):
        def dfs(node):
            if node is None:
                return False

            if node.val == B.val:
                if self.helper(node, B):
                    return True

            return dfs(node.left) or dfs(node.right)

        if B is None:
            return False
        return dfs(A)


p = TreeNode(10)

p.left = TreeNode(12)
p.right = TreeNode(6)

p.left.left = TreeNode(8)
p.left.right = TreeNode(3)

# p.right.left = TreeNode(6)
# p.right.right = TreeNode(7)


# p.left.left.left = TreeNode(8)
# p.left.left.right = TreeNode(9)


q = TreeNode(10)
q.left = TreeNode(12)
q.right = TreeNode(6)
q.left.left = TreeNode(8)
s= Solution()
d = s.isSubStructure(p , q)
print(d)

# [10,12,6,8,3,11]
# [10,12,6,8]

