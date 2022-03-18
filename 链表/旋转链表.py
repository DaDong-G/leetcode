# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]

# 输入：head = [0,1,2], k = 1
# 输出：[2,0,1]
# (n - 1) - (k % n)个节点
# [1,2], k = 1
# 输出 [2, 1]
# [1,2,3,4,5,6] k = 10 ,10 % 6 = 4
# [1,2,3,4,5]   k = 10 ,10 % 5 = 0
# [1,2,3,4] ,   k = 10 ,10 % 4 = 2
# [1,2,3] ,     k = 10 ,10 % 3 = 1

# [1,2,3,4,5,6] k = 9 ,9 % 6 = 3
# [1,2,3,4,5]   k = 9 ,9 % 5 = 4
# [1,2,3,4] ,   k = 9 ,9 % 4 = 1
# [1,2,3] ,     k = 9 ,9 % 3 = 0

# n - k % n
# [1,2,3,4,5]   k = 2
# [1,2,3]       k = 2


# 这道题的想法很重要，关键点在于 找到旋转后的头节点， 而  n - k 就是头节点。之前陷入了误区。
# 第一步 ： 计算出总长度
# 第二部 ： 根据总长度计算出新的头节点位置。 n - k % n
# 第三步 ： 两个指针，一个前移到新的头节点节点， 另一个前移到头节点的前一个指针。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k: int):
        if head is None:
            return None

        n = 1
        r = head
        # 用r.next 方便将链表形成一个回环。
        while r.next is not None:
            n += 1
            r = r.next

        r.next = head
        offset = n - k % n
        if offset == 0:
            return head

        while offset:
            r = r.next
            offset -= 1

        res = r.next
        r.next = None

        return res






        # l, r = ListNode(), ListNode()
        # c = head
        # while c.next != head:
        #     if k <=



        # tail_head = ListNode()
        # t = tail_head
        # h = head
        # pre_head = ListNode()
        # p = pre_head
        # # if count % 2 != 0:
        # #     k = k + 1
        # #
        # for i in range(0, count):
        #     # print(i)
        #     if i <= k:
        #         t.next = ListNode()
        #         t = t.next
        #         t.val = h.val
        #     else:
        #         p.next = ListNode()
        #         p = p.next
        #         p.val = h.val
        #
        #     h = h.next
        #
        # p.next = tail_head.next
        #
        # pre_head = pre_head.next
        # while pre_head != None:
        #     print(pre_head.val)
        #     pre_head = pre_head.next

        # return pre_head.next





# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         if k == 0 or not head or not head.next:
#             return head
#
#         n = 1
#         cur = head
#         while cur.next:
#             cur = cur.next
#             n += 1
#
#         if (add := n - k % n) == n:
#             return head
#         print(add)
#         cur.next = head
#         while add:
#             cur = cur.next
#             add -= 1
#
#         ret = cur.next
#         cur.next = None
#         return ret
#
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
s = Solution()
d = s.rotateRight(a, 2)

while d != None:
    print(d.val)
    d = d.next