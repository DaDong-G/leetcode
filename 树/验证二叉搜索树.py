# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 有效 二叉搜索树定义如下：
#
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/validate-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 按层序遍历
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        queue = []
        if root is None:
            return False
        queue.append(root)
        while queue:
            n = queue.pop(0)
            if n.left:
                if n.left.val < n.val:
                    queue.append(n.left)
                else:
                    return False
            if n.right:
                if n.right.val > n.val:
                    print(n.right.val , n.val)
                    queue.append(n.right)
                else:
                    return False
        return True
# 思路

# 需要设置一个上限值，一个下限值，每次递归的时候进行更新。
# 注意边界问题，如果 [2,2,2] 返回的是False
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if node is None:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False
            # 左半个树,如果每一个节点都满足, 这里的lower 和 upper 每次都在变换，很巧妙。
            if helper(node.left, lower=lower,upper=val) is False:
                return False

            if helper(node.right, lower=val,upper=upper) is False:
                return False
            # 右半个树，如果每一个节点都满足
            # if:
            #     return True
            return True
            # if not helper(node.right, val, upper):
            #     return False
            # if not helper(node.left, lower, val):
            #     return False
            # return True


        return helper(root)


q = TreeNode(2)
q.left = TreeNode(2)
q.right = TreeNode(2)
# q.right.left = TreeNode(3)
# q.right.right = TreeNode(7)
s = Solution()
e = s.isValidBST(q)
print(e)
