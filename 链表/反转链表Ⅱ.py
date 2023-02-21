# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
# 示例 2：
#
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/reverse-linked-list-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        cur = head
        c = 1
        while cur:
            c += 1
            print(cur.val)
            if cur.val == 2:
                cur = head
                while True:

            cur = cur.next


one = ListNode(1)
one.next = ListNode(2)
one.next.next = ListNode(3)
one.next.next.next = ListNode(4)
one.next.next.next.next = ListNode(5)
one.next.next.next.next.next = ListNode(6)
s = Solution()
s.reverseBetween(one, 2, 4)
