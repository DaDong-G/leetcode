# 实现RandomizedSet 类：
#
# RandomizedSet() 初始化 RandomizedSet 对象
# bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
# bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
# int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
# 你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。


# 示例：
#
# 输入
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# 输出
# [null, true, false, true, 2, true, false, 2]
#
# 解释
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
# randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
# randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
# randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
# randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
# randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
# randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/insert-delete-getrandom-o1
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import random

class RandomizedSet(object):

    def __init__(self):
        self.obj = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.obj:
            self.obj.append(val)
            return True
        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.obj:
            self.obj.remove(val)
            return True
        return False

    def getRandom(self):
        """
        :rtype: int
        """
        # count = 0
        res = None
        for i, v in enumerate(self.obj):
            r = random.randrange(i + 1)
            if r == i:
                res = v
        return random.choice(self.obj)





# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
print(param_1)
param_2 = obj.insert(2)
print(param_2)
# param_2 = obj.remove(2)
param_3 = obj.getRandom()
print(param_3)
