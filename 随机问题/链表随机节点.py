# 给你一个单链表，随机选择链表的一个节点，并返回相应的节点值。每个节点 被选中的概率一样 。
# #
# # 实现 Solution 类：
# #
# # Solution(ListNode head) 使用整数数组初始化对象。
# # int getRandom() 从链表中随机选择一个节点并返回该节点的值。链表中所有节点被选中的概率相等。
# #  
# #
# 输入
# ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
# [[[1, 2, 3]], [], [], [], [], []]
# 输出
# [null, 1, 3, 2, 2, 3]
#
# 解释
# Solution solution = new Solution([1, 2, 3]);
# solution.getRandom(); // 返回 1
# solution.getRandom(); // 返回 3
# solution.getRandom(); // 返回 2
# solution.getRandom(); // 返回 2
# solution.getRandom(); // 返回 3
# // getRandom() 方法应随机返回 1、2、3中的一个，每个元素被返回的概率相等。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/linked-list-random-node
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for singly-linked list.
import random
from fractions import Fraction


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head

    def getRandom(self):
        """
        :rtype: int
        """
        shuffle = None
        cur = self.head
        count = 0
        # node, i, ans = self.head, 1, 0
        # while node:
        #     ran = random.randrange(i)
        #     if ran == i:  # 1/i 的概率选中（替换为答案）
        #         ans = node.val
        #     i += 1
        #     node = node.next
        # return ans

        while cur:
            count += 1
            ran = random.uniform(0, 1)
            if (Fraction(count, 1)) > ran:
                shuffle = cur.val
            cur = cur.next

        # print(shuffle)
        return shuffle


# print(random.randrange(2))
# head = ListNode(0)
# head.next = ListNode(1)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(3)
a = Fraction(5, 4)
print(a)
# print()
# s = Solution(head)
# s.getRandom()
# s.getRandom()
# s.getRandom()
# s.getRandom()

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
print(random.randrange(2))
