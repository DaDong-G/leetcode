# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#  
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
# 示例 2：
#
#
# 输入：head = [1,2]
# 输出：[2,1]
# 示例 3：
#
# 输入：head = []
# 输出：[]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/reverse-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 两个指针的方法
# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         pre = None
#         cur = head
#
#         while cur is not None:
#             t = cur.next
#             cur.next = pre
#             pre = cur
#             cur = t
#
#         return pre
# while pre:
#     print(pre.val)
#     pre = pre.next


# 递归的方法
class Solution(object):
    def __init__(self):
        self.s = ListNode()
        self.h = self.s

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.pase(head)
        return self.s.next

    def pase(self, head):
        if head is None:
            return head
        self.reverseList(head.next)
        t = ListNode(head.val)
        self.h.next = t
        self.h = self.h.next

        # if r:
        #     print(r.val)
        # r.next = r
        # p = reverseList(head.next);
        # head.next.next = head;
        # head.next = null;
        # return p;


one = ListNode(1)
one.next = ListNode(2)
one.next.next = ListNode(3)

s = Solution()
s.reverseList(one)
s.pase()
