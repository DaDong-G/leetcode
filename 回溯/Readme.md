# 回溯问题思路
1. 一定要画出来图
2. 想办法进行剪枝操作
3，实在不行，全排列出来去重，就是慢。



# 自己总结有一套框架可以参考
```
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
class Solution:
    def permute(self, nums):
        def dfs(p, s, r):
            if s == len(nums):
                r.append(p)
                return
            # 控制要遍历的内容
            for i in range(len(nums)):
                if nums[i] in p:
                    continue
                print(p)
                dfs(p + [nums[i]], s + 1, r)

        size = len(nums)
        if size == 0:
            return
        p = []
        res = []
        控制有几个开始节点
        dfs(p, 0, res)
        return res
```



```
# 模板
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(p,s,r):
            if s == size + 1:
                return
            print(p)
            for i in range(len(nums)):
                dfs(p + [nums[i]], s + 1,res)

        res = []
        p = []
        if len(nums) == 0:
            return []
        size = len(nums)
        dfs(p,0,res)

```