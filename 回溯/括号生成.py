# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#  
#
# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 示例 2：
#
# 输入：n = 1
# 输出：["()"]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/generate-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 先把所有的括号可能种类 列出来，然后再减枝操作即可。


class Solution:
    def generateParenthesis(self, n: int):
        def dfs(temp, left, right,result):
            if left == n and right == n:
                print(temp)
                result.append(temp)
                # print(path)
                return

            if right > left:
                return
            # print(left,right)
            if left < n:
                dfs(temp + "(",left + 1, right,result)
            if right < n:
                dfs(temp + ")",left, right + 1,result)


        res = []
        dfs("", 0, 0,res)
        return res


s = Solution()
s.generateParenthesis(3)
