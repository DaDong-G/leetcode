# 83.
# 删除排序链表中的重复元素给定一个已排序的链表的头head ， 删除所有重复的元素，使每个元素只出现一次 。返回已排序的链表 。
#
#
#
# 示例
# 1：
#
#
# 输入：head = [1, 1, 2]
# 输出：[1, 2]
# 示例
# 2：
#
#
# 输入：head = [1, 1, 2, 3, 3]
# 输出：[1, 2, 3]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 双指针
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        dy_head = ListNode()
        dy_head.next = head
        r = head

        while r is not None:
            l = r
            while r.next is not None and r.val == r.next.val:
                r = r.next

            r = r.next
            l.next = r

        return dy_head.next
        # while dy_head != None:
        #     print(dy_head.val)
        #     dy_head = dy_head.next


h = ListNode()
h.val = 1
h.next = ListNode(2)
h.next.next = ListNode(2)
h.next.next.next = ListNode(2)
# h.next.next.next.next = ListNode(5)

s = Solution()
s.deleteDuplicates(h)