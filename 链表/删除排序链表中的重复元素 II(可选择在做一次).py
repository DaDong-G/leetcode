# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return
        dy_link = ListNode()
        dy_link.next = head
        pre = dy_link
        cur = pre.next

        while cur is not None:
            f = 0
            difNode = cur
            while difNode is not None and difNode.val == cur.val:
                f += 1
                difNode = difNode.next
            # 如果大于1， 说明存在了重复的元素。
            if f > 1:
                pre.next = difNode
            # cur指向的结点没有重复出现，则将变量prev指向cur所指向的结点
            else:
                pre = cur

            cur = difNode


h = ListNode()
h.val = 1
h.next = ListNode(2)
h.next.next = ListNode(1)
h.next.next.next = ListNode(2)
h.next.next.next.next = ListNode(3)

s = Solution()
s.deleteDuplicates(h)
