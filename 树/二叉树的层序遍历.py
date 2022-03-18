# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
# 示例 2：
#
# 输入：root = [1]
# 输出：[[1]]
# 示例 3：
#
# 输入：root = []
# 输出：[]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 维护一个队列即可。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        queue = []
        result = []
        if root is None:
            return []

        queue.append([root])
        while queue[0]:
            node_list = queue.pop(0)
            temp_result = []
            temp_queue = []
            for i in node_list:
                temp_result.append(i.val)
                if i.left is not None:
                    temp_queue.append(i.left)
                if i.right is not None:
                    temp_queue.append(i.right)
            queue.append(temp_queue)
            result.append(temp_result)
        return result

r = TreeNode(2)
r.left = TreeNode(4)
r.right = TreeNode(3)
r.left.left = TreeNode(5)
s = Solution()
s.levelOrder(r)





